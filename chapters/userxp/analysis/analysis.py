# import django
import json
import copy
import numpy as np
from collections import defaultdict
import glob
import pandas as pd

import naminggamesal as ngal
from naminggamesal.tools.export import get_agent_past,reconstruct_ag

import measures



xp_cfg = {
	    "step": 1,
	    "pop_cfg": {
	        "voc_cfg": {
	            "voc_type": "2dictdict"
	        },
	        "strat_cfg": {
	        	"memory_policies":[{'mem_type':'interaction_counts_sliding_window_local','time_scale':2}],
	            "vu_cfg": {
	                "vu_type": "minimalsynonly"
	            },
	            "success_cfg": {
	                "success_type": "global"
	            },
	            "strat_type": "naive",
	            "allow_idk":True,
	        },
	        "nbagent": 5,
	        "env_cfg": {
	            "env_type": "simple",
	            "M": 5,
	            "W": 6
	        },
	        "interact_cfg": {
	            "interact_type": "speakerschoice"
	        }
	    }
	}

xp_cfg_alone = {
	    "step": 1,
	    "pop_cfg": {
	        "voc_cfg": {
	            "voc_type": "2dictdict"
	        },
	        "strat_cfg": {
	        	"memory_policies":[{'mem_type':'interaction_counts_sliding_window_local','time_scale':2}],
	            "vu_cfg": {
	                "vu_type": "minimalsynonly"
	            },
	            "success_cfg": {
	                "success_type": "global"
	            },
	            "strat_type": "naive",
	            "allow_idk":True,
	        },
	        "nbagent": 5,

            "agent_init_cfg": {
              "agent_init_type": "onedifferent",
                'first_ag_cfg':{
                    #'strat_cfg':{'strat_type':'naive'},
                    'strat_cfg':{'strat_type':'success_threshold_wise','vu_cfg':{'vu_type':'minimal'}},
                    'memory_policies':[{'mem_type':'past_interactions_all'}]}
                    },
	        "env_cfg": {
	            "env_type": "simple",
	            "M": 5,
	            "W": 6
	        },
	        "interact_cfg": {
	            "interact_type": "speakerschoice"
	        }
	    }
	}


def info_dict_read(filepath):
	with open(filepath,'r') as f:
		return json.loads(f.read())

def clean_dict(info_dict):
	ans = []
	for elt in info_dict:
		if elt['model'] in ['ng.userng','ng.experiment','ng.pastinteraction','ng.score','ng.subscore']:
			ans.append(elt)
	return ans

def clean_file(filename):
	info_dict = info_dict_read(filename+'.json')
	with open(filename+'_cleaned.json','w') as f:
		f.write(json.dumps(clean_dict(info_dict)))


def processed_info_dict(info_dict):
	model_dict = defaultdict(dict)
	ans = dict()
	for elt in info_dict:
		model_dict[elt['model']][elt['pk']] = elt


	for u in model_dict['ng.userng'].values():
		u['xp_dict'] = {}

	for xp in model_dict['ng.experiment'].values():
		model_dict['ng.userng'][xp['fields']['user']]['xp_dict'][xp['pk']] = xp
		xp['pi_dict'] = {}
		xp['score_dict'] = {}
		xp_cfg_id = xp['fields']['xp_config']

		xp['cfg_name'] = model_dict['ng.xpconfig'][xp_cfg_id]['fields']['xp_cfg_name']
	for pi in model_dict['ng.pastinteraction'].values():
		model_dict['ng.experiment'][pi['fields']['experiment']]['pi_dict'][pi['fields']['time_id']] = pi

	for sc in model_dict['ng.score'].values():
		sc['subscore_dict'] = {}
		model_dict['ng.experiment'][sc['fields']['experiment']]['score_dict'][sc['pk']] = sc

	for ssc in model_dict['ng.subscore'].values():
		model_dict['ng.score'][ssc['fields']['score']]['subscore_dict'][ssc['pk']] = ssc

	return model_dict['ng.userng']


def filter(model_dict,
	q_filled=False,
	q_seen=False,
	cfg='normal',
	is_complete=True,
	whitelist_tags=None,
	blacklist_tags=['test'],
	before_info=True,
	after_date=None,
	before_date=None,
	xp_finished=True,
	check_q1=False,
	check_q2=False,
	not_first=False,
	game_won=False,
	only_1_per_user=False,
	subscores=False,
	):
	"""
	filters:

	"""
	ans = copy.deepcopy(model_dict)

	def test_u(u):
		if q_filled and not u['fields']['q_filled']:
			return False
		if q_seen and not u['fields']['q_seen']:
			return False
		if check_q1 and not u['fields']['q1']:
			return False
		if check_q2 and u['fields']['q2']:
			return False
		if blacklist_tags is not None and u['fields']['code'] in blacklist_tags:
			return False
		if whitelist_tags is not None and u['fields']['code'] not in whitelist_tags:
			return False

		return True

	def test_xp(xp):
		if cfg is not None and xp['cfg_name'] != cfg:
			return False
		if before_info and not xp['fields']['before_info']:
			return False
		if is_complete and not xp['fields']['is_complete']:
			return False
		if game_won and not xp['fields']['game_won']:
			return False
		if before_date is not None and xp['fields']['updated_at']>before_date:
			return False
		if after_date is not None and xp['fields']['updated_at']<after_date:
			return False
		if not_first and xp['fields']['xp_number']<=2:
			return False
		if subscores and not len(list(xp['score_dict'].values())[0]['subscore_dict'].keys()):
			return False
		return True

	u_to_rm = []
	for ku,u in ans.items():
		if not test_u(u):
			u_to_rm.append(ku)
		else:
			to_rm = []
			for k,xp in u['xp_dict'].items():
				if not test_xp(xp):
					to_rm.append(k)
			for rm in to_rm:
				del(u['xp_dict'][rm])

	for ku in u_to_rm:
		del(ans[ku])

	if only_1_per_user:
		for ku,u in ans.items():
			to_rm = []
			nb = 0
			for k,xp in u['xp_dict'].items():
				if nb>0:
					to_rm.append(k)
				nb += 1
			for rm in to_rm:
				del(u['xp_dict'][rm])



	ansc = copy.deepcopy(ans)

	for k,v in ansc.items():
		if not v['xp_dict']:
			del(ans[k])


	return ans

def get_pi_list(xp):
	ans = []
	time_stamps = sorted(xp['pi_dict'].keys())
	for t in time_stamps:
		pi = xp['pi_dict'][t]['fields']
		pi_d = {
			"w": pi['word'],
			"bool_succ": bool(pi['bool_succ']),
			"role": pi['role'],
			"mh": pi['meaning_h'],
			"ms": int(pi['meaning']),
			}
		if pi_d['mh'] == 'none':
			pi_d['mh'] = None
		else:
			pi_d['mh'] = int(pi_d['mh'])
		ans.append(pi_d)
	return ans


class Results(object):
	def __init__(self,filepath,filter_dict={}):
		self.info_dict = filter(processed_info_dict(info_dict_read(filepath=filepath)),**filter_dict)
		self.pi_struct = []
		for u in self.info_dict.values():
			u_l = []
			for xp in u['xp_dict'].values():
				u_l.append(get_pi_list(xp))
			self.pi_struct.append(u_l)
		self.options = []
		self.xp_cfg = xp_cfg
		measures.replace_words(self)
		measures.replace_meanings(self)
		self.check_xp_cfg()

	def check_xp_cfg(self):
		if self.xp_cfg['pop_cfg']['env_cfg']['env_type'] == 'simple_realwords':
			self.xp_cfg['pop_cfg']['env_cfg']['env_type'] = 'simple'

	def extend(self,other):
		self.pi_struct.extend(copy.deepcopy(other.pi_struct))

	def __add__(self,other):
		ans = copy.deepcopy(self)
		ans.extend(other)
		return ans

	def get_measure(self,measure,level='user',**kwargs):
		func = getattr(self,measure)
		ans = []
		if level == 'user':
			for u in self.pi_struct:
				ans.append(np.mean([func(p,**kwargs) for p in u]))
			return ans
		elif level == 'xp':
			for u in self.pi_struct:
				for p in u:
					ans.append(func(p,**kwargs))
			return ans
		elif level == 'all_user':
			l = self.get_measure(measure=measure,level='user',**kwargs)
			return np.mean([a for a in l if not np.isnan(a)])
		elif level == 'all_xp':
			l = self.get_measure(measure=measure,level='xp',**kwargs)
			return np.mean([a for a in l if not np.isnan(a)])

	def get_measure_std(self,measure,level='user'):
		func = getattr(self,measure)
		ans = []
		if level == 'user':
			for u in self.pi_struct:
				ans.append(np.std([func(p,**kwargs) for p in u]))
			return ans
		elif level == 'xp':
			for u in self.pi_struct:
				for p in u:
					ans.append(func(p),**kwargs)
			return ans
		elif level == 'all_user':
			l = self.get_measure(measure=measure,level='user',**kwargs)
			return np.std([a for a in l if not np.isnan(a)])
		elif level == 'all_xp':
			l = self.get_measure(measure=measure,level='xp',**kwargs)
			return np.std([a for a in l if not np.isnan(a)])

	def nb_inv(self,pi_l,data=False):
		known_m = set()
		ans = 0
		dat = []
		for pi in pi_l:
			if pi['role'] == 'speaker':
				if pi['ms'] not in known_m:
					ans += 1
					dat.append(1)
				else:
					dat.append(0)
			known_m.add(pi['ms'])
		if data:
			return dat
		else:
			return ans


	# def explo_rate_global(self):
	# 	nb_total = 0
	# 	nb_explo = 0
	# 	for u in self.pi_struct:
	# 		for xp in u:
	# 			known_m = set()
	# 			for pi in xp:
	# 				if pi['role'] == 'speaker':
	# 					nb_total += 1
	# 					if pi['ms'] not in known_m:
	# 						nb_explo += 1
	# 				known_m.add(pi['ms'])
	# 	return nb_explo*1./nb_total


	# def explo_rate_global_m(self):
	# 	nb_total = np.asarray([0. for _ in range(6)])
	# 	nb_explo = np.asarray([0. for _ in range(6)])
	# 	for u in self.pi_struct:
	# 		for xp in u:
	# 			known_m = set()
	# 			for pi in xp:
	# 				if pi['role'] == 'speaker':
	# 					nb_total[len(known_m)] += 1
	# 					if pi['ms'] not in known_m:
	# 						nb_explo[len(known_m)] += 1
	# 				known_m.add(pi['ms'])
	# 	return nb_explo*1./nb_total

	# def counts_m(self):
	# 	nb_total = np.asarray([0. for _ in range(6)])
	# 	nb_explo = np.asarray([0. for _ in range(6)])
	# 	for u in self.pi_struct:
	# 		for xp in u:
	# 			known_m = set()
	# 			for pi in xp:
	# 				if pi['role'] == 'speaker':
	# 					nb_total[len(known_m)] += 1
	# 					if pi['ms'] not in known_m:
	# 						nb_explo[len(known_m)] += 1
	# 				known_m.add(pi['ms'])
	# 	return nb_total

	def size(self):
		return sum([ len(u) for u in self.pi_struct])

	def scores(self):
		ans = []
		for u in self.info_dict.values():
			for xp in u['xp_dict'].values():
				for sc in xp['score_dict'].values():
					ans.append(sc['fields']['score']/5.)
		return ans


	def subscores(self):
		ans = []
		for u in self.info_dict.values():
			for xp in u['xp_dict'].values():
				for sc in xp['score_dict'].values():
					ssc_vals = [ssc['fields']['subscore'] for ssc in sc['subscore_dict'].values()]
					ssc_vals = sorted(ssc_vals,reverse=True)
					if not ssc_vals:
						ans.append(np.nan)
					else:
						ans.append(np.asarray(ssc_vals))
		return ans

	def prepare(self):
		measures.explo_rate(self)

	def discard_first_explo(self,reverse=False):
		self.prepare()
		new_pi_struct = []
		for u in self.pi_struct:
			new_u = []
			for xp in u:
				for pi in xp:
					if pi['KM'] == 1:
						if not pi['explo']:
							if not reverse:
								new_u.append(xp)
						elif reverse:
							new_u.append(xp)
						break
			if new_u:
				new_pi_struct.append(new_u)
		self.pi_struct = new_pi_struct




class ResultsFromXPFiles(Results):
	def __init__(self,files):
		self.pi_struct = []
		for fp in files:
			with open(fp,'r') as f:
				f_content = json.loads(f.read())
			self.pi_struct.append([f_content])
		self.options = []
		self.xp_cfg = xp_cfg
		measures.replace_words(self)
		measures.replace_meanings(self)
		self.check_xp_cfg()

	def scores(self):
		return []

	def subscores(self):
		return []

class ResultsFromFolder(ResultsFromXPFiles):
	def __init__(self,folder):
		self.folder = folder
		files = glob.glob(folder+'/*.json')
		ResultsFromXPFiles.__init__(self,files=files)

db = ngal.ngdb.NamingGamesDB()
db.move_to_RAM()

class ResultsFromSimu(Results):
	def __init__(self,xp_cfg,T,nb,all_agents=True):
		self.pi_struct = []
		self.nb = nb
		self.T = T
		self.all_agents = all_agents
		self.db = db
		self.xp_cfg = copy.deepcopy(xp_cfg)
		if 'memory_policies' not in self.xp_cfg['pop_cfg']['strat_cfg']:
			self.xp_cfg['pop_cfg']['strat_cfg']['memory_policies'] = []
		self.xp_cfg['pop_cfg']['strat_cfg']['memory_policies'].append({'mem_type':'past_interactions_all'})
		self.exec_simu()
		self.options = []


	def scores(self):
		return self.score_values

	def subscores(self):
		return self.subscore_values

	def exec_simu(self):
		self.score_values = []
		self.subscore_values = []
		blacklist = []
		for i in range(self.nb):
			xp = self.db.get_experiment(blacklist=blacklist,**self.xp_cfg)
			xp.continue_exp_until(T=self.T)
			blacklist.append(xp.uuid)
			if self.all_agents:
				ag_l = range(5)
			else:
				ag_l = [0]
			for ag in ag_l:
				self.pi_struct.append([get_agent_past(xp=xp,agent_number=ag)])
			self.score_values.append(100*xp.graph('srtheo')._Y[0][-1])
			ssc = []
			for m in range(5):
				val = 100*ngal.ngmeth.srtheo(pop=xp._poplist.get_last(),m=m)
				ssc.append(val)
			self.subscore_values.append(sorted(ssc,reverse=True))


def results_from_strat(strat_cfg,name,all_agents=True,nb=80):
	if all_agents:
		xp_cfg2 = copy.deepcopy(xp_cfg)
		xp_cfg2['pop_cfg']['strat_cfg'].update(**strat_cfg)
	else:
		xp_cfg2 = copy.deepcopy(xp_cfg_alone)
		xp_cfg2['pop_cfg']['agent_init_cfg']['first_ag_cfg']['strat_cfg'].update(**strat_cfg)
	res = ResultsFromSimu(xp_cfg=xp_cfg2,T=50,nb=nb,all_agents=all_agents)
	res.name = name
	if all_agents:
		res.name += '_allagents'
	# else:
	# 	res.name += '_oneagent'
	return res




def get_df(res_list,m):
	xlabel = ''
	ylabel = ' '
	assert xlabel != ylabel
	dat = {xlabel:[],ylabel:[]}
	for r in res_list:
		dat[xlabel].append(r.name)
		dat[ylabel].append(getattr(measures,m)(r,data=True))

	a = []
	names = []
	dat = dict()
	for r in res_list:
		a.append(getattr(measures,m)(r,data=True))
		names.append(r.name)
		if m == 'scores' and r.name == 'DataKreyon' and a[-1] == []:
			a[-1] = [np.nan]
		dat[r.name] = a[-1]
	#plt.bar(x=names,height=a)
	# a = a[0:2]+[0]+a[2:-1]
	# names = names[0:2]+['']+names[2:-1]
	b = []
	d2 = {xlabel:[],ylabel:[]}

	if hasattr(a[0],'items'):
		for aa,n in zip(a,names):
			bb = []
			for k,v in aa.items():
				bb.extend(v)
				for vv in v:
					d2[xlabel].append(n)
					d2[ylabel].append(vv)
			b.append(bb)

	else:
		for aa,n in zip(a,names):
			for aaa in aa:
				d2[xlabel].append(n)
				d2[ylabel].append(aaa)

	return pd.DataFrame(d2)


def prepare_analysis(nb=80,discard=False,reverse=False):

	res_list = []

	res = Results(filepath='./dumps_test.json')
	res.name = 'Data'
	if discard:
		res.discard_first_explo(reverse=reverse)
	res_list.append(res)

	res = ResultsFromFolder(folder='./json_data_kreyon')
	res.name = 'DataKreyon'
	if discard:
		res.discard_first_explo(reverse=reverse)
	res_list.append(res)



	strat_cfg_l = [
				({'strat_type':'naive'},'Random'),
				({'strat_type':'naive_explobiased'},'ExploBiased'),
				({'strat_type':'success_threshold_wise','threshold_explo':0.5},'ST0.5'),
				({'strat_type':'mincounts','mincounts':0.9},'MC1'),
				({'strat_type':'lapsmax_mab_explothreshold'},'LAPSmax'),
				({'strat_type':'coherence_last','time_scale':3},'Coherence'),

			]


	for s,n in strat_cfg_l:
		# res_list.append(results_from_strat(strat_cfg=s,name=n))
		res_list.append(results_from_strat(strat_cfg=s,name=n,all_agents=False,nb=nb))
	return res_list
	# res.xp_cfg = copy.deepcopy(xp_cfg)

	# xp_cfg2 = copy.deepcopy(xp_cfg)
	# xp_cfg2['pop_cfg']['strat_cfg']['strat_type'] = 'success_threshold_wise'
	# xp_cfg2['pop_cfg']['strat_cfg']['threshold_explo'] = 0.5

	# xp_cfg3 = copy.deepcopy(xp_cfg)
	# xp_cfg3['pop_cfg']['strat_cfg']['strat_type'] = 'mincounts'
	# xp_cfg3['pop_cfg']['strat_cfg']['mincounts'] = 0.9

	# xp_cfg4 = copy.deepcopy(xp_cfg)
	# xp_cfg4['pop_cfg']['strat_cfg']['strat_type'] = 'lapsmax_mab_explothreshold'

	# xp_cfg5 = copy.deepcopy(xp_cfg)
	# xp_cfg5['pop_cfg']['strat_cfg']['strat_type'] = 'coherence_last'
	# xp_cfg5['pop_cfg']['strat_cfg']['time_scale'] = 2

	# xp_cfg2 = copy.deepcopy(xp_cfg)
	# xp_cfg2['pop_cfg']['strat_cfg']['strat_type'] = 'success_threshold_wise'
	# xp_cfg2['pop_cfg']['strat_cfg']['threshold_explo'] = 0.5

	# xp_cfg3 = copy.deepcopy(xp_cfg)
	# xp_cfg3['pop_cfg']['strat_cfg']['strat_type'] = 'mincounts'
	# xp_cfg3['pop_cfg']['strat_cfg']['mincounts'] = 0.9

	# xp_cfg4 = copy.deepcopy(xp_cfg)
	# xp_cfg4['pop_cfg']['strat_cfg']['strat_type'] = 'lapsmax_mab_explothreshold'

	# xp_cfg5 = copy.deepcopy(xp_cfg)
	# xp_cfg5['pop_cfg']['strat_cfg']['strat_type'] = 'coherence_last'
	# xp_cfg5['pop_cfg']['strat_cfg']['time_scale'] = 2

	# res2 = ResultsFromSimu(xp_cfg=xp_cfg,T=50,nb=20,all_agents=True)
	# res2.name = 'naive'
	# res_list.append(res2)

	# res3 = ResultsFromSimu(xp_cfg=xp_cfg2,T=50,nb=20,all_agents=True)
	# res3.name = 'ST0.5'
	# res_list.append(res3)

	# res3 = ResultsFromSimu(xp_cfg=xp_cfg3,T=50,nb=20,all_agents=True)
	# res3.name = 'MC1'
	# res_list.append(res3)

	# res3 = ResultsFromSimu(xp_cfg=xp_cfg4,T=50,nb=20,all_agents=True)
	# res3.name = 'lapsmax'
	# res_list.append(res3)

	# res3 = ResultsFromSimu(xp_cfg=xp_cfg5,T=50,nb=20,all_agents=True)
	# res3.name = 'coherence'
	# res_list.append(res3)

	# print('size')
	# for r in res_list:
	# 	print(r.name,r.size())
if __name__ == '__main__':
	import matplotlib.pyplot as plt
	import seaborn as sns
	import pandas as pd
	res_list = prepare_analysis()
	measures_1 = ['nb_inv',
				# 'time_between_inventions',
				# 'mincounts',
				# 'mincounts_s',
				# 'success_threshold',
				# 'mean_mincounts',
				# 'mean_mincounts_s',
				# 'mean_success_threshold',
				]

	measures_m = [
				# 'explo_count_m',
				# 'nonexplo_count_m',
				# 'count_m',
				# 'mincounts_m',
				# 'mincounts_s_m',
				# 'success_threshold_m',
				# 'mean_mincounts_m',
				# 'mean_mincounts_s_m',
				# 'mean_success_threshold_m',
				# 'samples_m',
				]

	measures_bis = [
				# 'mincounts',
				# 'mincounts_m',
				# 'mean_mincounts_m',
				# 'mean_mincounts',
				# 'mincounts_s',
				# 'mean_mincounts_s',
				# 'mincounts_s_m',
				# 'mean_mincounts_s_m',
				# 'success_threshold',
				# 'success_threshold_m',
				# 'mean_success_threshold',
				# 'mean_success_threshold_m',
				#'explo_rate_global',
				#'explo_rate_global_m',
				#'counts_m',
				 'size'
				]

	measures_ter = [
				'success_threshold',
				'success_threshold_m',
				# 'minsuccess_threshold',
				# 'minsuccess_threshold_m',
				'mincounts',
				'mincounts_m',
				# 'meancounts',
				# 'meancounts_m',
				# 'mincounts2',
				# 'mincounts2_m',
				# 'meancounts2',
				# 'meancounts2_m',
				'laps_m',
				'coher',
				'coher_m',
				# 'dlaps_m',
				'explo_rate_m',
				'explo_rate',
				'criterion_laps',
				'criterion_ST',
				'criterion_MC',
				'criterion_CH',
				'criterion_EB',
				'criterion_RTC',
				'criterion_partial_laps',
				'criterion_partial_ST',
				'criterion_partial_MC',
				'criterion_partial_CH',
				'criterion_laps_global',
				'criterion_ST_global',
				'criterion_MC_global',
				'criterion_CH_global',
				'criterion_partial_laps_global',
				'criterion_partial_ST_global',
				'criterion_partial_MC_global',
				'criterion_partial_CH_global',
				'scores',
				'subscores',
				]

	measures_ter2 = [
				'explo_rate',
				# 'criterion_MC',
				'criterion_MC_global',
				'criterion_RTC_global',
				'criterion_EB_global',
				'criterion_partial_MC_global',
				'criterion_partial_ST_global',
				'criterion_partial_laps_global',
				'criterion_partial_CH_global',
				]

	measures_ter3 = [
				'mincounts',
				'success_threshold',
				'laps_m',
				'coher_m',
				'criterion_ST',
				'criterion_MC',
				'criterion_EB',
				'criterion_laps',
				'criterion_CH',
				'similarity_ST',
				'similarity_MC',
				'similarity_EB',
				'similarity_laps',
				'similarity_CH',
				'similarity_RTC',
				'scores'
				]

	measures_ter4 = [
				'explo_rate_m',
				]

	for m in measures_1:
		print('\n\n',m,'\n')
		for r in res_list:
			print(r.name,r.get_measure(measure=m,level='all_xp'))



	for m in measures_m:
		print('\n\n',m,'\n')
		for r in res_list:
			print(r.name,[r.get_measure(measure=m,level='all_xp',m=mm) for mm in range(6)])

	# print('\n\n','new_explo_rate_m','\n')
	# for r in res_list:
	# 	vec_c = np.asarray([r.get_measure(measure='count_m',level='all_xp',m=mm) for mm in range(6)])
	# 	vec_e = np.asarray([r.get_measure(measure='explo_count_m',level='all_xp',m=mm) for mm in range(6)])
	# 	print(r.name,list(vec_e/vec_c))



	# print('\n\n','new_explo_rate','\n')
	# for r in res_list:
	# 	c = r.get_measure(measure='count',level='all_xp')
	# 	e = r.get_measure(measure='explo_count',level='all_xp')
	# 	print(r.name,e * 1./c)

	for m in measures_bis:
		print('\n\n',m,'\n')
		for r in res_list:
			print(r.name,getattr(r,m)())


	for m in measures_ter:
		print('\n\n',m,'\n')
		for r in res_list:
			print(r.name,getattr(measures,m)(r))

	for r in res_list:
		print(measures.similarity_class(r))

	for m in measures_ter2:
		a = []
		names = []
		dat = dict()
		for r in res_list:
			a.append(getattr(measures,m)(r))
			names.append(r.name)
			dat[r.name] = a[-1]
		#plt.bar(x=names,height=a)
		# a = a[0:2]+[0]+a[2:-1]
		# names = names[0:2]+['']+names[2:-1]
		sns.barplot(x=names,y=a)
		plt.title(m)
		plt.show()


	for m in measures_ter3:
		a = []
		names = []
		dat = dict()
		for r in res_list:
			a.append(getattr(measures,m)(r,data=True))
			names.append(r.name)
			dat[r.name] = a[-1]
		#plt.bar(x=names,height=a)
		# a = a[0:2]+[0]+a[2:-1]
		# names = names[0:2]+['']+names[2:-1]
		b = []
		d2 = {'name':[],'value':[]}

		if hasattr(a[0],'items'):
			for aa,n in zip(a,names):
				bb = []
				for k,v in aa.items():
					bb.extend(v)
					for vv in v:
						d2['name'].append(n)
						d2['value'].append(vv)
				b.append(bb)
		else:
			for aa,n in zip(a,names):
				for aaa in aa:
					d2['name'].append(n)
					d2['value'].append(aaa)
		sns.violinplot(x='name',y='value',data=pd.DataFrame(d2),cut=0)
		plt.title(m)
		plt.show()


	for m in measures_ter4:
		a = []
		names = []
		dat = dict()
		for r in res_list:
			a.append(getattr(measures,m)(r,data=True))
			names.append(r.name)
			dat[r.name] = a[-1]
		#plt.bar(x=names,height=a)
		# a = a[0:2]+[0]+a[2:-1]
		# names = names[0:2]+['']+names[2:-1]
		b = []
		d2 = {'name':[],'value':[],'m':[]}

		if hasattr(a[0],'items'):
			for aa,n in zip(a,names):
				bb = []
				for k,v in aa.items():
					bb.extend(v)
					for vv in v:
						d2['name'].append(n)
						d2['value'].append(vv)
						d2['m'].append(k)
				b.append(bb)
		else:
			for aa,n in zip(a,names):
				for aaa in aa:
					d2['name'].append(n)
					d2['value'].append(aaa)
		sns.catplot(x='m',y='value',hue='name',data=pd.DataFrame(d2),kind='bar')
		plt.title(m)
		plt.show()

	# for a in res_list[4].pi_struct:
	# 	for pi in a[0]:
	# 		val = {i:[] for i in range(6)}
	# 		measures.pi_mincounts(pi,val)
	# 		print(pi['explo'],pi['counts_s'],val)

	# for pi in res_list[4].pi_struct[-1][0]:
	# 	val = {i:[] for i in range(6)}
	# 	measures.pi_mincounts(pi,val)
	# 	print(pi['explo'],pi['counts_s'],val)

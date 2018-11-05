import random
import copy
import numpy as np
from collections import defaultdict,deque

import naminggamesal as ngal
from naminggamesal.tools.export import get_agent_past,reconstruct_ag

# def base_m(res,absolute,func):
# 	nb_total = np.asarray([0. for _ in range(6)])
# 	nb_total[-1] = 1.
# 	val = np.asarray([0. for _ in range(6)])
# 	for u in res.pi_struct:
# 		for xp in u:
# 			counts = defaultdict(float)
# 			counts_s = defaultdict(float)
# 			for pi in xp:
# 				if pi['role'] == 'speaker':
# 					if pi['ms'] not in counts.keys():
# 						if absolute:
# 							c_vec = [counts_s[m] for m in counts.keys()]
# 						else:
# 							c_vec = [counts_s[m]*1./counts[m] for m in counts.keys()]
# 						if c_vec:
# 							val[len(counts.keys())] += func(c_vec)
# 						nb_total[len(counts.keys())] += 1.
# 				counts[pi['ms']] += 1.
# 				if pi['bool_succ']:
# 					counts_s[pi['ms']] += 1.
# 				else:
# 					counts_s[pi['ms']] = counts_s[pi['ms']]
# 	return val*1./nb_total

# def base(res,absolute,func):
# 	nb_total = 0.
# 	val = 0.
# 	for u in res.pi_struct:
# 		for xp in u:
# 			counts = defaultdict(float)
# 			counts_s = defaultdict(float)
# 			for pi in xp:
# 				if pi['role'] == 'speaker':
# 					if pi['ms'] not in counts.keys():
# 						if absolute:
# 							c_vec = [counts_s[m] for m in counts.keys()]
# 						else:
# 							c_vec = [counts_s[m]*1./counts[m] for m in counts.keys()]
# 						if c_vec:
# 							val += func(c_vec)
# 							nb_total += 1.
# 				counts[pi['ms']] += 1.
# 				if pi['bool_succ']:
# 					counts_s[pi['ms']] += 1.
# 				else:
# 					counts_s[pi['ms']] = counts_s[pi['ms']]
# 	if nb_total == 0:
# 		return 0
# 	else:
# 		return val*1./nb_total

# def base2_m(res,absolute,func):
# 	nb_total = np.asarray([0. for _ in range(6)])
# 	nb_total[-1] = 1.
# 	val = np.asarray([0. for _ in range(6)])
# 	for u in res.pi_struct:
# 		for xp in u:
# 			counts = defaultdict(float)
# 			counts_s = defaultdict(float)
# 			for pi in xp:
# 				if pi['role'] == 'speaker':
# 					if pi['ms'] not in counts.keys():
# 						c_vec = [counts[m] for m in counts.keys()]
# 						if c_vec:
# 							val[len(counts.keys())] += func(c_vec)
# 						nb_total[len(counts.keys())] += 1.
# 				counts[pi['ms']] += 1.
# 				if pi['bool_succ']:
# 					counts_s[pi['ms']] += 1.
# 				else:
# 					counts_s[pi['ms']] = counts_s[pi['ms']]
# 	return val*1./nb_total

# def base2(res,absolute,func):
# 	nb_total = 0.
# 	val = 0.
# 	for u in res.pi_struct:
# 		for xp in u:
# 			counts = defaultdict(float)
# 			counts_s = defaultdict(float)
# 			for pi in xp:
# 				if pi['role'] == 'speaker':
# 					if pi['ms'] not in counts.keys():
# 						c_vec = [counts[m] for m in counts.keys()]
# 						if c_vec:
# 							val += func(c_vec)
# 							nb_total += 1.
# 				counts[pi['ms']] += 1.
# 				if pi['bool_succ']:
# 					counts_s[pi['ms']] += 1.
# 				else:
# 					counts_s[pi['ms']] = counts_s[pi['ms']]
# 	return val*1./nb_total



def replace_words(res):
	for u in res.pi_struct:
		for xp in u:
			w_l = dict()
			next_val = 0
			for pi in xp:
				if pi['w'] not in w_l.keys():
					w_l[pi['w']] = next_val
					next_val += 1
				pi['w'] = w_l[pi['w']]

def replace_meanings(res):
	for u in res.pi_struct:
		for xp in u:
			m_l = {None:None}
			next_val = 0
			for pi in xp:
				if pi['ms'] not in m_l.keys():
					m_l[pi['ms']] = next_val
					next_val += 1
				if pi['mh'] not in m_l.keys():
					m_l[pi['mh']] = next_val
					next_val += 1
				pi['ms'] = m_l[pi['ms']]
				pi['mh'] = m_l[pi['mh']]

def add_laps(res):
	if 'laps' not in res.options:
		res.options.append('laps')
		for u in res.pi_struct:
			for xp in u:
				ag = reconstruct_ag(past_interactions=[],pop_cfg=res.xp_cfg['pop_cfg'])
				for pi in xp:
					pi_ag = {k:pi[k] for k in ['w','role','ms','mh','bool_succ']}
					if pi['KM'] != 0:
						fac_norm = 5./pi['KM']
					else:
						fac_norm = 0
					pi['laps'] = ngal.ngmeth.srtheo_local(agent=ag) * fac_norm
					pi['laps_nonorm'] = ngal.ngmeth.srtheo_local(agent=ag)
					ag.update_agent(**pi_ag)
					pi['delta_laps'] = ngal.ngmeth.srtheo_local(agent=ag)- pi['laps_nonorm']

def add_coherencecounts(res):
	if 'ch_c' not in res.options:
		res.options.append('ch_c')
		for u in res.pi_struct:
			for xp in u:
				known_m = set()
				past_c = [deque(maxlen=3) for _ in range(5)]
				for pi in xp:
					ch_c =   [len(  [1. for w in past_c[m] if w==past_c[m][-1]]   ) for m in known_m]
					pi['ch_c'] = ch_c
					if ch_c:
						pi['ch_val'] = min(ch_c)
					else:
						pi['ch_val'] = 1.
					past_c[pi['ms']].append(pi['w'])
					known_m.add(pi['ms'])


def add_KM(res):
	if 'KM' not in res.options:
		res.options.append('KM')
		for u in res.pi_struct:
			for xp in u:
				known_m = set()
				for pi in xp:
					pi['KM'] = len(known_m)
					known_m.add(pi['ms'])


def add_explo(res):
	if 'explo' not in res.options:
		res.options.append('explo')
		for u in res.pi_struct:
			for xp in u:
				known_m = set()
				for pi in xp:
					pi['explo'] = (pi['role'] == 'speaker' and pi['ms'] not in known_m)
					known_m.add(pi['ms'])

def add_counts(res):
	if 'counts' not in res.options:
		res.options.append('counts')
		for u in res.pi_struct:
			for xp in u:
				counts = np.asarray([0. for _ in range(6)])
				counts_s = np.asarray([0. for _ in range(6)])
				for pi in xp:
					pi['counts'] = copy.copy(counts)
					pi['counts_s'] = copy.copy(counts_s)
					counts[pi['ms']] += 1.
					if pi['bool_succ']:
						counts_s[pi['ms']] += 1.


def add_lapscriterion(res):
	if 'lapscriterion' not in res.options:
		res.options.append('lapscriterion')
		for u in res.pi_struct:
			for xp in u:
				for pi in xp:
					if pi['KM'] == 5:
						pi['explo_laps'] = 0
					elif pi['laps'] >= (1.-10**-5):#(pi['KM']/5.)*(1.-10**-5):
						pi['explo_laps'] = 1
					else:
						pi['explo_laps'] = 0

def add_MCcriterion(res):
	if 'MCcriterion' not in res.options:
		res.options.append('MCcriterion')
		for u in res.pi_struct:
			for xp in u:
				for pi in xp:
					vec = [a for a,b in zip(pi['counts_s'],pi['counts']) if b != 0 ]
					if pi['KM'] == 5:
						pi['explo_MC'] = 0
					elif pi['KM'] == 0 or min(vec) >= 1.:
						pi['explo_MC'] = 1
					else:
						pi['explo_MC'] = 0

def add_STcriterion(res):
	if 'STcriterion' not in res.options:
		res.options.append('STcriterion')
		for u in res.pi_struct:
			for xp in u:
				for pi in xp:
					vec = [a*1./b for a,b in zip(pi['counts_s'],pi['counts']) if b != 0 ]
					if pi['KM'] == 5:
						pi['explo_ST'] = 0
					elif pi['KM'] == 0 or np.mean(vec) >= 0.5:
						pi['explo_ST'] = 1
					else:
						pi['explo_ST'] = 0

def add_CHcriterion(res):
	if 'CHcriterion' not in res.options:
		res.options.append('CHcriterion')
		for u in res.pi_struct:
			for xp in u:
				for pi in xp:
					if pi['KM'] == 5:
						pi['explo_CH'] = 0
					elif pi['KM'] == 0 or min(pi['ch_c']) >= 3:
						pi['explo_CH'] = 1
					else:
						pi['explo_CH'] = 0


def add_EBcriterion(res):
	if 'EBcriterion' not in res.options:
		res.options.append('EBcriterion')
		for u in res.pi_struct:
			for xp in u:
				for pi in xp:
					pi['explo_EB'] = 1./(pi['KM']+1)


def add_RTCcriterion(res):
	if 'RTCcriterion' not in res.options:
		res.options.append('RTCcriterion')
		for u in res.pi_struct:
			for xp in u:
				for pi in xp:
					pi['explo_RTC'] = (5-pi['KM'])/5.


# def laps_m(res,data=False,global_mean=False,func=np.mean):
# 	add_laps(res)
# 	add_KM(res)
# 	add_explo(res)
# 	val = {i:[] for i in range(6)}
# 	for u in res.pi_struct:
# 		for xp in u:
# 			for pi in xp:
# 				if pi['explo']:
# 					val[pi['KM']].append(pi['laps'])
# 	if data:
# 		return val
# 	elif global_mean:
# 		vv = []
# 		for v in val:
# 			vv.extend(v)
# 		return np.mean(v)
# 	else:
# 		#return np.asarray([np.mean(v) for v in val.values()])
# 		return np.asarray([((len(v)>0) and np.mean(v)) or np.nan for v in val.values()])

# def dlaps_m(res):
# 	add_laps(res)
# 	add_KM(res)
# 	add_explo(res)
# 	nb_total = np.asarray([0. for _ in range(6)])
# 	nb_total[-1] = 1.
# 	val = np.asarray([0. for _ in range(6)])
# 	for u in res.pi_struct:
# 		for xp in u:
# 			for pi in xp:
# 				if pi['explo']:
# 					nb_total[pi['KM']] += 1.
# 					val[pi['KM']] += pi['delta_laps']
# 	return val*1./nb_total



def template_measure(measure,res,data=False,global_mean=False,level_xp=False,*args,**kwargs):
	add_KM(res)
	add_laps(res)
	add_coherencecounts(res)
	add_explo(res)
	add_counts(res)
	add_lapscriterion(res)
	add_STcriterion(res)
	add_MCcriterion(res)
	add_CHcriterion(res)
	add_EBcriterion(res)
	add_RTCcriterion(res)

	val = {i:[] for i in range(6)}
	for u in res.pi_struct:
		for xp in u:
			for pi in xp:
				measure(pi=pi,val=val,*args,**kwargs)
	if data:
		return val
	elif global_mean:
		vv = []
		for v in val.values():
			vv.extend(v)
		return np.mean(vv)
	else:
		#return np.asarray([np.mean(v) for v in val.values()])
		return np.asarray([((len(v)>0) and np.mean(v)) or np.nan for v in val.values()])

def template_measure_xp(measure,res,data=False,global_mean=False,*args,**kwargs):
	add_KM(res)
	add_laps(res)
	add_coherencecounts(res)
	add_explo(res)
	add_counts(res)
	add_lapscriterion(res)
	add_STcriterion(res)
	add_MCcriterion(res)
	add_CHcriterion(res)
	add_EBcriterion(res)
	add_RTCcriterion(res)

	val = {i:[] for i in range(6)}
	for u in res.pi_struct:
		for xp in u:
			valt = {i:[] for i in range(6)}
			for pi in xp:
				measure(pi=pi,val=valt,*args,**kwargs)
			vt = []
			for vv in valt.values():
				vt.extend(vv)
			val[0].append(np.mean(vt))
	if data:
		return val
	elif global_mean:
		vv = []
		for v in val.values():
			vv.extend(v)
		return np.mean(vv)
	else:
		#return np.asarray([np.mean(v) for v in val.values()])
		return np.asarray([((len(v)>0) and np.mean(v)) or np.nan for v in val.values()])

def similarity_class(res):
	classes = ['RTC','EB','ST','MC','laps','CH']
	counts = {k:0 for k in classes}
	for u in res.pi_struct:
		for xp in u:
			val = {}
			for cl in classes:
				valt = {i:[] for i in range(6)}
				for pi in xp:
					globals()['pi_criterion_'+cl](pi=pi,val=valt)
				vt = []
				for vv in valt.values():
					vt.extend(vv)
				val[cl] = np.mean(vt)
			max_val = max(val.values())
			keys = [k for k in val.keys() if val[k] == max_val]
			for k in keys:
				counts[k] += 1.#/len(keys)
	return counts

#############################
def pi_laps(pi,val):
	if pi['explo'] and pi['KM']:
		val[pi['KM']].append(pi['laps'])

def pi_coher(pi,val):
	if pi['explo'] and pi['KM']:
		val[pi['KM']].append(pi['ch_val'])


def pi_dlaps(pi,val):
	if pi['explo'] and pi['KM']:
		val[pi['KM']].append(pi['delta_laps'])

def pi_mincounts(pi,val,func=min):
	if pi['explo']:
		vec = [a for a,b in zip(pi['counts_s'],pi['counts']) if b != 0 ]
		if len(vec):
			val[pi['KM']].append(func(vec))
		else:
			return np.nan

def pi_success_threshold(pi,val,func=min):
	if pi['explo']:
		vec = [a*1./b for a,b in zip(pi['counts_s'],pi['counts']) if b != 0 ]
		if len(vec):
			val[pi['KM']].append(func(vec))
		else:
			return np.nan

def pi_explo_rate(pi,val):
	if pi['role'] == 'speaker':
		val[pi['KM']].append(float(pi['explo']))

def pi_criterion(pi,val,criterion):
	if pi['KM'] not in [0,5]:
		# val[pi['KM']].append(float(pi['explo_'+criterion] == pi['explo']))
		val[pi['KM']].append( ( (1.-pi['explo'])*(1.-pi['explo_'+criterion]) + (pi['explo'] * pi['explo_'+criterion]) )/max(pi['explo_'+criterion],1.-pi['explo_'+criterion]) )

def pi_criterion_partial(pi,val,criterion):
	if pi['explo'] and pi['KM'] != 0 :
		val[pi['KM']].append(float(pi['explo_'+criterion]))

def pi_criterion_laps(pi,val):
	return pi_criterion(pi=pi,val=val,criterion='laps')

def pi_criterion_ST(pi,val):
	return pi_criterion(pi=pi,val=val,criterion='ST')

def pi_criterion_MC(pi,val):
	return pi_criterion(pi=pi,val=val,criterion='MC')

def pi_criterion_CH(pi,val):
	return pi_criterion(pi=pi,val=val,criterion='CH')

def pi_criterion_EB(pi,val):
	return pi_criterion(pi=pi,val=val,criterion='EB')

def pi_criterion_RTC(pi,val):
	return pi_criterion(pi=pi,val=val,criterion='RTC')

def pi_criterion_partial_laps(pi,val):
	return pi_criterion_partial(pi=pi,val=val,criterion='laps')

def pi_criterion_partial_ST(pi,val):
	return pi_criterion_partial(pi=pi,val=val,criterion='ST')

def pi_criterion_partial_MC(pi,val):
	return pi_criterion_partial(pi=pi,val=val,criterion='MC')

def pi_criterion_partial_CH(pi,val):
	return pi_criterion_partial(pi=pi,val=val,criterion='CH')
###############################

def success_threshold(res,data=False):
	return template_measure(res=res,measure=pi_success_threshold,global_mean=True,func=np.mean,data=data)

def success_threshold_m(res,data=False):
	return template_measure(res=res,measure=pi_success_threshold,func=np.mean,data=data)

def minsuccess_threshold(res,data=False):
	return template_measure(res=res,measure=pi_success_threshold,global_mean=True,func=min,data=data)

def minsuccess_threshold_m(res,data=False):
	return template_measure(res=res,measure=pi_success_threshold,func=min,data=data)

def meancounts(res,data=False):
	return template_measure(res=res,measure=pi_mincounts,global_mean=True,func=np.mean,data=data)

def meancounts_m(res,data=False):
	return template_measure(res=res,measure=pi_mincounts,func=np.mean,data=data)

def mincounts(res,data=False):
	return template_measure(res=res,measure=pi_mincounts,global_mean=True,func=min,data=data)

def mincounts_m(res,data=False):
	return template_measure(res=res,measure=pi_mincounts,func=min,data=data)

def explo_rate(res,data=False):
	return template_measure(res=res,measure=pi_explo_rate,global_mean=True,data=data)

def explo_rate_m(res,data=False):
	return template_measure(res=res,measure=pi_explo_rate,data=data)

def laps_m(res,data=False):
	return template_measure(res=res,measure=pi_laps,data=data)

def coher(res,data=False):
	return template_measure(res=res,measure=pi_coher,global_mean=True,data=data)

def coher_m(res,data=False):
	return template_measure(res=res,measure=pi_coher,data=data)

def dlaps_m(res,data=False):
	return template_measure(res=res,measure=pi_dlaps,data=data)

def criterion_laps(res,data=False):
	return template_measure(res=res,measure=pi_criterion_laps,data=data)
def criterion_ST(res,data=False):
	return template_measure(res=res,measure=pi_criterion_ST,data=data)
def criterion_MC(res,data=False):
	return template_measure(res=res,measure=pi_criterion_MC,data=data)
def criterion_CH(res,data=False):
	return template_measure(res=res,measure=pi_criterion_CH,data=data)
def criterion_EB(res,data=False):
	return template_measure(res=res,measure=pi_criterion_EB,data=data)
def criterion_RTC(res,data=False):
	return template_measure(res=res,measure=pi_criterion_RTC,data=data)


def similarity_laps(res,data=False):
	return template_measure_xp(res=res,measure=pi_criterion_laps,data=data)
def similarity_ST(res,data=False):
	return template_measure_xp(res=res,measure=pi_criterion_ST,data=data)
def similarity_MC(res,data=False):
	return template_measure_xp(res=res,measure=pi_criterion_MC,data=data)
def similarity_CH(res,data=False):
	return template_measure_xp(res=res,measure=pi_criterion_CH,data=data)
def similarity_EB(res,data=False):
	return template_measure_xp(res=res,measure=pi_criterion_EB,data=data)
def similarity_RTC(res,data=False):
	return template_measure_xp(res=res,measure=pi_criterion_RTC,data=data)

def criterion_partial_laps(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_laps,data=data)
def criterion_partial_ST(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_ST,data=data)
def criterion_partial_MC(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_MC,data=data)
def criterion_partial_CH(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_CH,data=data)


def criterion_laps_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_laps,global_mean=True,data=data)
def criterion_ST_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_ST,global_mean=True,data=data)
def criterion_MC_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_MC,global_mean=True,data=data)
def criterion_CH_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_CH,global_mean=True,data=data)
def criterion_EB_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_EB,global_mean=True,data=data)
def criterion_RTC_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_RTC,global_mean=True,data=data)

def criterion_partial_laps_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_laps,global_mean=True,data=data)
def criterion_partial_ST_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_ST,global_mean=True,data=data)
def criterion_partial_MC_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_MC,global_mean=True,data=data)
def criterion_partial_CH_global(res,data=False):
	return template_measure(res=res,measure=pi_criterion_partial_CH,global_mean=True,data=data)
# def meancounts2(res):
# 	return base2(res=res,absolute=True,func=np.mean)

# def meancounts2_m(res):
# 	return base2_m(res=res,absolute=True,func=np.mean)

# def mincounts2(res):
# 	return base2(res=res,absolute=True,func=min)

# def mincounts2_m(res):
# 	return base2_m(res=res,absolute=True,func=min)


def scores(res,data=False):
	if data:
		return res.scores()
	else:
		return np.mean(res.scores())

def subscores(res,data=False):
	vec = [ssc for ssc in res.subscores() if ssc is not np.nan]
	if data:
		return vec
	else:
		return np.mean(vec,axis=0)

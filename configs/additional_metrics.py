#####classic#####

import json

def perf_tconv(db,xp_uuid):
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	val = cv._Y[0][0]
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	ans = ngal.ngmeth.conv_utils.perf1(tc=val,N=N,M=M)
	cv._Y[0][0] = ans
	return cv

def perf_valconv(db,xp_uuid):
	sr_gr = db.get_graph(xp_uuid=xp_uuid,method='srtheo')
	sr_vec = sr_gr._Y[0]
	t_vec = sr_gr._X[0]
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	val = ngal.ngmeth.conv_utils.perf2(srtheo_vec=sr_vec,t_vec=t_vec,N=N,M=M)
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	cv._Y[0][0] = val
	return cv

additional_metrics = {
	'perf_tconv':{'func':perf_tconv,'dependencies':['conv_time2',]},
	'perf_valconv':{'func':perf_valconv,'dependencies':['srtheo','conv_time2']},
}


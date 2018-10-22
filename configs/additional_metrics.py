#####classic#####

import json

def perf_ct(db,xp_uuid):
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	val = cv._Y[0][0]
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	ans = ngal.ngmeth.conv_utils.perf1(tc=val,N=N,M=M)
	cv._Y[0] = [ans]
	cv.ymin = 0
	cv.ymax = 1
	cv.semilog = True
	return cv

def perf_cs(db,xp_uuid):
	sr_gr = db.get_graph(xp_uuid=xp_uuid,method='srtheo')
	sr_vec = sr_gr._Y[0]
	t_vec = sr_gr._X[0]
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	val = ngal.ngmeth.conv_utils.perf2(srtheo_vec=sr_vec,t_vec=t_vec,N=N,M=M)
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	cv._Y[0] = [val]
	cv.ymin = 0
	cv.ymax = 1
	return cv

def perf_ex(db,xp_uuid):
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	val_cv = cv._Y[0][0]
	maxNd = db.get_graph(xp_uuid=xp_uuid,method='nb_inventions')
	val_Nd = maxNd._Y[0][-1]
	Ninv = val_Nd
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	if np.isnan(cv._Y[0][0]):
		ans = np.nan
	else:
		ans = ngal.ngmeth.conv_utils.perf_ex(ninv=Ninv,N=N,M=M)
	cv._Y[0] = [ans]
	cv.ymin = 0
	cv.ymax = 1
	cv.semilog = True
	return cv


def perf_st(db,xp_uuid):
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	val = cv._Y[0][0]
	maxNd = db.get_graph(xp_uuid=xp_uuid,method='nb_inventions')
	val_Nd = maxNd._Y[0][-1]
	Ninv = val_Nd
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	if np.isnan(cv._Y[0][0]):
		ans = np.nan
	else:
		ans = ngal.ngmeth.conv_utils.perf_st(tc=val,N=N,M=M,ninv=Ninv)
	cv._Y[0] = [ans]
	cv.ymin = 0
	cv.ymax = 1
	cv.semilog = True
	return cv

def perf_ss(db,xp_uuid):
	sr_gr = db.get_graph(xp_uuid=xp_uuid,method='srtheo')
	sr_vec = sr_gr._Y[0]
	t_vec = sr_gr._X[0]
	maxNd = db.get_graph(xp_uuid=xp_uuid,method='nb_inventions')
	val_Nd = maxNd._Y[0][-1]
	Ninv = val_Nd
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	if np.isnan(cv._Y[0][0]):
		val = np.nan
	else:
		val = ngal.ngmeth.conv_utils.perf_ss(srtheo_vec=sr_vec,t_vec=t_vec,N=N,M=M,ninv=Ninv)
	cv._Y[0] = [val]
	cv.ymin = 0
	cv.ymax = 1
	cv.semilog = True
	return cv

def perf_ls(db,xp_uuid):
	maxmem = db.get_graph(xp_uuid=xp_uuid,method='max_mem')
	val = maxmem._Y[0][0]
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	M = cfg['pop_cfg']['env_cfg']['M']
	val = ngal.ngmeth.conv_utils.perf_ls(memmax=val,N=N,M=M)
	cv = db.get_graph(xp_uuid=xp_uuid,method='conv_time2')
	if np.isnan(cv._Y[0][0]):
		val = np.nan
	cv._Y[0][0] = val
	cv.ymin = 0
	cv.ymax = 1
	cv.semilog = True
	return cv

def tmax_rescaled(db,xp_uuid):
	gr = db.get_graph(xp_uuid=xp_uuid,method='max_Nlink_time')
	val = gr._Y[0][0]
	cfg = json.loads(db.get_param(xp_uuid=xp_uuid,param='Config'))
	N = cfg['pop_cfg']['nbagent']
	gr._Y[0][0] = val/N**1.5
	gr.ymax = None
	return gr

additional_metrics = {
	'perf_ct':{'func':perf_ct,'dependencies':['conv_time2',]},
	'perf_cs':{'func':perf_cs,'dependencies':['srtheo','conv_time2']},
	'perf_ex':{'func':perf_ex,'dependencies':['nb_inventions']},
	'perf_st':{'func':perf_st,'dependencies':['conv_time2','nb_inventions']},
	'perf_ss':{'func':perf_ss,'dependencies':['srtheo','conv_time2','nb_inventions']},
	'perf_ls':{'func':perf_ls,'dependencies':['conv_time2','max_mem']},
	'tmax_rescaled':{'func':tmax_rescaled,'dependencies':['max_Nlink_time']},
}


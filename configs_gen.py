configs = [
{"folder":"tests/cogsci",
"imports":["import naminggamesal as ngal"],
"nbiter":4,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"classic",
"tmax_type":"classic",
"params":["N_few","M","active","time_scale"],
"metrics_local":["Nlink","srtheo","N_d"],
"metrics_global":["conv_time","max_mem","max_N_d"],
},

{"folder":"tests/coherence",
"imports":["import naminggamesal as ngal"],
"nbiter":4,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"coherence",
"tmax_type":"classic",
"params":["N_few","M","active","time_scale"],
"metrics_local":["Nlink","srtheo","N_d"],
"metrics_global":["conv_time","max_mem","max_N_d"],
},

{"folder":"tests/halfline",
"imports":["import naminggamesal as ngal"],
"nbiter":4,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"halfline",
"tmax_type":"classic",
"params":["N_few","M","active","time_scale"],
"metrics_local":["Nlink","srtheo","N_d"],
"metrics_global":["conv_time","max_mem","max_N_d"],
},

]



if __name__ == '__main__':
	from experiment_manager.metaexp import metaexp
	for c in configs:
		metaexp.auto_gen(**c)

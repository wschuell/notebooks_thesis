configs = [
{"folder":"tests/cogsci",
"imports":[],
"nbiter":4,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"classic",
"tmax_type":"classic",
"params":["N","M"],
"metrics_local":["Nlink","srtheo","N_d"],
"metrics_global":["conv_time"],
},

{"folder":"tests/coherence",
"imports":[],
"nbiter":4,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"coherence",
"tmax_type":"classic",
"params":["N","M","active","time_scale"],
"metrics_local":["Nlink","srtheo","N_d"],
"metrics_global":["conv_time","mem_max","N_d_max"],
},

]



if __name__ == '__main__':
	from experiment_manager.metaexp import metaexp
	for c in configs:
		metaexp.auto_gen(**c)

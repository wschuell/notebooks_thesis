configs = [
{"folder":"blah",
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

{"folder":"blih/blah/bloh",
"imports":[],
"nbiter":4,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"classic",
"tmax_type":"classic",
"params":["N","M"],
"metrics_local":[],
"metrics_global":["conv_time"],
},

]



if __name__ == '__main__':
	from experiment_manager.metaexp import metaexp
	for c in configs:
		metaexp.auto_gen(**c)

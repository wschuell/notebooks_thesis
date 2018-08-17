configs = [
{"folder":"tests/cogsci",
"imports":["import naminggamesal as ngal"],
"nbiter":4,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"classic",
"tmax_type":"scaling",
"params":["N_few","M_100","active","time_scale_few",'W_inf','wordchoice'],
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
"params":["N_few","M_100","active","time_scale_few","W_inf"],
"metrics_local":["Nlink","srtheo","N_d"],
"metrics_global":["conv_time","max_mem","max_N_d"],
},

{"folder":"tests/halfline",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"halfline",
"tmax_type":"ultralong",
"params":["N_halfline","M_few_low","active","time_scale_few"],
"metrics_local":["Nlink","srtheo","N_d","line_border","line_border_width","line_border_abs"],
"metrics_global":["conv_time","max_mem","max_N_d"],
},

]



if __name__ == '__main__':
	from experiment_manager.metaexp import metaexp
	for c in configs:
		metaexp.auto_gen(**c)

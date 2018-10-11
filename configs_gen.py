configs = [

######## THESIS

### NG ####
{"folder":"chapters/naminggame/normal",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"basic",
"tmax_type":"scaling_bigmax",
"params":["N","M",'W_inf_true'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/naminggame/VU",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"basic",
"tmax_type":"scaling_bigmax",
"params":["N","M_1",'W_inf_true','vu_type_basic'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/naminggame/wordchoice",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"basic",
"tmax_type":"scaling_bigmax",
"params":["N","M_1",'W_inf_true','wordchoice'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/naminggame/homonymy",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"basic",
"tmax_type":"scaling_bigmax",
"params":["N","M_100",'W_inf_all'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/naminggame/accpol",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"basic",
"tmax_type":"scaling_bigmax",
"params":["N","M_1",'W_inf_true','accpol'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},
###### ATC constraints ######

{"folder":"chapters/topicchoice/exploexplo",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all','strat_type_exploexplo','vu_type_minimal'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/explobias",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all','strat_type_explobiased'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/STW",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all','strat_type_ST','threshold_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},


{"folder":"chapters/topicchoice/STN",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_few_imit","M_100",'strat_type_ST','threshold_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/ST2",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'strat_type_ST2','threshold_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/ST_HC",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'strat_type_ST','threshold_param','interact_type_hearerschoice'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/MCW",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all','strat_type_MC','mincounts_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},


{"folder":"chapters/topicchoice/MCN",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_few_imit","M_100",'strat_type_MC','mincounts_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/MC2",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'strat_type_MC2','mincounts_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/MC_HC",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'strat_type_MC','mincounts_param','interact_type_hearerschoice'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/IGW",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all','strat_type_infogain','temperature_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},


{"folder":"chapters/topicchoice/IGN",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_few_imit","M_100",'strat_type_infogain','temperature_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/chunksW",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all','strat_type_chunks','chunks_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},


{"folder":"chapters/topicchoice/chunksN",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_few_imit","M_100",'strat_type_chunks','chunks_param'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/chunks_HC",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'strat_type_chunks','chunks_param','interact_type_hearerschoice'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/comparison",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N","M_100",'strat_type_compare_atc'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/comparisonHC",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N","M_100",'strat_type_compare_atc','interact_type_hearerschoice'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/topicchoice/comparisonM",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_scale",'strat_type_compare_atc'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},


###### LAPS ######

{"folder":"chapters/laps/previous",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"ATC",
"tmax_type":"scaling_bigmax",
"params":["N","M_100",'strat_type_compare_atc','vu_type_minimal_imit'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/normal",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_few","M_100","memory_policy"],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local','entropy_final'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/lapsWT",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all',"strat_type_laps",'timescale_laps'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/lapsNT",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_few","M_100","strat_type_laps",'timescale_laps'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/lapsHC",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100","strat_type_laps",'timescale_laps'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/lapsT2",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100","strat_type_laps",'timescale_laps','gamma'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/entropyWT",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all',"strat_type_entropy",'timescale_laps','gamma_1'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local','entropy_final'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/entropyNT",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_few","M_100","strat_type_entropy",'timescale_laps','gamma_1'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local','entropy_final'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/entropyT2",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100","strat_type_entropy",'timescale_laps','gamma'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local','entropy_final'],
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},


# {"folder":"chapters/laps/lapsNTimitation",
# "imports":["import naminggamesal as ngal"],
# "nbiter":8,
# "exec_type":"avakas",
# "plt_settings":"classic",
# "func_type":"laps",
# "tmax_type":"scaling_bigmax",
# "params":["N_few","M_100","strat_type_laps",'timescale_laps','vu_type_imitation'],
# "metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
# "metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
# },

#{"folder":"chapters/laps/NMB_WT",
#"imports":["import naminggamesal as ngal"],
#"nbiter":8,
#"exec_type":"avakas",
#"plt_settings":"classic",
#"func_type":"laps",
#"tmax_type":"scaling_bigmax",
#"params":["N_100","M_100",'W_inf_all','wordchoice_membased','timescale_laps'],
#"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
#"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
#},

# {"folder":"chapters/laps/NMB_NT",
# "imports":["import naminggamesal as ngal"],
# "nbiter":8,
# "exec_type":"avakas",
# "plt_settings":"classic",
# "func_type":"laps",
# "tmax_type":"scaling_bigmax",
# "params":["N_few","M_100",'wordchoice_membased','timescale_laps'],
# "metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
# "metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
# },

{"folder":"chapters/laps/lapsscaling",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N","M_100","strat_type_laps"],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

# {"folder":"chapters/laps/lapsscaling_MB",
# "imports":["import naminggamesal as ngal"],
# "nbiter":8,
# "exec_type":"avakas",
# "plt_settings":"classic",
# "func_type":"laps",
# "tmax_type":"scaling_bigmax",
# "params":["N","M_100","strat_type_laps","wordchoice_membased"],
# "metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
# "metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
# },
{"folder":"chapters/laps/coherenceWT",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100",'W_inf_all',"strat_type_coherence",'timescale_laps'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/coherenceNT",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N","M_10_100","strat_type_coherence",'timescale_laps_coher'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

{"folder":"chapters/laps/coherenceT2",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100","strat_type_coherence2",'timescale_laps','gamma'],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

# {"folder":"chapters/laps/coherenceNTimitation",
# "imports":["import naminggamesal as ngal"],
# "nbiter":8,
# "exec_type":"avakas",
# "plt_settings":"classic",
# "func_type":"laps",
# "tmax_type":"scaling_bigmax",
# "params":["N_few","M_100","strat_type_coherence",'timescale_laps','vu_type_imitation'],
# "metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
# "metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
# },
{"folder":"chapters/laps/coherencescaling",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"laps",
"tmax_type":"scaling_bigmax",
"params":["N","M_100","strat_type_coherence"],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
},

# {"folder":"chapters/laps/coherencescaling_MB",
# "imports":["import naminggamesal as ngal"],
# "nbiter":8,
# "exec_type":"avakas",
# "plt_settings":"classic",
# "func_type":"laps",
# "tmax_type":"scaling_bigmax",
# "params":["N","M_100","strat_type_coherence","wordchoice_membased"],
# "metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
# "metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',],
# },



###### replace ######

{"folder":"chapters/replace/replace",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"replace",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100","rate_replace","accpol_replace"],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',"srtheo_end","srtheo_end_smooth"],
},

{"folder":"chapters/replace/decay",
"imports":["import naminggamesal as ngal"],
"nbiter":8,
"exec_type":"avakas",
"plt_settings":"classic",
"func_type":"replace",
"tmax_type":"scaling_bigmax",
"params":["N_100","M_100","rate_replace","accpol_replace","agent_init_converged"],
"metrics_local":["Nlink","srtheo","N_d",'N_meanings','N_words','actual_successrate','srtheo_local','decay_coherence'],#'entropy_extrapol',
"metrics_global":["conv_time","conv_time2","max_mem","max_N_d",'max_N_d_time','max_Nlink_time','tdiff_d','tdiff_w','tdiff_wd',"srtheo_end","srtheo_end_smooth",'decay_time','decay_time_total'],
},



]



if __name__ == '__main__':
	from experiment_manager.tools import metaexp_gen
	cfg_gen = metaexp_gen.ConfigGenerator()
	for c in configs:
		cfg_gen.auto_gen(figures_dir=True,**c)

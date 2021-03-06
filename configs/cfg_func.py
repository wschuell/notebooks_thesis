
###basic###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"minimal" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": "naive" #random topic choice: changed if active is True
            },
            "nbagent": {{% N,100 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,100 %}}, #number of meanings
              "W": {{% M,100 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": "speakerschoice"
            }
          }
        }
    if {{% W_inf,True %}}:
        if not isinstance({{% W_inf,True %}},bool):
            base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,100 %}} * {{% W_inf,True %}}
        else:
            base_cfg['pop_cfg']['env_cfg']['W'] = base_cfg['pop_cfg']['env_cfg']['M']*{{% N,100 %}}
            base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':base_cfg['pop_cfg']['env_cfg']['M'],'W_range':base_cfg['pop_cfg']['env_cfg']['M']*{{% N,40 %}}}
    elif {{% W,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = max({{% W,0 %}},base_cfg['pop_cfg']['env_cfg']['M'])
    if {{% optimized,False %}}:
        base_cfg['pop_cfg']['optimized_run'] = True
    if {{% accpol,False %}}:
        base_cfg['pop_cfg']['strat_cfg']['vu_cfg'] = {'vu_type':'acceptance_beta','beta':0.4,'subvu_cfg':{'vu_type':{{% vu_type,'minimal' %}}}}

    return base_cfg

###ATC###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"imitation" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": {{% strat_type,"naive" %}} #random topic choice: changed if active is True
            },
            "nbagent": {{% N,100 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,100 %}}, #number of meanings
              "W": {{% M,100 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": {{% interact_type,"speakerschoice" %}}
            }
          }
        }
    if {{% W_inf,True %}}:
        if not isinstance({{% W_inf,True %}},bool):
            base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,100 %}} * {{% W_inf,True %}}
        else:
            base_cfg['pop_cfg']['env_cfg']['W'] = base_cfg['pop_cfg']['env_cfg']['M']*{{% N,100 %}}
            base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':base_cfg['pop_cfg']['env_cfg']['M'],'W_range':base_cfg['pop_cfg']['env_cfg']['M']*{{% N,40 %}}}
    elif {{% W,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = max({{% W,0 %}},base_cfg['pop_cfg']['env_cfg']['M'])
    if {{% optimized,False %}}:
        base_cfg['pop_cfg']['optimized_run'] = True
    if base_cfg['pop_cfg']['strat_cfg']['strat_type'][:17] == 'success_threshold':
        if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'speakerschoice':
            base_cfg['pop_cfg']['strat_cfg']['threshold_explo'] = {{% threshold_param,0.8 %}}
        else:
            base_cfg['pop_cfg']['strat_cfg']['threshold_explo'] = {{% threshold_param,0.2 %}}
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:9] == 'mincounts':
        if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'speakerschoice':
            base_cfg['pop_cfg']['strat_cfg']['mincounts'] = int({{% N,100 %}}*{{% mincounts_param,0.6 %}})
        else:
            base_cfg['pop_cfg']['strat_cfg']['mincounts'] = int({{% N,100 %}}*{{% mincounts_param,0.2 %}})
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:16] == 'decision_vector_':
        if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'speakerschoice':
            base_cfg['pop_cfg']['strat_cfg']['Temp'] = {{% temp_param,0.001 %}}
        else:
            base_cfg['pop_cfg']['strat_cfg']['Temp'] = {{% temp_param,0.001 %}}
    if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'hearerschoice' and base_cfg['pop_cfg']['strat_cfg']['strat_type'] == 'decision_vector_gainsoftmax':
        base_cfg['pop_cfg']['strat_cfg']['strat_type'] == 'decision_vector_gainsoftmax_hearer'
    if base_cfg['pop_cfg']['strat_cfg']['strat_type'][-6:] == 'chunks':
        base_cfg['pop_cfg']['strat_cfg']['N'] = {{% N,100 %}}

    return base_cfg

###laps###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"minimal" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": {{% strat_type,"naive" %}}, #random topic choice: changed if active is True
            },
            "nbagent": {{% N,100 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,100 %}}, #number of meanings
              "W": {{% M,100 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": {{% interact_type,"speakerschoice" %}}
            }
          }
        }
    if {{% W_inf,True %}}:
        if not isinstance({{% W_inf,True %}},bool):
            base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,100 %}} * {{% W_inf,True %}}
        else:
            base_cfg['pop_cfg']['env_cfg']['W'] = base_cfg['pop_cfg']['env_cfg']['M']*{{% N,100 %}}
            base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':base_cfg['pop_cfg']['env_cfg']['M'],'W_range':base_cfg['pop_cfg']['env_cfg']['M']*{{% N,40 %}}}
    elif {{% W,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = max({{% W,0 %}},base_cfg['pop_cfg']['env_cfg']['M'])
    if {{% optimized,False %}}:
        base_cfg['pop_cfg']['optimized_run'] = True
    if base_cfg['pop_cfg']['strat_cfg']['strat_type'][:17] == 'success_threshold':
        if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'speakerschoice':
            base_cfg['pop_cfg']['strat_cfg']['threshold_explo'] = {{% threshold_param,0.8 %}}
        elif {{% M,100 %}} == 5 and {{% W,100 %}} == 6:
            base_cfg['pop_cfg']['strat_cfg']['threshold_explo'] = {{% threshold_param,0.5 %}}
        else:
            base_cfg['pop_cfg']['strat_cfg']['threshold_explo'] = {{% threshold_param,0.2 %}}
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:9] == 'mincounts':
        if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'speakerschoice':
            base_cfg['pop_cfg']['strat_cfg']['mincounts'] = int({{% N,100 %}}*{{% mincounts_param,0.6 %}})
        elif {{% M,100 %}} == 5 and {{% W,100 %}} == 6:
            base_cfg['pop_cfg']['strat_cfg']['mincounts'] = 0.9
        else:
            base_cfg['pop_cfg']['strat_cfg']['mincounts'] = int({{% N,100 %}}*{{% mincounts_param,0.2 %}})
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:16] == 'decision_vector_':
        if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'speakerschoice':
            base_cfg['pop_cfg']['strat_cfg']['Temp'] = {{% temp_param,0.001 %}}
        else:
            base_cfg['pop_cfg']['strat_cfg']['Temp'] = {{% temp_param,0.001 %}}
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:7] == 'lapsmax':
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'gamma':{{% gamma,0.01 %}},'time_scale':{{% time_scale,2 %}},                  "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:9] == 'coherence':
        if {{% time_scale,False %}}:
            time_scale = {{% time_scale,2 %}}
        else:
            time_scale = 1 + math.ceil(np.log2({{% N,100 %}}))
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'time_scale':time_scale,                  "memory_policies": [{
                      "time_scale": time_scale,
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'] == 'naive_smart':
        base_cfg['pop_cfg']['strat_cfg']['strat_type'] = 'naive'
        base_cfg['pop_cfg']['strat_cfg']['wordchoice_cfg'] = {'wordchoice_type':'play_smart'}
    if {{% memory_policy,False %}} or {{% wordchoice,False %}}=='membased':
        base_cfg['pop_cfg']['strat_cfg'].update(**{"memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }],})

    if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'hearerschoice' and base_cfg['pop_cfg']['strat_cfg']['strat_type'] == 'decision_vector_gainsoftmax':
        base_cfg['pop_cfg']['strat_cfg']['strat_type'] == 'decision_vector_gainsoftmax_hearer'
    if base_cfg['pop_cfg']['strat_cfg']['strat_type'][-6:] == 'chunks':
        base_cfg['pop_cfg']['strat_cfg']['N'] = {{% N,100 %}}
    return base_cfg

###replace###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"minimal" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": {{% strat_type,"naive" %}}, #random topic choice: changed if active is True
            },
            "nbagent": {{% N,100 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,100 %}}, #number of meanings
              "W": {{% M,100 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": {{% interact_type,"speakerschoice" %}}
            },
              "evolution_cfg":{
                  "evolution_type":"replace",
                  "rate":{{% rate,10 %}}*{{% N,100 %}}/2,
              },
              "agent_init_cfg":{
                  "agent_init_type":{{% agent_init,"agent_init" %}},
              }
          }
        }
    if {{% W_inf,True %}}:
        if not isinstance({{% W_inf,True %}},bool):
            base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,100 %}} * {{% W_inf,True %}}
        else:
            base_cfg['pop_cfg']['env_cfg']['W'] = base_cfg['pop_cfg']['env_cfg']['M']*{{% N,100 %}}
            #if not {{% agent_init,True %}}:
            base_cfg['pop_cfg']['agent_init_cfg']['sub_agent_init_cfg'] = {'agent_init_type':'own_words','M':base_cfg['pop_cfg']['env_cfg']['M'],'W_range':base_cfg['pop_cfg']['env_cfg']['M']*{{% N,40 %}}}
    elif {{% W,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = max({{% W,0 %}},base_cfg['pop_cfg']['env_cfg']['M'])
    if {{% optimized,False %}}:
        base_cfg['pop_cfg']['optimized_run'] = True
    if base_cfg['pop_cfg']['strat_cfg']['strat_type'][:17] == 'success_threshold':
        base_cfg['pop_cfg']['strat_cfg']['threshold_explo'] = {{% threshold_param,0.9 %}}
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:9] == 'mincounts':
        base_cfg['pop_cfg']['strat_cfg']['mincounts'] = int({{% N,100 %}}*{{% mincounts_param,0.9 %}})
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:27] == 'decision_vector_gainsoftmax':
        base_cfg['pop_cfg']['strat_cfg']['Temp'] = {{% temp_param,0.9 %}}
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:7] == 'lapsmax':
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'gamma':{{% gamma,0.01 %}},'time_scale':{{% time_scale,2 %}},                  "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
    elif base_cfg['pop_cfg']['strat_cfg']['strat_type'][:9] == 'coherence':
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'time_scale':{{% time_scale,2 %}},                  "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
    if {{% memory_policy,False %}} or {{% wordchoice,False %}}=='membased':
        base_cfg['pop_cfg']['strat_cfg'].update(**{"memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }],})
    if {{% accpol,False %}}:
        base_cfg['pop_cfg']['strat_cfg']['vu_cfg'] = {'vu_type':{{% 'acceptance_beta',accpol %}},'subvu_cfg':{'vu_type':{{% vu_type,'minimal' %}}}}
        if {{% accpol,False %}} == 'acceptance_beta' :
            base_cfg['pop_cfg']['strat_cfg']['vu_cfg']['beta']= {{% beta,0.3 %}}
        elif {{% accpol,False %}} in ['acceptance_tsmax_new','acceptance_coherencemax'] :
            if base_cfg['pop_cfg']['strat_cfg']['strat_type'][:7] in ['coheren','lapsmax']:
                base_cfg['pop_cfg']['strat_cfg']['vu_cfg']['no_mp'] = True
            else:
                base_cfg['pop_cfg']['strat_cfg']['vu_cfg']['mem_policy'] = { 'mem_type':'interaction_counts_sliding_window_local','time_scale':{{% time_scale,2 %}} }
    return base_cfg

###classic###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type":  {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"minimal" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": "naive" #random topic choice: changed if active is True
            },
            "nbagent": {{% N,40 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,40 %}}, #number of meanings
              "W": {{% M,40 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": "speakerschoice"
            }
          }
        }
    if {{% active,True %}}:
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'strat_type':'lapsmax_mab_explothreshold','bandit_type':'bandit_laps','gamma':{{% gamma,0.01 %}},'time_scale':{{% time_scale,2 %}},
                "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
    if base_cfg['pop_cfg']['nbagent'] > 100 and base_cfg['pop_cfg']['env_cfg']['M'] > 100:
        base_cfg['pop_cfg']['env_cfg']['M'] = 100
    if {{% W_inf,True %}}:
        if not isinstance({{% W_inf,True %}},bool):
            base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,100 %}} * {{% W_inf,True %}}
        else:
            base_cfg['pop_cfg']['env_cfg']['W'] = base_cfg['pop_cfg']['env_cfg']['M']*{{% N,100 %}}
            base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':base_cfg['pop_cfg']['env_cfg']['M'],'W_range':base_cfg['pop_cfg']['env_cfg']['M']*{{% N,40 %}}}
    elif {{% W,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = max({{% W,0 %}},base_cfg['pop_cfg']['env_cfg']['M'])
    if {{% optimized,False %}}:
        base_cfg['pop_cfg']['optimized_run'] = True

    return base_cfg

###old###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type":  {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"imitation" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": {{% strat_type,"naive" %}} #random topic choice: changed if active is True
            },
            "nbagent": {{% N,40 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,40 %}}, #number of meanings
              "W": {{% M,40 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": {{% interact_type,"speakerschoice" %}},
            }
          }
        }
    if base_cfg['pop_cfg']['nbagent'] > 100 and base_cfg['pop_cfg']['env_cfg']['M'] > 100:
        base_cfg['pop_cfg']['env_cfg']['M'] = 100
    if base_cfg['pop_cfg']['interact_cfg']['interact_type'] == 'hearerschoice' and base_cfg['pop_cfg']['strat_cfg']['strat_type'] == 'decision_vector_gainsoftmax':
        base_cfg['pop_cfg']['strat_cfg']['strat_type'] == 'decision_vector_gainsoftmax_hearer'
    if {{% W_inf,True %}}:
        if not isinstance({{% W_inf,True %}},bool):
            base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,100 %}} * {{% W_inf,True %}}
        else:
            base_cfg['pop_cfg']['env_cfg']['W'] = base_cfg['pop_cfg']['env_cfg']['M']*{{% N,100 %}}
            base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':base_cfg['pop_cfg']['env_cfg']['M'],'W_range':base_cfg['pop_cfg']['env_cfg']['M']*{{% N,40 %}}}
    elif {{% W,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = max({{% W,0 %}},base_cfg['pop_cfg']['env_cfg']['M'])
    if {{% optimized,False %}}:
        base_cfg['pop_cfg']['optimized_run'] = True

    return base_cfg

###coherence###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type":  {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"minimal" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": "naive" #random topic choice: changed if active is True
            },
            "nbagent": {{% N,10 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,20 %}}, #number of meanings
              "W": {{% M,20 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": "speakerschoice"
            }
          }
        }
    if {{% active,True %}}:
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'strat_type':{{% strat_type,'coherence' %}},'time_scale':{{% time_scale,2 %}},
                "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }],})
    if base_cfg['pop_cfg']['nbagent'] > 100 and base_cfg['pop_cfg']['env_cfg']['M'] > 100:
        base_cfg['pop_cfg']['env_cfg']['M'] = 100
    if {{% W_inf,True %}}:
        if not isinstance({{% W_inf,True %}},bool):
            base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,100 %}} * {{% W_inf,True %}}
        else:
            base_cfg['pop_cfg']['env_cfg']['W'] = base_cfg['pop_cfg']['env_cfg']['M']*{{% N,100 %}}
            base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':base_cfg['pop_cfg']['env_cfg']['M'],'W_range':base_cfg['pop_cfg']['env_cfg']['M']*{{% N,40 %}}}
    elif {{% W,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = max({{% W,0 %}},base_cfg['pop_cfg']['env_cfg']['M'])
    if {{% optimized,False %}}:
        base_cfg['pop_cfg']['optimized_run'] = True
    return base_cfg

###halfline###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type":  {{% voc_type,'2dictdict' %}},
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": {{% vu_type,"minimal" %}}
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": {{% wordchoice,"random" %}}
              },
              "strat_type": "naive" #random topic choice: changed if active is True
            },
            "nbagent": {{% N,10 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,20 %}}, #number of meanings
              "W": {{% W,100 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": "speakerschoice"
            },
            "topology_cfg": {
              'topology_type':'line'
            },
            "agent_init_cfg": {
              'agent_init_type':'converged_halfline'
            },
            "agentpick_cfg": {
              'agentpick_type':'neighbor_pick'
            },
          }
        }
    if {{% active,True %}}:
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'strat_type':'coherence','time_scale':{{% time_scale,2 %}},
                "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }],})
    return base_cfg


###theory###

    base_cfg = {
          "step": 1,
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": '2dictdict',
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": "minimal"
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
          "wordchoice_cfg": {
            "wordchoice_type": "random"
              },
              "strat_type": "naive"
            },
            "nbagent": {{% N,10 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": 1, #number of meanings
              "W": {{% N,10 %}}  #number of words
            },
            "interact_cfg": {
              "interact_type": "speakerschoice"
            },
            "agent_init_cfg": {
              "agent_init_type": "own_words",
              "M":1,
              "W_range":{{% N,10 %}},

            }
          }
        }

    return base_cfg

###userxp###

    base_cfg = {
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
                  "success_type": "global_norandom"
              },
              "strat_type": "naive",
              "allow_idk":True,
          },
          "nbagent": {{% N,5 %}},

            "agent_init_cfg": {
              "agent_init_type": "onedifferent",
                'first_ag_cfg':{
                    #'strat_cfg':{'strat_type':'naive'},
                    'strat_cfg':{'strat_type':{{% strat_type,'naive' %}},'vu_cfg':{'vu_type':'minimal'}},
                    'memory_policies':[{'mem_type':'past_interactions_all'}]}
                    },
          "env_cfg": {
              "env_type": "simple",
              "M": {{% M,5 %}},
              "W": {{% W,6 %}}
          },
          "interact_cfg": {
              "interact_type": "speakerschoice"
          }
      }
    }

    if {{% strat_type,'naive' %}} == 'success_threshold_wise':
        base_cfg['pop_cfg']['strat_cfg']['threshold_explo'] = 0.5
    elif {{% strat_type,'naive' %}} == 'mincounts':
        base_cfg['pop_cfg']['strat_cfg']['mincounts'] = 0.9
    # elif {{% strat_type,'naive' %}} == 'lapsmax_mab_explothreshold':
    #     base_cfg['pop_cfg']['strat_cfg']['time_scale'] = 2
    elif {{% strat_type,'naive' %}} == 'coherence_last':
        base_cfg['pop_cfg']['strat_cfg']['time_scale'] = 3

    return base_cfg


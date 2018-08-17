
###classic###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": 'matrix_new'
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
                'strat_type':'lapsmax_mab_explothreshold','bandit_type':'bandit_laps','gamma':{{% gamma,0.1 %}},'time_scale':{{% time_scale,2 %}},
                "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
    if {{% W_inf,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,20 %}}*{{% N,10 %}}
        base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':{{% M,20 %}},'W_range':{{% M,20 %}}*{{% N,10 %}}}

    return base_cfg

###coherence###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": 'matrix_new'
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
                'strat_type':'coherence','time_scale':{{% time_scale,2 %}}, 
                "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }],})
    if {{% W_inf,False %}}:
        base_cfg['pop_cfg']['env_cfg']['W'] = {{% M,20 %}}*{{% N,10 %}}
        base_cfg['pop_cfg']['agent_init_cfg'] = {'agent_init_type':'own_words','M':{{% M,20 %}},'W_range':{{% M,20 %}}*{{% N,10 %}}}
    return base_cfg

###halfline###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": 'matrix_new'
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


###classic###

    base_cfg = {
          "step": "log_improved",
          "pop_cfg": {
            "voc_cfg": {
          "voc_type": 'matrix_new'
            },
        "strat_cfg": {
          "vu_cfg": {
            "vu_type": "minimal"
          },
          "success_cfg": {
            "success_type": "global_norandom"
              },
              "strat_type": "naive" #random topic choice: changed if active is True
            },
            "nbagent": {{% N,10 %}}, #population size
            "env_cfg": {
              "env_type": "simple",
              "M": {{% M,20 %}}, #number of meanings
              "W": 500  #number of words
            },
            "interact_cfg": {
              "interact_type": "speakerschoice"
            }
          }
        }
    if {{% active,True %}}:
        base_cfg['pop_cfg']['strat_cfg'].update(**{
                'strat_type':'lapsmax_mab_explothreshold','bandit_type':'bandit_laps','gamma':{{% gamma,1. %}},'time_scale':{{% time_scale,2 %}},
                "memory_policies": [{
                      "time_scale": {{% time_scale,2 %}},
                      "mem_type": "interaction_counts_sliding_window_local"
                        }], })
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
            "vu_type": "minimal"
          },
          "success_cfg": {
            "success_type": "global_norandom"
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
                'strat_type':'coherence','time_scale':{{% time_scale,2 %}},, })
    return base_cfg

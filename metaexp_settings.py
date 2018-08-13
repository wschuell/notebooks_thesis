import experiment_manager as xp_man
import naminggamesal as ngal

from experiment_manager.metaexp.metaexp import MetaExperiment


#### Function to construct the coinfiguration of each simulation, depending on a few parameters, described below ####

def xp_cfg(N,M,vu_type):
    W=M
    base_xp_cfg = {
    'pop_cfg':{
        'voc_cfg':{'voc_type':'matrix_new'},
        'strat_cfg':{'strat_type':'naive',
                    'vu_cfg':{'vu_type':vu_type}},
        'interact_cfg':{'interact_type':'speakerschoice'},
        'env_cfg':{'env_type':'simple','M':M,'W':W},
        'nbagent':N
    },
    'step':'log_improved'
    
}
    return base_xp_cfg

#### Function to determine the number of time steps for each simulation ####

def Tmax_func(N,M,vu_type):
  return 4.5*N**(1.6)*M


#### Number of trials per distinct configuration ####

nbiter = 8


#### Description of the parameters of experiment configuration ####

params = {'N':{'default_value':20,'label':'population size','values':[20,50,100,200],'min':0},
          'M':{'default_value':20,'label':'#meanings','values':[20,50,100,200],'min':0},
          #'W':{'default_value':20,'label':'#words','values':[20,40],'min':0},
          'vu_type':{'default_value':'minimal','values':['minimal','imitation','BLIS']},
        }



#### Measures, to be found in naminggamesal.ngmeth ####

local_measures = {'srtheo':{'label':'Theoretical Communicative Success'},
            'Nlink':{'unit_label':'#associations','label':'Local Complexity'},
            'N_d':{'unit_label':'#associations','label':'Global Complexity'},
            'executed_time':{'unit_label':'execution time (s)','label':'Execution Time'},}
global_measures = {'conv_time':{'unit_label':'#interactions','label':'Convergence Time'},
                    'max_mem':{'unit_label':'#associations','label':'Maximum Local Complexity'},
                    'max_N_d':{'unit_label':'#associations','label':'Maximum Global Complexity'},
                    }


#### Defining the MetaExperiment object, containing all this information ####

meta_exp = MetaExperiment(params=params,
              local_measures=local_measures,
              global_measures=global_measures,
              xp_cfg=xp_cfg,
              Tmax_func=Tmax_func,
              default_nbiter=nbiter,
              time_label='#interactions',
              time_short_label='T',
              #time_max=80000,
              time_min=0)

#### Parameters for running the simulations. By default, using all available cores on local computer ####


jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True}
jq_cfg_plafrim = {'jq_type':'plafrim','erase':True,
         'modules':['language/python/3.5.2'],
         'virtual_env':'testpy3',
'requirements' : [
    '-e git+https://github.com/wschuell/experiment_manager.git@origin/develop#egg=experiment_manager',
    '-e git+https://github.com/flowersteam/naminggamesal.git@origin/develop#egg=naminggamesal'
]}
jq_cfg_avakas = {'jq_type':'avakas','erase':True,
         'modules':['python3/3.6.0'],
         'virtual_env':'testpy3',
'requirements' : [
    '-e git+ssh://git@github.com/wschuell/experiment_manager.git@develop#egg=experiment_manager',
    '-e git+ssh://git@github.com/flowersteam/naminggamesal.git@develop#egg=naminggamesal'
]}



db = ngal.ngdb.NamingGamesDB(do_not_close=True)
meta_exp.set_db(db)

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)
#meta_exp.set_batch(jq_cfg=jq_cfg_plafrim,estimated_time=1200)
meta_exp.set_batch(jq_cfg=jq_cfg_avakas,estimated_time=1200)

meta_exp.default_batch='avakas'
#meta_exp.default_batch='local_multiprocess'



##### Making matplotlib more readable #####
def plt_settings():
    import pylab
    import matplotlib
    import matplotlib.pyplot as plt


    fontsize = 15
    matplotlib.rcParams['font.size'] = fontsize
    matplotlib.rcParams['xtick.labelsize'] = fontsize
    matplotlib.rcParams['ytick.labelsize'] = fontsize
    matplotlib.rcParams['axes.titlesize'] = fontsize+5
    matplotlib.rcParams['axes.labelsize'] = fontsize
    matplotlib.rcParams['legend.fontsize'] = fontsize
    matplotlib.rcParams['figure.figsize'] = 8,5.5
    pylab.rcParams['figure.figsize'] = (8.0, 5.5)
    plt.rcParams['figure.figsize'] = (8.0, 5.5)
    matplotlib.rcParams['lines.linewidth'] = 3

if __name__ == '__main__':
    meta_exp.run()
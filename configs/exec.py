#####avakas#####


jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True}

jq_cfg_avakas = {'jq_type':'avakas','erase':True,'reinit_missubmitted_times':1,
         'modules':['python3/3.6.0'],
         'virtual_env':'testpy3',
'requirements' : [
    '-e git+ssh://git@github.com/wschuell/experiment_manager.git@develop#egg=experiment_manager',
    '-e git+ssh://git@github.com/flowersteam/naminggamesal.git@develop#egg=naminggamesal'
]}

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)
meta_exp.set_batch(jq_cfg=jq_cfg_avakas,estimated_time=1200)

meta_exp.default_batch='avakas'
meta_exp.profile_test = True

#####avakas_profiling#####


jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True}

jq_cfg_avakas = {'jq_type':'avakas','erase':False,'force_profiling':True,
         'modules':['python3/3.6.0'],
         'virtual_env':'testpy3',
'requirements' : [
    '-e git+ssh://git@github.com/wschuell/experiment_manager.git@develop#egg=experiment_manager',
    '-e git+ssh://git@github.com/flowersteam/naminggamesal.git@develop#egg=naminggamesal'
]}

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)
meta_exp.set_batch(jq_cfg=jq_cfg_avakas,estimated_time=1200)

meta_exp.default_batch='avakas'

#####plafrim#####

jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True}

jq_cfg_plafrim = {'jq_type':'plafrim','erase':True,
         'modules':['language/python/3.5.2'],
         'virtual_env':'testpy3',
'requirements' : [
    '-e git+https://github.com/wschuell/experiment_manager.git@origin/develop#egg=experiment_manager',
    '-e git+https://github.com/flowersteam/naminggamesal.git@origin/develop#egg=naminggamesal'
]}

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)
meta_exp.set_batch(jq_cfg=jq_cfg_plafrim,estimated_time=1200)

meta_exp.default_batch='plafrim'
meta_exp.profile_test = True

#####local_multiprocess#####

jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True}

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)

meta_exp.default_batch='local_multiprocess'
#####local_multiprocess_profiling#####

jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True,'force_profiling':True}

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)

meta_exp.default_batch='local_multiprocess'

#####local#####

jq_cfg_local = {'jq_type':'local','erase':True}
jq_cfg_local_multi = {'jq_type':'local_multiprocess','erase':True}

meta_exp.set_batch(jq_cfg=jq_cfg_local)
meta_exp.set_batch(jq_cfg=jq_cfg_local_multi)

meta_exp.default_batch='local'

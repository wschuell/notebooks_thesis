######header######


from metaexp_settings import meta_exp,plot_settings,savefig
import matplotlib.pyplot as plt


#######chapters/_otherfigs/decvec#######

import naminggamesal as ngal

M=100
N=50
W=2*M
plot_settings('margin')
plt.plot(list(range(M+1)),[(M-i)/(M) for i in range(M+1)],label='Random')
plt.plot(list(range(M+1)),[(1)/(i+1) for i in range(M+1)],label='ExploBiased')
plt.xlabel('$\mu$')
plt.ylabel('$D_{\mu}$')

plt.xlim(0,M)
plt.ylim(0,1)
plt.legend()
# plt.title('Decision Vector')
savefig(None,'decvec_explobiased',plot_mode='margin')

plt.figure()
# M=100
# W=20
Temp = [0.01,0.1,1]
for t in Temp:
    plt.plot(list(range(M+1)),ngal.ngmeth_utils.decvec_utils.decvec4_softmax_from_MW(M, W, t),label=str(t))
plt.xlabel('$\mu$')
plt.ylabel('$D_{\mu}$')
plt.xlim(0,M)
plt.ylim(0,1)
plt.legend()
# plt.title('Decision Vector')
savefig(None,'decvec_infogain',plot_mode='margin')


plt.figure()
# M=100
# W=200
# N=10
plt.plot(list(range(M+1)),ngal.ngmeth_utils.decvec_utils.decvec_chunks_from_MW(M=M, W=W, N=N,Temp=0.001))
plt.xlabel('$\mu$')
plt.ylabel('$D_{\mu}$')
plt.xlim(0,M)
plt.ylim(0,1)
# plt.title('Decision Vector')
savefig(None,'decvec_chunks',plot_mode='margin')

plt.figure()
M=12
W=24
N=10
plot_settings('half')
plt.plot(list(range(M+1)),ngal.ngmeth_utils.decvec_utils.decvec_chunks_from_MW(M=M, W=W, N=N,Temp=0.001))
plt.xlabel('$\mu$')
plt.ylabel('$D_{\mu}$')
plt.xlim(0,M)
plt.ylim(0,1)
plt.title('Chunks decision vector')
# plt.title('Decision Vector')
savefig(None,'decvec_chunks10',plot_mode='half')


# xfav10 = [1.,0.59091375, 0.34853376, 0.02105435, 0.9192925 , 0.91107212,
       # 0.09316722, 0.01361819, 0.41919292, 0.00474532,0.]
xfav = [1., 0.28922885,  0.83188353,  0.96783212,  0.0485293 ,  0.80432386,
        0.86428831,  0.98404819,  0.07680652,  0.93561109,  0.0409585 ,
        0.00521002, 0.]
plt.figure()
M=12
# W=200
# N=10
plot_settings('half')
plt.plot(list(range(M+1)),xfav)
plt.xlabel('$\mu$')
plt.ylabel('$D_{\mu}$')
plt.xlim(0,M)
plt.ylim(0,1)
plt.title('Optimized decision vector')
# plt.title('Decision Vector')
savefig(None,'decvec_cma',plot_mode='half')
#######chapters/naminggame/normal#######


p = meta_exp.plot('srtheo',M=1,get_object=True,N=1000)
p.xmax = 7*10**4#4000
#savefig(p,'srtheobasic')
xmax = min([x for x,y in zip(p._X[0],p._Y[0]) if y==1.])
plot_settings(ptype='margin')
p.title = ''
p.draw()
ax = plt.gca()
plt.plot([xmax,xmax],[0,1],color='black',linestyle='--')
ax.annotate(' $t_{conv}$', xy=(xmax, 0.), xytext=(xmax, 0.12),
            arrowprops=dict(facecolor='black', shrink=0.0),
            )
savefig(None,'srtheobasic_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot('Nlink',M=1,get_object=True,N=1000)
p.xmax = 7*10**4#4000
#p.ymax = 10**4
p.title = ''
#savefig(p,'Nlink')
p.draw()
ax = plt.gca()
ymax = max(p._Y[0])
xmax = min([x for x,y in zip(p._X[0],p._Y[0]) if y==ymax])
plt.plot([xmax,xmax],[0,ymax],color='black',linestyle='--')
ax.annotate(' $t_{max}$', xy=(xmax, 0.), xytext=(xmax, 0.84),
            arrowprops=dict(facecolor='black', shrink=0.5),
            )
plt.plot([0,xmax],[ymax,ymax],color='black',linestyle='--')
ax.annotate(' $N_l^{max}$', xy=(xmax, ymax), xytext=(xmax+10000,ymax),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
ax.annotate(' $M$', xy=(p.xmax, 1), xytext=(p.xmax-15000,2),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
savefig(None,'Nlink_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot('N_d',M=1,get_object=True,N=1000)
p.xmax = 7*10**4#4000
p.title = ''
#savefig(p,'N_d')p.draw()
p.draw()
ax = plt.gca()
ymax = max(p._Y[0])
xmax = min([x for x,y in zip(p._X[0],p._Y[0]) if y==ymax])
plt.plot([xmax,xmax],[0,ymax],color='black',linestyle='--')
ax.annotate(' $t_{GC}$', xy=(xmax, 0.), xytext=(xmax, 20),
            arrowprops=dict(facecolor='black', shrink=0.5),
            )
plt.plot([0,xmax],[ymax,ymax],color='black',linestyle='--')
ax.annotate(' $N_d^{max}$', xy=(xmax, ymax), xytext=(xmax+5000,ymax-80),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
ax.annotate(' $M$', xy=(p.xmax, 1), xytext=(p.xmax-15000,20),
            arrowprops=dict(facecolor='black', shrink=0.1),
            )
savefig(None,'N_d_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot_against(measure='conv_time',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1.
p.ymax = 10**7
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,alpha_noind=True)
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][3] = '_nolegend_'
savefig(p2,'scaling_conv',plot_mode='normal')

p = meta_exp.plot_against(measure='max_mem',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1
p.ymax = 10**6
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,alpha_noind=True)
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][3] = '_nolegend_'
p2.symlog = False
savefig(p2,'scaling_Nmax',plot_mode='normal')

p = meta_exp.plot_against(measure='max_N_d',token='N',M='all',get_object=True)
p.ymax = 10**6
p.xmin = 10
p.ymin = 1
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,alpha_noind=True)
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][3] = '_nolegend_'
p2.symlog = False
savefig(p2,'scaling_Ndmax',plot_mode='normal')



#######chapters/naminggame/VU#######

# p = meta_exp.plot('srtheo',vu_type='all',get_object=True)
# p.xmax = 6*10**4
# savefig(p,'srtheoVU')

# p = meta_exp.plot('Nlink',vu_type='all',get_object=True)
# p.xmax = 6*10**4
# savefig(p,'NlinkVU',plot_mode='fullwidth2')

p = meta_exp.plot_against(measure='conv_time',token='N',vu_type='all',get_object=True)
p.xmin = 10
p.ymin = 1
p.ymax = 10**6
p.legendoptions['labels'] = ['Minimal NG','BLIS','Imitation']
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
p2.legendoptions['labels'][1] = '_nolegend_'
savefig(p2,'scaling_VU_conv',plot_mode='fullwidth2')

p = meta_exp.plot_against(measure='max_mem',token='N',vu_type='all',get_object=True)
p.xmin = 10
p.ymin = 1
p.legendoptions['labels'] = ['Minimal NG','BLIS','Imitation']
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
p2.legendoptions['labels'][5] = '_nolegend_'
savefig(p2,'scaling_VU_Nmax',plot_mode='fullwidth2')

#######chapters/naminggame/accpol#######

p = meta_exp.plot('srtheo',accpol='all',get_object=True,N=1000)
p.xmax = 1.5*10**5
p.std_mode='minmax'
p.title = ''
p.legendoptions['labels'] = ['Standard','Acceptance Policy']
savefig(p,'srtheo_accpol',plot_mode='fullwidth2')

p = meta_exp.plot('Nlink',accpol='all',get_object=True,N=1000)
p.xmax = 1.5*10**5
p.title = ''
p.std_mode='minmax'
p.legendoptions['labels'] = ['Standard','Acceptance Policy']
savefig(p,'Nlink_accpol',plot_mode='fullwidth2')

p = meta_exp.plot_against(measure='conv_time',token='N',accpol='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_accpol_conv')

p = meta_exp.plot_against(measure='max_mem',token='N',accpol='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_accpol_Nmax')

#######chapters/naminggame/wordchoice#######

p = meta_exp.plot('srtheo',wordchoice='all',get_object=True,N=1000)
p.xmax = 6*10**4
savefig(p,'srtheo_wordchoice')

p = meta_exp.plot('Nlink',wordchoice='all',get_object=True,N=1000)
p.xmax = 6*10**4
savefig(p,'Nlink_wordchoice')

p = meta_exp.plot('Nlink',wordchoice='all',get_object=True,N=1000)
p.xmax = 6*10**4
savefig(p,'N_d_wordchoice')

p = meta_exp.plot_against(measure='conv_time',token='N',wordchoice='all',get_object=True)
p.xmin = 10
p.ymin = 1
p.legendoptions['labels'] = ['Random word','Play smart']

#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
savefig(p2,'scaling_wordchoice_conv',plot_mode='fullwidth2')

p = meta_exp.plot_against(measure='max_mem',token='N',wordchoice='all',get_object=True)
p.xmin = 10
p.ymin = 1
p.legendoptions['labels'] = ['Random word','Play smart']
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,xmin=[100,10])
savefig(p2,'scaling_wordchoice_Nmax',plot_mode='fullwidth2')

#######chapters/topicchoice/exploexplo#######

p = meta_exp.plot('srtheo',strat_type='only_exploit',W_inf=True,get_object=True)
p.xmax = 1.5*10**5
p.title = ''
#p.std_mode='minmax'
savefig(p,'srtheo_blocked',plot_mode='margin')

#######chapters/topicchoice/normal#######

ni=8
p = meta_exp.plot('srtheo',vu_type='imitation',N=10,nbiter=ni,get_object=True)
p2=meta_exp.plot('entropycouples_norm',vu_type='imitation',N=10,nbiter=ni,get_object=True)
p3 = p+p2
p3.xmax =30000
p3.title = ''
p3.ylabel = ''
p3.legendoptions['labels'] = ['S(t)','$<i_2>(t)$']
savefig(p3,'entropycouples',plot_mode='margin')

# #######chapters/topicchoice/STN#######

# for NN,ym in zip(meta_exp.params['N']['values'],[50000,10**7,10**7]):
#     p = meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type='all',N=NN,get_object=True)
#     p.ymax = ym
#     p.xmax=1.
#     savefig(p,'srtheo_STN_'+str(NN))

#######chapters/topicchoice/STW#######

p = meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type='naive',W_inf=[True],get_object=True)
p.add_graph(meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type='success_threshold_wise',W_inf=[True,2,False],get_object=True))
p.ymax = 10**7
p.xmax=1.
savefig(p,'srtheo_STW')

#######chapters/topicchoice/ST2#######

p = meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type=['naive','success_threshold_wise','success_threshold'],N=100,get_object=True)
p.ymax = 0.5*10**7
p.xmax=1.
p.legendoptions['labels'] = ['Random Topic Choice','Success Threshold (Level 1+2)','Success Threshold Level 1 only']#,'ST Level 2']
p.Yoptions[0]['linestyle']='--'
for i in [1,2]:
    p.Yoptions[i]['marker'] = 'o'
p.xlabel = '$\\alpha_{ST}$'
savefig(p,'convtime_ST2',plot_mode='normal')

#######chapters/topicchoice/MC2#######

p = meta_exp.plot_against(token='mincounts_param',measure='conv_time',strat_type=['naive','mincounts','mincounts_basic'],N=100,get_object=True)
p.ymax = 0.5*10**7
p.xmax=1.
p.legendoptions['labels'] = ['Random Topic Choice','Min. Counts (Level 1+2)','Min. Counts Level 1 only']#,'ST Level 2']
p.Yoptions[0]['linestyle']='--'
for i in [1,2]:
    p.Yoptions[i]['marker'] = 'o'
p.xlabel = '$\\~n_{MC}$'
savefig(p,'convtime_MC2',plot_mode='normal')

#######chapters/topicchoice/comparison#######

p = meta_exp.plot_against(measure='conv_time',token='N',strat_type=['naive','success_threshold_wise','mincounts',
   'decision_vector_chunks'],get_object=True)
p.xmin = 10
p.ymin = 10
plot_settings('normal')
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
#p2.show()
p2.legendoptions['labels'][0] = 'Random Topic Choice'
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][2] = 'Success Threshold'
p2.legendoptions['labels'][4] = 'Minimal Counts'
p2.legendoptions['labels'][6] = 'Chunks'
p2.Yoptions[1]['alpha'] = 0.
p2.Yoptions[5]['alpha'] = 0.
p2.Yoptions[7]['alpha'] = 0.
p2.legendoptions['labels'][5] = '_nolegend_'
p2.legendoptions['labels'][7] = '_nolegend_'
savefig(p2,'memconstr_comparison',plot_mode='normal')


p = meta_exp.plot('srtheo',strat_type=['naive','naive_explobiased',
    'decision_vector_gainsoftmax',
   'decision_vector_chunks'],get_object=True)
p.xmax = 3*10**6
p.legendoptions['labels'] = ['Random Topic Choice','Explo. Biased','Info. Gain','Chunks']
p.Yoptions[0]['linestyle'] = '--'
savefig(p,'IGvsCH',plot_mode='normal')

#######chapters/topicchoice/comparisonHC#######

p = meta_exp.plot_against(measure='conv_time',token='N',strat_type='all',get_object=True)
p.xmin = 10
p.ymin = 10
plot_settings('normal')
p.title +=": Hearer's Choice"
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
#p2.show()
p2.legendoptions['labels'][0] = 'Random Topic Choice'
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][2] = 'Success Threshold'
p2.legendoptions['labels'][4] = 'Minimal Counts'
p2.legendoptions['labels'][6] = 'Chunks'
p2.Yoptions[1]['alpha'] = 0.
p2.Yoptions[5]['alpha'] = 0.
p2.Yoptions[7]['alpha'] = 0.
p2.legendoptions['labels'][5] = '_nolegend_'
p2.legendoptions['labels'][7] = '_nolegend_'
savefig(p2,'memconstr_comparisonHC',plot_mode='normal')

#######chapters/topicchoice/comparisonW#######

p = meta_exp.plot_against(measure='conv_time',token='N',strat_type='all',W_inf=2,get_object=True)
p.xmin = 10
p.ymin = 10
plot_settings('normal')
p.title +=": Homonymy"
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
#p2.show()
p2.legendoptions['labels'][0] = 'Random Topic Choice'
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][2] = 'Success Threshold'
p2.legendoptions['labels'][4] = 'Minimal Counts'
p2.legendoptions['labels'][6] = 'Chunks'
p2.Yoptions[1]['alpha'] = 0.
p2.Yoptions[5]['alpha'] = 0.
p2.Yoptions[7]['alpha'] = 0.
p2.legendoptions['labels'][5] = '_nolegend_'
p2.legendoptions['labels'][7] = '_nolegend_'
savefig(p2,'memconstr_comparisonW',plot_mode='normal')


#######chapters/replace/replace#######

p = meta_exp.plot('srtheo',get_object=True,rate=[100,20,10,1])
p.legendoptions['labels'] = ['$t_r='+val.split('=')[1]+'$' for val in p.legendoptions['labels']]
p.xmax = 460000
savefig(p,'replace_simple_srtheo',plot_mode='normal')

#######chapters/theory/perf#######

p = meta_exp.plot_against(measure='perf_ct',
                          token='N',
                          strat_type=['naive','naive_smart','success_threshold_wise','lapsmax_mab_explothreshold','coherence_last'],
                          nbiter=8,get_object=True)
p.ymin=0
p.ymax=1
p.semilog= True
p.xmin = 10
p.legendoptions['labels'] = ['Random','Random + Play smart','Success Threshold','LAPSmax','Coherence']
p.title = 'Performance: Convergence time'
for yopt,m in zip(p.Yoptions,['o','s','v','d','+']):
    yopt['marker'] = m
savefig(p,'perf_ct',plot_mode='normal')


p = meta_exp.plot_against(measure='perf_cs',
                          token='N',
                          strat_type=['naive','naive_smart','success_threshold_wise','lapsmax_mab_explothreshold','coherence_last'],
                          nbiter=8,get_object=True)
p.ymin=0
p.ymax=1
p.semilog= True
p.xmin = 10
p.legendoptions['labels'] = ['Random','Random + Play smart','Success Threshold','LAPSmax','Coherence']
p.title = 'Performance: Convergence speed'
for yopt,m in zip(p.Yoptions,['o','s','v','d','+']):
    yopt['marker'] = m
savefig(p,'perf_cs',plot_mode='normal')


p = meta_exp.plot_against(measure='perf_st',
                          token='N',
                          strat_type=['naive','naive_smart','success_threshold_wise','lapsmax_mab_explothreshold','coherence_last'],
                          nbiter=8,get_object=True)
p.ymin=0
p.ymax=1
p.semilog= True
p.xmin = 10
p.legendoptions['labels'] = ['Random','Random + Play smart','Success Threshold','LAPSmax','Coherence']
p.title = 'Performance: Spreading'
for yopt,m in zip(p.Yoptions,['o','s','v','d','+']):
    yopt['marker'] = m
savefig(p,'perf_st',plot_mode='normal')


p = meta_exp.plot_against(measure='perf_ss',
                          token='N',
                          strat_type=['naive','naive_smart','success_threshold_wise','lapsmax_mab_explothreshold','coherence_last'],
                          nbiter=8,get_object=True)
p.ymin=0
p.ymax=1
p.semilog= True
p.xmin = 10
p.legendoptions['labels'] = ['Random','Random + Play smart','Success Threshold','LAPSmax','Coherence']
p.title = 'Performance: Spreading speed'
for yopt,m in zip(p.Yoptions,['o','s','v','d','+']):
    yopt['marker'] = m
savefig(p,'perf_ss',plot_mode='normal')


p = meta_exp.plot_against(measure='perf_ex',
                          token='N',
                          strat_type=['naive','naive_smart','success_threshold_wise','lapsmax_mab_explothreshold','coherence_last'],
                          nbiter=8,get_object=True)
p.ymin=0
p.ymax=1
p.semilog= True
p.xmin = 10
p.legendoptions['labels'] = ['Random','Random + Play smart','Success Threshold','LAPSmax','Coherence']
p.title = 'Performance: Exploration'
for yopt,m in zip(p.Yoptions,['o','s','v','d','+']):
    yopt['marker'] = m
savefig(p,'perf_ex',plot_mode='normal')


p = meta_exp.plot_against(measure='perf_ls',
                          token='N',
                          strat_type=['naive','naive_smart','success_threshold_wise','lapsmax_mab_explothreshold','coherence_last'],
                          nbiter=8,get_object=True)
p.ymin=0
p.ymax=1
p.semilog= True
p.xmin = 10
p.legendoptions['labels'] = ['Random','Random + Play smart','Success Threshold','LAPSmax','Coherence']
p.title = 'Performance: Lexicon size'
for yopt,m in zip(p.Yoptions,['o','s','v','d','+']):
    yopt['marker'] = m
savefig(p,'perf_ls',plot_mode='normal')

#######chapters/laps/lapsT2#######


p1 = meta_exp.plot_against(token='time_scale',
                            time_scale='all',
                            measure='conv_time',
                            get_object=True)
p1.legendoptions['labels'] = ['Random Topic Choice']
p1.Yoptions[0]={'linestyle':'--'}
p2 =  meta_exp.plot_against(token='time_scale',
                           strat_type='lapsmax_mab_explothreshold',
                            time_scale='all',
                            gamma=[1.,0.01],
                            measure='conv_time',
                            get_object=True)
p2.legendoptions['labels'] = ['LAPSmax, only 1st level (γ=1)','LAPSmax with Bandit (γ=0.01)']
p3 = p1 + p2
p3.ymax = 6*10**5
for yopt,m in zip(p3.Yoptions,[None,'o','s','v','d','+']):
    yopt['marker'] = m
savefig(p3,'lapsT2',plot_mode='normal')



p1 = meta_exp.plot(measure='srtheo',get_object=True)
p1.add_option(linestyle='--')
p1.legendoptions['labels'] = ['Random Topic Choice']
p2 = meta_exp.plot(measure='srtheo',strat_type='lapsmax_mab_explothreshold',time_scale=[1,2,3,5,10],get_object=True,gamma=0.01)
p3 = p1+p2
p3.xmax = 4*10**5
savefig(p3,'laps_srtheo',plot_mode='fullwidth2')

p1 = meta_exp.plot(measure='Nlink',get_object=True)
p1.add_option(linestyle='--')
p1.legendoptions['labels'] = ['Random Topic Choice']
p2 = meta_exp.plot(measure='Nlink',strat_type='lapsmax_mab_explothreshold',time_scale=[1,2,3,5,10],get_object=True,gamma=0.01)
p3 = p1+p2
p3.xmax = 4*10**5
savefig(p3,'laps_Nlink',plot_mode='fullwidth2')



#######chapters/laps/coherenceT2#######


p1 = meta_exp.plot_against(token='time_scale',
                            time_scale='all',#list(range(1,16)),
                            measure='conv_time',
                            get_object=True)
p1.legendoptions['labels'] = ['Random Topic Choice']
p1.Yoptions[0]={'linestyle':'--'}
p2 =  meta_exp.plot_against(token='time_scale',
                           strat_type=['coherence_last_only1stlevel','coherence_last'],
                            time_scale=list(range(1,16)),
                            measure='conv_time',
                            get_object=True)
p2.legendoptions['labels'] = ['Coherence, only 1st level','Coherence']
p3 = p1 + p2
p3.ymax = 6*10**5
for yopt,m in zip(p3.Yoptions,[None,'o','s','v','d','+']):
    yopt['marker'] = m
savefig(p3,'coherT2',plot_mode='normal')

#######chapters/laps/previous#######

p = meta_exp.plot('srtheo',strat_type='all',get_object=True)
p.xmax = 6*10**5
p.Yoptions[0]['linestyle'] = '--'
p.legendoptions['labels'] = ['Random','Success Threshold', 'Min. Counts', 'Chunks','Explo Biased']
savefig(p,'previous_srtheo',plot_mode='fullwidth2')


p = meta_exp.plot('Nlink',strat_type='all',get_object=True)
p.xmax = 6*10**5
p.legendoptions['labels'] = ['Random','Success Threshold', 'Min. Counts', 'Chunks','Explo Biased']
p.Yoptions[0]['linestyle'] = '--'
savefig(p,'previous_Nlink',plot_mode='fullwidth2')

#######chapters/laps/normal#######

p = meta_exp.plot(measure='entropy_final',N=1000,get_object=True)
p.xmax=4*10**6
# p.Yoptions[0]['linestyle'] = '--'
savefig(p,'entropy',plot_mode='margin')

#######chapters/laps/normal2#######
p = meta_exp.plot(measure='srtheo_local',get_object=True,time_scale='all')
p.xmax=8*10**6
p.title = ''
savefig(p,'laps_typical',plot_mode='margin')


#######chapters/laps/lapsscaling#######

ST = ['naive','lapsmax_mab_explothreshold','coherence_last']
p = meta_exp.plot_against(measure='conv_time2',token='N',strat_type=ST,get_object=True)
p.xmin = 10
p.ymin = 1
p.legendoptions['labels'] = ['Random Topic Choice','LAPSmax','Coherence']
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,alpha_noind=True)
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][3] = '_nolegend_'
p2.ymin=10**3
savefig(p2,'laps_scaling',plot_mode='fullwidth2')

ST = ['naive','lapsmax_mab_explothreshold','coherence_last']
p = meta_exp.plot_against(measure='max_mem',token='N',strat_type=ST,get_object=True)
p.xmin = 10
p.ymin = 10
p.legendoptions['labels'] = ['Random Topic Choice','LAPSmax','Coherence']
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,alpha_noind=True)
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][3] = '_nolegend_'
p2.legendoptions['labels'][5] = '_nolegend_'
p2.Yoptions[3]['alpha'] = 0.
savefig(p2,'laps_Nlscaling',plot_mode='fullwidth2')

#######chapters/laps/lapsWT#######

p = meta_exp.plot('srtheo',W_inf='all',get_object=True,N=100,strat_type='lapsmax_mab_explothreshold')
p.xmax = 1.5*10**5
p.legendoptions['labels'] = ['W=M','W=2M','W=$\infty$']
p.title = 'LAPSmax homonymy'
savefig(p,'laps_WT',plot_mode='fullwidth2')

#######chapters/laps/coherenceWT#######

p = meta_exp.plot('srtheo',W_inf='all',get_object=True,N=100,strat_type='coherence_last',time_scale=8)
p.xmax = 1.5*10**5
p.legendoptions['labels'] = ['W=M','W=2M','W=$\infty$']
p.title = 'Coherence homonymy'
savefig(p,'coherence_WT',plot_mode='fullwidth2')


#######chapters/laps/lapsHC#######

p = meta_exp.plot('Nlink',get_object=True,N=100,strat_type='naive')
p += meta_exp.plot('Nlink',get_object=True,N=100,strat_type='lapsmax_mab_explothreshold',time_scale=5)
p += meta_exp.plot('Nlink',get_object=True,N=100,strat_type='coherence_last',time_scale=2)
p.xmax = 6*10**5
p.legendoptions['labels'] = ['Random Topic Choice','LAPSmax','Coherence']
p.Yoptions[0]['linestyle']='--'
savefig(p,'lapsHC_Nl',plot_mode='fullwidth2')


p = meta_exp.plot('srtheo',get_object=True,N=100,strat_type='naive')
p += meta_exp.plot('srtheo',get_object=True,N=100,strat_type='lapsmax_mab_explothreshold',time_scale=5)
p += meta_exp.plot('srtheo',get_object=True,N=100,strat_type='coherence_last',time_scale=2)
p.legendoptions['labels'] = ['Random Topic Choice','LAPSmax','Coherence']
p.xmax = 6*10**5
p.Yoptions[0]['linestyle']='--'
savefig(p,'lapsHC_conv',plot_mode='fullwidth2')


#######chapters/userxp/analysis#######

p = meta_exp.plot('srtheo',get_object=True,strat_type='naive')
p.xmax = 50
p.title = ''
savefig(p,'userxp_srtheo',plot_mode='margin')


#######chapters/userxp/tutorial#######

p = meta_exp.plot('srtheo',get_object=True,strat_type='naive')
p.xmax = 10
p.title = ''
savefig(p,'tutorial_srtheo',plot_mode='margin')

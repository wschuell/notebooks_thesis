######header######


from metaexp_settings import meta_exp,plot_settings,savefig
import matplotlib.pyplot as plt


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

p = meta_exp.plot('srtheo',vu_type='all',get_object=True)
p.xmax = 6*10**4
savefig(p,'srtheoVU')

p = meta_exp.plot('Nlink',vu_type='all',get_object=True)
p.xmax = 6*10**4
savefig(p,'NlinkVU',plot_mode='fullwidth2')

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

#######chapters/topicchoice/STN#######

for NN,ym in zip(meta_exp.params['N']['values'],[50000,10**7,10**7]):
    p = meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type='all',N=NN,get_object=True)
    p.ymax = ym
    p.xmax=1.
    savefig(p,'srtheo_STN_'+str(NN))

#######chapters/topicchoice/STW#######

p = meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type='naive',W_inf=[True],get_object=True)
p.add_graph(meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type='success_threshold_wise',W_inf=[True,2,False],get_object=True))
p.ymax = 10**7
p.xmax=1.
savefig(p,'srtheo_STW')

#######chapters/topicchoice/ST2#######

p = meta_exp.plot_against(token='threshold_param',measure='conv_time',strat_type=['naive','success_threshold_wise','success_threshold'],N=100,get_object=True)
p.ymax = 10**7
p.xmax=1.
savefig(p,'convtime_ST2')

#######chapters/topicchoice/comparison#######

p = meta_exp.plot_against(measure='conv_time',token='N',strat_type='all',get_object=True)
p.xmin = 10
p.ymin = 1
plot_settings()
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
savefig(p,'memconstr_comparison')

#######chapters/topicchoice/comparison_HC#######

p = meta_exp.plot_against(measure='conv_time',token='N',strat_type='all',get_object=True)
p.xmin = 10
p.ymin = 1
plot_settings()
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
savefig(p,'memconstr_comparisonHC')


#######chapters/replace/replace#######

p = meta_exp.plot('srtheo',get_object=True,rate=[100,20,10,1])
p.legendoptions['labels'] = ['$t_r='+val.split('=')[1]+'$' for val in p.legendoptions['labels']]
p.xmax = 460000
savefig(p,'replace_simple_srtheo',plot_mode='normal')

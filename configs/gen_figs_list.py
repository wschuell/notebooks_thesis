######header######


from metaexp_settings import meta_exp,plot_settings,savefig 
import matplotlib.pyplot as plt


#######chapters/naminggame/normal#######


p = meta_exp.plot('srtheo',M=1,get_object=True,N=1000)
p.xmax = 7*10**4#4000
#savefig(p,'srtheobasic')
xmax = min([x for x,y in zip(p._X[0],p._Y[0]) if y==1.])
plot_settings(ptype='margin')
p.draw()
ax = plt.gca()
plt.plot([xmax,xmax],[0,1],color='black',linestyle='--')
ax.annotate(' $t_{conv}$', xy=(xmax, 0.), xytext=(xmax, 0.12),
            arrowprops=dict(facecolor='black', shrink=0.0),
            )
p.title = ''
savefig(None,'srtheobasic_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot('Nlink',M=1,get_object=True,N=1000)
p.xmax = 7*10**4#4000
#p.ymax = 10**4
p.title = ''
#savefig(p,'Nlink')
savefig(p,'Nlink_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot('N_d',M=1,get_object=True,N=1000)
p.xmax = 7*10**4#4000
p.title = ''
#savefig(p,'N_d')
savefig(p,'N_d_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot_against(measure='conv_time',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
# p2.legendoptions['labels'][1] = '_nolegend_'
# p2.legendoptions['labels'][3] = '_nolegend_'
savefig(p2,'scaling_conv')

p = meta_exp.plot_against(measure='max_mem',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1
#p.title = ''
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][3] = '_nolegend_'
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,alpha_noind=True)
savefig(p2,'scaling_Nmax')

p = meta_exp.plot_against(measure='max_N_d',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,alpha_noind=True)
p2.legendoptions['labels'][1] = '_nolegend_'
p2.legendoptions['labels'][3] = '_nolegend_'
savefig(p2,'scaling_Ndmax')



#######chapters/naminggame/VU#######

p = meta_exp.plot('srtheo',vu_type='all',get_object=True)
p.xmax = 6*10**4
savefig(p,'srtheoVU')

p = meta_exp.plot('Nlink',vu_type='all',get_object=True)
p.xmax = 6*10**4
savefig(p,'NlinkVU')

p = meta_exp.plot_against(measure='conv_time',token='N',wordchoice='all',get_object=True)
p.xmin = 10
p.ymin = 1
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
savefig(p2,'scaling_VU_conv',plot_mode='half')

p = meta_exp.plot_against(measure='max_mem',token='N',wordchoice='all',get_object=True)
p.xmin = 10
p.ymin = 1
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
savefig(p2,'scaling_VU_Nmax',plot_mode='half')

#######chapters/naminggame/accpol#######

p = meta_exp.plot('srtheo',accpol='all',get_object=True)
#p.xmax = 4000
savefig(p,'srtheo_accpol')

p = meta_exp.plot('Nlink',accpol='all',get_object=True)
#p.xmax = 4000
savefig(p,'Nlink_accpol')

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
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True)
savefig(p2,'scaling_wordchoice_conv',plot_mode='half')

p = meta_exp.plot_against(measure='max_mem',token='N',wordchoice='all',get_object=True)
p.xmin = 10
p.ymin = 1
#p.title = ''
p2 = meta_exp.powerlaw_fit(p,get_object=True,simple_labels=True,xmin=[100,10])
savefig(p2,'scaling_wordchoice_Nmax',plot_mode='half')

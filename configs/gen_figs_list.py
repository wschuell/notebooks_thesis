######header######


from metaexp_settings import meta_exp,plot_settings,savefig 



#######chapters/naminggame/normal#######


p = meta_exp.plot('srtheo',M=1,get_object=True)
p.xmax = 4000
#savefig(p,'srtheobasic')
savefig(p,'srtheobasic_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot('Nlink',M=1,get_object=True)
p.xmax = 4000
#savefig(p,'Nlink')
savefig(p,'Nlink_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot('N_d',M=1,get_object=True)
p.xmax = 4000
#savefig(p,'N_d')
savefig(p,'N_d_margin',plot_mode='margin')
#p.show()

p = meta_exp.plot_against(measure='conv_time',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_conv')

p = meta_exp.plot_against(measure='max_mem',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_Nmax')

p = meta_exp.plot_against(measure='max_N_d',token='N',M='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_Ndmax')



#######chapters/naminggame/VU#######

p = meta_exp.plot('srtheo',vu_type='all',get_object=True)
#p.xmax = 4000
savefig(p,'srtheoVU')

p = meta_exp.plot('Nlink',vu_type='all',get_object=True)
#p.xmax = 4000
savefig(p,'NlinkVU')

p = meta_exp.plot_against(measure='conv_time',token='N',vu_type='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_VU_conv')

p = meta_exp.plot_against(measure='max_mem',token='N',vu_type='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_VU_Nmax')

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

p = meta_exp.plot('srtheo',wordchoice='all',get_object=True)
#p.xmax = 4000
savefig(p,'srtheo_wordchoice')

p = meta_exp.plot('Nlink',wordchoice='all',get_object=True)
#p.xmax = 4000
savefig(p,'Nlink_wordchoice')

p = meta_exp.plot_against(measure='conv_time',token='N',wordchoice='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_wordchoice_conv')

p = meta_exp.plot_against(measure='max_mem',token='N',wordchoice='all',get_object=True)
p.xmin = 10
p.ymin = 1
p2 = meta_exp.powerlaw_fit(p,get_object=True)
savefig(p2,'scaling_wordchoice_Nmax')


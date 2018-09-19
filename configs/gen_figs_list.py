######header######


from metaexp_settings import meta_exp,plot_settings,savefig 



#######chapters/naminggame/basicNG#######


p = meta_exp.plot('srtheo',M=1,get_object=True)
p.xmax = 200
#savefig(p,'srtheobasic')
savefig(p,'srtheobasic_margin',plot_mode='margin')

p = meta_exp.plot('Nlink',M=1,get_object=True)
p.xmax = 200
#savefig(p,'Nlink')
savefig(p,'Nlink_margin',plot_mode='margin')

p = meta_exp.plot('N_d',M=1,get_object=True)
p.xmax = 200
#savefig(p,'N_d')
savefig(p,'N_d_margin',plot_mode='margin')


#######chapters/naminggame/basicNGM1#######


p = meta_exp.plot('srtheo',N=100,get_object=True)
p.xmax = 4000
#savefig(p,'srtheobasic')
savefig(p,'srtheobasicM1_margin',plot_mode='margin')

p = meta_exp.plot('Nlink',N=100,get_object=True)
p.xmax = 4000
#savefig(p,'Nlink')
savefig(p,'NlinkbasicM1_margin',plot_mode='margin')

p = meta_exp.plot('N_d',N=100,get_object=True)
p.xmax = 4000
#savefig(p,'N_d')
savefig(p,'N_dbasicM1_margin',plot_mode='margin')

#######chapters/naminggame/basicNGscaling#######


p = meta_exp.plot('srtheo',N=100,M='all',get_object=True)
p.xmax = 4000
#savefig(p,'srtheobasic')
savefig(p,'srtheobasicM1_margin',plot_mode='margin')

p = meta_exp.plot('Nlink',N=100,M='all',get_object=True)
p.xmax = 4000
#savefig(p,'Nlink')
savefig(p,'NlinkbasicM1_margin',plot_mode='margin')

p = meta_exp.plot('N_d',N=100,M='all',get_object=True)
p.xmax = 4000
#savefig(p,'N_d')
savefig(p,'N_dbasicM1_margin',plot_mode='margin')


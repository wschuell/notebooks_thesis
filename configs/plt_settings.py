

####classic####


import os
import matplotlib

def plot_settings(ptype=None):
	if ptype == 'margin':	
		fontsize = 15
		figsize = 1.95,1.95
		correction_ticks = -2
		correction_title = 0
		tight = True
		linew = 1.5
	elif ptype == 'fullwidth':
		fontsize = 15
		figsize = 6.48,2
		correction_ticks = 0
		correction_title = 5
		tight = False
		linew = 3
	elif ptype == 'fullwidth3':
		fontsize = 15
		figsize = 2.16,2
		correction_ticks = 0
		correction_title = 5
		tight = False
		linew = 3
	elif ptype == 'half':
		fontsize = 15
		figsize = 2.105,2
		correction_ticks = 0
		correction_title = 5
		tight = False
		linew = 3
	elif ptype == 'normal':
		fontsize = 15
		figsize = 4.21,2
		correction_ticks = 0
		correction_title = 5
		tight = False
		linew = 3
	else:
		fontsize = 15
		figsize = 8,5.5
		correction_ticks = 0
		correction_title = 5
		tight = False
		linew = 3
	matplotlib.rcParams['font.size'] = 10#fontsize
	matplotlib.rcParams['xtick.labelsize'] = 8#fontsize + correction_ticks
	matplotlib.rcParams['ytick.labelsize'] = 8#fontsize + correction_ticks
	matplotlib.rcParams['axes.titlesize'] = 10#fontsize + correction_title
	matplotlib.rcParams['axes.labelsize'] = 10#fontsize
	matplotlib.rcParams['legend.fontsize'] = 8#fontsize
	matplotlib.rcParams['figure.figsize'] = figsize
	matplotlib.rcParams['lines.linewidth'] = linew
	matplotlib.rcParams['lines.markersize'] = 8#fontsize-3
	matplotlib.rcParams['font.family'] = 'serif'
	if matplotlib.rcParams['font.serif'][:2] != ['Computer Modern Roman','Latin Modern Roman']:
		matplotlib.rcParams['font.serif'] = ['Computer Modern Roman','Latin Modern Roman'] + matplotlib.rcParams['font.serif']


def savefig(p,name,plot_mode=None,file_format='pdf'):
	if not os.path.exists('figures'):
		os.makedirs('figures')
	plot_settings(plot_mode)
	if p is not None:
		p.savefig("figures/"+name+"."+file_format, format=file_format, bbox_inches='tight', dpi=500)
	else:
		matplotlib.pyplot.savefig("figures/"+name+"."+file_format, format=file_format, bbox_inches='tight', dpi=500)

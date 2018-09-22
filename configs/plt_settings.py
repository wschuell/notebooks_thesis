

####classic####


import os
import matplotlib

def plot_settings(type=None):
	if type == 'margin':	
		fontsize = 15
		figsize = 8*0.5,5.5*0.5
		correction_ticks = -2
		correction_title = 0
		tight = True
		linew = 1.5
	elif type == 'fullwidth':
		fontsize = 15
		figsize = 8,5.5
		correction_ticks = 0
		correction_title = 5
		tight = False
		linew = 3
	elif type == 'fullwidth3':
		fontsize = 15
		figsize = 8,5.5
		correction_ticks = 0
		correction_title = 5
		tight = False
		linew = 3
	elif type == 'half':
		fontsize = 15
		figsize = 8,5.5
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
	matplotlib.rcParams['font.size'] = fontsize
	matplotlib.rcParams['xtick.labelsize'] = fontsize + correction_ticks
	matplotlib.rcParams['ytick.labelsize'] = fontsize + correction_ticks
	matplotlib.rcParams['axes.titlesize'] = fontsize + correction_title
	matplotlib.rcParams['axes.labelsize'] = fontsize
	matplotlib.rcParams['legend.fontsize'] = fontsize
	matplotlib.rcParams['figure.figsize'] = figsize
	matplotlib.rcParams['lines.linewidth'] = linew
	matplotlib.rcParams['lines.markersize'] = fontsize
	matplotlib.rcParams['font.family'] = 'serif'
	if matplotlib.rcParams['font.serif'][:2] != ['Computer Modern Roman','Latin Modern Roman']:
		matplotlib.rcParams['font.serif'] = ['Computer Modern Roman','Latin Modern Roman'] + matplotlib.rcParams['font.serif']


def savefig(p,name,plot_mode=None,file_format='pdf'):
	if not os.path.exists('figures'):
		os.makedirs('figures')
	plot_settings(plot_mode)
	p.savefig("figures/"+name+"."+file_format, format=file_format, bbox_inches='tight', dpi=500)

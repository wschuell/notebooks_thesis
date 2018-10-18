

####classic####


import os
import matplotlib

coeff = 2.

def plot_settings(ptype=None):
	if ptype == 'margin':	
		fontsize = 10*coeff
		figsize = 1.95*coeff,1.95*coeff
		correction_ticks = -2*coeff
		correction_title = 0
		tight = True
		linew = 1.5*coeff
	elif ptype == 'fullwidth':
		fontsize = 10*coeff
		figsize = 6.48,2*coeff
		correction_ticks = 0*coeff
		correction_title = 5*coeff
		tight = False
		linew = 3
	elif ptype == 'fullwidth3':
		fontsize = 10*coeff
		figsize = 2.16*coeff,2*coeff
		correction_ticks = 0
		correction_title = 5*coeff
		tight = False
		linew = 3*coeff
	elif ptype == 'half':
		fontsize = 10*coeff
		figsize = 2.105*coeff,2*coeff
		correction_ticks = 0
		correction_title = 5*coeff
		tight = False
		linew = 3*coeff
	elif ptype == 'normal':
		fontsize = 10*coeff
		figsize = 4.21*coeff,2*coeff
		correction_ticks = 0
		correction_title = 5*coeff
		tight = False
		linew = 3*coeff
	else:
		fontsize = 15*coeff
		figsize = 8*coeff,5.5*coeff
		correction_ticks = 0*coeff
		correction_title = 5*coeff
		tight = False
		linew = 3*coeff
	matplotlib.rcParams['font.size'] = 10*coeff#fontsize
	matplotlib.rcParams['xtick.labelsize'] = 8*coeff#fontsize + correction_ticks
	matplotlib.rcParams['ytick.labelsize'] = 8*coeff#fontsize + correction_ticks
	matplotlib.rcParams['axes.titlesize'] = 10*coeff#fontsize + correction_title
	matplotlib.rcParams['axes.labelsize'] = 10*coeff#fontsize
	matplotlib.rcParams['legend.fontsize'] = 8*coeff#fontsize
	matplotlib.rcParams['figure.figsize'] = figsize
	matplotlib.rcParams['lines.linewidth'] = linew
	matplotlib.rcParams['lines.markersize'] = 8*coeff#fontsize-3
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



####classic####



import matplotlib

def plot_settings():
	fontsize = 15
	matplotlib.rcParams['font.size'] = fontsize
	matplotlib.rcParams['xtick.labelsize'] = fontsize
	matplotlib.rcParams['ytick.labelsize'] = fontsize
	matplotlib.rcParams['axes.titlesize'] = fontsize+5
	matplotlib.rcParams['axes.labelsize'] = fontsize
	matplotlib.rcParams['legend.fontsize'] = fontsize
	matplotlib.rcParams['figure.figsize'] = 8,5.5
	matplotlib.rcParams['lines.linewidth'] = 3

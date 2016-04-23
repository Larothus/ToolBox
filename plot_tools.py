#----------------------------------------------------------------------------------------------------
# DESCRIPTION:
#
#
#  INPUT:
# OUTPUT:
#
#
#
#----------------------------------------------------------------------------------------------------

#===============================================
#		MODULES
#===============================================

from numpy import array
from matplotlib import pyplot
from os import path,mkdir

#===============================================
#		GLOBAL VARIABLES
#===============================================

#===============================================
#		OBJECTS AND FUNCTIONS
#===============================================

def read_config(properties):
	out = {}
	with open(properties) as in_file:
		for line in in_file:
			if line[0]=='\n' or line[0]=='#': continue
			(key, val) = line.split(':')
			out[key] = val[:-1].strip()
	return out

def plot_single(properties):
	"""Plots an x vs y plot from two csv files. Uses as input the data given in the properties file."""

	properties = read_config(properties)

	#++++++++++ DATA ++++++++++
	infile = genfromtxt(properties['infile'],delimiter=',',names=True,dtype=None,comments='#',missing_values='None')
	x_data,y_data = infile[properties['x,y'].split(',')[0]],infile[properties['x,y'].split(',')[1]]

	#++++++++++ LINE FORMAT ++++++++++
	if properties['size'] != 'False': pyplot.figure(num=1,figsize=eval(properties['size']),dpi=eval(properties['dpi']))
	else: pyplot.figure(num=1,dpi=eval(properties['dpi']))
	pyplot.clf()
	pyplot.subplot(1,1,1)
	p, = pyplot.plot(x_data,y_data,marker=properties['marker'],markersize=int(properties['markersize']),markeredgewidth=float(properties['markeredgewidth']),linestyle=properties['linestyle'],color=array(eval(properties['color']))/255,alpha=float(properties['alpha']))

	#++++++++++ PLOT FORMAT ++++++++++
	pyplot.suptitle(properties['suptitle'],fontsize=16)
	pyplot.figtext(0.5,0.05,properties['x_label'],ha='center',va='center')
	pyplot.figtext(0.05,0.5,properties['y_label'],rotation=90,ha='center',va='center')
	pyplot.xticks(fontsize=8)
	pyplot.yticks(fontsize=8)
	if properties['x_lim'] != 'False':
		xlim = eval(properties['x_lim'])
		pyplot.xlim(xlim[0],xlim[1])
	if properties['y_lim'] != 'False':
		ylim = eval(properties['y_lim'])
		pyplot.ylim(ylim[0],ylim[1])
	if properties['invert_x'] == 'True': pyplot.gca().invert_xaxis()
	if properties['invert_y'] == 'True': pyplot.gca().invert_yaxis()
	if properties['grid'] != 'False': pyplot.grid(b='on',which='major',axis=properties['grid'])
	if properties['equalize_grid'] == 'True': pyplot.gca().set_aspect('equal', adjustable='box')

	#++++++++ SAVE PLOT ++++++++
	if properties['outfile'] == 'False': outfile = properties['infile'].split('.')[0]+'.pdf'
	else: outfile = properties['outfile']
	outpath = properties['outpath']
	if not path.exists(outpath): mkdir(outpath)
	pyplot.savefig('%s%s' %(outpath,outfile))
	print('Plot saved to %s%s' %(outpath,outfile))
	pyplot.close()

def plot_double(properties):
	"""Plots an x vs y plot from two csv files. Uses as input the data given in the properties file."""

	properties = read_config(properties)

	#++++++++++ DATA ++++++++++
	infile1 = genfromtxt(properties['infile1'],delimiter=',',names=True,dtype=None,comments='#',missing_values='None')
	infile2 = genfromtxt(properties['infile2'],delimiter=',',names=True,dtype=None,comments='#',missing_values='None')
	x_data1,y_data1 = infile1[properties['x1,y1'].split(',')[0]],infile1[properties['x1,y1'].split(',')[1]]
	x_data2,y_data2 = infile2[properties['x2,y2'].split(',')[0]],infile2[properties['x2,y2'].split(',')[1]]

	#++++++++++ LINE FORMAT ++++++++++
	if properties['size'] != 'False': pyplot.figure(num=1,figsize=eval(properties['size']),dpi=eval(properties['dpi']))
	else: pyplot.figure(num=1,dpi=eval(properties['dpi']))
	pyplot.clf()
	pyplot.subplot(1,1,1)
	p1, = pyplot.plot(x_data1,y_data1,marker=properties['marker1'],markersize=int(properties['markersize1']),markeredgewidth=float(properties['markeredgewidth1']),linestyle=properties['linestyle1'],color=array(eval(properties['color1']))/255,alpha=float(properties['alpha1']))
	p2, = pyplot.plot(x_data2,y_data2,marker=properties['marker2'],markersize=int(properties['markersize2']),markeredgewidth=float(properties['markeredgewidth2']),linestyle=properties['linestyle2'],color=array(eval(properties['color2']))/255,alpha=float(properties['alpha2']))

	#++++++++++ PLOT FORMAT ++++++++++
	pyplot.suptitle(properties['suptitle'],fontsize=16)
	pyplot.figtext(0.5,0.05,properties['x_label'],ha='center',va='center')
	pyplot.figtext(0.05,0.5,properties['y_label'],rotation=90,ha='center',va='center')
	pyplot.xticks(fontsize=8)
	pyplot.yticks(fontsize=8)
	if properties['x_lim'] != 'False':
		xlim = eval(properties['x_lim'])
		pyplot.xlim(xlim[0],xlim[1])
	if properties['y_lim'] != 'False':
		ylim = eval(properties['y_lim'])
		pyplot.ylim(ylim[0],ylim[1])
	if properties['invert_x'] == 'True': pyplot.gca().invert_xaxis()
	if properties['invert_y'] == 'True': pyplot.gca().invert_yaxis()
	if properties['grid'] != 'False': pyplot.grid(b='on',which='major',axis=properties['grid'])
	if properties['equalize_grid'] == 'True': pyplot.gca().set_aspect('equal', adjustable='box')
	if properties['legend'] != 'False': pyplot.legend([p1,p2],eval(properties['legend']),loc=eval(properties['legend_loc']))

	#++++++++ SAVE PLOT ++++++++
	if properties['outfile'] == 'False': outfile = properties['infile'].split('.')[0]+'.pdf'
	else: outfile = properties['outfile']
	outpath = properties['outpath']
	if not path.exists(outpath): mkdir(outpath)
	pyplot.savefig('%s%s' %(outpath,outfile))
	print('Plot saved to %s%s' %(outpath,outfile))
	pyplot.close()

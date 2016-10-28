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

from ConfigParser import SafeConfigParser
from numpy import array,genfromtxt
from matplotlib import pyplot
from os import path,mkdir

#===============================================
#		GLOBAL VARIABLES
#===============================================

#===============================================
#		OBJECTS AND FUNCTIONS
#===============================================

def plot(properties):
	"""Plots an x vs y plot from any number of csv files. Uses as input the data given in the properties file."""

	config = SafeConfigParser()
	config.read(properties)

	#++++++++++ PLOT FORMAT ++++++++++
	if config.get('plot_format','size') != 'False': pyplot.figure(num=1,figsize=eval(config.get('plot_format','size')),dpi=eval(config.get('plot_format','dpi')))
	else: pyplot.figure(num=1,dpi=eval(config.get('plot_format','dpi')))
	pyplot.clf()
	pyplot.subplot(1,1,1)

	#++++++++++ PLOT ++++++++++
	data_range = range(len(eval(config.get('data','infiles'))))
	for i in data_range:
		infile = genfromtxt(eval(config.get('data','infiles'))[i],delimiter=',',names=True,dtype=None,comments='#',missing_values='None')
		x_data,y_data = infile[eval(config.get('data','columns'))[i][0]],infile[eval(config.get('data','columns'))[i][1]]

		if config.get('axis_format','logx') == 'True' and config.get('axis_format','logy') == 'True':
			p, = pyplot.loglog(x_data,y_data,marker=eval(config.get('line_format','marker'))[i],markersize=eval(config.get('line_format','markersize'))[i],markeredgewidth=eval(config.get('line_format','markeredgewidth'))[i],linestyle=eval(config.get('line_format','linestyle'))[i],color=array(eval(config.get('line_format','color'))[i])/255,alpha=eval(config.get('line_format','alpha'))[i])
		elif config.get('axis_format','logx') == 'True':
			p, = pyplot.semilogx(x_data,y_data,marker=eval(config.get('line_format','marker'))[i],markersize=eval(config.get('line_format','markersize'))[i],markeredgewidth=eval(config.get('line_format','markeredgewidth'))[i],linestyle=eval(config.get('line_format','linestyle'))[i],color=array(eval(config.get('line_format','color'))[i])/255,alpha=eval(config.get('line_format','alpha'))[i])
		elif config.get('axis_format','logy') == 'True':
			p, = pyplot.semilogy(x_data,y_data,marker=eval(config.get('line_format','marker'))[i],markersize=eval(config.get('line_format','markersize'))[i],markeredgewidth=eval(config.get('line_format','markeredgewidth'))[i],linestyle=eval(config.get('line_format','linestyle'))[i],color=array(eval(config.get('line_format','color'))[i])/255,alpha=eval(config.get('line_format','alpha'))[i])
		else:
			p, = pyplot.plot(x_data,y_data,marker=eval(config.get('line_format','marker'))[i],markersize=eval(config.get('line_format','markersize'))[i],markeredgewidth=eval(config.get('line_format','markeredgewidth'))[i],linestyle=eval(config.get('line_format','linestyle'))[i],color=array(eval(config.get('line_format','color'))[i])/255,alpha=eval(config.get('line_format','alpha'))[i])

	#++++++++++ PLOT FORMAT ++++++++++
	pyplot.suptitle(config.get('plot_format','suptitle'),fontsize=16)
	pyplot.figtext(0.5,0.05,config.get('axis_format','x_label'),ha='center',va='center')
	pyplot.figtext(0.05,0.5,config.get('axis_format','y_label'),rotation=90,ha='center',va='center')
	pyplot.xticks(fontsize=8)
	pyplot.yticks(fontsize=8)
	if config.get('axis_format','x_lim') != 'False':
		xlim = eval(config.get('axis_format','x_lim'))
		pyplot.xlim(xlim[0],xlim[1])
	if config.get('axis_format','y_lim') != 'False':
		ylim = eval(config.get('axis_format','y_lim'))
		pyplot.ylim(ylim[0],ylim[1])
	if config.get('axis_format','invert_x') == 'True': pyplot.gca().invert_xaxis()
	if config.get('axis_format','invert_y') == 'True': pyplot.gca().invert_yaxis()
	if config.get('axis_format','grid') != 'False': pyplot.grid(b='on',which='major',axis=config.get('axis_format','grid'))
	if config.get('axis_format','equalize_grid') == 'True': pyplot.gca().set_aspect('equal', adjustable='box')

	#++++++++ SAVE PLOT ++++++++
	if config.get('output','outfile') == 'False': outfile = config.get('infile').split('.')[0]+'.pdf'
	else: outfile = config.get('output','outfile')
	outpath = config.get('output','outpath')
	if not path.exists(outpath): mkdir(outpath)
	pyplot.savefig('%s%s' %(outpath,outfile))
	print('Plot saved to %s%s' %(outpath,outfile))
	pyplot.close()

from matplotlib.image import imread, imsave
from matplotlib.colors import rgb_to_hsv
from matplotlib.pyplot import imsave

def extract_hue(infile):
	"""
		Returns a hue greyscale image from an rgb image.
	"""
	rgb_image = imread(infile)
	hsv_image = rgb_to_hsv(rgb_image)
	hue_image = -hsv_image[:,:,0]
	imsave(fname='%s-hue.png' %(infile.split('.')[0]),arr=hue_image,cmap='gray')

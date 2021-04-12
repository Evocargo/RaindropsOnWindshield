import cv2
import math
import numpy as np
from PIL import Image
from PIL import ImageDraw
import pyblur
import random
from random import randint
from raindrop.config import cfg

"""
This module contains a description of Raindrop class
"""

def make_bezier(xys):
    # xys should be a sequence of 2-tuples (Bezier control points)
    n = len(xys)
    combinations = pascal_row(n-1)
    def bezier(ts):
        # This uses the generalized formula for bezier curves
        # http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization
        result = []
        for t in ts:
            tpowers = (t**i for i in range(n))
            upowers = reversed([(1-t)**i for i in range(n)])
            coefs = [c*a*b for c, a, b in zip(combinations, tpowers, upowers)]
            result.append(
                tuple(sum([coef*p for coef, p in zip(coefs, ps)]) for ps in zip(*xys)))
        return result
    return bezier

def pascal_row(n, memo={}):
    # This returns the nth row of Pascal Triangle
    if n in memo:
        return memo[n]
    result = [1]
    x, numerator = 1, n
    for denominator in range(1, n//2+1):
        x *= numerator
        x /= denominator
        result.append(x)
        numerator -= 1
        if n&1 == 0:
            result.extend(reversed(result[:-1]))
        else:
            result.extend(reversed(result))
        memo[n] = result
    return result


class Raindrop():
	def __init__(self, key, centerxy = None, radius = None, shape = None):
		"""
		:param key: a unique key identifying a drop
		:param centerxy: tuple defining coordinates of raindrop center in the image
		:param radius: radius of a drop
		:param shape: int from 0 to 2 defining raindrop shape type
		"""
		self.key = key		
		self.ifcol = False	
		self.col_with = []
		self.center = centerxy
		self.radius = radius
		self.shape = shape            
		self.type = "default"
        # label map's WxH = 4*R , 5*R
		self.labelmap = np.zeros((self.radius * 5, self.radius*4))
		self.alphamap = np.zeros((self.radius * 5, self.radius*4))
		self.background = None
		self.texture = None
		self._create_label()
		self.use_label = False


	def setCollision(self, col, col_with):
		self.ifcol = col
		self.col_with = col_with

	def updateTexture(self, bg):		
		fg = pyblur.GaussianBlur(Image.fromarray(np.uint8(bg)), 5)
		fg = np.asarray(fg)
		# add fish eye effect to simulate the background
		K = np.array([[30*self.radius, 0, 2*self.radius],
				[0., 20*self.radius, 3*self.radius],
				[0., 0., 1]])
		D = np.array([0.0, 0.0, 0.0, 0.0])
		Knew = K.copy()
        
		Knew[(0,1), (0,1)] = math.pow(self.radius, 1/500)*2 * Knew[(0,1), (0,1)]
		fisheye = cv2.fisheye.undistortImage(fg, K, D=D, Knew=Knew)     

		tmp = np.expand_dims(self.alphamap, axis = -1)
		tmp = np.concatenate((fisheye, tmp), axis = 2)
		
		self.texture = Image.fromarray(tmp.astype('uint8'), 'RGBA')
        
		# uncomment if you want a background in drop to be flipped
		#self.texture = self.texture.transpose(Image.FLIP_TOP_BOTTOM)
        
	def _create_label(self):  
		self._createDefaultDrop()

	def _createDefaultDrop(self):
		"""
		create the raindrop Alpha Map according to its shape type
		update raindrop label
		"""         
		if (self.shape == 0):    
			cv2.circle(self.labelmap, (self.radius * 2, self.radius * 3), int(self.radius), 128, -1)
			self.alphamap = pyblur.GaussianBlur(Image.fromarray(np.uint8(self.labelmap)), 50)        
			self.alphamap = np.asarray(self.alphamap).astype(np.float)
			self.alphamap = self.alphamap/np.max(self.alphamap)*255.0
			# set label map
			self.labelmap[self.labelmap>0] = 1
               
		if (self.shape == 1):    
			cv2.circle(self.labelmap, (self.radius * 2, self.radius * 3), int(self.radius), 128, -1)
			cv2.ellipse(self.labelmap, (self.radius * 2, self.radius * 3), (self.radius, int(1.3*math.sqrt(3) * self.radius)), 0, 180, 360, 128, -1)

			self.alphamap = pyblur.GaussianBlur(Image.fromarray(np.uint8(self.labelmap)), 50)        
			self.alphamap = np.asarray(self.alphamap).astype(np.float)
			self.alphamap = self.alphamap/np.max(self.alphamap)*255.0
			# set label map
			self.labelmap[self.labelmap>0] = 1
            
		if (self.shape == 2): 
			A = cfg["A"]
			B = cfg["B"]
			C = cfg["C"]
			D = cfg["D"]
			img = Image.fromarray(np.uint8(self.labelmap) , 'L')
			draw = ImageDraw.Draw(img)
			ts = [t/100.0 for t in range(101)]
			xys = [(self.radius * C[0], self.radius * C[1]), (self.radius * B[0], self.radius * B[1]), (self.radius * D[0], self.radius * D[1])]
			bezier = make_bezier(xys)
			points = bezier(ts)

			xys = [(self.radius * C[0], self.radius * C[1]), (self.radius * A[0], self.radius * A[1]), (self.radius * D[0], self.radius * D[1])]
			bezier = make_bezier(xys)
			points.extend(bezier(ts))
			draw.polygon(points, fill = 'gray')           

			self.alphamap = pyblur.GaussianBlur(img, 50)       
			self.alphamap = np.asarray(self.alphamap).astype(np.float)
			self.alphamap = self.alphamap/np.max(self.alphamap)*255.0
			# set label map
			self.labelmap[self.labelmap>0] = 1            


	def setKey(self, key):
		self.key = key

	def getLabelMap(self):
		return self.labelmap

	def getAlphaMap(self):
		return self.alphamap

	def getTexture(self):
		return self.texture

	def getCenters(self):
		return self.center
		
	def getRadius(self):
		return self.radius

	def getKey(self):
		return self.key

	def getIfColli(self):
		return self.ifcol

	def getCollisionList(self):
		return self.col_with
	
	def getUseLabel(self):
		return self.use_label

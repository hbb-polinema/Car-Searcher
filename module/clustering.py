# import the necessary packages
from colordescriptor import ColorDescriptor
import numpy as np
import cv2

class Clustering:
	def __init__(self, Ncluster):
		# store number of clustering per image
		self.Ncluster = Ncluster
	
	def color_quantization_kmeans(self, image, quantify=7):
		# reshape image to converted purpose
		data = image.reshape((-1,3))

		# convert to np.float32
		data = np.float32(data)
		
		# define criteria, number of clusters(K) and apply kmeans()
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

		# cv2.kmeans(data, K, bestLabels, criteria,
		# attempts(Flag to specify the number of times the algorithm is executed using different initial labellings),
		# flags[, centers]) --> retval(compactness), bestLabels, centers
		ret,label,center = cv2.kmeans(data, quantify, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
		
		# Now convert back into uint8, and make original image
		center = np.uint8(center)
		res = center[label.flatten()]
		image = res.reshape((image.shape))
		
		# return result image
		return image
	
	def cal_center_region_hist(self, image):
		# initialize the color descriptor
		# using 8 Hue bins, 12 Saturation bins, and 3 Value bins
		cd = ColorDescriptor((8, 12, 3))
		
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# grab the dimensions and compute the center of the image
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

		# construct an elliptical mask representing the center of the image
		(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

		# extract a color histogram from the elliptical region and
		# update the feature vector
		hist = cd.histogram(image, ellipMask)
		hist = self.kmeans_region_features(hist)
		features.extend(hist.flatten())

		# return the feature vector
		return features
	
	def cal_region_hist(self, image):
		# initialize the color descriptor
		# using 8 Hue bins, 12 Saturation bins, and 3 Value bins
		cd = ColorDescriptor((8, 12, 3))
		
		# convert the image to the HSV color space and initialize
		# the features used to quantify the image
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# grab the dimensions and compute the center of the image
		(h, w) = image.shape[:2]
		(cX, cY) = (int(w * 0.5), int(h * 0.5))

		# divide the image into four rectangles/segments (top-left,
		# top-right, bottom-right, bottom-left)
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
			(0, cX, cY, h)]

		# construct an elliptical mask representing the center of the
		# image
		(axesX, axesY) = (int(w * 0.75) / 2, int(h * 0.75) / 2)
		ellipMask = np.zeros(image.shape[:2], dtype = "uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

		# loop over the segments
		for (startX, endX, startY, endY) in segments:
			# construct a mask for each corner of the image, subtracting
			# the elliptical center from it
			cornerMask = np.zeros(image.shape[:2], dtype = "uint8")
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			cornerMask = cv2.subtract(cornerMask, ellipMask)

			# extract a color histogram from the image, then update the
			# feature vector
			hist = cd.histogram(image, cornerMask)
			hist = self.kmeans_region_features(hist)
			features.extend(hist.flatten())

		# extract a color histogram from the elliptical region and
		# update the feature vector
		hist = cd.histogram(image, ellipMask)
		hist = self.kmeans_region_features(hist)
		features.extend(hist.flatten())

		# return the feature vector
		return features
	
	def kmeans_region_features(self, features):
		# convert to np.float32
		data = np.float32(features)
		
		# define criteria, number of clusters(K) and apply kmeans()
		criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)

		# cv2.kmeans(data, K, bestLabels, criteria,
		# attempts(Flag to specify the number of times the algorithm is executed using different initial labellings),
		# flags[, centers]) --> retval(compactness), bestLabels, centers
		ret,label,center = cv2.kmeans(data, self.Ncluster, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
		
		# return center of clustering
		return center		
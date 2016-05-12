# import the necessary packages
import numpy as np
import math
import csv

class Searcher:
	def __init__(self, indexPath):
		# store our index path
		self.indexPath = indexPath
		
	def search_info(self, results, infoCar):
		# Get best ID image
		best_id = []
		for (score,image) in results:
			best_id.append(int(image[:image.find("_")]))
		
		# initialize our dictionary of results
		info_results = {}
		
		# open the index file for reading
		with open(infoCar) as f:
			# initialize the CSV reader
			reader = csv.reader(f)
			
			for row in reader:
				# if ID_image found in database infocar, take it
				if int(row[0]) in best_id:
					info_results[int(row[0])] = row[1:]
			
			# close the reader
			f.close()
		
		# return best match info car
		return info_results

	def search(self, queryFeatures, limit = 10):
		# initialize our dictionary of results
		results = {}

		# open the index file for reading
		with open(self.indexPath) as f:
			# initialize the CSV reader
			reader = csv.reader(f)

			# loop over the rows in the index
			for row in reader:
				# parse out the image ID and features, then compute the
				# chi-squared distance between the features in our index
				# and our query features
				features = [float(x) for x in row[1:]]
				d = self.chi2_distance(features, queryFeatures)
				print row[0],' : ',d
				
				# now that we have the distance between the two feature
				# vectors, we can udpate the results dictionary -- the
				# key is the current image ID in the index and the
				# value is the distance we just computed, representing
				# how 'similar' the image in the index is to our query
				results[row[0]] = d

			# close the reader
			f.close()

		# sort our results, so that the smaller distances (i.e. the
		# more relevant images are at the front of the list)
		results = sorted([(v, k) for (k, v) in results.items()])

		# return our (limited) results
		return results[:limit]

	def chi2_distance(self, histA, histB, eps = 1e-10):
		# compute the chi-squared distance
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps)
			for (a, b) in zip(histA, histB)])

		# return the chi-squared distance
		return d
	
	def euclidean_dist(self, histA, histB):
		# compute the euclidean distance
		d = [(a - b)**2 for a,b in zip(histA, histB)]
		d = math.sqrt(sum(d))
		
		# return the euclidean distance
		return d
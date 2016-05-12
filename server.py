from bottle import route, request, static_file, template, run
from module.colordescriptor import ColorDescriptor
from module.searcher import Searcher
from module.clustering import Clustering
import numpy
import csv
import cv2
import os
import time

@route('/')
def root():
	year,maker = query_by_tag()
	print year,'\n',maker
	
	return template('./frontend/index.tpl', year = year, maker = maker, root='.')

'''# This is used to get static file for image type
@route('/images/<filename:re:.*\.jpg>')
def car_image(filename):
	return static_file(filename, root='.\datacars', mimetype='image/jpg')
'''

# Get static file for all types, include HTML, CSS, Javascript, any others
@route('/<filepath:path>')
def index(filepath):
    return static_file(filepath, root='.')
	
def searchQuery(Q, fileIndex):
	# Use Method handler
	index = fileIndex[0]
	MethodUsed = fileIndex[1]
	query = cv2.imread("queries/{q}".format(q=Q))
	
	# Estimated timing
	start_time = time.time()
	
	# This method for used describe query and searching
	if MethodUsed is 1:
		# Use Method 1
		# initialize the image descriptor
		# using 8 Hue bins, 12 Saturation bins, and 3 Value bins
		cd = ColorDescriptor((8, 12, 3))

		# Describe the query
		features = cd.describe(query)
		
	elif MethodUsed is 2:
		# Use Method 2
		# initialize cluster of the color quantization kmeans descriptor
		K = fileIndex[2]
		C = Clustering(K)

		# Describe the query
		new_img = C.color_quantization_kmeans(query)
		features = C.cal_region_hist(new_img)
		
	elif MethodUsed is 3:
		# Use Method 3
		# initialize the image descriptor
		# using 8 Hue bins, 12 Saturation bins, and 3 Value bins
		cd = ColorDescriptor((8, 12, 3))

		# Describe the query
		features = cd.describe_center_region(query)
		
	elif MethodUsed is 4:
		# Use Method 4
		# initialize cluster of the color quantization kmeans descriptor
		K = fileIndex[2]
		C = Clustering(K)

		# Describe the query
		new_img = C.color_quantization_kmeans(query)
		features = C.cal_center_region_hist(new_img)
		
	elif MethodUsed is 5:
		# Use Method 5
		print 'not yet implement'
	
	# perform the search
	searcher = Searcher(index)
	results = searcher.search(features)
	info_car = searcher.search_info(results,"infocar.csv")
	
	# loop over the results
	i = 0
	print '\n 10 Best Matching Result for Query: ',Q, '\n'
	for (score, resultID) in results:
		i = i + 1
		print i,'.\t Score: ', score, '\t\t | image: ', resultID
	
	# Result estimated time
	time_exec = round(time.time() - start_time, 4)
	print("\n--- Estimated time execution: %s seconds ---" % time_exec)
	
	return results, info_car, time_exec

def Color_Dominants():
	# Color Dominants process
	return None

@route('/tag')
def query_by_tag():
	# initialize our dictionary of results
	info_results = {}
		
	# open the index file for reading
	with open('infocar.csv') as f:
		# initialize the CSV reader
		reader = csv.reader(f)
			
		for row in reader:
			info_results[int(row[0])] = row[1:]
			
	# close the reader
	f.close()

	year = []
	maker = []

	for id in info_results:
		year.append(info_results[id][3])
		maker.append(info_results[id][4])

	year = numpy.unique(year)
	maker = numpy.unique(maker)
	
	return year,maker
	
@route('/search_result', method='POST')
def do_upload():
	upload = request.files.get('image')
	opsiR = request.forms.get('opsiR')
	region = request.forms.get('region')
	opsiClusterAllRegion = request.forms.get('opsiClusterAllRegion')
	opsiClusterCenterRegion = request.forms.get('opsiClusterCenterRegion')
	print 'opsiR: ',opsiR,' region: ',region,' opsiClusterAllRegion: ',opsiClusterAllRegion,' opsiClusterCenterRegion: ',opsiClusterCenterRegion
	
	# Relevance feedback options handler
	if opsiR is '1':
		# Color Dominants process
		if region is '1': # All - 5 Region
			if opsiClusterAllRegion is '1': # No Clustering
				# without centroid
				fileIndex = ['indexcar.csv', 1]
			elif opsiClusterAllRegion is not None: # Clustering with Centroid
				# Clustering with Centroid
				centroid = int(opsiClusterAllRegion)
				fileIndex = ['index_clustering_{centroid}.csv'.format(centroid=centroid), 2, centroid]
		
		elif region is '2': # Center Region only
			if opsiClusterCenterRegion is '1': # No Clustering
				# without centroid
				fileIndex = ['index_center_region.csv', 3]
			elif opsiClusterCenterRegion is not None: # Clustering with Centroid
				# Clustering with Centroid
				centroid = int(opsiClusterCenterRegion)
				fileIndex = ['index_center_region_clustering_{centroid}.csv'.format(centroid=centroid), 4, centroid]
			
	elif opsiR is '2':
		# Shape Dominants process
		fileIndex = ['indexCEDD.csv', 5]
	
	print 'fileIndex: ',fileIndex[0],' MethodUsed: ',fileIndex[1]
	
	# Check file extension allow or not
	name, ext = os.path.splitext(upload.filename)
	if ext not in ('.png', '.jpg', '.jpeg'):
		return "File extension not allowed."
	
	# Save Directory, create new if not exist
	save_path = ".\queries"
	if not os.path.exists(save_path):
		os.makedirs(save_path)
	
	# Give filename query with this time
	timenow = time.strftime("%Y%m%d-%H%M%S")
	upload.filename = "q_{currentTime}{ext}".format(currentTime=timenow, ext=ext)
	file_path = "{path}\{file}".format(path=save_path, file=upload.filename)
	upload.save(file_path)
	
	# search query image
	bestMatch, infocar, time_exec = searchQuery(upload.filename, fileIndex)
	
	# show result page
	return template('./frontend/result', bestMatch=bestMatch, infocar=infocar, time_exec=time_exec, query=upload.filename)

if __name__ == '__main__':
    run(host='0.0.0.0', port=80, debug=False, reloader=False)
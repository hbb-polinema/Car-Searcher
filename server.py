from bottle import route, request, static_file, template, run
from module.colordescriptor import ColorDescriptor
from module.searcher import Searcher
import cv2
import os
import time

@route('/')
def root():
    return static_file('./frontend/index.html', root='.')

'''# This is used to get static file for image type
@route('/images/<filename:re:.*\.jpg>')
def car_image(filename):
	return static_file(filename, root='.\datacars', mimetype='image/jpg')
'''

# Get static file for all types, include HTML, CSS, Javascript, any others
@route('/<filepath:path>')
def index(filepath):
    return static_file(filepath, root='.')
	
def searchQuery(Q):
	# Estimated timing
	start_time = time.time()
	
	# initialize the image descriptor
	# using 8 Hue bins, 12 Saturation bins, and 3 Value bins
	cd = ColorDescriptor((8, 12, 3))

	# load the query image and describe it
	query = cv2.imread("queries/{q}".format(q=Q))
	features = cd.describe(query)

	# perform the search
	searcher = Searcher("indexcar.csv")
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
	
@route('/search_result', method='POST')
def do_upload():
	upload = request.files.get('image')
	opsiR = request.forms.get('opsiR')
	region = request.forms.get('region')
	opsiClusterAllRegion = request.forms.get('opsiClusterAllRegion')
	opsiClusterCenterRegion = request.forms.get('opsiClusterCenterRegion')
	print 'opsiR: ',opsiR,' region: ',region,' opsiClusterAllRegion: ',opsiClusterAllRegion,' opsiClusterCenterRegion: ',opsiClusterCenterRegion
	
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
	bestMatch, infocar, time_exec = searchQuery(upload.filename)
	
	if opsiR is '1':
		
		# Color Dominants process
		if region is '1': # All - 5 Region
			if opsiClusterAllRegion is '1': # No Clustering
				# without centroid
				fileIndex = 'indexcar.csv'
			elif opsiClusterAllRegion is not None: # Clustering with Centroid
				# Clustering with Centroid
				fileIndex = 'index_clustering_{centroid}.csv'.format(centroid=int(opsiClusterAllRegion))
		
		elif region is '2': # Center Region only
			
			
	elif opsiR is '2':
		# Shape Dominants process
	
	# show result page
	return template('./frontend/result', bestMatch=bestMatch, infocar=infocar, time_exec=time_exec, query=upload.filename)

if __name__ == '__main__':
    run(host='0.0.0.0', port=80, debug=True, reloader=True)
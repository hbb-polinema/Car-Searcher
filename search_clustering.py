# Usage: >> python search.py --index index.csv --query queries/sample_query.jpg --result-path datacars --cluster 10
# or >> py search_clustering.py -i <your_index_filename> -q <your_query_image> -r <your_dataset> -c <number_of_cluster>

# import the necessary packages
from module.clustering import Clustering
from module.searcher import Searcher
import argparse
import cv2
import time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
ap.add_argument("-c", "--cluster", required = True,
	help = "Number of Clustering")
args = vars(ap.parse_args())

# Estimated timing
start_time = time.time()

# initialize cluster of the color quantization kmeans descriptor
K = int(args["cluster"])
C = Clustering(K)

# load the query image and describe it
query = cv2.imread(args["query"])
new_img = C.color_quantization_kmeans(query)
features = C.cal_region_hist(new_img)

# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
print "\nResults: ",results

# display the query
cv2.imshow("Query: %s"% (args["query"]), query)
cv2.imshow("Color Quantization KMeans", new_img)

# Result estimated time
print("\n--- Estimated time execution: %s seconds ---" % round(time.time() - start_time, 4))

# loop over the results
i = 0
print '\n 10 Best Matching Result for Query: ', args["query"], '\n'
for (score, resultID) in results:
	# load the result image and display it
	result = cv2.imread(args["result_path"] + "/" + resultID)
	
	i = i + 1
	cv2.imshow('Result #%s - %s'% (i, resultID), result)
	print i,'.\t Score: ', score, '\t\t | image: ', resultID
	
	cv2.waitKey(0)
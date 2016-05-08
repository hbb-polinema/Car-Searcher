# Usage: >> python index.py --dataset dataset --index index.csv --cluster 10
# or >> py index_clustering.py -d <your_folder_data_images> -i <output_file_index.csv> -c <number_of_cluster>

# import the necessary packages
from module.clustering import Clustering
import argparse
import glob
import cv2
import time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-c", "--cluster", required = True,
	help = "Number of Clustering")
args = vars(ap.parse_args())

# Estimated timing
start_time = time.time()

# initialize cluster of the color quantization kmeans descriptor
K = int(args["cluster"])
C = Clustering(K)

# open the output index file for writing
output = open(args["index"], "w")

# use glob to grab the image paths and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	# extract the image ID (i.e. the unique filename) from the image
	# path and load the image itself
	imageID = imagePath[imagePath.rfind("\\") + 1:]
	image = cv2.imread(imagePath)
	
	# describe the image
	new_img = C.color_quantization_kmeans(image)
	features = C.cal_region_hist(new_img)

	print 'imageID: ',imageID, 'len(features): ', len(features)
	
	# write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()

# Result estimated time
print("\n--- Estimated time execution: %s seconds ---" % round(time.time() - start_time, 4))

# --- Estimated time execution: 560.427 seconds --- 20:09 - 08/05/2016 250 features-center/image - 50 features/region - 5 region
# --- Estimated time execution: 176.922 seconds --- 21:01 - 08/05/2016 50 features-center/image - 10 features/region - 5 region
# --- Estimated time execution: 150.203 seconds --- 21:28 - 08/05/2016 35 features-center/image - 7 features/region - 5 region
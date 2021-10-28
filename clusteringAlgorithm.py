"""
# This work is submitted by:
#     Name: Shubham Singh
#     Student ID: 201538011
#     Date of submission: 20 March 2021
"""

# distance calculator function 
# for distance between two points
def distanceBetweenTwoPoints(p1, p2):
    '''
    Takes in two data points (tuples) p1 and p2,
    unpacks them to x1, y1 and x1,y2 coordinates
    return distance between the two poits using 
    distance formula: 
    ((x2-x1)**2 + (y2-y1)**2)**0.5)
    '''
    x1, y1 = p1
    x2, y2 = p2

    return ((x2-x1)**2 + (y2-y1)**2)**0.5

# mean calculator function
# claculates mean of set of (x,y) coordinates
def meanOfPoints(setOfPoints):
    '''
    Takes in set of points
    and return their mean.
    '''
    meanX = sum([point[0] for point in setOfPoints])/len(setOfPoints)
    meanY = sum([point[1] for point in setOfPoints])/len(setOfPoints)

    return (round(meanX,2), round(meanY,2))

def main():

    print("Entering main loop...............\n")

    print("Executing the program clusteringAlgorithm.py")
    dataSet = {(0,0), (1,0), (1,1), (0,1), (-1,0)}
    print("The given five data points are: \n", dataSet)

    # cluster centroids are preassigned
    centroid1 = (1,0)
    centroid2 = (1,1)
    print("Chosen two centroids are: {},{}\n".format(centroid1, centroid2))

    # define two clusters
    # they can be defined as two empty sets
    cluster1 = set()
    cluster2 = set()
    print("Intialising two clusters as empty sets....\n")

    numOfIterations = 2
    print("Number of iterations slected: ", numOfIterations)

    for iteration in range(numOfIterations):

        print("="*100)
        print("Current iteration: ", iteration+1)
        
        # compare the distance of a point from the two centroids
        for dataPoint in dataSet:
            
            distanceFromCentroid1 = distanceBetweenTwoPoints(centroid1,dataPoint)
            distanceFromCentroid2 = distanceBetweenTwoPoints(centroid2,dataPoint)

            # cluster the point which has minimum distance from centroid
            if distanceFromCentroid1 < distanceFromCentroid2:
                cluster1.add(dataPoint)
            else:
                cluster2.add(dataPoint)


        print("Cluter 1 formed: {}".format(cluster1))
        print("Cluter 2 formed: {}".format(cluster2))

   
        meanOfCluster1 = meanOfPoints(cluster1)
        meanOfCluster2 = meanOfPoints(cluster2)
        print("Mean of points in cluster 1: ", meanOfCluster1)
        print("Mean of points in cluster 2: ", meanOfCluster2)

     
        
        print("re-intialising clusters with new means......")
        centroid1 = meanOfCluster1
        centroid2 = meanOfCluster2
        print("The new centroid is: ", centroid1)
        print("The new centroid is: ", centroid2)
        
        # reset the clusters
        cluster1 = set()
        cluster2 = set()

        print("="*100)

   
    print("Exiting the main loop........")
    print("Exiting the program!")


# main iteration loop
if __name__ == "__main__":
    main()

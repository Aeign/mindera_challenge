import numpy as np


def cluster(ints, centroids):
    clusters = {}

    for i in ints:
        best_centroid = min(centroids, key=lambda x: abs(i - x))
        try:
            clusters[best_centroid].append(i)
        except KeyError:
            clusters[best_centroid] = [i]

    return clusters


def calculate_centroids(clusters):
    centroids = []
    keys = sorted(clusters.keys())

    for k in keys:
        centroids.append(np.mean(clusters[k], axis=0))

    return centroids


def centroids_changed(old_centroids, centroids):
    return set(old_centroids) != set(centroids)


def group(ints, k):
    # initialize clusters and k centroids
    clusters = np.array_split(ints, k)

    # if we want the initial list sorted then use this instead
    #  clusters = np.array_split(sorted(ints), k)

    centroids = []

    for i in range(k):
        centroids.append(np.mean(clusters[i], axis=0))

    old_centroids = []

    while centroids_changed(old_centroids, centroids):
        old_centroids = centroids

        # assign ints to clusters
        clusters = cluster(ints, centroids)

        # calculate new centroids
        centroids = calculate_centroids(clusters)

    return clusters


def print_clusters(clusters):
    for x in clusters.keys():
        print(clusters[x])


# test 1
ls = [16, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 67]
k = 3
print_clusters(group(ls, k))
print()

'''
[ [ 16, 15, 14, 13, 12, 12 ],
[ 34, 23, 24, 25, 26, 28, 34, 23, 29, 23, 23, 34, 23, 23 ],
[ 45, 45, 67, 45, 67, 67 ] ]
'''

# test 2
ls = [16, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 670]
k = 3
print_clusters(group(ls, k))
print()

'''
[ [ 16, 15, 14, 13, 23, 24, 25, 26, 28, 23, 29, 12, 23, 23, 12, 23, 23 ],
[ 34, 45, 34, 45, 67, 34, 45, 67 ],
[ 670 ] ]
'''

# test 3
ls = [160, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 670]
k = 4
print_clusters(group(ls, k))
print()

'''
[ [ 160 ],
[ 15, 14, 13, 23, 24, 25, 26, 28, 23, 29, 12, 23, 23, 12, 23, 23 ],
[ 34, 45, 34, 45, 67, 34, 45, 67 ],
[ 670 ] ]
'''

# test 4
ls = [16, 15, 14, 13, 34, 23, 24, 25, 26, 28, 45, 34, 23, 29, 12, 23, 45, 67, 23, 12, 34, 45, 23, 67, 23, 67]
k = 5
print_clusters(group(ls, k))
print()

'''
[ [ 16, 15, 14, 13, 12, 12 ],
[ 34, 34, 29, 34 ],
[ 23, 24, 25, 26, 28, 23, 23, 23, 23, 23 ],
[ 45, 45, 45 ],
[ 67, 67, 67 ] ]
'''
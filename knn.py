from collections import Counter
from linear_algebra import distance
from statistics import mean
import math, random
import matplotlib.pyplot as plt
from data import cities
import copy

def deep_copy(list):
    new_list = copy.deepcopy(list)
    return new_list

def majority_vote(labels):
    """assumes that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count])

    if num_winners == 1:
        return winner                     # unique winner, so return it
    else:
        return majority_vote(labels[:-1]) # try again without the farthest


def knn_classify(k, labeled_points, new_point):
    """each labeled point should be a pair (point, label)"""

    # order the labeled points from nearest to farthest
    by_distance = sorted(labeled_points,
                         key=lambda point_label: distance(point_label[0], new_point))

    # find the labels for the k closest
    k_nearest_labels = [label for _, label in by_distance[:k]]

    # and let them vote
    return majority_vote(k_nearest_labels)


def predict_preferred_language_by_city(k_values, cities):
    """
    TODO
    predicts a preferred programming language for each city using above knn_classify() and
    counts if predicted language matches the actual language.
    Finally, print number of correct for each k value using this:
    print(k, "neighbor[s]:", num_correct, "correct out of", len(cities))
    """
    positive_count = {}
    a= []

    for k_val in k_values:
        positive_count[k_val] = 0

    for city, language in cities:
        n_l = deep_copy(cities)
        n_l.remove((city,language))
        for k_val in k_values:
            res = knn_classify(k_val, n_l,city)
            if res == language:
                positive_count[k_val] += 1

    for k in k_values:
        print(k, "neighbor[s]:", positive_count[k], "correct out of", len(cities))

if __name__ == "__main__":
    k_values = [1, 3, 5, 7]
    # TODO
    # Import cities from data.py and pass it into predict_preferred_language_by_city(x, y).
    predict_preferred_language_by_city(k_values, cities)
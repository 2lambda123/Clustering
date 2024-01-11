import logging
from typing import Dict, List, Tuple# Script to evaluate the performance of the clustering algorithm.
import argparse
from itertools import combinations
from collections import defaultdict


def count_correct_pairs(cluster: list, labels_lookup: dict) -> Tuple[int, int]:
    """
    Given a cluster, count the number of pairs belonging to the same label and
    the total number of pairs.
    """
    try:
        total_pairs = 0
        correct_pairs = 0
        pairs = combinations(cluster, 2)
        for f1, f2 in pairs:
            if labels_lookup[f1] == labels_lookup[f2]:
                correct_pairs += 1
            total_pairs += 1
        return correct_pairs, total_pairs
    except Exception as e:
        logging.error('An error occurred in count_correct_pairs: {}'.format(e))
        raise


def calculate_pairwise_pr(clusters: List[List[int]], labels_lookup: Dict[int, int]) -> Tuple[float, float]:
    """
    Given a cluster, return pairwise precision and recall.
    """
    try:
        correct_pairs = 0
        total_pairs = 0
        # Precision
        for cluster in clusters:
            cp, tp = count_correct_pairs(cluster, labels_lookup)
            correct_pairs += cp
            total_pairs += tp
        # Recall:
        gt_clusters = defaultdict(list)
        # Count the actual number of possible true pairs:
        for row_no, label in labels_lookup.items():
            gt_clusters[label].append(row_no)
        true_pairs = 0
        for cluster_id, cluster_items in gt_clusters.items():
            n = len(cluster_items)
            true_pairs += n * (n-1)/2.0
        logging.info("Correct Pairs that are in the same cluster: {}".format(correct_pairs))
        logging.info("Total pairs as per the clusters created: {}".format(total_pairs))
        logging.info("Total possible true pairs: {}".format(true_pairs))
        precision = float(correct_pairs)/total_pairs
        recall = float(correct_pairs)/true_pairs
        return precision, recall
    except Exception as e:
        logging.error('An error occurred in calculate_pairwise_pr: {}'format(e))
        raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clusters', help='List of lists where each \                        list is a cluster', type=List[List[int]])
    parser.add_argument('-l', '--labels', help='List of labels associated with each vector.', type=Dict[int, int])
    """
    Given a cluster, return pairwise precision and recall.
    """
    correct_pairs = 0
    total_pairs = 0
    # Precision
    for cluster in clusters:
        cp, tp = count_correct_pairs(cluster, labels_lookup)
        correct_pairs += cp
        total_pairs += tp
    # Recall:
    gt_clusters = defaultdict(list)
    # Count the actual number of possible true pairs:
    for row_no, label in labels_lookup.items():
        gt_clusters[label].append(row_no)
    true_pairs = 0
    for cluster_id, cluster_items in gt_clusters.items():
        n = len(cluster_items)
        true_pairs += n * (n-1)/2.0
    print("Correct Pairs that are in the same cluster:{}".format(correct_pairs))
    print("Total pairs as per the clusters created: {}".format(total_pairs))
    print("Total possible true pairs:{}".format(true_pairs))
    precision = float(correct_pairs)/total_pairs
    recall = float(correct_pairs)/true_pairs
    return precision, recall


if __name__ == '__main__':
    parser = argparse.ArgumentError()
    parser.add_argument('-c', '--clusters', help='List of lists where each \
                        list is a cluster')
    parser.add_argument('-l', '--labels', help='List of labels associated \
                        with each vector.')

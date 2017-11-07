"""A Yelp-powered Restaurant Recommendation Program"""

from abstractions import *
from data import ALL_RESTAURANTS, CATEGORIES, USER_FILES, load_user_file
from ucb import main, trace, interact
from utils import distance, mean, zip, enumerate, sample
from visualize import draw_map

##################################
# Phase 2: Unsupervised Learning #
##################################


def find_closest(location, centroids):
    """Return the centroid in centroids that is closest to location.
    If multiple centroids are equally close, return the first one.

    >>> find_closest([3.0, 4.0], [[0.0, 0.0], [2.0, 3.0], [4.0, 3.0], [5.0, 5.0]])
    [2.0, 3.0]
    """
    closest = centroids[0]
    dist = distance(location, centroids[0])
    for cent in centroids:
        if distance(location, cent) < dist:
            dist = distance(location, cent)
            closest = cent
    return closest


def group_by_first(pairs):
    """Return a list of pairs that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    Arguments:
    pairs -- a sequence of pairs

    >>> example = [ [1, 2], [3, 2], [2, 4], [1, 3], [3, 1], [1, 2] ]
    >>> group_by_first(example)
    [[2, 3, 2], [2, 1], [4]]
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]


def group_by_centroid(restaurants, centroids):
    """Return a list of clusters, where each cluster contains all restaurants
    nearest to a corresponding centroid in centroids. Each item in
    restaurants should appear once in the result, along with the other
    restaurants closest to the same centroid.
    """

    restaurant_locations = [restaurant_location(i) for i in restaurants]
    closest_to_centroid = [find_closest(i, centroids) for i in restaurant_locations]
    #restaurants paired to their closest centroid [centroid, restaurant]
    restaurant_centroid_pairs = [[closest_to_centroid[i], restaurants[i]] \
        for i in range(len(closest_to_centroid))]
    return group_by_first(restaurant_centroid_pairs)



def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    return [mean([restaurant_location(cent)[0] for cent in cluster]), \
        mean([restaurant_location(cent)[1] for cent in cluster])]


def k_means(restaurants, k, max_updates=100):
    """Use k-means to group restaurants by location into k clusters."""
    assert len(restaurants) >= k, 'Not enough restaurants to cluster'
    old_centroids, n = [], 0
    # Select initial centroids randomly by choosing k different restaurants
    centroids = [restaurant_location(r) for r in sample(restaurants, k)]

    while old_centroids != centroids and n < max_updates:
        old_centroids = centroids
        same_centroids_list = group_by_centroid(restaurants, centroids)
        centroids = [find_centroid(i) for i in same_centroids_list]
        n += 1
    return centroids


################################
# Phase 3: Supervised Learning #
################################


def find_predictor(user, restaurants, feature_fn):
    """Return a rating predictor (a function from restaurants to ratings),
    for a user by performing least-squares linear regression using feature_fn
    on the items in restaurants. Also, return the R^2 value of this model.

    Arguments:
    user -- A user
    restaurants -- A sequence of restaurants
    feature_fn -- A function that takes a restaurant and returns a number
    """
    reviews_by_user = {review_restaurant_name(review): review_rating(review)
                       for review in user_reviews(user).values()}

    xs = [feature_fn(r) for r in restaurants]
    ys = [reviews_by_user[restaurant_name(r)] for r in restaurants]

    sxx_sub = [i-mean(xs) for i in xs]
    sxx = 0
    for i in range(len(sxx_sub)):
        sxx += sxx_sub[i] * sxx_sub[i]

    syy_sub = [j-mean(ys) for j in ys]
    syy = 0
    for j in range(len(syy_sub)):
        syy += syy_sub[j] * syy_sub[j]
    sxy = 0
    for k in range(len(sxx_sub)):
        sxy += sxx_sub[k] * syy_sub[k]

    b = sxy/sxx
    a = mean(ys) - b * mean(xs)
    r_squared = sxy * sxy / (sxx * syy)


    def predictor(restaurant):
        return b * feature_fn(restaurant) + a

    return predictor, r_squared


def best_predictor(user, restaurants, feature_fns):
    """Find the feature within feature_fns that gives the highest R^2 value
    for predicting ratings by the user; return a predictor using that feature.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of functions that each takes a restaurant
    """
    reviewed = user_reviewed_restaurants(user, restaurants)

    predictor_for_feature_fns = [find_predictor(user, reviewed, fn) for fn in feature_fns]

    highest_r_square = None
    highest_r_square_predictor = None
    for (predictor, r_squared) in predictor_for_feature_fns:
        if highest_r_square is None:
            highest_r_square = r_squared
            highest_r_square_predictor = predictor

        elif r_squared > highest_r_square:
            highest_r_square = r_squared
            highest_r_square_predictor = predictor
    return highest_r_square_predictor


def rate_all(user, restaurants, feature_fns):
    """Return the predicted ratings of restaurants by user using the best
    predictor based on a function from feature_fns.

    Arguments:
    user -- A user
    restaurants -- A list of restaurants
    feature_fns -- A sequence of feature functions
    """
    predictor = best_predictor(user, ALL_RESTAURANTS, feature_fns)
    reviewed = user_reviewed_restaurants(user, restaurants)

    user_ratings_dictionary = {}


    for r in restaurants:
        name = restaurant_name(r)
        if r not in reviewed:
            user_ratings_dictionary[name] = predictor(r)
        else:
            user_ratings_dictionary[name] = user_rating(user, name)
    return user_ratings_dictionary



def search(query, restaurants):
    """Return each restaurant in restaurants that has query as a category.

    Arguments:
    query -- A string
    restaurants -- A sequence of restaurants
    """

    return [r for r in restaurants if query in restaurant_categories(r)]


def feature_set():
    """Return a sequence of feature functions."""
    return [restaurant_mean_rating,
            restaurant_price,
            restaurant_num_ratings,
            lambda r: restaurant_location(r)[0],
            lambda r: restaurant_location(r)[1]]


@main
def main(*args):
    import argparse
    parser = argparse.ArgumentParser(
        description='Run Recommendations',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('-u', '--user', type=str, choices=USER_FILES,
                        default='test_user',
                        metavar='USER',
                        help='user file, e.g.\n' +
                        '{{{}}}'.format(','.join(sample(USER_FILES, 3))))
    parser.add_argument('-k', '--k', type=int, help='for k-means')
    parser.add_argument('-q', '--query', choices=CATEGORIES,
                        metavar='QUERY',
                        help='search for restaurants by category e.g.\n'
                        '{{{}}}'.format(','.join(sample(CATEGORIES, 3))))
    parser.add_argument('-p', '--predict', action='store_true',
                        help='predict ratings for all restaurants')
    parser.add_argument('-r', '--restaurants', action='store_true',
                        help='outputs a list of restaurant names')
    args = parser.parse_args()

    # Output a list of restaurant names
    if args.restaurants:
        print('Restaurant names:')
        for restaurant in sorted(ALL_RESTAURANTS, key=restaurant_name):
            print(repr(restaurant_name(restaurant)))
        exit(0)

    # Select restaurants using a category query
    if args.query:
        restaurants = search(args.query, ALL_RESTAURANTS)
    else:
        restaurants = ALL_RESTAURANTS

    # Load a user
    assert args.user, 'A --user is required to draw a map'
    user = load_user_file('{}.dat'.format(args.user))

    # Collect ratings
    if args.predict:
        ratings = rate_all(user, restaurants, feature_set())
    else:
        restaurants = user_reviewed_restaurants(user, restaurants)
        names = [restaurant_name(r) for r in restaurants]
        ratings = {name: user_rating(user, name) for name in names}

    # Draw the visualization
    if args.k:
        centroids = k_means(restaurants, min(args.k, len(restaurants)))
    else:
        centroids = [restaurant_location(r) for r in restaurants]
    draw_map(centroids, restaurants, ratings)

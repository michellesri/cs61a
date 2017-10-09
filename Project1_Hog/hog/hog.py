"""CS 61A Presents The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

import math

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS>0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return the
    number of 1's rolled.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    sum_dice = 0
    one_die_count = 0
    while num_rolls > 0:
        dice_roll = dice()
        num_rolls -= 1
        if dice_roll == 1:
            one_die_count += 1
        else:
            sum_dice += dice_roll
    if one_die_count > 0:
        return one_die_count
    return sum_dice
    # END PROBLEM 1


def free_bacon(opponent_score):
    """Return the points scored from rolling 0 dice (Free Bacon)."""
    # BEGIN PROBLEM 2
    digits = [int(x) for x in str(opponent_score)]
    return max(digits) + 1
    # END PROBLEM 2

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True


def next_prime(n):
    """Return the next prime number after n"""
    if n < 0:
        return 'Error: invalid number for next_prime fn'
    if n == 0:
        return 1
    num = n + 1
    while is_prime(num) is False:
        num += 1
    return num
# Write your prime functions here!


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player. Also
    implements the Hogtimus Prime and When Pigs Fly rules.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 2
    rolls = num_rolls

    # free bacon
    if rolls == 0:
        turn_total = free_bacon(opponent_score)
    else:
        turn_total = roll_dice(num_rolls, dice)

    # hogtimus prime
    if is_prime(turn_total):
        turn_total = next_prime(turn_total)

    # when pigs fly
    if turn_total > (25 - num_rolls):
        turn_total = 25 - num_rolls

    return turn_total
    # END PROBLEM 2


def reroll(dice):
    """Return dice that return even outcomes and re-roll odd outcomes of DICE."""
    def rerolled():
        # BEGIN PROBLEM 3
        dice_outcome = dice()
        if dice_outcome % 2 != 0:
            return dice()
        return dice_outcome
        # END PROBLEM 3
    return rerolled


def select_dice(score, opponent_score, dice_swapped):
    """Return the dice used for a turn, which may be re-rolled (Hog Wild) and/or
    swapped for four-sided dice (Pork Chop).

    DICE_SWAPPED is True if and only if four-sided dice are being used.
    """
    # BEGIN PROBLEM 4
    if dice_swapped:
        dice = four_sided
    else:
        dice = six_sided
    # END PROBLEM 4
    if (score + opponent_score) % 7 == 0:
        dice = reroll(dice)
    return dice


def other(player):
    """Return the other player, for a player PLAYER numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - player

dice_swapped = False

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """

    global dice_swapped
    player = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    dice_swapped = False  # Whether 4-sided dice have been swapped for 6-sided
    # BEGIN PROBLEM 5

    def swine_swap(score0, score1):
        if score0 * 2 == score1:
            higher_score = score1
            score1 = score0
            score0 = higher_score
        elif score1 * 2 == score0:
            higher_score = score0
            score0 = score1
            score1 = higher_score
        return score0, score1

    while score0 < goal and score1 < goal:
        if player == 0:
            num_rolls = strategy0(score0, score1)
            if num_rolls == -1:
                dice_swapped = not dice_swapped
                score0 += 1
            else:
                selected_dice = select_dice(score0, score1, dice_swapped)
                score0 += take_turn(num_rolls, score1, selected_dice)
        else:
            num_rolls = strategy1(score1, score0)
            if num_rolls == -1:
                dice_swapped = not dice_swapped
                score1 += 1
            else:
                selected_dice = select_dice(score1, score0, dice_swapped)
                score1 += take_turn(num_rolls, score0, selected_dice)

        score0, score1 = swine_swap(score0, score1)
        player = other(player)
    return score0, score1




#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


def check_strategy_roll(score, opponent_score, num_rolls):
    """Raises an error with a helpful message if NUM_ROLLS is an invalid
    strategy output. All strategy outputs must be integers from -1 to 10.

    >>> check_strategy_roll(10, 20, num_rolls=100)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(10, 20) returned 100 (invalid number of rolls)

    >>> check_strategy_roll(20, 10, num_rolls=0.1)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(20, 10) returned 0.1 (not an integer)

    >>> check_strategy_roll(0, 0, num_rolls=None)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(0, 0) returned None (not an integer)
    """
    msg = 'strategy({}, {}) returned {}'.format(
        score, opponent_score, num_rolls)
    assert type(num_rolls) == int, msg + ' (not an integer)'
    assert -1 <= num_rolls <= 10, msg + ' (invalid number of rolls)'


def check_strategy(strategy, goal=GOAL_SCORE):
    """Checks the strategy with all valid inputs and verifies that the
    strategy returns a valid input. Use `check_strategy_roll` to raise
    an error with a helpful message if the strategy returns an invalid
    output.

    >>> def fail_15_20(score, opponent_score):
    ...     if score != 15 or opponent_score != 20:
    ...         return 5
    ...
    >>> check_strategy(fail_15_20)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(15, 20) returned None (not an integer)
    >>> def fail_102_115(score, opponent_score):
    ...     if score == 102 and opponent_score == 115:
    ...         return 100
    ...     return 5
    ...
    >>> check_strategy(fail_102_115)
    >>> fail_102_115 == check_strategy(fail_102_115, 120)
    Traceback (most recent call last):
     ...
    AssertionError: strategy(102, 115) returned 100 (invalid number of rolls)
    """
    # BEGIN PROBLEM 6
    for i in range(0, goal):
        for j in range(0, goal):
            num_rolls = strategy(i, j)
            check_strategy_roll(i, j, num_rolls)


    # END PROBLEM 6


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    """
    # BEGIN PROBLEM 7
    def inner(*args):
        result = 0
        for _ in range(num_samples):
            result += fn(*args)
        result = result / num_samples
        return result
    return inner

# newFn = make_averaged(roll_dice, num_samples)
# def inner(dice=1, 3, num_rolls=1):
#     result = 0
#     for _ in range(1000):
#         result += roll_dice(dice, num_rolls=1)
#     result = result / 1000
#     return result

        # END PROBLEM 7


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN PROBLEM 8
    highest = 0
    best_num_rolls = 0
    for i in range(1, 11):
        averaged_val = make_averaged(roll_dice, num_samples)(i, dice)
        if averaged_val > highest:
            highest = averaged_val
            best_num_rolls = i
    return best_num_rolls


    # END PROBLEM 8

def max_scoring_turn(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    highest = 0
    best_num_rolls = 0
    for i in range(1, 11):
        # passing in 0 for opponent score because we don't want to take
         # into account free bacon
        averaged_val = make_averaged(take_turn, num_samples)(i, 0, dice)
        if averaged_val > highest:
            highest = averaged_val
            best_num_rolls = i
    return best_num_rolls
#take_turn(num_rolls, opponent_score, dice)


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(4)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        rerolled_max = max_scoring_num_rolls(reroll(six_sided))
        print('Max scoring num rolls for re-rolled dice:', rerolled_max)

    if False:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_turn(six_sided, 10000)
        four_sided_max = max_scoring_turn(four_sided, 10000)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

        rerolled_max_six_sided = max_scoring_turn(reroll(six_sided))
        rerolled_max_four_sided = max_scoring_turn(reroll(four_sided))

        print('Max scoring num rolls for re-rolled dice six_sided', rerolled_max_six_sided)
        print('Max scoring num rolls for re-rolled dice four_sided', rerolled_max_four_sided)


    if False:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8))) #21%

    if False:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy)) #51.8%

    if False:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy)) #46%

    print('My strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN PROBLEM 9
    bacon_score = free_bacon(opponent_score)
    if is_prime(bacon_score):
        bacon_score = next_prime(bacon_score)
    if bacon_score >= margin:
        #and (score + opponent_score + bacon_score) % 7 != 0
        return 0
    return num_rolls
    # END PROBLEM 9
check_strategy(bacon_strategy)


def swap_strategy(score, opponent_score, margin=8, num_rolls=4):
    """This strategy rolls 0 dice when it triggers a beneficial swap. It also
    rolls 0 dice if it gives at least MARGIN points. Otherwise, it rolls
    NUM_ROLLS.
    """
    if opponent_score * 2 == score or \
    bacon_strategy(score, opponent_score, margin, num_rolls) == 0:
        return 0
    return num_rolls
    # END PROBLEM 10
check_strategy(swap_strategy)


def final_strategy(score, opponent_score):
    """Strategy:
    Force the dice to be a 4 sided so that there is a lower chance of getting a 1.
    Check if hog wild is in play.
    Roll more if hog wild.
    If we are leading by at least 1.5x, lower our margin.
    If opponent score is 2x, swap scores.

    """
    # BEGIN PROBLEM 11
    if score == 0:
        return -1

    is_hog_wild = (score + opponent_score) % 7 == 0
    # is_six_sided = not dice_swapped

    if is_hog_wild:
        # if is_six_sided:
        #     num_rolls = 5
        #     margin = 1
        # else: #four sided
        num_rolls = 6
        margin = 8
    else:
        # if is_six_sided:
        #     num_rolls = 4
        #     margin = 10
        # else: #four sided
        num_rolls = 4
        margin = 6

    margin = min(margin, 100 - score)

    if opponent_score * 1.5 <= score:
        margin = min(5, 100 - score)

    if swap_strategy(score, opponent_score, margin, num_rolls) == 0:
        return 0

    return num_rolls
check_strategy(final_strategy)


##########################
# Command Line Interface #
##########################

# NOTE: Functions in this section do not need to be changed. They use features
# of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()

import re
import statistics

def parse_votes(votes_string):
    votes_string_list = votes_string.strip().split()
    votes = []
    for vote in votes_string_list:
        try:
            votes.append(int(vote))
        except ValueError:
            pass
    return votes

def check_for_break(votes_list):
    fib_series = generate_fibonacci(20)
    min_val = min(votes_list)
    max_val = max(votes_list)
    while min_val not in fib_series:
        if min_val < min(fib_series):
            min_val = min(fib_series)
        else:
            min_val -= 1
    while max_val not in fib_series:
        if max_val > max(fib_series):
            max_val = max(fib_series)
        else:
            max_val += 1
    min_index = fib_series.index(min_val)
    max_index = fib_series.index(max_val)
    return ((max_index - min_index) > 3)

def generate_fibonacci(length):
    series = [0, 1, 2]
    if length <=0:
        raise Exception("Cannot take 0 or negative value for length")
    if length < 3:
        return series[0: length]
    while len(series) < length:
        series.append(series[-1] + series[-2])
    return series


if __name__ == '__main__':
    print("Welcome to Planning Poker!")
    while True:
        string_votes = input("\nEnter estimates separated by a space: ")
        if string_votes == 'no':
            break
        votes = parse_votes(string_votes)
        mean = statistics.mean(votes)
        discussion_needed = check_for_break(votes)
        print("\nAverage estimate is: {}".format(round(mean, 1)))
        if (discussion_needed):
            print("{} and {} differ by more that 3 Fibonacci numbers. Discuss!".format(min(votes), max(votes)))
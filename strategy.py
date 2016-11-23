import time

SLOW = 3  # delay 3 seconds
LIMIT = 10  # the number of characters
WARNING = 'You get a slow algorithm!'


def pairs(seq):
    """
    generate a generator that take two adjacent elements circularly.
    :param seq: a sequence
    :return: a generator
    """
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i+1) % n]


def all_unique_sort(seq):
    if len(seq) >= LIMIT:
        # simulate a situation when the algorithm can't work efficiently
        print(WARNING)
        time.sleep(SLOW)

    sorted_seq = sorted(seq)
    for (c1, c2) in pairs(sorted_seq):
        if c1 == c2:
            return False
    return True


def all_unique_set(seq):
    n = len(seq)
    if n < LIMIT:
        # simulate a situation when the algorithm can't work efficiently
        print(WARNING)
        time.sleep(SLOW)

    # make use of set's non-repeatability
    return True if len(set(seq)) == n else False


def all_unique(seq, strategy=None):
    if strategy is None:
        if len(seq) >= LIMIT:
            return all_unique_set(seq)
        else:
            return all_unique_sort(seq)
    else:
        return strategy(seq)


if __name__ == '__main__':
    strategies = {'1': all_unique_set, '2': all_unique_sort}
    while True:
        # get input
        word = raw_input("Input the word(type 'exit' to exit)>")
        if word == 'exit':
            break
        strategy_id = raw_input("choose strategy: [1] Use a set, [2] Use a sort>")

        # get strategy
        strategy = strategies.get(strategy_id, None)

        print('all_unique("{}") is {}\n'.format(word, all_unique(word, strategy)))

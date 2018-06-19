def is_palinedrome_permutation(string):
    counter = Counter()
    for letter in string:
        if letter not in [" ", ":", ";"]:
            counter[letter] += 1

    odd_count = 0
    for count in counter.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False

    return True

class Counter(dict):
    def __missing__(self, key):
        return 0

if __name__ == "__main__":
    import sys
    print(is_palinedrome_permutation(sys.argv[-1]))
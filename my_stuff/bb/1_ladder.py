# You have a ladder n-steps in height.  You can either take one step or two steps up the ladder at a time.
# How can you find out all the different combinations up the ladder?  Then figure out an algorithm that will
# actually print out all the different ways up the ladder. i.e.: 1,1,2,1,2,2... etc...

# looks like a recursive/dynamic programming problem
# solve for n=0, n=1, n=2 etc

'''
input: n - the size of the ladder
output: list of step combinations
code is recursive. very memory heavy.
might be possible to print combinations without having to remember all of them.
'''
def ladder_combinations(n):
    if n is 0:
        return []

    if n is 1:
        return [[1]]

    results = ladder_combinations(n-1)

    additional_combos = []
    for result in results:

        if result[-1] is 1:
            temp = result.copy()
            temp[-1] = 2
            additional_combos.append(temp)
        result = result.append(1)

    return results + additional_combos

print(ladder_combinations(5))

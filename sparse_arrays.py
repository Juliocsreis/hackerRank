from collections import Counter

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
query = ['red', 'blue']


def matchingStrings(strings, queries):
    occurrances = [x for x in strings if x in queries]
    counted = Counter(occurrances)
    result = []
    for i in queries:
        result.append(counted[i])
    return result


print(matchingStrings(z, query))

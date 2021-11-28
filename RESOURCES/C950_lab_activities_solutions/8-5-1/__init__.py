def sorted_string(stringToSort):
    return ''.join(sorted(stringToSort))

def group_anagrams(stringList):
    result = dict()
    for string in stringList:
        # Build a sorted version of the string
        sortedString = sorted_string(string)
        if sortedString in result:
            result[sortedString].append(string)
        else:
            result[sortedString] = [string]
    return result

# Read a line of input and parse into a list of strings
stringList = input().split(' ')

# Build the dictionary grouping of anagrams
anagrams = group_anagrams(stringList)

# Display the groups
keys = list(anagrams.keys())
keys.sort()
for key in keys:
    print(key + ': ' + str(anagrams[key]))
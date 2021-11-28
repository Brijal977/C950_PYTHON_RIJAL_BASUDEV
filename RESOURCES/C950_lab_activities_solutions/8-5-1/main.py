def sublists_of_length(full_list, length):
    # Verify length argument
    if length <= 0 or length > len(full_list):
        return []

    # Produce the list of sublists
    sublists = list()
    for i in range(len(full_list) - length + 1):
        sublist = full_list[i:i + length]
        sublists.append(sublist)

    return sublists


# Returns a list of all possible sublists in full_list
def all_sublists(full_list):
    result = []
    for i in range(1, len(full_list) + 1):
        result = result + sublists_of_length(full_list, i)
    return result


def all_sublists_as_tuples(full_list):
    initial_list = all_sublists(full_list)
    return list(map(lambda x: tuple(x), initial_list))


def distinct_sublists(full_list):
    # First get a list of all sublists
    all = all_sublists_as_tuples(full_list)
    # Convert to a set to get distinct lists
    return set(all)


# No output is required for this lab. Unit tests are used to grade your submission.
# The code below shows a few samples to help you check your work before submitting.
if __name__ == "__main__":
    test_lists = [[4, 7, 1, 7], ["red", "green", "blue"], [1, 2, 1, 2]]
    for test_list in test_lists:
        print("Sublists of length 2 from " + str(test_list) + ":")
        print("  " + str(sublists_of_length(test_list, 2)))
        print("All sublists from " + str(test_list) + ":")
        print("  " + str(all_sublists(test_list)))
        print("All sublists as tuples from " + str(test_list) + ":")
        print("  " + str(all_sublists_as_tuples(test_list)))
        print("Distinct sublists from " + str(test_list) + ":")
        print("  " + str(distinct_sublists(test_list)))
        print()
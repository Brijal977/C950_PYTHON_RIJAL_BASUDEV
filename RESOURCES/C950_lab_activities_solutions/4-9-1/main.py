from BinarySearchTree import BinarySearchTree, Node


# Write find_in_range() function
def find_in_range(curr_node, r_1, r_2, keys_in_range):
    # Base case for recursion
    if curr_node is None:
        return
    # Three cases
    if r_1 < curr_node.key:
        find_in_range(curr_node.left, r_1, r_2, keys_in_range)
    if r_1 <= curr_node.key and r_2 >= curr_node.key:
        keys_in_range.append(curr_node.key)
    if r_2 > curr_node.key:
        find_in_range(curr_node.right, r_1, r_2, keys_in_range)


# Main
if __name__ == "__main__":
    tree = BinarySearchTree()
    keys_in_range = []
    # Insert some random-looking integers into the tree.
    user_values = input('Enter values to be inserted separated by spaces: ')
    print()

    for value in user_values.split():
        new_node = Node(value)
        tree.insert(new_node)

    print('Initial tree:')
    print(tree)
    print()

    r_1 = (input('Enter the first range value: '))
    print()
    r_2 = (input('Enter the second range value (greater than the first): '))
    print()
    start_key = (input('Enter the start node\'s key: '))
    print()

    start_node = tree.search(start_key)
    find_in_range(start_node, r_1, r_2, keys_in_range)

    print('Keys in range:', keys_in_range)
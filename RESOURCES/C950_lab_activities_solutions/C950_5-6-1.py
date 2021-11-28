##Lab Activity 5.6.1
from BinarySearchTree import BinarySearchTree, BSTNode
from AVLTree import AVLTree, AVLNode


# FIXME Function to determine the max depth of a tree
def max_depth(node):
    if node is None:
        return -1;  # An empty tree has height −1
    else:
        # Compute the depth of each subtree
        left_depth = max_depth(node.left)
        right_depth = max_depth(node.right)

        # Select max depth
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1


# Create empty tree objects
avl_tree = AVLTree()
binary_search_tree = BinarySearchTree()

# Insert some random-looking integers into the tree.
keys_string = input('Enter values to be inserted separated by spaces: ')

# FIXME Determine number of comparisons per key &
# total number of comparisons for the tree
total_avl_comparisons = 0
total_bst_comparisons = 0

for key in keys_string.split():
    key = int(key)
    avl_node = AVLNode(key)
    avl_insert_comparisons = avl_tree.insert(avl_node)
    total_avl_comparisons += avl_insert_comparisons

    bst_node = BSTNode(key)
    bst_insert_comparisons = binary_search_tree.insert(bst_node)
    total_bst_comparisons += bst_insert_comparisons

    print('Key: %d' % key)
    print('AVL - Insert comparisons: %d' % avl_insert_comparisons)
    print('BST - Insert comparisons: %d\n' % bst_insert_comparisons)

# Print total number of comparisons
print('Total # of comparisons')
print('AVL tree: %d' % total_avl_comparisons)
print('Binary search tree: %d\n' % total_bst_comparisons)

# Print max depth
print('Max tree depth')
print('AVL tree: %d' % max_depth(avl_tree.root))
print('Binary search tree: %d\n' % max_depth(binary_search_tree.root))

# Print the tree after all inserts are complete
print('Trees after insertions:')
print('AVL tree', avl_tree)
print('\nBinary search tree', binary_search_tree)
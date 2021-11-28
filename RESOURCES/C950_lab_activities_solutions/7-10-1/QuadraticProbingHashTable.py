# class to represent an empty bucket
class EmptyBucket:
    pass


# Hashtable class definition using linear probing
class QuadraticProbingHashTable:

    # Constructor with optional initial capacity. All buckets are
    # assigned with an EmptyBucket() instance called self.EMPTY_SINCE_START.
    def __init__(self, initial_capacity=10, c1=0, c2=1):

        # Special constants to be used as the two types of empty buckets.
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        # Initialize all the table buckets to be EMPTY_SINCE_START.
        self.table = [self.EMPTY_SINCE_START] * initial_capacity

        self.c1 = c1
        self.c2 = c2

    # Inserts a new item into the hashtable.
    def insert(self, item):
        # TO-DO: implement the insert() method using quadratic probing
        # when collisions occur. Return True if the item is inserted.
        return False

    # Removes an item with a matching key from the hashtable.
    def remove(self, key):
        # TO-DO: implement the remove() method using quadratic probing
        # when collisions occur. Return True if the item is removed.
        return False

    # Searches for an item with a matching key in the hashtable. Returns the
    # item if found, or None if not found.
    def search(self, key):
        # TO-DO: implement the search() method using quadratic probing
        # when collisions occur. Return the item with a matching key if one
        # is found while probing.
        return None

    # Overloaded string conversion method to create a string
    # representation of the entire hashtable. Special values
    # "E/S" and "E/R" are used to represent "EMPTY_SINCE_START"
    # and "EMPTY_AFTER_REMOVAL".
    def __str__(self):
        s = "   --------\n"
        index = 0
        for bucket in self.table:
            value = str(bucket)
            if bucket is self.EMPTY_SINCE_START:
                value = 'E/S'
            elif bucket is self.EMPTY_AFTER_REMOVAL:
                value = 'E/R'
            s += '{:2}:|{:^6}|\n'.format(index, value)
            index += 1
        s += "   --------"
        return s
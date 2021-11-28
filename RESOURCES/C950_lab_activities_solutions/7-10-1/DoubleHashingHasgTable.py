# class to represent an empty bucket
class EmptyBucket:
    pass


# Hashtable class definition using double hashing.
class DoubleHashingHashTable:

    # Constructor with optional initial capacity. The capacity should always be
    # set to a prime number.
    def __init__(self, initial_capacity=11):

        # Special constants to be used as the two types of empty cells.
        self.EMPTY_SINCE_START = EmptyBucket()
        self.EMPTY_AFTER_REMOVAL = EmptyBucket()

        # Initialize all the table cells to be EMPTY_SINCE_START.
        self.table = [self.EMPTY_SINCE_START] * initial_capacity

    # The secondary hash function. Many different functions can
    # be used here. The function used here is a common one, with
    # different (usually prime number) constants used where the 7 is.
    def h2(self, item):
        return 32 - hash(item) % 32

    # Inserts a new item into the hashtable.
    # TO-DO: add a "collisions" variable to keep track of how many times
    # a collision occurs while trying to insert the key. Return the collision
    # count with the Boolean that is currently being returned.
    def insert(self, item):
        for i in range(len(self.table)):
            # calculate bucket index for the item for this value of i.
            bucket = (hash(item) + self.h2(item) * i) % len(self.table)
            if type(self.table[bucket]) is EmptyBucket:
                self.table[bucket] = item
                return True

        # the entire table was full and the key could not be inserted.
        return False

    # Searches for an item with a matching key in the hashtable.
    # Returns the item if found, or None if not found.
    def search(self, key):
        for i in range(len(self.table)):
            # calculate bucket index for the item for this value of i.
            # hash() is used as the h1 hashing function.
            bucket = (hash(key) + self.h2(key) * i) % len(self.table)
            if self.table[bucket] == key:
                return self.table[bucket]

        # the entire table was full and the key was not found
        return None

    # Removes an item with a matching key from the hashtable,
    # if found.
    def remove(self, key):
        for i in range(len(self.table)):
            # calculate bucket index for the item for this value of i.
            bucket = (hash(key) + self.h2(key) * i) % len(self.table)
            if self.table[bucket] == key:
                self.table[bucket] = self.EMPTY_AFTER_REMOVAL

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
# HashTable class using chaining.
class HashTable:

    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, init_cap=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for x in range(init_cap):
            self.table.append([])

    # finds  the bucket_list
    def bucket_list(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        return bucket_list


    # Inserts a new item into the hash table.
    def insert(self, key, item):
        key_value = [key, item]
        self.bucket_list(key).append(key_value)
        return True


    # update key if it is already in the bucket
    def update(self, key, item):
        for x in self.bucket_list(key):
            # print (key_value)
            if x[0] == key:
                x[1] = item
                return True


    # Removes an item with matching key from the hash table.
    def remove(self, key):
        for x in self.bucket_list(key):
            # print (key_value)
            if x[0] == key:
                self.bucket_list(key).remove([x[0], x[1]])


    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        if self.bucket_list(key) is not None:
            for x in self.bucket_list(key):
                # print (key_value)
                if x[0] == key:
                    return x[1]  # value
        return None

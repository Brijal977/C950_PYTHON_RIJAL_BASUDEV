# import the three hash tables
from LinearProbingHashTable import LinearProbingHashTable
from QuadraticProbingHashTable import QuadraticProbingHashTable
from DoubleHashingHashTable import DoubleHashingHashTable

import random, sys

# double hashing table sizes that will be 3/4 full when adding
# n keys, for n values of:
#     [10, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000].
# Using other values of n could lead to unfair results related to the
# double hashing hash table.
primes_sizes = [17, 67, 137, 269, 673, 1361, 2671, 6673, 13337, 26669, 66683]

# Assume n is 20,000, but this can be overridden by providing a different
# number on the command line.
n = 20000
if len(sys.argv) > 1: n = int(sys.argv[1])

# We want the hashtables to be roughly 75% full after adding n keys.
reg_hashtable_size = int(4 / 3 * n)

# The double hashing hash table needs a prime number for the table size. This
# finds a suitable prime number that will leave the table roughly 75% full after
# adding n keys.
prime_index = 0
while prime_index < len(primes_sizes) and primes_sizes[prime_index] < reg_hashtable_size:
    prime_index += 1
if prime_index == len(primes_sizes):
    import primes

    prime_hashtable_size = primes.next_prime(int(4 / 3 * reg_hashtable_size))
else:
    prime_hashtable_size = primes_sizes[prime_index]

# seed the random number generator so we can have predictable results.
random.seed(123)

# generate n random numbers between 0 and 1 million.
keys = []
for i in range(n):
    keys.append(random.randint(0, 1000000))

# construct 4 different hash tables, with collision-counting variables initialized
# with zero.
lp = LinearProbingHashTable(reg_hashtable_size)
lp_collisions = 0

qp1 = QuadraticProbingHashTable(reg_hashtable_size)
qp1_collisions = 0

qp2 = QuadraticProbingHashTable(reg_hashtable_size, 13, 7)
qp2_collisions = 0

dh = DoubleHashingHashTable(prime_hashtable_size)
dh_collisions = 0

# insert the keys, in order, into all the hash tables, keeping track of
# the total number of collisions for that table.
for k in keys:
    success, collisions = lp.insert(k)
    lp_collisions += collisions
    success, collisions = qp1.insert(k)
    qp1_collisions += collisions
    success, collisions = qp2.insert(k)
    qp2_collisions += collisions
    success, collisions = dh.insert(k)
    dh_collisions += collisions

# Display the results.
print("%35s: %d" % ("Linear Probing", lp_collisions))
print("%35s: %d" % ("Quadratic Probing (c1=0, c2=1)", qp1_collisions))
print("%35s: %d" % ("Quadratic Probing (c1=13, c2=7)", qp2_collisions))
print("%35s: %d" % ("Double Hashing", dh_collisions))

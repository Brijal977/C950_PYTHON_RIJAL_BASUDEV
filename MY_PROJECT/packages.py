import distances
import csv_reader

# Empty lists created
first_tr_pk_list = []
second_tr_pk_list = []
third_tr_pk_list = []

first_tr_distance = []
second_tr_distance = []
third_tr_distance = []

# initial leave time for trucks
first_tr_start_time = ['8:00:00']
second_tr_start_time = ['9:10:00']
third_tr_start_time = ['11:00:00']

# ================================================= first truck ======================================================

# set delivery start time to packets of truck 1   :> O(n)
for index, value in enumerate(csv_reader.get_first_tr_pk_list()):
    csv_reader.get_first_tr_pk_list()[index][9] = first_tr_start_time[0]
    first_tr_pk_list.append(csv_reader.get_first_tr_pk_list()[index])

# Compare first truck addresses to full address list :> O(n^2)
for index, outer in enumerate(first_tr_pk_list):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            first_tr_distance.append(outer[0])
            first_tr_pk_list[index][1] = inner[0]

# Call greedy  algorithm to sort packages for first truck
distances.find_fastest_route(first_tr_pk_list, 1, 0)
total_distance_tr1 = 0

# Calculate :> O(n)
# 1.Total distance of the First truck
# 2.distance of each packages
for index in range(len(distances.get_first_tr_sort_index())):
    try:
        total_distance_tr1 = distances.get_distance(int(distances.get_first_tr_sort_index()[index]),
                                                    int(distances.get_first_tr_sort_index()[index + 1]),
                                                    total_distance_tr1)

        deliver_package = distances.get_time(
            distances.get_current_distance(int(distances.get_first_tr_sort_index()[index]),
                                           int(distances.get_first_tr_sort_index()[index + 1])),
            first_tr_start_time)
        distances.get_first_tr_sort_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_table().update(int(distances.get_first_tr_sort_list()[index][0]), first_tr_pk_list)
    except IndexError:
        pass

# ================================================= Second truck ======================================================

# set delivery start time to packets of truck 1   :> O(n)
for index, value in enumerate(csv_reader.get_second_tr_pk_list()):
    csv_reader.get_second_tr_pk_list()[index][9] = second_tr_start_time[0]
    second_tr_pk_list.append(csv_reader.get_second_tr_pk_list()[index])

# Compare Second truck addresses to full address list :> O(n^2)
for index, outer in enumerate(second_tr_pk_list):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            second_tr_distance.append(outer[0])
            second_tr_pk_list[index][1] = inner[0]

# Call greedy  algorithm to sort packages for Second truck
distances.find_fastest_route(second_tr_pk_list, 2, 0)
total_distance_tr2 = 0

# Calculate :> O(n)
# 1.Total distance of the Second truck
# 2.distance of each package
for index in range(len(distances.get_second_tr_sort_index())):
    try:
        total_distance_tr2 = distances.get_distance(int(distances.get_second_tr_sort_index()[index]),
                                                    int(distances.get_second_tr_sort_index()[index + 1]),
                                                    total_distance_tr2)

        deliver_package = distances.get_time(
            distances.get_current_distance(int(distances.get_second_tr_sort_index()[index]),
                                           int(distances.get_second_tr_sort_index()[
                                                   index + 1])), second_tr_start_time)
        distances.get_second_tr_sort_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_table().update(int(distances.get_second_tr_sort_list()[index][0]), second_tr_pk_list)
    except IndexError:
        pass

# ================================================= Third truck ======================================================

# set delivery start time to packets of truck 3   :> O(n)
for index, value in enumerate(csv_reader.get_third_tr_pk_list()):
    csv_reader.get_third_tr_pk_list()[index][9] = third_tr_start_time[0]
    third_tr_pk_list.append(csv_reader.get_third_tr_pk_list()[index])

# Compare Third truck addresses to full address list :> O(n^2
for index, outer in enumerate(third_tr_pk_list):
    for inner in distances.get_address():
        if outer[2] == inner[2]:
            third_tr_distance.append(outer[0])
            third_tr_pk_list[index][1] = inner[0]

# Call greedy  algorithm to sort packages for Third truck
distances.find_fastest_route(third_tr_pk_list, 3, 0)
total_distance_tr3 = 0

# Calculate :> O(n)
# 1.Total distance of the Third truck
# 2.distance of each package
for index in range(len(distances.get_third_tr_sort_index())):
    try:
        total_distance_tr3 = distances.get_distance(int(distances.get_third_tr_sort_index()[index]),
                                                    int(distances.get_third_tr_sort_index()[index + 1]),
                                                    total_distance_tr3)

        deliver_package = distances.get_time(
            distances.get_current_distance(int(distances.get_third_tr_sort_index()[index]),
                                           int(distances.get_third_tr_sort_index()[index + 1])),
            third_tr_start_time)
        distances.get_third_tr_sort_list()[index][10] = (str(deliver_package))
        csv_reader.get_hash_table().update(int(distances.get_third_tr_sort_list()[index][0]), third_tr_pk_list)
    except IndexError:
        pass

"""
for testing only 
-------------------------------------
#check each truck's total distance
print(total_distance_tr1)
print(total_distance_tr2)
print(total_distance_tr3)
"""


# Get the total distance of all 40 packages :> O(1)
def total_distance_all_tr():
    return total_distance_tr1 + total_distance_tr2 + total_distance_tr3

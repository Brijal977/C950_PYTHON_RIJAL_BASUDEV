import csv
import datetime

# ========================================== Read in csv file  =======================================================
# Read :  distance matrix of addresses csv
with open('distance_data.csv') as csvfile_1:
    distance_csv = list(csv.reader(csvfile_1, delimiter=','))

# Read : list of all addresses csv
with open('address_data.csv') as csvfile_2:
    distance_name_csv = list(csv.reader(csvfile_2, delimiter=','))


    # ==================================== some Distance functions ====================================================
    # Get package address data -> O(n)
    def get_address():
        return distance_name_csv


    def get_distance(row, col, total):  # gets the total distance from given row/column value:> O(1)
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return total + float(distance)


    def get_current_distance(row, col):  # gets the current distance of given truck:>  O(1)
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]

        return float(distance)


    def get_time(distance, truck_list):  # Calculate total distance for a given truck -> O(n)
        new_time = distance / 18
        distance_in_minutes = '{0:02.0f}:{1:02.0f}'.format(
            *divmod(new_time * 60, 60))
        final_time = distance_in_minutes + ':00'
        truck_list.append(final_time)
        total = datetime.timedelta()
        for i in truck_list:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs),
                                        minutes=int(mins), seconds=int(secs))
        return total


    # After applying greedy algorithm : these  optimized (sorted) packets and index lists will be filled
    first_tr_sort_list = []
    first_tr_sort_indices = []

    second_tr_sort_list = []
    second_tr_sort_indices = []

    third_tr_sort_list = []
    third_tr_sort_indices = []

    # =====================================greedy algorithm===========================================================
    """
    ABOUT ME : find_fastest_route :> O(n^2)
    --------------------------------------------------------------------------------------------------
    it uses the greedy technique to find the next closest location based on truck's current location.

    there are  three parameter used:
    1._packet_list  = is the list of packets to be sorted using greedy algorithm
    2.truck_number  = is truck number to which the _packet_list is assigned to
    3.curr_loc      = tracks the current location of given truck as it moves 

    In first for loop:
    it aims to find the shortest distance in _packet_list from the curr_distance 
    the lowest_value variable  keeps updating until it finds the lowest one , 
    and when it finds : assigns to closest_location

    In second for loop:
    the found closest_location will be appended to the new optimized (sorted) packet and index lists (outputs)
    and also will be removed from unsorted list(input) for next iteration 

    it repeats until the base case if condition  satisfies ,then it returns the empty  unsorted list.

    """


    def find_fastest_route(_list, num, curr_location):
        if not len(_list):
            return _list

        lowest_value = 50.0
        location = 0

        for i in _list:
            value = int(i[1])
            if get_current_distance(curr_location, value) <= lowest_value:
                lowest_value = get_current_distance(
                    curr_location, value)
                location = value

        for i in _list:
            if get_current_distance(curr_location, int(i[1])) == lowest_value:
                if num == 1:
                    first_tr_sort_list.append(i)
                    first_tr_sort_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    find_fastest_route(_list, 1, curr_location)
                elif num == 2:
                    second_tr_sort_list.append(i)
                    second_tr_sort_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    find_fastest_route(_list, 2, curr_location)
                elif num == 3:
                    third_tr_sort_list.append(i)
                    third_tr_sort_indices.append(i[1])
                    _list.pop(_list.index(i))
                    curr_location = location
                    find_fastest_route(_list, 3, curr_location)


    # Insert 0 for the first index of each index list
    first_tr_sort_indices.insert(0, '0')
    second_tr_sort_indices.insert(0, '0')
    third_tr_sort_indices.insert(0, '0')


    # return sorted list and indexes - functions :> O(1) each
    # truck_1------------------------------------------------
    def get_first_tr_sort_index():
        return first_tr_sort_indices

    def get_first_tr_sort_list():
        return first_tr_sort_list


    # truck_2------------------------------------------------
    def get_second_tr_sort_index():
        return second_tr_sort_indices

    def get_second_tr_sort_list():
        return second_tr_sort_list


    # truck_3------------------------------------------------
    def get_third_tr_sort_index():
        return third_tr_sort_indices

    def get_third_tr_sort_list():
        return third_tr_sort_list

import csv
from hash_table import HashTable

# Read CSV files
with open('packets_data.csv') as csvfile:
    read_csv = csv.reader(csvfile, delimiter=',')

    hash_table = HashTable()  # Create an instance of HashTable class
    first_tr_pk_list = []  # packets list assigned to truck 1
    second_tr_pk_list = []  # packets list assigned to truck 2
    third_tr_pk_list = []  # packets list assigned to truck 3

    # Insert values from csv file into key/value pairs of the hash table -> O(n)
    for row in read_csv:
        p_id = row[0]
        p_addr_street = row[1]
        p_addr_city = row[2]
        p_addr_state = row[3]
        p_addr_zip = row[4]
        p_delivery = row[5]
        p_size = row[6]
        p_sp_note = row[7]
        delivery_start = ''
        addr_loc = ''
        delivery_status = 'At hub'
        value = [p_id, addr_loc, p_addr_street, p_addr_city, p_addr_state, p_addr_zip, p_delivery, p_size, p_sp_note,
                 delivery_start, delivery_status]

        # following are filters to assign packets to truck
        # the packets are assigned to truck manually based on similarity (patterns) or packet's feathers

        if 'EOD' not in value[6]:
            if 'Delayed on flight---will not arrive to depot until 9:05 am' in value[8] or '3365 S 900 W' in value[2]:
                second_tr_pk_list.append(value)
            elif '3365 S 900 W' in value[2]:
                second_tr_pk_list.append(value)
            else:
                first_tr_pk_list.append(value)

        elif ('EOD' in value[6]) and ('none' not in value[8]):
            if 'Wrong address listed' in value[8]:
                third_tr_pk_list.append(value)
            elif '84103' in value[5]:
                third_tr_pk_list.append(value)
            else:
                second_tr_pk_list.append(value)

        elif ('EOD' in value[6]) and ('none' in value[8]):
            if '177 W Price Ave' in value[2] or '2010 W 500 S' in value[2] or '1330 2100 S' in value[2] or \
                    ('3575 W Valley Central Station bus Loop' in value[2]) or ('3148 S 1100 W' in value[2]):
                first_tr_pk_list.append(value)

            else:
                if ('84103' in value[5]) or ('84111' in value[5]) or ('84117' in value[5]) or ('84119' in value[5]):
                    if '300 State St' in value[2]:
                        third_tr_pk_list.append(value)
                    else:
                        second_tr_pk_list.append(value)
                else:
                    third_tr_pk_list.append(value)

        # Insert value into the hash table
        hash_table.insert(p_id, value)


    """
    # print personalization : for testing only
    # Truck assignments
    # ------------------------------------------------------------------------
    print('=' * 150)
    print("# packets list details  assigned to truck 1")
    print('-' * 100, *first_tr_pk_list, sep="\n")
    print('=' * 150)

    # ------------------------------------------------------------------------
    print('=' * 150)
    print("# packets list details assigned to truck 2")
    print('-' * 100, *second_tr_pk_list, sep="\n")
    print('=' * 150)

    # ------------------------------------------------------------------------
    print('=' * 150)
    print("# packets list details assigned to truck 3")
    print('-' * 100, *third_tr_pk_list, sep="\n")
    print('=' * 150)

    # -----------------------------------------------------------------------------------
    """

    # Get packets list assigned to truck 1  :> O(1)
    def get_first_tr_pk_list():
        return first_tr_pk_list


    # Get packets list assigned to truck 2  :> O(1)
    def get_second_tr_pk_list():
        return second_tr_pk_list


    # Get packets list assigned to truck 3  :> O(1)
    def get_third_tr_pk_list():
        return third_tr_pk_list


    # Get full list of packages :> O(1)
    def get_hash_table():
        return hash_table

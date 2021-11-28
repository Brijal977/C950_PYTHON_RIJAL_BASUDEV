# C950 Data Structures and Algorithms II
# CODED BY : Basudev Rijal
# Student ID: 001365006
# Email: brijal1@wgu.edu
# ----------------------------------------------------------------------------------------------------------------------

from csv_reader import get_hash_table
from packages import total_distance_all_tr
import datetime


# reusable print  functions :> O(1)
def print_status(count):
    print(

        f'Package ID: {get_hash_table().search(str(count))[0]}', """    """
                                                                 f'Truck load time: {get_hash_table().search(str(count))[9]}',
        """    """
        f'Deli1very status: {get_hash_table().search(str(count))[10]}'
    )


# reusable print  functions :> # O(1)
def print_pk_detail(count):
    print(
        '-' * 30, 'package information', '-' * 49, '\n'
                                                   f'Package ID: {get_hash_table().search(str(count))[0]}\n'
                                                   f'Street address: {get_hash_table().search(str(count))[2]}, '
                                                   f'{get_hash_table().search(str(count))[3]}, '
                                                   f'{get_hash_table().search(str(count))[4]}, '
                                                   f'{get_hash_table().search(str(count))[5]},\n'

                                                   f'Delivery deadline : {get_hash_table().search(str(count))[6]}\n'
                                                   f'Package weight: {get_hash_table().search(str(count))[7]} KG\n'
                                                   f'Special note: {get_hash_table().search(str(count))[8]}\n',
        '-' * 30, 'delivery status', '-' * 51,
    )


class Main:
    # welcome page Header
    print('*' * 100)
    print('----------------------------  WGUPS - Packet Tracking Console  ------------------------------------',
          sep='\n')
    print('*' * 100)

    # total delivery package for all 40 packets
    print('# Complete delivery of all 40 packets were accomplished at ', "{0:.2f}".format(total_distance_all_tr(), 2),
          'miles.\n')

    # display today's date and time
    now = datetime.datetime.now()
    cur_time = now.strftime("%H:%M:%S\n")
    cur_date = now.strftime("%Y-%m-%d\n")
    print(""" #Today is          :""", cur_date, """#Current time      :""", cur_time)


    # initial user selection : report for  1 packet or all packets
    user_input = int(input("""
    TYPE 1 : To  lookup  ALL  package packages 
    TYPE 2 : To  lookup  an individual package\n  """))
    if user_input > 2 or user_input < 1:
        print("Invalid entry")
        exit()

    # And we start here
    # ================================================================================================================
    while user_input != 'quit':

        # user input : Timeframe to retrieve report
        input_time_raw = input('Enter a time to retrieve report (HH:MM:SS):\n')
        print('-' * 100)
        (hrs0, mins0, secs0) = input_time_raw.split(':')
        input_time = datetime.timedelta(hours=int(hrs0), minutes=int(mins0), seconds=int(secs0))

        # Case if user selects Option #1
        # Get info for all packages at a particular time :> O(n)
        # ---------------------------------------- CASE 1: ALL PACKET REPORT  -----------------------------------------
        if user_input == 1:
            try:
                for count in range(1, 41):

                    try:
                        # Time variables (T1 : start time, T2: delivery time )
                        t1_temp = get_hash_table().search(str(count))[9]
                        t2_temp = get_hash_table().search(str(count))[10]

                        (hrs1, mins1, secs1) = t1_temp.split(':')
                        (hrs2, mins2, secs2) = t2_temp.split(':')

                        T1 = datetime.timedelta(hours=int(hrs1), minutes=int(mins1), seconds=int(secs1))
                        T2 = datetime.timedelta(hours=int(hrs2), minutes=int(mins2), seconds=int(secs2))

                    except ValueError:
                        pass

                    # Determine which packages have left the hub
                    if T1 >= input_time:
                        get_hash_table().search(str(count))[10] = 'At Hub'
                        get_hash_table().search(str(count))[9] = t1_temp
                        print_status(count)  # Print package's current info


                    # Determine which packages have left but have not been delivered
                    elif T1 <= input_time:
                        if input_time < T2:
                            get_hash_table().search(str(count))[10] = 'In transit'
                            get_hash_table().search(str(count))[9] = t1_temp
                            print_status(count)  # Print package's current info

                        # Determine which packages have already been delivered
                        else:
                            get_hash_table().search(str(count))[10] = 'Delivered at ' + t2_temp
                            get_hash_table().search(str(count))[9] = t1_temp
                            print_status(count)  # Print package's current info
                break


            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry!')
                exit()



        # Case if user selects Option #2
        # Get info for a single package at a particular time -> O(n)
        # ------------------------------ CASE 2 : SINGLE PACKET REPORT ------------------------------------------------
        elif user_input == 2:
            try:
                # Time variables (T1 : start time, T2: delivery time )
                count = input('Enter a valid package ID: \n')
                t1_temp = get_hash_table().search(str(count))[9]
                t2_temp = get_hash_table().search(str(count))[10]

                (hrs, mins, secs) = t1_temp.split(':')
                (hrs, mins, secs) = t2_temp.split(':')

                T1 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                T2 = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                print_pk_detail(count)  # prints specified packet's info

                # Determine which packages have left the hub
                if T1 >= input_time:

                    get_hash_table().search(str(count))[10] = 'At Hub'
                    get_hash_table().search(str(count))[9] = t1_temp

                    print_status(count)  # Print package's current delivery status

                # Determine which packages have left but have not been delivered
                elif T1 <= input_time:

                    if input_time < T2:
                        get_hash_table().search(str(count))[10] = 'In transit'
                        get_hash_table().search(str(count))[9] = t1_temp

                        print_status(count)  # Print package's current delivery status

                    # Determine which packages have already been delivered
                    else:
                        get_hash_table().search(str(count))[10] = 'Delivered at ' + t2_temp
                        get_hash_table().search(str(count))[9] = t1_temp

                        print_status(count)  # Print package's current delivery status

            except ValueError:
                print('Invalid entry')
                exit()


        # Case Error
        # Print Invalid Entry and quit the program
        else:
            print('Invalid entry!')
            exit()

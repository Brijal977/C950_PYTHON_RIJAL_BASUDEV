##Lab Activity 3.9.1
from simulation import simulation, random_scheduler
import sys


def load_data(filename):
    with open(filename, 'r') as f:
        num_processors = int(f.readline())
        processes = []
        for line in f:
            if len(line) > 0:
                processes.append(int(line))

    return num_processors, processes


# A scheduler that assigns the next process with the shortest processing time.
# The next-available processor is assigned.
def shortest_process_first_scheduler(processes, processors):
    # The smallest process is chosen next.
    min_process_index = 0
    for i in range(1, len(processes)):
        if processes[i] < processes[min_process_index]:
            min_process_index = i

    # The next processor is always the first one available.
    min_processor_index = 0
    for i in range(1, len(processors)):
        if processors[i] < processors[min_processor_index]:
            min_processor_index = i

    return min_process_index, min_processor_index


# A scheduler that assigns processes in the order they are
# presented, to the first available processor
def first_come_first_served_scheduler(processes, processors):
    # The next process is always the first in the list.
    next_process_index = 0

    # The next processor is always the first one available.
    min_processor_index = 0
    for i in range(1, len(processors)):
        if processors[i] < processors[min_processor_index]:
            min_processor_index = i

    return next_process_index, min_processor_index


if __name__ == "__main__":
    num_processors, processes = load_data(sys.argv[1])

    print("SIM 1: random scheduler")
    processes_copy = [x for x in processes]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy, random_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 2: first-come-first-served scheduler")
    processes_copy = [x for x in processes]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy,
                                                            first_come_first_served_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))

    print()
    print("SIM 3: shortest-process-first scheduler")
    processes_copy = [x for x in processes]
    final_time, total_wait_time, max_wait_time = simulation(num_processors, processes_copy,
                                                            shortest_process_first_scheduler)
    print('%20s: %d' % ('Final Time', final_time))
    print('%20s: %d' % ('Total Wait Time', total_wait_time))
    print('%20s: %d' % ('Max Wait time', max_wait_time))
    print('%20s: %0.2f' % ('Average Wait Time', total_wait_time / num_processors))
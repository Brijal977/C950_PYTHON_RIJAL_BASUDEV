import random

# Use a fixed random number seed to generate predictable results
random.seed(1)


def simulation(num_processors, processes, scheduler):
    time = 0
    total_wait_time = 0
    max_wait_time = 0

    # Processors list contains the next available time
    # tick for each processor. They all start as available
    # at time zero.
    processors = [0] * num_processors

    while len(processes) > 0:
        next_process_index, next_processor_index = scheduler(processes, processors)

        # Jump time to when next processor is available.
        time = max(time, processors[next_processor_index])

        print('Process %d starts at %d' % (next_process_index, time))

        # Update wait time statistics.
        wait_time = time
        total_wait_time += wait_time
        if wait_time > max_wait_time:
            max_wait_time = wait_time

        # update processor next available time
        processors[next_processor_index] = time + processes[next_process_index]

        # remove the selected process from the list.
        processes.pop(next_process_index)

    time = time + max(processors)
    return time, total_wait_time, max_wait_time


# A random scheduler. Both process and processor are
# chosen at random.
def random_scheduler(processes, processors):
    return random.randrange(0, len(processes)), random.randrange(0, len(processors))

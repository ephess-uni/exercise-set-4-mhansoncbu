""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Gets a list of shutdown events from a log file and calculates the time between the first and last shutdown events.
    """
    first_shutdown = (get_shutdown_events(logfile)[0])
    last_shutdown = (get_shutdown_events(logfile)[-1])
    first_shutdown_time = str.split(first_shutdown, sep=" ")[1]
    last_shutdown_time = str.split(last_shutdown, sep=" ")[1]
    first_shutdown_timestamp = logstamp_to_datetime(first_shutdown_time)
    last_shutdown_timestamp = logstamp_to_datetime(last_shutdown_time)
    time_between = last_shutdown_timestamp - first_shutdown_timestamp
    return time_between
    


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f'{time_between_shutdowns(FILENAME)=}')

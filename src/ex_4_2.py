""" ex_4_2.py """
from datetime import datetime


def logstamp_to_datetime(datestr):
    """
    Reads a date/time entry and returns a datetime.datetime object.
    """
    date_time_string = datestr
    format_string = '%Y-%m-%dT%H:%M:%S'
    date_time_object = datetime.strptime(date_time_string, format_string)
    return date_time_object


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    test_date = '2000-01-01T01:01:01'
    print(f'{logstamp_to_datetime(test_date)=}')

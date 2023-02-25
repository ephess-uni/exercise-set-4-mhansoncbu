""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Opens a logfile and returns a list of shutdown events.
    """
    logfile = open(logfile)
    all_entries = logfile.read()
    entry_lines = all_entries.splitlines()
    shutdown_entries = list()
    for entry in entry_lines:
        if 'Shutdown initiated' in entry:
            shutdown_entries.append(entry)
    return shutdown_entries
                    
# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")

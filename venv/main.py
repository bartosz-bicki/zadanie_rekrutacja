import sys
import logging

# __name__ statement provides the info about where the script was run
from os import path

my_logger = logging.getLogger(__name__)

# settig level to debug to get an information upon the console
my_logger.setLevel(logging.INFO)

# setting a simple formatter to specify given info
basic_formatter = logging.Formatter("%(name)s:%(asctime)s:%(message)s")

my_handler = logging.FileHandler("info.log")
my_handler.setFormatter(basic_formatter)
my_logger.addHandler(my_handler)

# with this line script will not mistake our logger with default
logging.basicConfig(level=logging.DEBUG)


def opening_file(args):
    # I check if the file exists
    if not path.exists("words.txt"):
        with open("words.txt", "w"):
            pass
        my_logger.info("File doesn't exists. Created new file.")

    # if file exists I open the file with decorator
    with open("words.txt", "r+") as file:
        my_logger.info("File Open.")
        # reading given arguments to a variable
        data = file.read()
        # as arguments comes as a list loop provides them to be separated
        for arg in args:
            if arg not in data:
                file.write(arg + "\n")
                my_logger.info(f"Adding argument '{arg}' to the file.")
        my_logger.info("File has been closed.")


# [1:] statement assures that script name won't be delivered as an argument
args = sys.argv[1:]
unique_args = []
# I check if the new arguments aren't double
[unique_args.append(arg) for arg in args if arg not in unique_args]
my_logger.info("Receiving arguments")
opening_file(unique_args)

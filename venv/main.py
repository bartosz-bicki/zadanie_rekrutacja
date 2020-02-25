import sys
import logging
#__name__ statement provides the info about where the script was run
my_logger = logging.getLogger(__name__)
#settig level to debug to get an information upon the console
my_logger.setLevel(logging.INFO)

basic_formatter = logging.Formatter('%(name)s:%(asctime)s:%(message)s')

my_handler = logging.FileHandler('info.log')
my_handler.setFormatter(basic_formatter)
my_logger.addHandler(my_handler)

#with this line script will not mistake our logger with default
logging.basicConfig(level=logging.DEBUG)

def opening_file(arg):

    #if it's first launch file will be created
    file = open("words.txt",'a+',encoding='utf-8')
    my_logger.info('File Open')

    #as arguments comes as a list loop provides them to be separated
    for i in arg:

        if i not in file:
            file.write(i + '\n')
            my_logger.info('Adding arguments to the file')
        else:
            pass

    file.close()
    my_logger.info('File has been closed')

#[1:] statement assures that sccipt name won't be delivered as an argument
arg = sys.argv[1:]
my_logger.info('Receiving arguments')
opening_file(arg)

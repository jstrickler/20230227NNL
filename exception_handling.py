import logging
logging.basicConfig(
    filename="mylog.txt",
    level=logging.INFO,
    format="%(levelname)s %(pathname)s:%(lineno)d %(asctime)s %(message)s",
    datefmt="%x-%X",
)



logging.info("Starting Program")
file_path = "DATA/walrus_gumbo.txt"

# catch:java::except:python
try:
    with open(file_path) as file_in:
        data = file_in.readlines()
except (FileNotFoundError, PermissionError) as err:
    logging.exception("Unable to open file: %s", err)
    # sys.exit(1)   # exit program
except Exception as err:
    logging.critical("Unexpected error! %s", err)
    # sys.exit(2)  # exit program

nums = [0, 800, 80, 0, 1000, 32, 255, 400, 5, 5000]
for i, num in enumerate(nums):
    try:
        result = 42 / num
    except ZeroDivisionError as err:
        # stopping Notepad, don't care if it fails
        logging.warning("Bad value %d in input data at item %d", num, i)
    else:
        print(result)
    finally:  # execute block no matter what
        pass  # cleanup here -- temp files, connections, etc.

logging.info("program finished")
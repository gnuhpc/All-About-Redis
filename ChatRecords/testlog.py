import logging
import logging.handlers
from subprocess import call
from time import sleep

formatter = logging.Formatter('%(asctime)s  %(message)s')

class MyTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    def doRollover(self):
        super(MyTimedRotatingFileHandler,self).doRollover()
        main_logger.info("Records log has been rotating...")
        call('git add .', shell = True)
        call('git commit -m "commiting..."', shell = True)
        call('git push origin master', shell = True)

def setup_logger(name, log_file):
    """Function setup as many loggers as you want"""

    handler = MyTimedRotatingFileHandler(log_file, when='M')
    handler.suffix = "%Y-%m-%d_%H-%M.log"

    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)

    return logger

main_logger = setup_logger("main_logger","main")

while True:
    sleep(10)
    main_logger.info("Logging...")

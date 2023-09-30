import logging
import logging.config
import mylib


def main1():
    logging.basicConfig(filename='.\log\logging_app.log', filemode='a', level=logging.DEBUG)
    # logging.basicConfig(filename='.\log\logging_app.log', filemode='a', level=logging.DEBUG,
    #                     format='%(levelname)s:%(message)s')
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')


def main2():
    logging.config.fileConfig('logging.conf')
    # create logger
    logger = logging.getLogger('simpleExample')

    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main1()
    main2()

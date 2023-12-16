from common import set_log
from logging import getLogger, config


if __name__ == '__main__':
    log_conf = set_log()
    config.dictConfig(log_conf)
    logger = getLogger(__name__)

    logger.info('test2')

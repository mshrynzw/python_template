from common import set_log
from logging import getLogger, config


log_conf = set_log()
config.dictConfig(log_conf)
logger = getLogger(__name__)


if __name__ == '__main__':
    logger.info('Testing xxx.')

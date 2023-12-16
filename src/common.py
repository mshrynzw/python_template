import json
from datetime import datetime


def set_log():
    with open('./conf/log.json', 'r') as f:
        log_conf = json.load(f)
    log_conf["handlers"]["fileHandler"]["filename"] = './log/{}.log'.format(datetime.utcnow().strftime("%Y%m%d%H%M%S"))

    return log_conf

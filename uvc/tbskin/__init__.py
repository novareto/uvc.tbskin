import logging
logger = logging.getLogger('uvc.tbskin')

def log(message, summary='', severity=logging.INFO):
    logger.log(severity, '%s %s', summary, message)

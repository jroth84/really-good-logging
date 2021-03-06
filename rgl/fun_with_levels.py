# vim: set expandtab ts=4 sw=4 filetype=python:

"""
baby steps...

Show how you can use the logging level to hide lower-priority messages.
"""

import argparse
import logging

def process_arguments():

    ap = argparse.ArgumentParser()

    ap.add_argument('log_level',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'])

    args = ap.parse_args()

    if args.log_level == 'DEBUG':
        level = logging.DEBUG

    elif args.log_level == 'INFO':
        level = logging.INFO

    elif args.log_level == 'WARNING':
        level = logging.WARNING

    elif args.log_level == 'ERROR':
        level = logging.ERROR

    elif args.log_level == 'CRITICAL':
        level = logging.CRITICAL

    return level

if __name__ == '__main__':

    level = process_arguments()
    logging.basicConfig(level=level)

    logging.debug('This is a boring debug message.')
    logging.info('Here is an info message...')
    logging.warn('This is a warning message!')
    logging.error('Even worse, This is an error message!')
    logging.critical('OH NO THIS IS CRITICAL')

    logging.info('All done!')

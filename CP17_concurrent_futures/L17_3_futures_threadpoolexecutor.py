__author__ = 'Hernan Y.Ke'
from concurrent import futures
import os
import time
import sys

import requests


MAX_WORKERS = 20


def download_one(cc):
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))

    return len(list(res))

def main(download_many):
    t0 = time.time()
    elapsed = time.time() - t0
    msg = '\ndownloaded in {:.2f}s'
    print(msg.format(elapsed))
if __name__ == '__main__':
    main(download_many)
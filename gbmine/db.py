#!/usr/bin/env python
import redis

#
# Connect 
#
def connect():

    try: 
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
    except ConnectionError:
        r = None

    return r

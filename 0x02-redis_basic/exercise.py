#!/usr/bin/env python3
"""This module implements a redis task"""
import redis
import uuid
from typing import TypeVar


T = TypeVar('T', str, bytes, int, float)


class Cache:
    def __init__(self):
        """
        Connects to the Redis server and initializes the cache object.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: T) -> str:
        """
        Stores the provided data in the cache and returns a unique key.

        Args:
            data: The data to be stored (can be any type).

        Returns:
            A string representing the unique key assigned to the data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

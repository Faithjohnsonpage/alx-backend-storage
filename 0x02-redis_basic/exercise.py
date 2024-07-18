#!/usr/bin/env python3
"""This module implements a redis task"""
import redis
import uuid
import functools
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """A decorator that counts the number of times a method is called."""
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the count for this method
        self._redis.incr(method.__qualname__)
        # Call the original method
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    def __init__(self):
        """
        Connects to the Redis server and initializes the cache object.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
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

    def get(self, key:
            str, fn: Optional[Callable] = None
            ) -> Optional[Union[str, int, float, bytes]]:
        """
        Retrieves the data stored at the specified key and applies the
        conversion function if provided.

        Args:
            key: The key of the data to retrieve.
            fn: An optional callable used to convert the data back to the
                desired format.

        Returns:
            The data stored at the key, converted if a conversion function is
            provided, or None if the key does not exist.
        """
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves the data stored at the specified key and converts
        it to a string.

        Args:
            key: The key of the data to retrieve.

        Returns:
            The data stored at the key, converted to a string, or
            None if the key does not exist.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves the data stored at the specified key and converts
        it to an integer.

        Args:
            key: The key of the data to retrieve.

        Returns:
            The data stored at the key, converted to an integer, or
            None if the key does not exist.
        """
        return self.get(key, int)

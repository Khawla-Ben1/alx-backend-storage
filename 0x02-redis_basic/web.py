#!/usr/bin/env python3
"""
Implementing an expiring web cache and tracker
"""

import redis
import requests
from typing import Callable
from functools import wraps

redis = redis.Redis()


def wrap_requests(fn: Callable) -> Callable:
    """Decorator that wraps d given func & provides caching functionality
    Returns:
        The wrapped function
    """

    @wraps(fn)
    def wrapper(url):
        """Wrapper function that adds caching logic to the decorated func
        Returns:
            The HTML content of the page
        """
        redis.incr(f"count:{url}")
        cached_response = redis.get(f"cached:{url}")
        if cached_response:
            return cached_response.decode('utf-8')
        result = fn(url)
        redis.setex(f"cached:{url}", 10, result)
        return result
    return wrapper


@wrap_requests
def get_page(url: str) -> str:
    """Fetches the HTML content of a web page.
    Returns:
        The HTML content of the web page
    """
    response = requests.get(url)
    return response.text

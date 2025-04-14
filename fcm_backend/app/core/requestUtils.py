import asyncio
import time
from typing import Optional, Dict, Any, Union
import aiohttp
import logging
from functools import wraps
from aiohttp import ClientError

logger = logging.getLogger(__name__)

class RequestUtils:
    def __init__(
        self,
        base_url: str = "",
        timeout: int = 30,
        max_retries: int = 3,
        retry_delay: int = 1,
        rate_limit: int = 100,  # requests per minute
        max_connections: int = 100,  # maximum number of concurrent connections
    ):
        """
        Initialize RequestUtils with configuration parameters.
        
        Args:
            base_url: Base URL for all requests
            timeout: Request timeout in seconds
            max_retries: Maximum number of retry attempts
            retry_delay: Delay between retries in seconds
            rate_limit: Maximum number of requests per minute
            max_connections: Maximum number of concurrent connections
        """
        self.base_url = base_url
        self.timeout = timeout
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.rate_limit = rate_limit
        self.max_connections = max_connections
        self.last_request_time = 0
        self.request_count = 0
        self._session = None
        self._semaphore = asyncio.Semaphore(max_connections)

    @property
    def session(self) -> aiohttp.ClientSession:
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession(
                timeout=aiohttp.ClientTimeout(total=self.timeout)
            )
        return self._session

    async def close(self):
        """Close the session."""
        if self._session and not self._session.closed:
            await self._session.close()
            self._session = None

    def _rate_limit_decorator(self, func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            current_time = time.time()
            if current_time - self.last_request_time < 60:
                if self.request_count >= self.rate_limit:
                    sleep_time = 60 - (current_time - self.last_request_time)
                    logger.warning(f"Rate limit reached. Sleeping for {sleep_time:.2f} seconds")
                    await asyncio.sleep(sleep_time)
                    self.request_count = 0
                    self.last_request_time = time.time()
            else:
                self.request_count = 0
                self.last_request_time = current_time
            
            self.request_count += 1
            return await func(*args, **kwargs)
        return wrapper

    async def _make_request(
        self,
        method: str,
        url: str,
        **kwargs
    ) -> aiohttp.ClientResponse:
        """
        Make an HTTP request with retry logic and error handling.
        
        Args:
            method: HTTP method (GET, POST, etc.)
            url: Request URL
            **kwargs: Additional arguments for aiohttp.ClientSession.request
            
        Returns:
            aiohttp.ClientResponse: Response object
            
        Raises:
            ClientError: If all retry attempts fail
        """
        full_url = f"{self.base_url}{url}" if self.base_url else url
        
        async with self._semaphore:
            for attempt in range(self.max_retries):
                try:
                    async with self.session.request(method=method, url=full_url, **kwargs) as response:
                        response.raise_for_status()
                        return response
                except ClientError as e:
                    if attempt == self.max_retries - 1:
                        logger.error(f"Request failed after {self.max_retries} attempts: {str(e)}")
                        raise
                    logger.warning(f"Request failed (attempt {attempt + 1}/{self.max_retries}): {str(e)}")
                    await asyncio.sleep(self.retry_delay * (attempt + 1))

    @_rate_limit_decorator
    async def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> aiohttp.ClientResponse:
        """Make a GET request."""
        return await self._make_request("GET", url, params=params, headers=headers, **kwargs)

    @_rate_limit_decorator
    async def post(
        self,
        url: str,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> aiohttp.ClientResponse:
        """Make a POST request."""
        return await self._make_request("POST", url, data=data, json=json, headers=headers, **kwargs)

    @_rate_limit_decorator
    async def put(
        self,
        url: str,
        data: Optional[Union[Dict[str, Any], str]] = None,
        json: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> aiohttp.ClientResponse:
        """Make a PUT request."""
        return await self._make_request("PUT", url, data=data, json=json, headers=headers, **kwargs)

    @_rate_limit_decorator
    async def delete(
        self,
        url: str,
        headers: Optional[Dict[str, str]] = None,
        **kwargs
    ) -> aiohttp.ClientResponse:
        """Make a DELETE request."""
        return await self._make_request("DELETE", url, headers=headers, **kwargs)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

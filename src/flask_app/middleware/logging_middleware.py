import time
import logging
from flask import request

logger = logging.getLogger('vulnarena.access')

class LoggingMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        start_time = time.time()
        
        # Call the original application
        response = self.app(environ, start_response)
        
        duration = time.time() - start_time
        method = environ.get('REQUEST_METHOD')
        path = environ.get('PATH_INFO')
        ip = environ.get('REMOTE_ADDR')
        
        logger.info(f"[{ip}] {method} {path} - {duration:.4f}s")
        
        return response

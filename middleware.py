import time

from django.utils import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    
    def process_request(self, request):
        request.start_time = time.time
    
    def process_response(self, request, response):
        
        total_time = time.time() - request.start_time
        
        log = f"URL : {request.url} - HTTP_METHOD : {request.method} - TIME : {total_time}"
        
        with open('request_logs.txt', 'w') as file:
            file.write(log)
            
        
        return response
    
    
    

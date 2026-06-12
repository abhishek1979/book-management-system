from fastapi import FastAPI, Request
from dotenv import load_dotenv
import os
import uvicorn
import time

from app.services.book_admin_service import BookAdminService
from app.api.book_admin_api import BookAdminAPI
from app.core.logger import logger

class MainApplication:

    def __init__(self):     

        # Load variables from .env into the environment
        load_dotenv()

        # Access the variables
        app_name = os.getenv('APP_NAME')
        app_version = os.getenv('APP_VERSION')    

        self.app = FastAPI(title=app_name, version=app_version)

        # Initialize Book Admin API
        book_admin_api = BookAdminAPI()       

        # Include Router
        self.app.include_router(book_admin_api.router)        

    def get_app(self):
        return self.app
    
main_app = MainApplication()
app = main_app.get_app()   

# --- Logging Middleware ---
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Logs the details of incoming requests and response times."""
    
    start_time = time.time()
    
    # Log the incoming request method and path
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    
    # Process the request
    response = await call_next(request)
    
    # Calculate processing time
    process_time = (time.time() - start_time) * 1000 # Convert to milliseconds
    
    # Log the response status code and time taken
    logger.info(
        f"Completed request: {request.method} {request.url.path} "
        f"- Status: {response.status_code} "
        f"- Duration: {process_time:.2f}ms"
    )
    
    return response



if __name__ == "__main__":   
   uvicorn.run("main:app", host="localhost", port=9999, reload=True)

# To run from command line or Terminal use this command : uvicorn main:app --reload
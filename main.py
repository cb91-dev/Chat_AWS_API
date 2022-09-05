import uvicorn
from pathlib import Path
from fastapi import FastAPI
from routes import login
from routes import register
from routes import profile
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum


app = FastAPI()
# To enable this to connect via API Gateway we need to wrap this app with Mangum
handler = Mangum(app, lifespan='off')

origins = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://localhost:8080",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Run application 
def main():
    config(dev_mode=False)
    # noinspection PyTypeChecker
    uvicorn.run(app, host='127.0.0.1', port=8000, debug=True)

# Configure app
def config(dev_mode:bool):
    config_routes()

    
# Loading routes
def config_routes():
    app.include_router(login.router)
    app.include_router(register.router)
    app.include_router(profile.router)


if __name__ == '__main__':
    main()
else:
    # Routes will always be loaded
    config(dev_mode=False)
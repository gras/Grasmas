from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# this line imports users.py from the routers folder
from routers import gifts

import os
from fastapi_sqlalchemy import DBSessionMiddleware  # middleware helper

# Also it will be will be import load_dotenv to connect to our db
from dotenv import load_dotenv

# this line is to connect to our base dir and connect to our .env file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = FastAPI()

# this is to access the db so any route can access the database session
app.add_middleware(DBSessionMiddleware,
                   db_url=os.environ["SQLALCHEMY_DATABASE_URI"])
# setup templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/grid")
async def grid(request: Request):
    return templates.TemplateResponse("grid.html", {"request": request})


@app.get("/test")
async def database_list(request: Request):

    return templates.TemplateResponse("db_list.html", {"request": request})

# this imports the route in the user into the main file
app.include_router(gifts.router)

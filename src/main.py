from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv('.env')
from routes import home_page
app=FastAPI()

app.include_router(home_page.router)

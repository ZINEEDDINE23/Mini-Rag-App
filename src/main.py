from fastapi import FastAPI
from routes import home_page
app=FastAPI()

app.include_router(home_page.router)

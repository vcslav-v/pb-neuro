from fastapi import FastAPI
from pb_neuro.api.routes import routes

app = FastAPI(debug=True)

app.include_router(routes)

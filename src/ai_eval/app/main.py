from fastapi import FastAPI
from ai_eval.app.experiment_webhook import router

app = FastAPI()
app.include_router(router)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.CICD import router as cicd_router
from app.routes.gestionProjet import router as gestion_projet_router
from app.routes.impact import router as impact_router
from app.routes.informationgeneral import router as information_general_router
from app.routes.performance import router as performance_router
from app.routes.TestFonctionnel import router as tests_fonctionnels_router

app = FastAPI()

app.include_router(cicd_router)
app.include_router(gestion_projet_router)
app.include_router(impact_router)
app.include_router(information_general_router)
app.include_router(performance_router)
app.include_router(tests_fonctionnels_router)
origins = [
    "http://localhost:4200",
    "http://127.0.0.1:4200",  # Angular
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def read_root():
    return {"message": "API working"}
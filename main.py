from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.routes import produtos, usuarios, analises



app = FastAPI(title="Afiliados Tech")


templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")


app.include_router(produtos.router)
#app.include_router(usuarios.router)
#app.include_router(analises.router)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "usuario": "Welligton"})



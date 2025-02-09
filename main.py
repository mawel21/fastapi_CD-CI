from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


web = FastAPI()
templates = Jinja2Templates(directory='templates') #definir la carpeta donde estarán los templates
web.mount("/static", StaticFiles(directory="static"), name="static")

@web.get("/")
def index(request: Request):
     return templates.TemplateResponse(
        request=request, name="index.html" ,                  
    )

@web.get("/position.html")
def Homer(request: Request):
     return templates.TemplateResponse(
        request=request, name="position.html" ,                  
    )

@web.get("/proyectos.html")
def proyectos(request: Request):
     return templates.TemplateResponse(
        request=request, name="proyectos.html" ,                  
    )
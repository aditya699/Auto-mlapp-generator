# app/routes.py
from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.models import BMIInput

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@router.post("/calculate", response_class=HTMLResponse)
async def calculate_bmi(request: Request, weight: float = Form(...), height: float = Form(...)):
    try:
        # Validate input using BMIInput model
        bmi_data = BMIInput(weight=weight, height=height)
        bmi = bmi_data.weight / (bmi_data.height ** 2)
        result = f"Your BMI is {bmi:.2f}."
        return templates.TemplateResponse("index.html", {"request": request, "result": result})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e)})

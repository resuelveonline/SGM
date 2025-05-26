# -*- coding: utf-8 -*-
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Sistema de Gestion Municipal con IA",
    description="API para automatizar tramites municipales - Puebla",
    version="0.1.0"
)

@app.get("/")
async def inicio():
    return {
        "mensaje": "Sistema Municipal con IA funcionando correctamente",
        "version": "0.1.0",
        "timestamp": datetime.now().isoformat(),
        "status": "desarrollo_local"
    }

@app.get("/salud")
async def verificar_salud():
    return {
        "status": "ok",
        "servicio": "activo",
        "ambiente": "desarrollo"
    }

@app.get("/municipio")
async def info_municipio():
    return {
        "municipio": "Puebla",
        "estado": "Puebla", 
        "servicios_disponibles": [
            "Informacion general",
            "Consulta de tramites",
            "Chatbot inteligente",
            "Portal ciudadano"
        ]
    }
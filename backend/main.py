# -*- coding: utf-8 -*-
from fastapi import FastAPI, HTTPException
from datetime import datetime
from typing import List, Dict, Optional

from chatbot import ChatbotMunicipal
from pydantic import BaseModel

# Inicializar chatbot
chatbot = ChatbotMunicipal()

# Modelo para el endpoint de chat
class MensajeChat(BaseModel):
    mensaje: str
    usuario_id: Optional[str] = None



app = FastAPI(
    title="Sistema de Gestion Municipal con IA",
    description="API para automatizar tramites municipales - Puebla",
    version="0.2.0"
)

# Base de datos simulada de trámites
tramites_db = {
    "licencia-funcionamiento": {
        "id": "licencia-funcionamiento",
        "nombre": "Licencia de Funcionamiento",
        "descripcion": "Permiso para operar un negocio comercial",
        "dependencia": "Direccion de Licencias",
        "tiempo_estimado": "15 dias habiles",
        "costo": 2500,
        "requisitos": [
            "Identificacion oficial",
            "Comprobante de domicilio",
            "Uso de suelo compatible",
            "Pago de derechos"
        ]
    },
    "uso-suelo": {
        "id": "uso-suelo",
        "nombre": "Certificado de Uso de Suelo",
        "descripcion": "Documento que especifica el uso permitido de un predio",
        "dependencia": "Direccion de Desarrollo Urbano",
        "tiempo_estimado": "10 dias habiles",
        "costo": 800,
        "requisitos": [
            "Escrituras o contrato de arrendamiento",
            "Identificacion oficial",
            "Croquis de localizacion"
        ]
    },
    "permiso-construccion": {
        "id": "permiso-construccion",
        "nombre": "Permiso de Construccion",
        "descripcion": "Autorizacion para realizar obras de construccion",
        "dependencia": "Direccion de Obras Publicas",
        "tiempo_estimado": "20 dias habiles", 
        "costo": 5000,
        "requisitos": [
            "Proyecto arquitectonico",
            "Licencia de uso de suelo",
            "Responsiva del Director Responsable de Obra",
            "Pago de derechos"
        ]
    }
}

# Base de datos simulada de expedientes
expedientes_db = {
    "EXP-2025-001": {
        "numero": "EXP-2025-001",
        "tramite": "licencia-funcionamiento",
        "solicitante": "Maria Rodriguez",
        "fecha_solicitud": "2025-05-20",
        "status": "en_revision",
        "observaciones": "Documentos completos, en proceso de verificacion"
    },
    "EXP-2025-002": {
        "numero": "EXP-2025-002", 
        "tramite": "uso-suelo",
        "solicitante": "Carlos Martinez",
        "fecha_solicitud": "2025-05-18",
        "status": "aprobado",
        "observaciones": "Tramite finalizado exitosamente"
    }
}

@app.get("/")
async def inicio():
    return {
        "mensaje": "Sistema Municipal con IA funcionando correctamente",
        "version": "0.2.0",
        "timestamp": datetime.now().isoformat(),
        "status": "desarrollo_local",
        "endpoints_disponibles": [
            "/tramites - Lista de tramites",
            "/tramites/{id} - Detalle de tramite",
            "/consulta/{expediente} - Estado de expediente", 
            "/horarios - Horarios de atencion",
            "/dependencias - Oficinas municipales"
        ]
    }

@app.get("/salud")
async def verificar_salud():
    return {
        "status": "ok",
        "servicio": "activo",
        "ambiente": "desarrollo",
        "base_datos": "simulada"
    }

@app.get("/tramites")
async def listar_tramites():
    """Obtener lista de todos los trámites municipales disponibles"""
    return {
        "total": len(tramites_db),
        "tramites": list(tramites_db.values())
    }

@app.get("/tramites/{tramite_id}")
async def detalle_tramite(tramite_id: str):
    """Obtener detalles específicos de un trámite"""
    if tramite_id not in tramites_db:
        raise HTTPException(status_code=404, detail="Tramite no encontrado")
    
    return tramites_db[tramite_id]

@app.get("/consulta/{numero_expediente}")
async def consultar_expediente(numero_expediente: str):
    """Consultar el estado de un expediente"""
    if numero_expediente not in expedientes_db:
        raise HTTPException(status_code=404, detail="Expediente no encontrado")
    
    expediente = expedientes_db[numero_expediente]
    tramite_info = tramites_db.get(expediente["tramite"], {})
    
    return {
        "expediente": expediente,
        "tramite_info": {
            "nombre": tramite_info.get("nombre"),
            "dependencia": tramite_info.get("dependencia"),
            "tiempo_estimado": tramite_info.get("tiempo_estimado")
        }
    }

@app.get("/horarios")
async def horarios_atencion():
    """Obtener horarios de atención de oficinas municipales"""
    return {
        "horarios_generales": {
            "lunes_viernes": "08:00 - 15:00",
            "sabados": "09:00 - 13:00",
            "domingos": "Cerrado"
        },
        "oficinas_especiales": {
            "registro_civil": {
                "lunes_viernes": "08:00 - 14:00",
                "sabados": "Cerrado"
            },
            "licencias": {
                "lunes_viernes": "08:30 - 14:30",
                "sabados": "09:00 - 12:00"
            }
        },
        "contacto": {
            "telefono": "222-XXX-XXXX",
            "email": "atencion@puebla.gob.mx"
        }
    }

@app.get("/dependencias")
async def listar_dependencias():
    """Obtener lista de dependencias municipales"""
    return {
        "dependencias": [
            {
                "nombre": "Direccion de Licencias",
                "ubicacion": "Palacio Municipal, Planta Baja",
                "telefono": "222-XXX-1001",
                "servicios": ["Licencias de funcionamiento", "Avisos de apertura"]
            },
            {
                "nombre": "Direccion de Desarrollo Urbano", 
                "ubicacion": "Edificio Administrativo, Piso 2",
                "telefono": "222-XXX-1002",
                "servicios": ["Uso de suelo", "Zonificacion"]
            },
            {
                "nombre": "Direccion de Obras Publicas",
                "ubicacion": "Edificio Administrativo, Piso 3", 
                "telefono": "222-XXX-1003",
                "servicios": ["Permisos de construccion", "Supervision de obras"]
            },
            {
                "nombre": "Registro Civil",
                "ubicacion": "Palacio Municipal, Planta Alta",
                "telefono": "222-XXX-1004", 
                "servicios": ["Actas de nacimiento", "Matrimonios", "Defunciones"]
            }
        ]
    }

@app.post("/chat")
async def chat_ciudadano(mensaje_data: MensajeChat):
    """Chatbot para atención ciudadana automatizada"""
    if not mensaje_data.mensaje.strip():
        raise HTTPException(status_code=400, detail="Mensaje no puede estar vacío")
    
    respuesta = chatbot.generar_respuesta(mensaje_data.mensaje)
    
    return {
        "timestamp": datetime.now().isoformat(),
        "usuario_id": mensaje_data.usuario_id,
        "chatbot_respuesta": respuesta["respuesta"],
        "intencion": respuesta["intencion_detectada"],
        "sugerencias": respuesta["sugerencias"],
        "mensaje_ciudadano": mensaje_data.mensaje
    }
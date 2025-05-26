# -*- coding: utf-8 -*-
import re
from unidecode import unidecode
from typing import Dict, List

class ChatbotMunicipal:
    def __init__(self):
        # Palabras clave para identificar intenciones
        self.intenciones = {
            "saludo": ["hola", "buenos dias", "buenas tardes", "que tal", "saludos"],
            "licencia": ["licencia", "permiso", "negocio", "abrir", "comercio", "tienda"],
            "uso_suelo": ["uso de suelo", "suelo", "terreno", "predio", "construccion"],
            "expediente": ["expediente", "numero", "consultar", "estado", "tramite", "seguimiento"],
            "horarios": ["horario", "atencion", "abierto", "cerrado", "hora", "cuando"],
            "ubicacion": ["donde", "direccion", "oficina", "ubicacion", "palacio"],
            "costo": ["costo", "precio", "cuanto", "pagar", "dinero", "pesos"],
            "requisitos": ["requisito", "documento", "necesito", "papeles", "que debo"],
            "ayuda": ["ayuda", "help", "no entiendo", "como", "explicame"]
        }
        
        # Respuestas predefinidas
        self.respuestas = {
            "saludo": [
                "¡Hola! Soy el asistente virtual del Municipio de Puebla. ¿En qué puedo ayudarte?",
                "¡Buenos días! ¿Qué trámite municipal necesitas realizar?",
                "¡Saludos! Estoy aquí para ayudarte con información municipal."
            ],
            "licencia": [
                "Para obtener una licencia de funcionamiento necesitas:\n- Identificación oficial\n- Comprobante de domicilio\n- Uso de suelo compatible\n- Pago de derechos ($2,500)\n\n¿Te gustaría conocer los pasos detallados?"
            ],
            "uso_suelo": [
                "El certificado de uso de suelo cuesta $800 y tarda 10 días hábiles.\nRequisitos:\n- Escrituras o contrato\n- Identificación oficial\n- Croquis de localización\n\n¿Necesitas más información?"
            ],
            "expediente": [
                "Para consultar tu expediente necesito el número. Ejemplo: EXP-2025-001\n¿Tienes tu número de expediente?"
            ],
            "horarios": [
                "Horarios de atención:\n📅 Lunes a Viernes: 8:00 - 15:00\n📅 Sábados: 9:00 - 13:00\n📅 Domingos: Cerrado\n\n¿Qué oficina específica necesitas?"
            ],
            "ubicacion": [
                "Principales ubicaciones:\n🏛️ Palacio Municipal: Licencias, Registro Civil\n🏢 Edificio Administrativo: Desarrollo Urbano, Obras Públicas\n\n¿Qué dependencia buscas?"
            ],
            "costo": [
                "Costos principales:\n💰 Licencia funcionamiento: $2,500\n💰 Uso de suelo: $800\n💰 Permiso construcción: $5,000\n\n¿Qué trámite específico te interesa?"
            ],
            "requisitos": [
                "Los requisitos varían según el trámite:\n📋 Licencia de funcionamiento\n📋 Uso de suelo\n📋 Permiso de construcción\n\n¿Cuál necesitas?"
            ],
            "ayuda": [
                "Puedo ayudarte con:\n✅ Información de trámites\n✅ Consulta de expedientes\n✅ Horarios y ubicaciones\n✅ Costos y requisitos\n\n¿Qué necesitas saber?"
            ],
            "default": [
                "No estoy seguro de entender tu pregunta. Puedo ayudarte con:\n- Trámites municipales\n- Consulta de expedientes\n- Horarios y ubicaciones\n\n¿Podrías ser más específico?"
            ]
        }

    def normalizar_texto(self, texto: str) -> str:
        """Normalizar texto para mejor procesamiento"""
        # Convertir a minúsculas y quitar acentos
        texto = unidecode(texto.lower())
        # Quitar caracteres especiales pero mantener espacios
        texto = re.sub(r'[^\w\s]', '', texto)
        return texto.strip()

    def detectar_intencion(self, mensaje: str) -> str:
        """Detectar la intención del mensaje basado en palabras clave"""
        mensaje_normalizado = self.normalizar_texto(mensaje)
        
        # Buscar coincidencias con palabras clave
        puntuaciones = {}
        for intencion, palabras_clave in self.intenciones.items():
            puntuacion = 0
            for palabra in palabras_clave:
                if palabra in mensaje_normalizado:
                    puntuacion += 1
            if puntuacion > 0:
                puntuaciones[intencion] = puntuacion
        
        # Devolver la intención con mayor puntuación
        if puntuaciones:
            return max(puntuaciones, key=puntuaciones.get)
        else:
            return "default"

    def generar_respuesta(self, mensaje: str) -> Dict:
        """Generar respuesta del chatbot"""
        intencion = self.detectar_intencion(mensaje)
        respuesta = self.respuestas.get(intencion, self.respuestas["default"])[0]
        
        return {
            "respuesta": respuesta,
            "intencion_detectada": intencion,
            "mensaje_original": mensaje,
            "sugerencias": self.obtener_sugerencias(intencion)
        }

    def obtener_sugerencias(self, intencion: str) -> List[str]:
        """Obtener sugerencias de seguimiento"""
        sugerencias_map = {
            "saludo": ["¿Qué trámite necesitas?", "Consultar expediente", "Ver horarios"],
            "licencia": ["Ver requisitos completos", "Consultar costos", "Ubicación de oficinas"],
            "uso_suelo": ["Ver ubicación", "Consultar horarios", "Otros trámites"],
            "expediente": ["Escribir número de expediente", "Otros trámites", "Contactar oficina"],
            "horarios": ["Ver ubicaciones", "Consultar trámites", "Contacto telefónico"],
            "default": ["Ver trámites disponibles", "Consultar expediente", "Horarios de atención"]
        }
        return sugerencias_map.get(intencion, sugerencias_map["default"])
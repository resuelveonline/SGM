# Bitácora Técnica de Desarrollo
## Sistema de Gestión Municipal con IA - Municipio de Puebla

**Proyecto:** Sistema de Gestión Municipal con IA  
**Desarrollador:** Francisco Carvajal  
**Repositorio:** https://github.com/resuelveonline/SGM  
**Período:** Mayo 25, 2025  
**Stack Tecnológico:** Python + FastAPI + React (planificado)

---

## 1. Verificación de Requisitos del Sistema

### 1.1 Verificación de Instalaciones Existentes
**Fecha:** 25 de mayo de 2025, 22:08 hrs  
**Objetivo:** Confirmar que el entorno de desarrollo tiene las herramientas necesarias

#### Comandos Ejecutados:
```bash
python3 --version
# Salida: Python 3.9.6

git --version  
# Salida: git version 2.39.5 (Apple Git-154)

node --version
# Salida: v22.16.0
```

#### Resultados:
- ✅ **Python 3.9.6** - Versión compatible para FastAPI y librerías de IA
- ✅ **Git 2.39.5** - Sistema de control de versiones actualizado  
- ✅ **Node.js v22.16.0** - Última versión LTS para frontend futuro
- ✅ **Sistema Operativo:** macOS (identificado por Apple Git)

#### Decisiones Técnicas:
- Python 3.9.6 es suficiente para FastAPI y OpenAI API
- Git está configurado correctamente para GitHub
- Node.js preparado para desarrollo de frontend con React

---

## 2. Configuración del Entorno de Desarrollo

### 2.1 Problema con Fish Shell
**Fecha:** 25 de mayo de 2025, 22:15 hrs  
**Problema Encontrado:** Error al activar entorno virtual de Python

#### Error Detectado:
```bash
source venv/bin/activate
# Error: venv/bin/activate (line 40): Unsupported use of '='. 
# In fish, please use 'set VIRTUAL_ENV "/Users/franciscocarvajal/proyectos/SGM/venv"'.
```

#### Causa:
Fish shell tiene sintaxis diferente a Bash para variables de entorno

#### Solución Implementada:
```bash
# Cambio temporal a bash
bash
source venv/bin/activate
```

### 2.2 Decisión de Cambio de Shell
**Objetivo:** Eliminar problemas de compatibilidad con herramientas de desarrollo

#### Proceso de Cambio a Bash:
```bash
# Verificar shells disponibles
cat /etc/shells

# Cambiar shell por defecto
chsh -s /bin/bash

# Verificar cambio
echo $SHELL
# Resultado esperado: /bin/bash
```

#### Configuración de Bash:
```bash
# Editar perfil de bash
nano ~/.bash_profile

# Contenido agregado:
export PS1="\u@\h \W $ "
export PATH="/usr/local/bin:$PATH"

# Aliases útiles para desarrollo
alias ll='ls -la'
alias activate='source venv/bin/activate'
alias runserver='uvicorn main:app --reload'
alias gs='git status'
alias gc='git commit -m'
alias gp='git push origin main'

# Aplicar cambios
source ~/.bash_profile
```

---

## 3. Configuración del Repositorio Git

### 3.1 Problema de Repositorio No Inicializado
**Fecha:** 25 de mayo de 2025, 22:45 hrs  
**Error Detectado:**
```bash
git push origin main
# Error: fatal: not a git repository (or any of the parent directories): .git
```

#### Causa:
La carpeta local no estaba conectada con el repositorio de GitHub

#### Solución Implementada:
```bash
# Navegar al directorio padre
cd ~/proyectos

# Respaldar trabajo existente
mv SGM SGM-backup

# Clonar repositorio desde GitHub
git clone https://github.com/resuelveonline/SGM.git
cd SGM

# Recuperar trabajo previo
cp -r ../SGM-backup/backend ./

# Limpiar directorio temporal
rm -rf ../SGM-backup
```

#### Verificación:
```bash
git remote -v
# Salida: origin https://github.com/resuelveonline/SGM.git (fetch)
# Salida: origin https://github.com/resuelveonline/SGM.git (push)
```

### 3.2 Configuración de Autenticación GitHub
**Problema:** GitHub no acepta contraseñas desde agosto 2021

#### Error Encontrado:
```bash
git push origin main
Username: paquitocarvajal@gmail.com
Password: [contraseña]
# Error: remote: Support for password authentication was removed on August 13, 2021
```

#### Solución: Personal Access Token
1. **Crear token en GitHub:**
   - GitHub.com → Settings → Developer settings → Personal access tokens
   - Generate new token (classic)
   - Scope: `repo` (acceso completo a repositorios)
   - Expiration: 90 days

2. **Usar token como contraseña:**
```bash
git push origin main
Username: paquitocarvajal@gmail.com
Password: [TOKEN_GENERADO]
```

3. **Guardar credenciales:**
```bash
git config --global credential.helper store
```

---

## 4. Configuración del Entorno Python

### 4.1 Creación del Entorno Virtual
**Ubicación:** `~/proyectos/SGM/backend/`

#### Comandos Ejecutados:
```bash
cd SGM/backend
python3 -m venv venv
```

#### Estructura Creada:
```
backend/
├── venv/
│   ├── bin/
│   ├── include/
│   ├── lib/
│   └── pyvenv.cfg
```

### 4.2 Activación del Entorno Virtual
```bash
# En bash
source venv/bin/activate
# Resultado: (venv) bash-3.2$ 
```

#### Verificación:
```bash
which python
# Salida: /Users/franciscocarvajal/proyectos/SGM/backend/venv/bin/python

which pip  
# Salida: /Users/franciscocarvajal/proyectos/SGM/backend/venv/bin/pip
```

### 4.3 Problema de Entorno Roto por Movimiento de Carpetas
**Error Encontrado:**
```bash
uvicorn main:app --reload
# Error: bash: uvicorn: command not found

pip --version
# Error: bash: pip: command not found
```

#### Causa:
Los entornos virtuales de Python no son portables. Al mover la carpeta `venv`, los paths internos se rompieron.

#### Solución: Recrear Entorno Virtual
```bash
# Eliminar entorno roto
rm -rf venv

# Crear nuevo entorno
python3 -m venv venv

# Activar entorno nuevo
source venv/bin/activate

# Verificar funcionamiento
which python
which pip
```

---

## 5. Instalación de Dependencias

### 5.1 Instalación de FastAPI y Uvicorn
```bash
# Con entorno virtual activado
pip install fastapi uvicorn python-dotenv
```

#### Verificación de Instalación:
```bash
pip list
# Salida esperada:
# fastapi        0.104.1
# uvicorn        0.24.0
# python-dotenv  1.0.0
# [otras dependencias]
```

#### Generación de Requirements:
```bash
pip freeze > requirements.txt
```

### 5.2 Instalación de Dependencias para Chatbot
**Fecha:** Posterior - Para funcionalidad de IA

```bash
pip install unidecode regex
pip freeze > requirements.txt
```

---

## 6. Desarrollo de la API Base

### 6.1 Creación del Archivo Principal
**Archivo:** `backend/main.py`

#### Contenido Inicial:
```python
# -*- coding: utf-8 -*-
from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="Sistema de Gestión Municipal con IA",
    description="API para automatizar trámites municipales - Puebla",
    version="0.1.0"
)

@app.get("/")
async def inicio():
    return {
        "mensaje": "Sistema Municipal funcionando",
        "version": "0.1.0",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/salud")
async def verificar_salud():
    return {"status": "ok"}
```

### 6.2 Primera Ejecución
```bash
# Con venv activado
uvicorn main:app --reload
```

#### Salida Esperada:
```
INFO:     Will watch for changes in these directories: ['/Users/franciscocarvajal/proyectos/SGM']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2335] using StatReload
INFO:     Started server process [2336]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

#### Verificación en Navegador:
- **URL Principal:** http://127.0.0.1:8000
- **Documentación:** http://127.0.0.1:8000/docs
- **Endpoint Salud:** http://127.0.0.1:8000/salud

### 6.3 Problema de Codificación UTF-8
**Error Detectado:** Caracteres especiales mostrándose como `ðŸ›ï¸` y `InformaciÃ³n`

#### Solución Aplicada:
```python
# Agregar al inicio del archivo
# -*- coding: utf-8 -*-

# Evitar emojis y caracteres especiales en respuestas JSON
"mensaje": "Sistema Municipal con IA funcionando correctamente"
# En lugar de:
"mensaje": "🏛️ Sistema Municipal con IA funcionando"
```

---

## 7. Expansión de Endpoints Municipales

### 7.1 Diseño de Base de Datos Simulada
**Objetivo:** Crear sistema completo de trámites municipales

#### Estructura Implementada:
```python
# Base de datos de trámites
tramites_db = {
    "licencia-funcionamiento": {
        "id": "licencia-funcionamiento",
        "nombre": "Licencia de Funcionamiento", 
        "descripcion": "Permiso para operar un negocio comercial",
        "dependencia": "Direccion de Licencias",
        "tiempo_estimado": "15 dias habiles",
        "costo": 2500,
        "requisitos": [...]
    },
    # ... más trámites
}

# Base de datos de expedientes
expedientes_db = {
    "EXP-2025-001": {
        "numero": "EXP-2025-001",
        "tramite": "licencia-funcionamiento",
        "solicitante": "Maria Rodriguez",
        "fecha_solicitud": "2025-05-20",
        "status": "en_revision",
        "observaciones": "..."
    }
}
```

### 7.2 Endpoints Implementados

#### Lista Completa:
1. **GET /** - Información general del sistema
2. **GET /salud** - Health check de la API  
3. **GET /tramites** - Lista de trámites municipales
4. **GET /tramites/{tramite_id}** - Detalle específico de trámite
5. **GET /consulta/{numero_expediente}** - Estado de expediente
6. **GET /horarios** - Horarios de atención municipales
7. **GET /dependencias** - Directorio de oficinas

#### Verificación:
```bash
# Probar todos los endpoints
curl http://127.0.0.1:8000/tramites
curl http://127.0.0.1:8000/tramites/licencia-funcionamiento  
curl http://127.0.0.1:8000/consulta/EXP-2025-001
curl http://127.0.0.1:8000/horarios
curl http://127.0.0.1:8000/dependencias
```

---

## 8. Implementación del Chatbot con IA

### 8.1 Diseño del Sistema de Chatbot
**Archivo:** `backend/chatbot.py`

#### Funcionalidades Implementadas:
- **Normalización de texto:** Eliminar acentos y caracteres especiales
- **Detección de intenciones:** Sistema de puntuación por palabras clave
- **Respuestas contextuales:** Información específica de Puebla
- **Sugerencias automáticas:** Guía al ciudadano en próximos pasos

#### Intenciones Detectadas:
1. `saludo` - Saludos iniciales
2. `licencia` - Consultas sobre licencias de funcionamiento
3. `uso_suelo` - Certificados de uso de suelo
4. `expediente` - Consulta de estado de trámites
5. `horarios` - Horarios de atención
6. `ubicacion` - Direcciones de oficinas
7. `costo` - Precios de trámites
8. `requisitos` - Documentos necesarios
9. `ayuda` - Solicitudes de asistencia general

### 8.2 Integración con FastAPI
```python
# En main.py
from chatbot import ChatbotMunicipal
from pydantic import BaseModel

chatbot = ChatbotMunicipal()

class MensajeChat(BaseModel):
    mensaje: str
    usuario_id: Optional[str] = None

@app.post("/chat")
async def chat_ciudadano(mensaje_data: MensajeChat):
    # Lógica del chatbot
```

#### Endpoint de Chat:
- **Método:** POST /chat
- **Input:** `{"mensaje": "¿Cómo saco una licencia?"}`
- **Output:** Respuesta + intención detectada + sugerencias

### 8.3 Pruebas del Chatbot
```bash
# Ejemplos de prueba en /docs
{
  "mensaje": "Hola, buenos días"
}

{
  "mensaje": "¿Cómo saco una licencia para mi negocio?"
}

{
  "mensaje": "¿Cuáles son los horarios de atención?"
}

{
  "mensaje": "¿Cuánto cuesta el uso de suelo?"
}
```

---

## 9. Control de Versiones y Documentación

### 9.1 Estructura de Commits
```bash
# Commits realizados
git commit -m "feat: configuración inicial Python + FastAPI"
git commit -m "feat: API básica FastAPI funcionando - endpoints de prueba creados"
git commit -m "feat: sistema municipal completo - 7 endpoints funcionando con documentación automática"
git commit -m "feat: 🤖 chatbot municipal con IA funcionando - reconocimiento de intenciones en español"
```

### 9.2 Gestión del CHANGELOG.md
**Formato:** Keep a Changelog + Versionado Semántico

#### Versiones Documentadas:
- **v0.1.0** - Inicialización del proyecto
- **v0.1.1** - API básica funcionando
- **v0.2.0** - Sistema municipal completo (7 endpoints)
- **v0.3.0** - Chatbot con IA funcionando

### 9.3 Estructura Final del Proyecto
```
SGM/
├── README.md
├── CHANGELOG.md
├── .gitignore
└── backend/
    ├── venv/           # Entorno virtual (no subido a git)
    ├── main.py         # API principal
    ├── chatbot.py      # Lógica del chatbot
    ├── requirements.txt # Dependencias Python
    └── __pycache__/    # Cache Python (no subido a git)
```

---

## 10. Comandos de Flujo de Trabajo

### 10.1 Rutina de Desarrollo Diaria
```bash
# 1. Activar entorno
cd ~/proyectos/SGM/backend
source venv/bin/activate

# 2. Ejecutar servidor de desarrollo
uvicorn main:app --reload

# 3. Probar cambios en:
# http://127.0.0.1:8000/docs

# 4. Detener servidor
# Ctrl+C

# 5. Subir cambios
deactivate
cd ..
git add .
git commit -m "descripción del cambio"
git push origin main
```

### 10.2 Comandos de Mantenimiento
```bash
# Actualizar dependencias
pip list --outdated
pip install --upgrade [paquete]
pip freeze > requirements.txt

# Limpiar cache
rm -rf __pycache__/
find . -name "*.pyc" -delete

# Recrear entorno virtual (si es necesario)
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 11. Configuración de .gitignore

### 11.1 Archivos Excluidos
```gitignore
# Entorno virtual
backend/venv/

# Cache de Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Variables de entorno
.env
.env.local

# Archivos del sistema
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
*.swp
*.swo
```

---

## 12. Métricas del Proyecto

### 12.1 Líneas de Código
- **main.py:** ~200 líneas
- **chatbot.py:** ~150 líneas
- **Total Python:** ~350 líneas
- **Documentación:** ~100 líneas

### 12.2 Funcionalidades Completadas
- ✅ 8 endpoints REST funcionales
- ✅ Documentación automática OpenAPI/Swagger
- ✅ Sistema de chatbot con IA básica
- ✅ Manejo de errores HTTP
- ✅ Base de datos simulada con datos reales
- ✅ Respuestas estructuradas y consistentes

### 12.3 Tiempo de Desarrollo
- **Configuración inicial:** 2 horas
- **API básica:** 1 hora  
- **Endpoints municipales:** 2 horas
- **Chatbot con IA:** 2 horas
- **Documentación y pruebas:** 1 hora
- **Total:** ~8 horas de desarrollo efectivo

---

## 13. Próximos Pasos Técnicos

### 13.1 Mejoras Inmediatas Planificadas
1. **Frontend React** - Interfaz web para ciudadanos
2. **Base de datos PostgreSQL** - Persistencia real
3. **Integración OpenAI API** - IA más avanzada
4. **Deploy a Railway/Render** - URL pública

### 13.2 Arquitectura Future
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Base de       │
│   React         │────│   FastAPI       │────│   Datos         │
│   TypeScript    │    │   Python        │    │   PostgreSQL    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                       ┌─────────────────┐
                       │   IA Services   │
                       │   OpenAI API    │
                       │   NLP español   │
                       └─────────────────┘
```

---

## 14. Notas Técnicas Importantes

### 14.1 Lecciones Aprendidas
1. **Fish Shell:** No compatible con venv de Python, mejor usar Bash
2. **GitHub:** Requiere Personal Access Token, no contraseñas
3. **Entornos Virtuales:** No son portables, mejor recrear que mover
4. **FastAPI:** Documentación automática es increíblemente útil
5. **UTF-8:** Evitar emojis en APIs JSON para mejor compatibilidad

### 14.2 Decisiones de Arquitectura
1. **Monolito sobre Microservicios:** Para prototipo, más simple mantener todo junto
2. **Base de datos simulada:** Permite desarrollo sin infraestructura externa
3. **Chatbot basado en reglas:** Más predecible que ML para MVP
4. **FastAPI sobre Django:** Mejor performance y documentación automática

### 14.3 Consideraciones de Seguridad
- Variables de entorno para secrets (preparado para producción)
- Validación de input con Pydantic
- Rate limiting pendiente para producción
- HTTPS requerido para deploy

---

**Bitácora generada:** 25 de mayo de 2025  
**Versión del sistema:** 0.3.0  
**Estado:** Funcional y demo-ready
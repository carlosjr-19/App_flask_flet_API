# 📊 API + Flet App — Gestión de Comisiones y Archivos 📁✨

¡Bienvenido a este proyecto que combina una **API en Flask** y una **aplicación de escritorio en Flet** para gestionar archivos de comisiones de manera eficiente y visual! 🚀

---

## 📦 Estructura del Proyecto

```
API_FLASK_FLET/
├── backend/
│   ├── backend.py
│   └── env.py
│
├── frontend/
│   ├── assets/
│   ├── components/
│   │   ├── config.py
│   │   ├── formulario.py
│   │   ├── info.py
│   │   ├── menu.py
│   │   └── utils.py
│   ├── storage/
│   └── app_flet.py
│
├── requiremets.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Tecnologías Utilizadas

- 🐍 **Python 3.11+**
- ⚙️ **Flask** — para la API REST.
- 🎨 **Flet** — para la aplicación de escritorio en Python.
- 📦 **Requests** — consumo de API desde Flet.
- 📊 **Polars** *(comentado, listo para uso en procesamiento de archivos)*.

---

## 🚀 Cómo Ejecutar el Proyecto

### 📌 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/carlosjr-19/App_flask_flet_API.git
cd API_FLASK_FLET
```

### 📌 2️⃣ Crear y activar entorno virtual

```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

### 📌 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 📌 4️⃣ Ejecutar API Flask

En una terminal:

```bash
cd backend
python backend.py
```

o directamente:

```bash
python backend/backend.py
```


### 📌 5️⃣ Ejecutar la App Flet

En otra terminal:

```bash
cd frontend
python app_flet.py
```

O directamente:

```bash
flet run frontend/app_flet.py
```

### ¡¡Importante!! primero se debe levantar el servidor en Flask y posteriormente ejecutar la app en Flet

---

## 🎨 Funcionalidades

✅ Cargar archivos CSV y Excel.  
✅ Configuración dinámica de formulario desde la API.  
✅ Menú lateral configurable vía API.  
✅ Área de información de proceso con logs de operaciones.  
✅ Progreso visual con `ProgressBar`.  
✅ Personalización de temas y colores desde la API.

---
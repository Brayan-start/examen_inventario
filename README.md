# Sistema de Gestión de Inventario - Tienda Tech

Este es un proyecto completo de una aplicación web para la gestión de inventario de una tienda de tecnología, desarrollado con **Python** y el framework **Flask**.

## 🚀 Características
- **CRUD Completo**: Registro, listado, edición y eliminación de productos.
- **Base de Datos**: Persistencia local mediante SQLite.
- **Interfaz Moderna**: Diseño limpio y responsivo utilizando Bootstrap 5 y Bootstrap Icons.
- **Validación**: Control básico de formularios y retroalimentación mediante mensajes flash.

## 🛠️ Requisitos
- Python 3.8 o superior.
- Pip (gestor de paquetes de Python).

## 📥 Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd examen_inventario
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Linux/macOS
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Inicializar la base de datos**:
   ```bash
   python database.py
   ```

## 🏃 Ejecución
Para iniciar el servidor de desarrollo:
```bash
python app.py
```
La aplicación estará disponible en `http://127.0.0.1:5000/`.

## 📁 Estructura del Proyecto
```text
examen_inventario/
├── app.py              # Lógica principal y rutas de Flask
├── database.py         # Configuración e inicialización de SQLite
├── requirements.txt    # Dependencias del proyecto
├── .gitignore          # Archivos excluidos del control de versiones
├── README.md           # Documentación
├── inventario.db       # Base de datos (generada automáticamente)
└── templates/          # Plantillas Jinja2 (HTML)
    ├── base.html       # Estructura principal
    ├── index.html      # Listado de productos
    ├── registrar.html  # Formulario de alta
    └── editar.html     # Formulario de modificación
```

## 📝 Notas de Desarrollo
- Se ha simulado un historial de commits para reflejar el ciclo de vida del desarrollo.
- El diseño utiliza componentes modernos de Bootstrap para una mejor experiencia de usuario.

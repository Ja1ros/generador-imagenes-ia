# Generador de Imagenes con IA

Interfaz web para generar imagenes a partir de descripciones de texto usando la API de DALL-E (OpenAI).

## Caracteristicas

- Generacion de imagenes a partir de prompts de texto.
- Seleccion de tamano y estilo (vivid o natural).
- Galeria de imagenes generadas durante la sesion.

## Stack tecnologico

- Python 3.10+
- Streamlit
- OpenAI API (DALL-E 3)

## Instalacion

```bash
git clone https://github.com/Ja1ros/generador-imagenes-ia.git
cd generador-imagenes-ia
pip install -r requirements.txt
```

## Uso

```bash
streamlit run app.py
```

1. Ingresa tu API Key de OpenAI en la barra lateral.
2. Selecciona el tamano y estilo de la imagen.
3. Escribe una descripcion y presiona "Generar imagen".

## Variables de entorno

Crea un archivo `.env` basado en `.env.example` si prefieres no ingresar la API Key manualmente.

## Proximas mejoras

- Soporte para modelos de Stable Diffusion como alternativa.
- Descarga directa de imagenes generadas.
- Historial persistente de generaciones.

## Licencia

Proyecto con fines educativos y de portafolio.

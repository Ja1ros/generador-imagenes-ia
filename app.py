import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Generador de Imagenes con IA", page_icon="🎨")
st.title("🎨 Generador de Imagenes con IA")
st.write("Escribe una descripcion (prompt) y genera una imagen usando DALL-E.")

api_key = st.sidebar.text_input("OpenAI API Key", type="password")
size = st.sidebar.selectbox("Tamano de imagen", ["1024x1024", "1792x1024", "1024x1792"])
style = st.sidebar.selectbox("Estilo", ["vivid", "natural"])

if "gallery" not in st.session_state:
    st.session_state.gallery = []

prompt = st.text_area("Describe la imagen que quieres generar", height=100)

if st.button("Generar imagen"):
    if not api_key:
        st.warning("Ingresa tu API Key de OpenAI en la barra lateral.")
    elif not prompt.strip():
        st.warning("Escribe una descripcion antes de generar la imagen.")
    else:
        client = OpenAI(api_key=api_key)
        with st.spinner("Generando imagen..."):
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size=size,
                style=style,
                n=1,
            )
            image_url = response.data[0].url
        st.session_state.gallery.insert(0, {"prompt": prompt, "url": image_url})

if st.session_state.gallery:
    st.subheader("Galeria de imagenes generadas")
    for item in st.session_state.gallery:
        st.image(item["url"], caption=item["prompt"], use_column_width=True)
        st.divider()

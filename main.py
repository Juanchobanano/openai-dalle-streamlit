from openai import OpenAI
import streamlit as st
import constants as ct
import requests
from io import BytesIO

st.set_page_config(page_title="DALL.E 3 Image Generation")
client = OpenAI(api_key=ct.OPEN_AI_API)

# Constants for cost estimation
COST_PER_IMAGE = 0.04 * 4500


def generate_image(image_description):
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_description,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    img_url = response.data[0].url
    return img_url


def download_image(image_url):
    response = requests.get(image_url)
    response.raise_for_status()
    return BytesIO(response.content)


st.title('Generador de imágenes')
img_description = st.text_area('Descripción de la imagen')


if st.button('Generar imagen'):
    with st.spinner('Generando imagen...'):
        generated_img_url = generate_image(img_description)
        st.image(generated_img_url, caption="Imagen generada")

        # Show cost information
        cost = COST_PER_IMAGE
        st.write(f"Costo de generación de la imagen: ${cost:.2f} COP")

        # Download button
        img_data = download_image(generated_img_url)
        st.download_button(
            label="Descargar imagen",
            data=img_data,
            file_name="generated_image.png",
            mime="image/png"
        )

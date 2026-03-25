import streamlit as st
from pathlib import Path

# Configuración de la página
st.set_page_config(
    page_title="Visor de PDF",
    page_icon="📄",
    layout="wide"
)

# Título y descripción
st.title("📄 Visor de PDF")
st.markdown("Sube tus archivos PDF para visualizarlos")

# Crear dos columnas
col1, col2 = st.columns([1, 4])

with col1:
    # Widget para subir archivo
    uploaded_file = st.file_uploader(
        "Selecciona un archivo PDF",
        type=['pdf'],
        help="Arrastra y suelta tu archivo PDF aquí"
    )

    if uploaded_file is not None:
        # Mostrar información del archivo
        file_details = {
            "Nombre": uploaded_file.name,
            "Tamaño": f"{uploaded_file.size / 1024:.1f} KB"
        }
        st.write("### Detalles del archivo")
        for key, value in file_details.items():
            st.write(f"**{key}:** {value}")

with col2:
    if uploaded_file is not None:
        # Mostrar el PDF
        st.pdf(
            uploaded_file,
            height="stretch"  # Se ajusta al contenedor
        )
    else:
        # Mensaje cuando no hay archivo
        st.info("👆 Por favor sube un archivo PDF para visualizarlo")
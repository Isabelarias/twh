import streamlit as st

st.set_page_config(page_title="Life Cycle", layout="wide")

st.title("Life Cycle")

flow = {
    "inicio": {
        "pregunta": "¿La prescripción necesita autorización?",
        "si": "autorizacion_si",
        "no": "autorizacion_no",
        "info": "kfjgdfigkjgdfjg"
    },
    "autorizacion_si": {
        "pregunta": "¿El paciente cumple criterios?",
        "si": "FIN1",
        "no": "FIN2",
        "info": "kdjglgjkdfgkfdhjgf"
    },
    "autorizacion_no": {
        "pregunta": "¿Es una prescripción válida?",
        "si": "FIN3",
        "no": "FIN4",
        "info": "dfjkgdfkgdfgndfkgkdjg"
    }
}

finales = {
    "FIN1": {
        "titulo": "Autorización aprobada",
        "texto": "El paciente cumple criterios. Procede la autorización.",
        "color": "success",
        "extra": "dfjlgklsñdoksñldsñkefoglj"
    },
    "FIN2": {
        "titulo": "Autorización denegada",
        "texto": "El paciente no cumple los criterios clínicos.",
        "color": "error",
        "extra": "kdsjgfkdgkj"
    },
    "FIN3": {
        "titulo": "No requiere autorización",
        "texto": "La prescripción es válida y no necesita proceso adicional.",
        "color": "info",
        "extra": "jkdsghrdfkjgnjkfdgn"
    },
    "FIN4": {
        "titulo": "Prescripción rechazada",
        "texto": "La prescripción no es válida. Revisar con el solicitante.",
        "color": "warning",
        "extra": "alkrjkfrjkdgnvjr"
    }
}

# -------------------------
# ESTADO
# -------------------------
if "nodo" not in st.session_state:
    st.session_state.nodo = "inicio"

if "historial" not in st.session_state:
    st.session_state.historial = []

nodo = st.session_state.nodo

# Diseño: 2 columnas (tu main + columna IA)
col_main, col_side = st.columns([2, 1])

# -------------------------
# FUNCIÓN PARA VOLVER
# -------------------------
def volver():
    if st.session_state.historial:
        st.session_state.nodo = st.session_state.historial.pop()
        st.rerun()

# -------------------------
# NODO FINAL
# -------------------------
if nodo in finales:
    data = finales[nodo]

    with col_main:
        if data["color"] == "success":
            st.success(f"### {data['titulo']}\n{data['texto']}")
        elif data["color"] == "error":
            st.error(f"### {data['titulo']}\n{data['texto']}")
        elif data["color"] == "warning":
            st.warning(f"### {data['titulo']}\n{data['texto']}")
        else:
            st.info(f"### {data['titulo']}\n{data['texto']}")

        if nodo != "inicio":
            if st.button("Regresar"):
                volver()

    # -------- COLUMNA DERECHA (INFO + IA) --------
    with col_side:
        st.markdown("###Información adicional")
        st.info(data["extra"])

        st.markdown("---")
        st.markdown("###Asistente Inteligente")

        notebook_url = "https://notebooklm.google.com/notebook/68134421-ea9c-45fc-97e2-648a101095d3"

        st.markdown(
            f"""
            <a href="{notebook_url}" target="_blank">
                <button style="
                    padding:10px 20px;
                    background-color:#4CAF50;
                    color:white;
                    border:none;
                    border-radius:8px;
                    font-size:16px;
                    cursor:pointer;">
                    Abrir NotebookLM
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

# -------------------------
# NODO INTERMEDIO
# -------------------------
else:
    pregunta = flow[nodo]["pregunta"]

    with col_main:
        st.markdown(f"## {pregunta}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Sí"):
                st.session_state.historial.append(nodo)
                st.session_state.nodo = flow[nodo]["si"]
                st.rerun()
        with col2:
            if st.button("No"):
                st.session_state.historial.append(nodo)
                st.session_state.nodo = flow[nodo]["no"]
                st.rerun()

        if nodo != "inicio":
            if st.button("Regresar"):
                volver()

    # -------- COLUMNA DERECHA (CURIOSO + IA) --------
    with col_side:

        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:8px;">
            <img src="https://img.icons8.com/?size=100&id=112286&format=png&color=000000" width="45" height="45">
            <span style="font-size:1.25rem; font-weight:bold;">Dato curioso</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.info(flow[nodo]["info"])

        st.markdown("---")
        st.markdown("Asistente Inteligente")

        notebook_url = "https://notebooklm.google.com/notebook/68134421-ea9c-45fc-97e2-648a101095d3"

        st.markdown(
            f"""
            <a href="{notebook_url}" target="_blank">
                <button style="
                    padding:10px 20px;
                    background-color:#4CAF50;
                    color:white;
                    border:none;
                    border-radius:8px;
                    font-size:16px;
                    cursor:pointer;">
                    Abrir NotebookLM
                </button>
            </a>
            """,
            unsafe_allow_html=True
        )

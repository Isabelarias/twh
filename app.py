import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Life Cycle", layout="wide")

st.title("Life Cycle")

# -------------------------
# FLUJO DEL DIAGRAMA
# -------------------------
flow = {
    "inicio": {
        "pregunta": "¿La prescripción necesita autorización?",
        "si": "autorizacion_si",
        "no": "autorizacion_no",
        "info": "Una prescripción puede requerir autorización cuando supera ciertos costos o entra en categorías especiales.",
        "curioso": "Muchos medicamentos de bajo costo no requieren autorización previa."
    },
    "autorizacion_si": {
        "pregunta": "¿El paciente cumple criterios?",
        "si": "FIN1",
        "no": "FIN2",
        "info": "Los criterios clínicos se basan en guías médicas y políticas del asegurador.",
        "curioso": "Los criterios pueden cambiar cada año según nuevas evidencias."
    },
    "autorizacion_no": {
        "pregunta": "¿Es una prescripción válida?",
        "si": "FIN3",
        "no": "FIN4",
        "info": "Se revisa si el médico diligenció la fórmula correctamente.",
        "curioso": "El 15% de las prescripciones rechazadas es por errores de digitación."
    }
}

# -------------------------
# RESULTADOS FINALES
# -------------------------
finales = {
    "FIN1": {
        "titulo": "Autorización aprobada",
        "texto": "El paciente cumple criterios. Procede la autorización.",
        "color": "success",
        "extra": "Verifica siempre si existe una versión más reciente de los criterios clínicos."
    },
    "FIN2": {
        "titulo": "Autorización denegada",
        "texto": "El paciente no cumple los criterios clínicos.",
        "color": "error",
        "extra": "Sugiere al solicitante presentar nueva evidencia clínica o exámenes recientes."
    },
    "FIN3": {
        "titulo": "No requiere autorización",
        "texto": "La prescripción es válida y no necesita proceso adicional.",
        "color": "info",
        "extra": "Muchos medicamentos de bajo costo no necesitan autorización previa."
    },
    "FIN4": {
        "titulo": "Prescripción rechazada",
        "texto": "La prescripción no es válida. Revisar con el solicitante.",
        "color": "warning",
        "extra": "Verifica que el diagnóstico coincida con el medicamento solicitado."
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

# -------------------------
# FUNCIÓN DE VOLVER
# -------------------------
def volver():
    if st.session_state.historial:
        st.session_state.nodo = st.session_state.historial.pop()
        st.rerun()

# -------------------------
# LAYOUT DE COLUMNAS
# -------------------------
col_left, col_right = st.columns([2.2, 1])

# ------------------------------------------------
#                NODO FINAL
# ------------------------------------------------
if nodo in finales:
    data = finales[nodo]

    with col_left:
        # TARJETA DEL RESULTADO
        if data["color"] == "success":
            st.success(f"### {data['titulo']}\n{data['texto']}")
        elif data["color"] == "error":
            st.error(f"### {data['titulo']}\n{data['texto']}")
        elif data["color"] == "warning":
            st.warning(f"### {data['titulo']}\n{data['texto']}")
        else:
            st.info(f"### {data['titulo']}\n{data['texto']}")

        # Botón regresar
        if nodo != "inicio":
            if st.button("Regresar"):
                volver()

        # Dato curioso debajo (IZQUIERDA)
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:8px; margin-top:30px;">
            <img src="https://img.icons8.com/?size=100&id=112286&format=png&color=000000" width="40">
            <span style="font-size:1.25rem; font-weight:bold;">Dato curioso</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.info(data["extra"])

    # IA NotebookLM (DERECHA)
    with col_right:
        st.markdown("### 🤖 Asistente Inteligente")
        st.write("Consulta información, haz preguntas o recibe ayuda contextual.")

        components.iframe(
            src="https://notebooklm.google.com/notebook/68134421-ea9c-45fc-97e2-648a101095d3",
            height=750,
            scrolling=True
        )

# ------------------------------------------------
#            NODO INTERMEDIO
# ------------------------------------------------
else:
    pregunta = flow[nodo]["pregunta"]

    with col_left:
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

        # Botón volver
        if nodo != "inicio":
            if st.button("Regresar"):
                volver()

        # -------------------------
        # DATO CURIOSO (IZQUIERDA)
        # -------------------------
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:8px; margin-top:30px;">
            <img src="https://img.icons8.com/?size=100&id=112286&format=png&color=000000" width="40">
            <span style="font-size:1.25rem; font-weight:bold;">Dato curioso</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.info(flow[nodo].get("curioso", "Aquí puedes agregar un dato curioso."))

    # -------------------------
    # IA (DERECHA)
    # -------------------------
    with col_side:
        st.markdown("### 🤖 Asistente Inteligente")

        st.markdown(
            """
            <div style="padding:15px; border-radius:10px; background-color:#f7f7f7;
                    border:1px solid #ddd; text-align:center;">
            <p style="font-size:1.1rem; font-weight:600; margin-bottom:10px;">
                Accede al asistente con la información completa
            </p>
            <a href="https://notebooklm.google.com/notebook/68134421-ea9c-45fc-97e2-648a101095d3" 
               target="_blank" 
               style="display:inline-block; padding:10px 18px; background-color:#4a90e2; color:white;
                      border-radius:8px; text-decoration:none; font-weight:bold;">
               Abrir Asistente NotebookLM
            </a>
            </div>
            """,
            unsafe_allow_html=True
        )

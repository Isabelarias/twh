import streamlit as st

st.set_page_config(page_title="Life Cycle", layout="wide")

st.title("Life Cycle")

flow = {
    "inicio": {
        "pregunta": "¿La prescripción necesita autorización?",
        "si": "autorizacion_si",
        "no": "autorizacion_no",
        "info": "Una prescripción necesita autorización cuando supera ciertos costos o es considerada especial por la aseguradora.",
        "extra2": "Curiosidad: Algunas aseguradoras cambian los topes de autorización cada año."
    },
    "autorizacion_si": {
        "pregunta": "¿El paciente cumple criterios?",
        "si": "FIN1",
        "no": "FIN2",
        "info": "Los criterios clínicos se basan en guías médicas y políticas de la aseguradora.",
        "extra2": "Tip avanzado: Los criterios de enfermedades crónicas suelen tener excepciones clínicas."
    },
    "autorizacion_no": {
        "pregunta": "¿Es una prescripción válida?",
        "si": "FIN3",
        "no": "FIN4",
        "info": "Aquí revisamos si el médico diligenció la prescripción correctamente.",
        "extra2": "Dato curioso: Algunos formatos electrónicos corrigen errores automáticamente."
    }
}

finales = {
    "FIN1": {
        "titulo": "Autorización aprobada",
        "texto": "El paciente cumple criterios. Procede la autorización.",
        "color": "success",
        "extra": "Tip: Siempre verifica si hay una guía más reciente sobre criterios clínicos.",
        "extra2": "Dato curioso: En algunos países, las autorizaciones se aprueban automáticamente con IA."
    },
    "FIN2": {
        "titulo": "Autorización denegada",
        "texto": "El paciente no cumple los criterios clínicos.",
        "color": "error",
        "extra": "Dato útil: Puedes sugerir al solicitante que presente nueva evidencia clínica.",
        "extra2": "Curiosidad: La mitad de las negaciones se deben a documentos incompletos."
    },
    "FIN3": {
        "titulo": "No requiere autorización",
        "texto": "La prescripción es válida y no necesita proceso adicional.",
        "color": "info",
        "extra": "Recuerda: Muchas prescripciones de bajo costo NO pasan por autorización.",
        "extra2": "Tip adicional: Si dudas, revisa la política de medicamentos de bajo impacto."
    },
    "FIN4": {
        "titulo": "Prescripción rechazada",
        "texto": "La prescripción no es válida. Revisar con el solicitante.",
        "color": "warning",
        "extra": "Tip: Sugiere revisar si el diagnóstico coincide con el medicamento solicitado.",
        "extra2": "Dato curioso: Los errores más comunes son fechas incorrectas o campos vacíos."
    }
}

# ESTADO
if "nodo" not in st.session_state:
    st.session_state.nodo = "inicio"

nodo = st.session_state.nodo

# Columnas: izquierda (pregunta) y derecha (tips)
col_main, col_side = st.columns([2, 1])

# -------------------------
#        NODO FINAL
# -------------------------
if nodo in finales:
    data = finales[nodo]

    # CONTENIDO PRINCIPAL
    with col_main:
        if data["color"] == "success":
            st.success(f"### {data['titulo']}\n{data['texto']}")
        elif data["color"] == "error":
            st.error(f"### {data['titulo']}\n{data['texto']}")
        elif data["color"] == "warning":
            st.warning(f"### {data['titulo']}\n{data['texto']}")
        else:
            st.info(f"### {data['titulo']}\n{data['texto']}")

    # PANEL DERECHO: 2 CUADROS
    with col_side:
        st.markdown("### ℹ️ Información adicional")
        st.info(data["extra"])

        st.markdown("### 💡 Dato curioso")
        st.warning(data["extra2"])

# -------------------------
#     NODO INTERMEDIO
# -------------------------
else:
    pregunta = flow[nodo]["pregunta"]

    with col_main:
        st.markdown(f"## {pregunta}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Sí"):
                st.session_state.nodo = flow[nodo]["si"]
                st.rerun()
        with col2:
            if st.button("No"):
                st.session_state.nodo = flow[nodo]["no"]
                st.rerun()

    # PANEL DERECHO: 2 CUADROS
    with col_side:
        st.markdown("### 📌 Info útil")
        st.info(flow[nodo]["info"])

        st.markdown("### 💡 Dato curioso")
        st.warning(flow[nodo]["extra2"])

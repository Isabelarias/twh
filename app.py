import streamlit as st

flow = {
    "inicio": {
        "pregunta": La prescripción necesita autorización",
        "si": "actividad_fisica",
        "no": "FIN1"
    },

    "actividad_fisica": {
        "pregunta": "¿Te gusta hacer ejercicio?",
        "si": "gimnasio",
        "no": "bici"
    },

    "gimnasio": {
        "pregunta": "¿Prefieres pesas?",
        "si": "FIN2",
        "no": "FIN3"
    },

    "bici": {
        "pregunta": "¿Te gustaría probar bicicleta?",
        "si": "FIN4",
        "no": "FIN5"
    }
}

finales = {
    "FIN1": "Está bien, también puedes trabajar en tu bienestar emocional 😊",
    "FIN2": "Haz entrenamiento de fuerza 3 veces por semana 💪",
    "FIN3": "Prueba subir escaleras o cardio suave",
    "FIN4": "Empieza con rutas cortas los fines de semana 🚴‍♀️",
    "FIN5": "Caminar 30 minutos al día es una buena alternativa 🚶‍♀️"
}

######## Para streamlit

st.title("Life Cycle")

# Inicializar estado
if "nodo" not in st.session_state:
    st.session_state["nodo"] = "inicio"
    st.session_state["historial"] = []

nodo = st.session_state["nodo"]

# Si estamos en un nodo final
if nodo in finales:
    st.success(finales[nodo])

    if st.button("🔄 Reiniciar"):
        st.session_state["nodo"] = "inicio"
        st.session_state["historial"] = []
        st.rerun()

else:
    # Mostrar pregunta
    pregunta = flow[nodo]["pregunta"]
    st.markdown(f"### {pregunta}")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sí"):
            st.session_state["historial"].append(nodo)
            st.session_state["nodo"] = flow[nodo]["si"]
            st.rerun()

    with col2:
        if st.button("No"):
            st.session_state["historial"].append(nodo)
            st.session_state["nodo"] = flow[nodo]["no"]
            st.rerun()

    # Botón para retroceder
    if st.session_state["historial"]:
        if st.button("⬅️ Regresar"):
            st.session_state["nodo"] = st.session_state["historial"].pop()
            st.rerun()

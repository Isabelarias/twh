import streamlit as st

# ----------- DEFINICIÓN DEL FLUJO ----------------
flow = {
    "inicio": {
        "pregunta": "¿Quieres mejorar tu salud?",
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

# ----------- ESTADO ----------------
if "nodo" not in st.session_state:
    st.session_state.nodo = "inicio"

nodo = st.session_state.nodo

# ----------- DIAGRAMA MERMAID --------------
def generar_mermaid(nodo_activo):
    mermaid = "flowchart TD;\n"

    for key, val in flow.items():
        mermaid += f"    {key}['{key}'];\n"
        mermaid += f"    {key} -->|Sí| {val['si']};\n"
        mermaid += f"    {key} -->|No| {val['no']};\n"

    for f in finales:
        mermaid += f"    {f}(['{f}']);\n"

    mermaid += f"\nclass {nodo_activo} activeNode;"

    style = """
    <style>
    .activeNode rect {
        fill: #ffdd57 !important;
        stroke: #d4a017 !important;
        stroke-width: 3px;
    }
    </style>
    """

    return style + f"```mermaid\n{mermaid}\n```"


st.markdown("## 🌳 Árbol de Decisiones Interactivo")

# Mostrar diagrama
st.markdown(generar_mermaid(nodo), unsafe_allow_html=True)

# Si es final → mostrar resultado
if nodo in finales:
    st.success(f"**Resultado:** {finales[nodo]}")
    if st.button("🔄 Reiniciar"):
        st.session_state.nodo = "inicio"
    st.stop()

# Mostrar pregunta y botones
st.subheader(flow[nodo]["pregunta"])

col1, col2 = st.columns(2)

if col1.button("Sí"):
    st.session_state.nodo = flow[nodo]["si"]

if col2.button("No"):
    st.session_state.nodo = flow[nodo]["no"]

st.rerun()

import streamlit as st

st.set_page_config(page_title="Life Cycle", layout="wide")

# Logo empresa ------------------------------------------------------
st.markdown(
    """
    <div style="display:flex; justify-content:flex-end; align-items:center; width:100%; margin-bottom:-40px; margin-top:-20px;">
        <img src="https://media.licdn.com/dms/image/sync/v2/D5627AQHFh-gz6oTSAQ/articleshare-shrink_480/B56ZmBlrxmJ4Ao-/0/1758815763863?e=2147483647&v=beta&t=GMDQ2mYSHgk7SWwFTFlkSBF4FhZRD3Bil1rFrB5W9bo" 
             style="width:180px; height:auto;">
    </div>
    """,
    unsafe_allow_html=True
)

# Botones ------------------------------------------------------
if "diagrama" not in st.session_state:
    st.session_state.diagrama = None

if "nodo" not in st.session_state:
    st.session_state.nodo = None

if "historial" not in st.session_state:
    st.session_state.historial = []
    
st.markdown(" ")

colA, colB, colC, colD, colE, colF, colG, colH = st.columns(8)

if "diagrama" not in st.session_state:
    st.session_state.diagrama = "A"  

with colA:
    if st.button("Ack"):
        st.session_state.diagrama = "A"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()

with colB:
    if st.button("AE"):
        st.session_state.diagrama = "B"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()

with colC:
    if st.button("ANS"):
        st.session_state.diagrama = "C"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()
        
with colD:
    if st.button("Status"):
        st.session_state.diagrama = "D"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()

with colE:
    if st.button("Pharmacy"):
        st.session_state.diagrama = "E"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()

with colF:
    if st.button("Post-Transfers"):
        st.session_state.diagrama = "F"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()

with colG:
    if st.button("Enrollments"):
        st.session_state.diagrama = "G"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()

with colH:
    if st.button("Insurances"):
        st.session_state.diagrama = "H"
        st.session_state.nodo = "inicio"
        st.session_state.historial = []
        st.rerun()


# Diagramas de decision ------------------------------------------------------

if st.session_state.diagrama == "A":
    flow = {
        "inicio": {
            "pregunta": "¿La prescripción necesita autorización?",
            "si": "autorizacion_si",
            "no": "autorizacion_no",
            "info": "En algunos sistemas médicos, más del 40% de las prescripciones pasan por un proceso de autorización previa."
        },
        "autorizacion_si": {
            "pregunta": "¿El paciente cumple criterios?",
            "si": "FIN1",
            "no": "FIN2",
            "info": "Los criterios clínicos pueden incluir edad, diagnóstico, historial y respuesta a tratamientos previos."
        },
        "autorizacion_no": {
            "pregunta": "¿Es una prescripción válida?",
            "si": "FIN3",
            "no": "FIN4",
            "info": "Una prescripción inválida puede ser por error de digitación o datos incompletos."
        }
    }

elif st.session_state.diagrama == "B":
    flow = {
        "inicio": {
            "pregunta": "¿El caso requiere escalación?",
            "si": "rev_supervisor",
            "no": "proceso_normal",
            "info": "El 70% de los casos se resuelve sin escalación en BPO de salud."
        },
        "rev_supervisor": {
            "pregunta": "¿Supervisor disponible?",
            "si": "FIN5",
            "no": "FIN6",
            "info": "En horarios pico, la disponibilidad baja entre 20%–30%."
        },
        "proceso_normal": {
            "pregunta": "¿Documentación completa?",
            "si": "FIN7",
            "no": "FIN8",
            "info": "La documentación incompleta es causa del 45% de retrasos."
        }
    }

elif st.session_state.diagrama == "C":
    flow = {
        "inicio": {
            "pregunta": "¿Existe riesgo para el paciente?",
            "si": "evaluacion_riesgo",
            "no": "proceso_continuo",
            "info": "La evaluación de riesgo es el primer paso para asegurar seguridad clínica."
        },
        "evaluacion_riesgo": {
            "pregunta": "¿Riesgo crítico?",
            "si": "FIN9",
            "no": "FIN10",
            "info": "El riesgo crítico implica intervención inmediata."
        },
        "proceso_continuo": {
            "pregunta": "¿Caso completo?",
            "si": "FIN11",
            "no": "FIN12",
            "info": "Un caso completo mejora la eficiencia del proceso hasta en un 60%."
        }
    }

elif st.session_state.diagrama == "D":
    flow = {
        "inicio": {
            "pregunta": "¿El caso requiere escalación?",
            "si": "rev_supervisor",
            "no": "proceso_normal",
            "info": "El 70% de los casos se resuelve sin escalación en BPO de salud."
        },
        "rev_supervisor": {
            "pregunta": "¿Supervisor disponible?",
            "si": "FIN5",
            "no": "FIN6",
            "info": "En horarios pico, la disponibilidad baja entre 20%–30%."
        },
        "proceso_normal": {
            "pregunta": "¿Documentación completa?",
            "si": "FIN7",
            "no": "FIN8",
            "info": "La documentación incompleta es causa del 45% de retrasos."
        }
    }

elif st.session_state.diagrama == "E":
    flow = {
        "inicio": {
            "pregunta": "¿El caso requiere escalación?",
            "si": "rev_supervisor",
            "no": "proceso_normal",
            "info": "El 70% de los casos se resuelve sin escalación en BPO de salud."
        },
        "rev_supervisor": {
            "pregunta": "¿Supervisor disponible?",
            "si": "FIN5",
            "no": "FIN6",
            "info": "En horarios pico, la disponibilidad baja entre 20%–30%."
        },
        "proceso_normal": {
            "pregunta": "¿Documentación completa?",
            "si": "FIN7",
            "no": "FIN8",
            "info": "La documentación incompleta es causa del 45% de retrasos."
        }
    }

elif st.session_state.diagrama == "F":
    flow = {
        "inicio": {
            "pregunta": "¿El caso requiere escalación?",
            "si": "rev_supervisor",
            "no": "proceso_normal",
            "info": "El 70% de los casos se resuelve sin escalación en BPO de salud."
        },
        "rev_supervisor": {
            "pregunta": "¿Supervisor disponible?",
            "si": "FIN5",
            "no": "FIN6",
            "info": "En horarios pico, la disponibilidad baja entre 20%–30%."
        },
        "proceso_normal": {
            "pregunta": "¿Documentación completa?",
            "si": "FIN7",
            "no": "FIN8",
            "info": "La documentación incompleta es causa del 45% de retrasos."
        }
    }

elif st.session_state.diagrama == "G":
    flow = {
        "inicio": {
            "pregunta": "¿El caso requiere escalación?",
            "si": "rev_supervisor",
            "no": "proceso_normal",
            "info": "El 70% de los casos se resuelve sin escalación en BPO de salud."
        },
        "rev_supervisor": {
            "pregunta": "¿Supervisor disponible?",
            "si": "FIN5",
            "no": "FIN6",
            "info": "En horarios pico, la disponibilidad baja entre 20%–30%."
        },
        "proceso_normal": {
            "pregunta": "¿Documentación completa?",
            "si": "FIN7",
            "no": "FIN8",
            "info": "La documentación incompleta es causa del 45% de retrasos."
        }
    }

elif st.session_state.diagrama == "H":
    flow = {
        "inicio": {
            "pregunta": "¿El caso requiere escalación?",
            "si": "rev_supervisor",
            "no": "proceso_normal",
            "info": "El 70% de los casos se resuelve sin escalación en BPO de salud."
        },
        "rev_supervisor": {
            "pregunta": "¿Supervisor disponible?",
            "si": "FIN5",
            "no": "FIN6",
            "info": "En horarios pico, la disponibilidad baja entre 20%–30%."
        },
        "proceso_normal": {
            "pregunta": "¿Documentación completa?",
            "si": "FIN7",
            "no": "FIN8",
            "info": "La documentación incompleta es causa del 45% de retrasos."
        }
    }


# ---------------------------------------------------
# NODOS FINALES
# ---------------------------------------------------

finales = {
    "FIN1": {"titulo": "Autorización aprobada", "texto": "El paciente cumple criterios.", "color": "success", "extra": "Puedes proceder sin restricciones."},
    "FIN2": {"titulo": "Autorización denegada", "texto": "No cumple criterios clínicos.", "color": "error", "extra": "Sugiere alternativas terapéuticas."},
    "FIN3": {"titulo": "No requiere autorización", "texto": "Prescripción válida.", "color": "info", "extra": "Continúa flujo normal."},
    "FIN4": {"titulo": "Prescripción rechazada", "texto": "No es válida.", "color": "warning", "extra": "Verifica con el médico solicitante."},

    "FIN5": {"titulo": "Supervisor revisa", "texto": "Caso escalado.", "color": "info", "extra": "Tiempo estimado: 5–10 minutos."},
    "FIN6": {"titulo": "Supervisor no disponible", "texto": "Intenta más tarde.", "color": "warning", "extra": "Puede haber alta demanda."},
    "FIN7": {"titulo": "Proceso completado", "texto": "Documentación en orden.", "color": "success", "extra": "Caso finalizado correctamente."},
    "FIN8": {"titulo": "Falta documentación", "texto": "No se puede continuar.", "color": "error", "extra": "Solicita los documentos faltantes."},

    "FIN9": {"titulo": "Riesgo crítico", "texto": "Acción inmediata requerida.", "color": "error", "extra": "Notifica al equipo clínico urgente."},
    "FIN10": {"titulo": "Riesgo moderado", "texto": "Continuar con precaución.", "color": "warning", "extra": "Monitorea cambios."},
    "FIN11": {"titulo": "Caso completo", "texto": "Todo en orden.", "color": "success", "extra": "Listo para registrar."},
    "FIN12": {"titulo": "Caso incompleto", "texto": "Faltan elementos.", "color": "info", "extra": "Revisa la documentación recibida."},
}

# ---------------------------------------------------
# ESTADO
# ---------------------------------------------------

if "nodo" not in st.session_state:
    st.session_state.nodo = "inicio"

if "historial" not in st.session_state:
    st.session_state.historial = []

nodo = st.session_state.nodo

# Diseño: 2 columnas (main + IA/info)
col_main, col_side = st.columns([2.2, 1])

# -------------------------
# FUNCIÓN PARA VOLVER
# -------------------------
def volver():
    if st.session_state.historial:
        st.session_state.nodo = st.session_state.historial.pop()
        st.rerun()

# ---------------------------------------------------
# NODO FINAL
# ---------------------------------------------------
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

        if st.button("Regresar"):
            volver()

    # -------- COLUMNA DERECHA: INFO + IA --------
    with col_side:

        # INFO EXTRA
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:10px;">
                <img src="https://img.icons8.com/?size=100&id=112286&format=png&color=000000" width="35">
                <span style="font-size:20px; font-weight:bold;">Información adicional</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.info(data["extra"])

        st.markdown("---")

        # ASISTENTE INTELIGENTE
        notebook_url = "https://notebooklm.google.com/notebook/68134421-ea9c-45fc-97e2-648a101095d3"

        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:10px;">
                <img src="https://img.icons8.com/?size=100&id=56740&format=png&color=000000" width="35">
                <span style="font-size:20px; font-weight:bold;">Asistente Inteligente</span>
            </div>
            """,
            unsafe_allow_html=True
        )

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

# ---------------------------------------------------
# NODO INTERMEDIO
# ---------------------------------------------------
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

    # -------- COLUMNA DERECHA: DATO CURIOSO + IA --------
    with col_side:

        # DATO CURIOSO
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:10px;">
                <img src="https://img.icons8.com/?size=100&id=112286&format=png&color=000000" width="35">
                <span style="font-size:20px; font-weight:bold;">Dato curioso</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.info(flow[nodo]["info"])

        st.markdown("---")

        # ASISTENTE INTELIGENTE
        notebook_url = "https://notebooklm.google.com/notebook/68134421-ea9c-45fc-97e2-648a101095d3"

        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:10px;">
                <img src="https://img.icons8.com/?size=100&id=115368&format=png&color=000000" width="35">
                <span style="font-size:20px; font-weight:bold;">Asistente Inteligente</span>
            </div>
            """,
            unsafe_allow_html=True
        )

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

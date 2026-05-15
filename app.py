import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------------------------------------
# CONFIGURACIÓN BÁSICA 
# ---------------------------------------------------------
st.set_page_config(
    page_title="Modelo y simulación - Agua eficiente",
    layout="wide"
)

# ---------------------------------------------------------
# TEXTOS CLAVE
# ---------------------------------------------------------

OBJETIVO_GENERAL_SIE = """
**Objetivo general (Sistemas de Información Empresarial)**  
Desarrollar un modelo conceptual y/o computacional aplicado a la optimización del riego en zonas áridas,
integrando datos climáticos, de suelo, cultivo y operación, para apoyar decisiones trazables y auditables
sobre cuánto, cuándo y con qué prioridad regar, contribuyendo a una distribución más eficiente y transparente
del agua en el norte de México.
"""

OBJETIVO_COMPUTO_COGNITIVO = """
**Objetivo general (Cómputo Cognitivo)**  
Diseñar un módulo de recomendación de lámina de riego basado en reglas agronómicas y modelos de
aprendizaje automático interpretables (por ejemplo, Random Forest + SHAP), que genere recomendaciones
numéricas acompañadas de explicaciones claras sobre los factores que influyen en la decisión, considerando
la calidad del dato y la incertidumbre de las mediciones.
"""

DEFINICION_MODELO = """
Un **modelo** es una representación simplificada y estructurada de un sistema real que permite analizar su
comportamiento, probar hipótesis y anticipar efectos de cambios en sus variables, sin intervenir directamente
en el sistema físico.
"""

DEFINICION_SIMULACION = """
La **simulación** es el proceso de ejecutar un modelo a lo largo del tiempo o bajo distintos escenarios para
observar cómo cambian las variables de interés, evaluar decisiones alternativas y estimar resultados posibles
antes de aplicarlos en el mundo real.
"""

# ---------------------------------------------------------
# CARGA DE DATOS
# ---------------------------------------------------------
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    try:
        df = pd.read_csv(path)
        df.columns = [c.strip() for c in df.columns]
        return df
    except Exception as e:
        st.warning(f"No se pudo cargar el archivo '{path}'. Verifica que exista en la carpeta. Detalle: {e}")
        return pd.DataFrame()

df = load_data("durango.csv")


# ---------------------------------------------------------
# SIDEBAR - NAVEGACIÓN POR FASES
# ---------------------------------------------------------
st.sidebar.title("Navegación")
seccion = st.sidebar.radio(
    "Ir a:",
    [
        "1. Objetivo y marco teórico",
        "2. Fases 1–3: Sistema y modelo conceptual",
        "3. Fase 4: Simulación de escenarios",
        "4. Fase 5: Integración al documento de investigación"
    ]
)




# ---------------------------------------------------------
# SECCIÓN 1: OBJETIVO Y MARCO TEÓRICO (FASE 1)
# ---------------------------------------------------------
if seccion == "1. Objetivo y marco teórico":

    # ---------------- PORTADA SOLO PARA ESTA FASE ----------------
    st.markdown(
        """
<div style="background-color:#FFFFFF;
            border:2px solid #1a4c8f;
            border-radius:12px;
            padding:25px;
            text-align:center;
            margin-bottom:25px;">

<h1 style='color:#1a4c8f; margin-bottom:10px;'>
Optimización del riego en zonas áridas
</h1>

<h3 style='color:black; margin-top:10px;'>
Integrantes
</h3>

<p style='font-size:18px; color:black; line-height:1.6; margin-top:10px;'>
Díaz Martínez Dulce Carolina<br>
Granados Sáenz José de Jesús<br>
Juárez Ortiz José Ángel
</p>

</div>
        """,
        unsafe_allow_html=True
    )

    # ---------------- LÍNEA DEBAJO DEL CUADRO ----------------
    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )

    # ---------------- TÍTULO PRINCIPAL ----------------
    st.title("Modelo y simulación del sistema de riego")

    st.subheader("Objetivos generales")
    st.markdown(OBJETIVO_GENERAL_SIE)
    st.markdown(OBJETIVO_COMPUTO_COGNITIVO)

    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )

    st.subheader("Definiciones clave para el marco teórico")

    # ---------------- TEXTO EXTRA PARA RELLENAR EL ESPACIO ----------------
    st.markdown("""
Las definiciones anteriores establecen la base conceptual del proyecto, ya que permiten comprender cómo 
se estructura el sistema de riego y cómo se comporta bajo diferentes condiciones ambientales y operativas.

En el contexto del riego en zonas áridas, estos conceptos son fundamentales para:

- Analizar cómo las variables climáticas influyen en la demanda hídrica del cultivo.
- Evaluar escenarios con disponibilidad limitada de agua.
- Determinar el impacto de decisiones operativas como frecuencia, método y lámina aplicada.
- Anticipar riesgos como el estrés hídrico y su efecto en la producción agrícola.
- Justificar la necesidad de un sistema de apoyo a decisiones basado en datos reales y modelos confiables.

Este marco teórico permite avanzar hacia la construcción del modelo conceptual y la simulación de escenarios,
asegurando que el análisis sea coherente, trazable y científicamente sustentado.
""")

    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Definición de modelo")
        st.markdown(DEFINICION_MODELO)
    with col2:
        st.markdown("### Definición de simulación")
        st.markdown(DEFINICION_SIMULACION)

    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )





    

# ---------------------------------------------------------
# SECCIÓN 2: FASES 1–3 (VARIABLES Y MODELO CONCEPTUAL)
# ---------------------------------------------------------
elif seccion == "2. Fases 1–3: Sistema y modelo conceptual":
    st.title("Fases 1–3: Sistema, variables y modelo conceptual")

    # ---------------------------------------------------------
    # FASE 1: Recuperación y síntesis de lecturas
    # ---------------------------------------------------------
    st.header("Fase 1: Recuperación y síntesis de las lecturas")

    st.subheader("Definición de modelo")
    st.markdown("""
Un **modelo** es una representación simplificada de un sistema real que permite analizar su comportamiento,
probar hipótesis y anticipar efectos de cambios sin intervenir directamente en el sistema físico.
    """)

    st.subheader("Definición de simulación")
    st.markdown("""
La **simulación** es el proceso de ejecutar un modelo bajo distintos escenarios o condiciones para observar
cómo cambian las variables de interés, evaluar decisiones alternativas y estimar resultados posibles antes
de aplicarlos en el mundo real.
    """)

    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
    st.subheader("Tabla de principios de modelación aplicados a 'Agua eficiente'")

    principios = [
        {
            "Principio": "Abstracción",
            "Explicación": "Reducir el sistema a sus elementos esenciales para facilitar el análisis.",
            "Ejemplo aplicado": "Modelar clima, suelo, cultivo y operación sin incluir detalles mecánicos del equipo de riego."
        },
        {
            "Principio": "Causalidad",
            "Explicación": "Las variables se relacionan mediante relaciones causa–efecto.",
            "Ejemplo aplicado": "Mayor temperatura → mayor ET0 → mayor demanda de riego."
        },
        {
            "Principio": "Escenarios",
            "Explicación": "Comparar configuraciones alternativas para evaluar decisiones.",
            "Ejemplo aplicado": "Simular riego tradicional, goteo y riego inteligente con sensores."
        },
        {
            "Principio": "Trazabilidad",
            "Explicación": "Cada resultado debe poder reconstruirse a partir de los datos y reglas utilizadas.",
            "Ejemplo aplicado": "Registrar lámina aplicada, estado del sistema y confiabilidad de sensores por parcela."
        },
        {
            "Principio": "Iteración",
            "Explicación": "El sistema evoluciona en el tiempo y depende de decisiones previas.",
            "Ejemplo aplicado": "Más riego hoy → mayor humedad mañana → menor necesidad de riego posterior."
        }
    ]

    st.table(pd.DataFrame(principios))

    # ---------------------------------------------------------
    # FASE 2: Identificación de elementos del sistema
    # ---------------------------------------------------------
    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
    st.header("Fase 2: Identificación de elementos del sistema")

    col_in, col_out, col_state = st.columns(3)

    with col_in:
        st.markdown("### Variables de entrada")
        st.markdown("""
        - Clima: `t_max`, `t_min`, `t_media`, `humedad_relativa`, `radiacion_solar`, `velocidad_viento`, `precipitacion`, `et0`.
        - Suelo: `textura_suelo`, `capacidad_campo`, `punto_marchitez`, `densidad_aparente`, `materia_organica`.
        - Cultivo: `cultivo_id`, `kc_inicial`, `kc_medio`, `kc_final`, `duracion_dias`.
        - Operación: `lamina_aplicada_mm`, `metodo_riego`, `caudal_lps`, `energia_kwh`.
        """)

    with col_out:
        st.markdown("### Variables de salida")
        st.markdown("""
        - Consumo de agua: suma de `lamina_aplicada_mm`.
        - Costo total: `costo_total`, `costo_por_mm`.
        - Eficiencia de riego: `eficiencia_riego`.
        - Riesgo de estrés hídrico: `riesgo_estres`.
        - Ahorro de agua: `ahorro_agua`.
        """)

    with col_state:
        st.markdown("### Variables de estado")
        st.markdown("""
        - Humedad del suelo: `humedad_volumetrica`.
        - Estado del sistema: `estado_sistema` (normal / degradado).
        - Confiabilidad de sensores: `confiabilidad_sensores`.
        """)

    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
    st.subheader("Justificación del modelado y la simulación")

    st.markdown("""
- El sistema de riego puede modelarse porque:
  - Tiene **entradas** medibles (clima, lámina aplicada, método de riego).
  - Presenta **estados internos** (humedad del suelo, confiabilidad de sensores).
  - Produce **salidas cuantificables** (consumo de agua, costos, eficiencia, riesgo de estrés).
  - Sus relaciones siguen patrones causales conocidos (FAO-56, balance hídrico, ET0).

- Decisiones que pueden optimizarse mediante simulación:
  - **Cuándo regar** (frecuencia y calendario).
  - **Cuánto regar** (lámina aplicada por evento).
  - **Con qué método** (gravedad, aspersión, goteo).
  - **Priorización de parcelas** bajo restricciones de agua y energía.
""")

    # ---------------------------------------------------------
    # MODELOS PREEXISTENTES (AGREGADO)
    # ---------------------------------------------------------
    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
    st.subheader("Modelos preexistentes que permiten analizar comportamientos y predecir efectos de cambios")

    st.markdown("""
Para fundamentar el análisis del sistema de riego y anticipar efectos de cambios en clima, suelo u operación,
el proyecto se apoya en modelos ampliamente validados en la literatura agronómica y de simulación:

### **1. Modelo FAO-56 (Evapotranspiración y balance hídrico)**
- Estima la demanda evaporativa (ET0) y el requerimiento hídrico del cultivo.
- Permite predecir cómo cambios en temperatura, radiación o viento afectan la necesidad de riego.
- Es el estándar internacional para programación de riego.

### **2. Modelo de balance hídrico del suelo**
- Simula la evolución de la humedad volumétrica.
- Permite anticipar estrés hídrico bajo distintos niveles de riego o precipitación.
- Es clave para evaluar escenarios de déficit o sobre riego.

### **3. Modelos de simulación de escenarios (What-if / Monte Carlo)**
- Permiten analizar efectos de cambios en:
  - método de riego,
  - frecuencia,
  - lámina aplicada,
  - disponibilidad de agua.
- Ayudan a comparar estrategias bajo condiciones climáticas contrastantes.

### **4. Modelos de aprendizaje automático (Random Forest)**
- Predicen la lámina recomendada a partir de múltiples variables.
- Capturan relaciones no lineales entre clima, suelo y operación.
- Permiten evaluar cómo cambios en una variable afectan la recomendación final.

En conjunto, estos modelos permiten analizar el comportamiento del sistema, anticipar efectos de cambios
y fundamentar decisiones de riego más eficientes y justificables.
    """)


    # ---------------------------------------------------------
    # FASE 3: Modelo conceptual
    # ---------------------------------------------------------
    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
    st.header("Fase 3: Modelo conceptual")

    st.markdown("""
**Relaciones principales entre variables:**

- Temperatura, radiación y viento → `et0` (demanda evaporativa).
- `et0` + coeficiente de cultivo (`kc`) → requerimiento hídrico del cultivo.
- Requerimiento hídrico − `precipitacion` → lámina de riego necesaria.
- Lámina aplicada (`lamina_aplicada_mm`) → cambio en `humedad_volumetrica`.
- `humedad_volumetrica` → `riesgo_estres` (si es baja, aumenta el riesgo).
- `lamina_aplicada_mm` + `costo_agua` + `costo_energia` → `costo_total`.
- `confiabilidad_sensores` y `calidad_dato` → estado del sistema (`estado_sistema`).

**Supuestos del modelo:**

- Los sensores están disponibles y operan con confiabilidad mínima aceptable.
- Las propiedades del suelo por parcela se mantienen constantes en el periodo analizado.
- El método de riego por parcela no cambia dentro de un escenario.
- Los datos climáticos representan adecuadamente las condiciones de la zona.

**Ciclo de retroalimentación (feedback):**

- Más riego → mayor `humedad_volumetrica` → menor `riesgo_estres` → menor necesidad de riego en el siguiente periodo.
- Menor riego → menor `humedad_volumetrica` → mayor `riesgo_estres` → incremento de lámina recomendada en el siguiente ciclo.
""")




    # ---------------------------------------------------------
    # DIAGRAMAS VISUALES DEL MODELO CONCEPTUAL
    # ---------------------------------------------------------
    st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
    st.subheader("Diagramas del modelo conceptual")

    # Diagrama causal
    st.markdown("### 🔵 Diagrama causal")
    st.image("diagrama_causal.png", caption="Diagrama causal del modelo conceptual", use_column_width=None)

    # Diagrama de flujo
    st.markdown("### 🟢 Diagrama de flujo del sistema de riego")
    st.image("diagrama_flujo.png", caption="Diagrama de flujo del sistema de riego", use_column_width=None)

    # Esquema de variables
    st.markdown("### 🟣 Esquema de variables del modelo conceptual")
    st.image("esquema_variables.png", caption="Esquema de variables del modelo conceptual", use_column_width=None)



# ---------------------------------------------------------
# SECCIÓN 3: FASE 4 - SIMULACIÓN DE ESCENARIOS
# ---------------------------------------------------------
elif seccion == "3. Fase 4: Simulación de escenarios":
    st.title("Fase 4: Simulación de escenarios de riego")

    if df.empty:
        st.warning("No hay datos cargados. Asegúrate de tener 'durango_riego_eficiente.csv' en la carpeta.")
    else:
        st.markdown("""
Vamos a aproximar tres escenarios usando el dataset:

1. **Escenario 1 – Riego tradicional:** registros con método de riego **gravedad**.  
2. **Escenario 2 – Riego por goteo:** registros con método de riego **goteo**.  
3. **Escenario 3 – Riego inteligente con sensores:** registros con cualquier método, pero con  
   `estado_sistema = "normal"` y `confiabilidad_sensores` ≥ 0.9 (alta confiabilidad).
""")

        # Normalizar texto de columnas clave
        df["metodo_riego"] = df["metodo_riego"].str.lower().str.strip()
        if "estado_sistema" in df.columns:
            df["estado_sistema"] = df["estado_sistema"].astype(str).str.lower().str.strip()

        # Escenarios
        esc1 = df[df["metodo_riego"] == "gravedad"].copy()
        esc2 = df[df["metodo_riego"] == "goteo"].copy()
        esc3 = df.copy()
        if "estado_sistema" in df.columns and "confiabilidad_sensores" in df.columns:
            esc3 = esc3[
                (esc3["estado_sistema"] == "normal") &
                (esc3["confiabilidad_sensores"] >= 0.9)
            ]

        def resumen_escenario(data: pd.DataFrame, nombre: str) -> dict:
            if data.empty:
                return {
                    "Escenario": nombre,
                    "Consumo_agua_mm": np.nan,
                    "Eficiencia_promedio": np.nan,
                    "Costo_total": np.nan,
                    "Costo_prom_mm": np.nan,
                    "Riesgo_estres_prom": np.nan
                }
            return {
                "Escenario": nombre,
                "Consumo_agua_mm": data["lamina_aplicada_mm"].sum(),
                "Eficiencia_promedio": data["eficiencia_riego"].mean(),
                "Costo_total": data["costo_total"].sum(),
                "Costo_prom_mm": (data["costo_por_mm"].mean()
                                  if "costo_por_mm" in data.columns else np.nan),
                "Riesgo_estres_prom": data["riesgo_estres"].mean()
            }

        resumen = pd.DataFrame([
            resumen_escenario(esc1, "Riego tradicional (gravedad)"),
            resumen_escenario(esc2, "Riego por goteo"),
            resumen_escenario(esc3, "Riego inteligente con sensores")
        ])

        st.subheader("Resumen comparativo de escenarios")
        st.dataframe(resumen.style.format({
            "Consumo_agua_mm": "{:,.0f}",
            "Eficiencia_promedio": "{:.2f}",
            "Costo_total": "{:,.0f}",
            "Costo_prom_mm": "{:.2f}",
            "Riesgo_estres_prom": "{:.2f}"
        }))

        st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
        st.subheader("Visualización: consumo de agua y costo total")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### Consumo de agua (mm)")
            st.bar_chart(
                data=resumen.set_index("Escenario")["Consumo_agua_mm"]
            )
        with col2:
            st.markdown("#### Costo total")
            st.bar_chart(
                data=resumen.set_index("Escenario")["Costo_total"]
            )

        st.markdown(
        "<hr style='border:.10px solid #FFFFFF; width:100%; margin:35px auto;'>",
        unsafe_allow_html=True
    )
        st.subheader("Análisis cualitativo sugerido")

        st.markdown("""
- **Consumo de agua:**  
  - Esperamos que el riego por goteo e inteligente muestren menor consumo total que el riego tradicional.
- **Eficiencia del sistema:**  
  - El escenario con sensores y estado normal debería mostrar mayor `eficiencia_riego`.
- **Impacto en producción (proxy):**  
  - Un menor `riesgo_estres_prom` sugiere menor probabilidad de pérdidas por estrés hídrico.
- **Costo por mm aplicado:**  
  - Un menor `Costo_prom_mm` indica mejor aprovechamiento del gasto en agua y energía.
""")

# ---------------------------------------------------------
# SECCIÓN 4: FASE 5 - INTEGRACIÓN AL DOCUMENTO
# ---------------------------------------------------------
elif seccion == "4. Fase 5: Integración al documento de investigación":
    st.title("Fase 5: Integración al documento de investigación")

    st.markdown("""
Esta sección consolida los elementos necesarios para integrar el **modelo y simulación del sistema de riego**
dentro del documento de investigación, siguiendo una estructura clara, profesional y alineada con los
criterios académicos del curso.

---

## 📘 **1. Descripción del sistema modelado**
El sistema de riego se concibe como un conjunto de procesos interrelacionados que transforman datos climáticos,
del suelo, del cultivo y de operación en decisiones óptimas de riego.  
Incluye:

- Entradas: clima, suelo, cultivo, operación.
- Procesos internos: cálculo de ET₀, requerimiento hídrico, balance hídrico, evaluación de estrés.
- Salidas: lámina recomendada, consumo, costo, eficiencia y riesgo.

---

## 🧩 **2. Principios de modelación aplicados**
El modelo se fundamenta en:

- **Modelación determinística** basada en FAO-56 para ET₀ y requerimiento hídrico.
- **Simulación de escenarios** para analizar variaciones climáticas y operativas.
- **Retroalimentación dinámica** entre humedad del suelo, estrés hídrico y necesidad de riego.
- **Supuestos estructurados** que delimitan el comportamiento del sistema.

---
""")

    # ---------------------------------------------------------
    # 3. MODELO CONCEPTUAL (IMÁGENES)
    # ---------------------------------------------------------
    st.markdown("## 🖼️ 3. Modelo conceptual (imagen o esquema)")
    st.markdown("A continuación se integran los diagramas generados:")

    # 🔵 Diagrama causal
    st.markdown("### 🔵 Diagrama causal")
    st.image("Diagrama_Causal1.png", width=900, caption="Diagrama causal del modelo conceptual")

    # 🟢 Diagrama de flujo
    st.markdown("### 🟢 Diagrama de flujo del sistema de riego")
    st.image("Diagrama.png", width=900, caption="Diagrama de flujo del sistema de riego")

    # 🟣 Esquema de variables
    st.markdown("### 🟣 Esquema de variables del modelo conceptual")
    st.image("Flujo.png", width=900, caption="Esquema de variables del modelo conceptual")

    # ---------------------------------------------------------
    # CONTINÚA FASE 5
    # ---------------------------------------------------------
    st.markdown("""
---

## 🌦️ **4. Descripción de escenarios simulados**
Los escenarios considerados permiten evaluar el comportamiento del sistema bajo condiciones contrastantes:

- **Escenario 1: Condiciones normales**  
  Clima promedio histórico, riego estándar por parcela.

- **Escenario 2: Sequía moderada**  
  Reducción del 20–30% en precipitación, incremento en ET₀, ajustes en lámina recomendada.

- **Escenario 3: Sequía extrema**  
  Reducción >50% en precipitación, ET₀ elevada, priorización de parcelas y riego deficitario controlado.

---

## 📊 **5. Resultados esperados**
Los resultados esperados del modelo incluyen:

- Variación en la **lámina recomendada** según clima y suelo.
- Cambios en la **humedad volumétrica** y riesgo de estrés.
- Diferencias en **consumo de agua** entre escenarios.
- Impacto en **costo total** y eficiencia del riego.
- Identificación de **puntos críticos** del sistema.

---

## ⚠️ **6. Limitaciones del modelo**
El modelo presenta las siguientes limitaciones:

- Dependencia de la calidad de datos climáticos y sensores.
- Suposición de homogeneidad en propiedades del suelo por parcela.
- No considera fallas operativas del sistema de riego.
- No incorpora variabilidad espacial avanzada (GIS).
- La simulación es diaria; no incluye dinámica horaria.

---
""")

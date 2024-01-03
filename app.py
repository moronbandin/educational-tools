import streamlit as st

from openai import OpenAI

# Título de la aplicación
st.title("Generador de Contenido Educativo con OpenAI")

# Descripción
st.write("""
Esta herramienta utiliza modelos avanzados de OpenAI para generar contenido educativo personalizado. 
Selecciona una materia, un curso y un tema, y elige entre generar un debate, un juego o preguntas de verdadero o falso.
""")

with st.sidebar:
    api_key = st.text_input("Introduce tu API Key de OpenAI", type="password")
    modelo_seleccionado = st.selectbox("Selecciona el modelo de OpenAI", ["gpt-3.5-turbo-1106", "gpt-4-1106-preview"])

    # Opciones predefinidas para la materia y el curso
    cursos = [
    "1º de Educación Primaria (6-7 años)",
    "2º de Educación Primaria (7-8 años)",
    "3º de Educación Primaria (8-9 años)",
    "4º de Educación Primaria (9-10 años)",
    "5º de Educación Primaria (10-11 años)",
    "6º de Educación Primaria (11-12 años)",
    "1º de Educación Secundaria Obligatoria (ESO) (12-13 años)",
    "2º de Educación Secundaria Obligatoria (ESO) (13-14 años)",
    "3º de Educación Secundaria Obligatoria (ESO) (14-15 años)",
    "4º de Educación Secundaria Obligatoria (ESO) (15-16 años)",
    "1º de Bachillerato (16-17 años)",
    "2º de Bachillerato (17-18 años)"
]
    materias = [
    "Biología",
    "Biología y Geología",
    "Ciencias Naturales",
    "Ciencias Sociales",
    "Competencia Digital",
    "Cultura Clásica",
    "Dibujo Técnico",
    "Educación Física",
    "Educación Plástica y Visual",
    "Filosofía",
    "Física",
    "Física y Química",
    "Geografía",
    "Griego",
    "Historia de España",
    "Historia del Arte",
    "Latín",
    "Lengua Castellana y Literatura",
    "Llengua Catalana i Literatura",
    "Lengua Francesa",
    "Lingua Galega e Literatura",
    "Lengua Inglesa",
    "Matemáticas",
    "Métodos Estadísticos y Numéricos",
    "Música y Danza",
    "Química",
    "Religión",
    "Tecnología y Digitalización"
]

    materia_seleccionada = st.selectbox("Selecciona la materia", materias)
    curso_seleccionado = st.selectbox("Selecciona el curso", cursos)
    tema = st.text_input("Introduce el tema")
    herramienta = st.selectbox("Elige la herramienta", ["Debate", "Verdadero o Falso", "Juego"])
    boton_generar = st.button("Generar")
    
    
# Función modificada para usar la API Key ingresada por el usuario
def get_openai_response(api_key, modelo_seleccionado, system_message, user_message):
    client = OpenAI(api_key=api_key)
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ],
        model=modelo_seleccionado,  # Usar el modelo seleccionado
        temperature=0
    )
    return chat_completion.choices[0].message.content

def debate(api_key, materia, curso, tema):
    debate_prompt = f"""Crea un debate educativo tipo Debate Tradicional para la materia de {materia} sobre el tema **{tema}**. Este debe ser adecuado para {curso}.

'''
#### Tema del Debate:
- **Tema**: [Tema del debate aquí]

#### Puntos Clave para el Equipo A Favor:
- Punto 1: [Argumento o idea aquí]
    - Argumentos:
- Punto 2: [Argumento o idea aquí]
    - Argumentos:
- Punto 3: [Argumento o idea aquí]
    - Argumentos:

#### Puntos Clave para el Equipo En Contra:
- Punto 1: [Argumento o idea aquí]
    - Argumentos:
- Punto 2: [Argumento o idea aquí]
    - Argumentos:
- Punto 3: [Argumento o idea aquí]
    - Argumentos:

#### Sugerencias de preguntas para la discusión posterior:
- Pregunta 1: [Pregunta aquí]
- Pregunta 2: [Pregunta aquí]
- Resto de preguntas: 
'''

Responde únicamente con la plantilla rellenada:
    """
    system_message = "Eres un generador de debates educativos. Respondes únicamente con la estructura del debate que se te pide."
    return get_openai_response(api_key, modelo_seleccionado, system_message, debate_prompt)

def game(api_key, materia, curso, tema):
    game_prompt = f"""Crea un juego educativo para la materia de {materia} sobre el tema **{tema}**. Este juego debe ser adecuado para {curso}.

'''
#### Título del Juego:
- **Juego**: [Título del juego aquí]

#### Objetivo del Juego:
- [Describir el objetivo del juego aquí]

#### Reglas del Juego:
- Regla 1: [Describir regla aquí]
- Regla 2: [Describir regla aquí]
- Regla 3: [Describir regla aquí]

#### Materiales Necesarios:
- Material 1: [Describir material aquí]
- Material 2: [Describir material aquí]
- Material 3: [Describir material aquí]

#### Procedimiento del Juego:
- Paso 1: [Describir paso aquí]
- Paso 2: [Describir paso aquí]
- Paso 3: [Describir paso aquí]

#### Preguntas y Respuestas para el Juego:
- Pregunta 1: [Pregunta aquí] - Respuesta: [Respuesta aquí]
- Pregunta 2: [Pregunta aquí] - Respuesta: [Respuesta aquí]
'''

Responde únicamente con la plantilla rellenada:"""
    system_message = "Eres un generador de juegos educativos. Crea un juego educativo siguiendo la estructura proporcionada."
    return get_openai_response(api_key, modelo_seleccionado, system_message, game_prompt)

def trueorfalse(api_key, materia, curso, tema):
    true_false_prompt = f"""Crea preguntas de verdadero o falso para la materia de {materia} sobre el tema **{tema}**. Este conjunto de preguntas debe ser adecuado para {curso}.

'''
#### Preguntas de Verdadero o Falso:
- Pregunta 1: [Escribe la pregunta aquí] - [**Verdadero**/Falso]
- Pregunta 2: [Escribe la pregunta aquí] - [Verdadero/**Falso**]
- Pregunta 3: [Escribe la pregunta aquí] - [**Verdadero**/Falso]
- Pregunta 4: [Escribe la pregunta aquí] - [Verdadero/**Falso**]
- Pregunta 5: [Escribe la pregunta aquí] - [**Verdadero**/Falso]
- Resto de preguntas:
'''

Responde únicamente con la plantilla rellenada y las opciones correctas marcadas en negrita:"""
    system_message = "Eres un generador de preguntas de verdadero o falso. Genera preguntas con las respuestas correctas marcadas en negrita."
    return get_openai_response(api_key, modelo_seleccionado, system_message, true_false_prompt)



# Mostrar el resultado en la segunda columna
if boton_generar:
    if herramienta == "Debate":
        resultado = debate(api_key, materia_seleccionada, curso_seleccionado, tema)
    elif herramienta == "Verdadero o Falso":
        resultado = trueorfalse(api_key, materia_seleccionada, curso_seleccionado, tema)
    elif herramienta == "Juego":
        resultado = game(api_key, materia_seleccionada, curso_seleccionado, tema)

    st.markdown(resultado, unsafe_allow_html=True)

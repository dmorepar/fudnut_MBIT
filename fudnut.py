import tensorflow as tf
from keras.models import load_model
import streamlit as st
from PIL import Image
import numpy as np

def get_food(max_predict):
        
    map_food = {
        0 : "Patatas fritas", 
        1 : "Arroz", 
        2 : "Yogur helado", 
        3 : "Pan", 
        4 : "Ensalada", 
        5 : "Guacamole", 
        6 : "Hamburguesa", 
        7 : "Hummus", 
        8 : "Helado", 
        9 : "Pizza", 
        10 : "Filete de ternera"
    }
        
    food = map_food.get(max_predict)
        
    return food

def get_info(): 
    informacion_nutricional = {
        "Patatas fritas": {"calorias": 312, "grasas": 15, "carbohidratos": 42, "proteinas": 3},
        "Arroz": {"calorias": 130, "grasas": 0.3, "carbohidratos": 28.7, "proteinas": 2.7},
        "Yogur helado": {"calorias": 140, "grasas": 4, "carbohidratos": 22, "proteinas": 4},
        "Pan": {"calorias": 270, "grasas": 3, "carbohidratos": 50, "proteinas": 9},
        "Ensalada": {"calorias": 20, "grasas": 0.5, "carbohidratos": 3, "proteinas": 1},
        "Guacamole": {"calorias": 150, "grasas": 15, "carbohidratos": 8, "proteinas": 2},
        "Hamburguesa": {"calorias": 350, "grasas": 20, "carbohidratos": 25, "proteinas": 18},
        "Hummus": {"calorias": 170, "grasas": 9, "carbohidratos": 15, "proteinas": 5},
        "Helado": {"calorias": 250, "grasas": 12, "carbohidratos": 30, "proteinas": 4},
        "Pizza": {"calorias": 300, "grasas": 15, "carbohidratos": 35, "proteinas": 12},
        "Filete de ternera": {"calorias": 250, "grasas": 15, "carbohidratos": 0, "proteinas": 25}
    }

    return informacion_nutricional


    
def load_model():
    filepath="fudnut_model.h5"
    model = tf.keras.models.load_model(filepath)
    return model

def preprocess_image(image):
    img = image.convert('RGB')  # Convertir a RGB si es necesario
    img = img.resize((224, 224))  # Redimensionar a tamaño de entrada del modelo
    img = np.array(img)  # Convertir a array numpy
    img = img / 255.0  # Normalizar los valores de píxeles
    img = np.expand_dims(img, axis=0)  # Agregar una dimensión adicional para el lote
    return img

# Configurar la página de la aplicación de Streamlit
st.title('FudNut App')
st.write('Realiza una foto al alimento')

# Permitir al usuario cargar una imagen
uploaded_file = st.file_uploader("Selecciona una imagen", type=['jpg', 'jpeg', 'png'])

if uploaded_file is not None:    
    # Mostrar la imagen cargada
    image = Image.open(uploaded_file)
    st.image(image, caption='Imagen cargada', use_column_width=True)

    processed_image = preprocess_image(image)

    model = load_model()

    prediction = model.predict(processed_image)

    max_predict = np.argmax(prediction)

    st.write('El alimento detectado es: ')

    food = get_food(max_predict)
    info_food = get_info()
    
    st.write(food)

    st.write("Calorías por 100g: ", info_food[food]["calorias"])
    st.write("Proteínas por 100g: ", info_food[food]["proteinas"])
    st.write("Grasas por 100g: ", info_food[food]["grasas"])
    st.write("Carbohidratos por 100g: ", info_food[food]["carbohidratos"])

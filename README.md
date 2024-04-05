En el siguiente repositorio se recoge el código desarrollado en el trabajo del Programa Experto en Inteligencia Artificial de MBIT.

En el notebook FudNutIA.ipynb se recoge todo el desarrollo del modelo, desde la descarga de datos, pasando por el entrenamiento del modelo y terminando con la visualización de resultados. Este código sería preferible ejecutar con la herramienta Google Colaboratory.

En el fichero env/env.txt se recogen las instrucciones para crear el entorno de desarrollo.

El notebook mlflow.ipynb debe ser ejecutado en local para levantar la interfaz de MLflow.

````
mlflow ui
````

El archivo fudnut.py ejecuta la aplicación con el modelo entrenado. Se debe descargar el modelo fudnut_model.h5 y ponerlo en el mismo directorio que el archivo .py. La aplicación se ejecuta con el siguiente comando, previa activación del entorno.

````
streamlit run fudnut.py
````

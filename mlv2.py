# -*- coding: utf-8 -*-
"""MLv2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yAEIMC-WJlJygYgQpVsHw-Q00rBP5f2Z
"""

import pandas as pd

url = "https://raw.githubusercontent.com/4GeeksAcademy/logistic-regression-project-tutorial/main/bank-marketing-campaign-data.csv"
df = pd.read_csv(url)

df = pd.read_csv(url, sep=';')

df.info()

df = pd.DataFrame(df)

# Contar las columnas por tipo
columnas_objeto = df.select_dtypes(include='object').columns
columnas_int64 = df.select_dtypes(include='int64').columns
columnas_float64 = df.select_dtypes(include='float64').columns

# Mostrar los resultados como lista
print(f'Columnas de tipo objeto ({len(columnas_objeto)}): {columnas_objeto.tolist()}')
print(f'Columnas de tipo int64 ({len(columnas_int64)}): {columnas_int64.tolist()}')
print(f'Columnas de tipo float64 ({len(columnas_float64)}): {columnas_float64.tolist()}')

df.shape

#Columnas nulas
print(df.isnull().sum())

# Verificar si hay valores nulos en el DataFrame
valores_nulos = df.isnull().sum()

# Mostrar los resultados
if valores_nulos.sum() == 0:
    print("No hay valores nulos en el conjunto de datos.")
else:
    print("Hay valores nulos. Aquí está la cuenta por columna:")
    print(valores_nulos)

#Valores duplicados
duplicates = df[df.duplicated()]

# Mostrar las filas duplicadas
print("Filas duplicadas:")
print(duplicates)

duplicates_count = df[df.duplicated(keep=False)].value_counts()

# Mostrar el conteo de duplicados
print("Conteo de valores duplicados:")
print(duplicates_count)

df.drop_duplicates(inplace=True)
print("after")
df.shape

#Eliminación de variables no necesarias para el análisis
df.drop(["contact", "month", "day_of_week", "pdays", "previous", "nr.employed"], axis = 1, inplace = True)

df.info()

#Graphic visualization about categorical variables
import matplotlib.pyplot as plt
import seaborn as sns

# Crear un objeto figura y ejes con subgráficos 2x4
fig, axes = plt.subplots(2, 4, figsize=(20, 10))

# Crear histogramas para cada variable
sns.histplot(data=df, x="age", ax=axes[0, 0]).set_xlim(0, 99)
sns.countplot(data=df, x="job", ax=axes[0, 1]).set(ylabel=None)
sns.countplot(data=df, x="marital", ax=axes[0, 2]).set(ylabel=None)
sns.countplot(data=df, x="education", ax=axes[0, 3]).set(ylabel=None)
sns.countplot(data=df, x="default", ax=axes[1, 0]).set(ylabel=None)
sns.countplot(data=df, x="housing", ax=axes[1, 1]).set(ylabel=None)

# Añadir las variables 'loan' y 'poutcome'
sns.countplot(data=df, x="loan", ax=axes[1, 2]).set(ylabel=None)
sns.countplot(data=df, x="poutcome", ax=axes[1, 3]).set(ylabel=None)

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()

#Graphic visualization about numerical variables
# Crear un objeto figura y ejes con subgráficos 4x4
fig, axes = plt.subplots(4, 4, figsize=(10, 7))

# Crear histogramas y boxplots para las variables numéricas
sns.histplot(ax=axes[0, 0], data=df, x="age").set(xlabel=None)
sns.boxplot(ax=axes[1, 0], data=df, x="age")
sns.histplot(ax=axes[0, 1], data=df, x="campaign").set(xlabel=None, ylabel=None)
sns.boxplot(ax=axes[1, 1], data=df, x="campaign")
sns.histplot(ax=axes[0, 2], data=df, x="emp.var.rate").set(xlabel=None, ylabel=None)
sns.boxplot(ax=axes[1, 2], data=df, x="emp.var.rate")
sns.histplot(ax=axes[0, 3], data=df, x="cons.price.idx").set(xlabel=None)
sns.boxplot(ax=axes[1, 3], data=df, x="cons.price.idx")

sns.histplot(ax=axes[2, 0], data=df, x="cons.conf.idx").set(xlabel=None, ylabel=None)
sns.boxplot(ax=axes[3, 0], data=df, x="cons.conf.idx")
sns.histplot(ax=axes[2, 1], data=df, x="euribor3m").set(xlabel=None, ylabel=None)
sns.boxplot(ax=axes[3, 1], data=df, x="euribor3m")
sns.histplot(ax=axes[2, 2], data=df, x="duration").set(xlabel=None, ylabel=None)
sns.boxplot(ax=axes[3, 2], data=df, x="duration")

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()

#MultiVariables Graphic visualization
fig, axis = plt.subplots(2, 2, figsize=(10, 7))

# Crear un diagrama de dispersión
sns.regplot(ax=axis[0, 0], data=df, x="age", y="campaign")
sns.heatmap(df[["age", "campaign"]].corr(), annot=True, fmt=".2f", ax=axis[1, 0], cbar=False)

# Puedes reemplazar "emp.var.rate" y "cons.price.idx" con las variables de interés
sns.regplot(ax=axis[0, 1], data=df, x="emp.var.rate", y="cons.price.idx").set(ylabel=None)
sns.heatmap(df[["emp.var.rate", "cons.price.idx"]].corr(), annot=True, fmt=".2f", ax=axis[1, 1])

# Ajustar el diseño
plt.tight_layout()

# Mostrar el gráfico
plt.show()

# Análisis de la clase máster ("y") frente a las características categóricas
fig, axis = plt.subplots(3, 2, figsize=(15, 10))

sns.countplot(ax=axis[0, 0], data=df, x="job", hue="y")
sns.countplot(ax=axis[0, 1], data=df, x="marital", hue="y").set(ylabel=None)
sns.countplot(ax=axis[1, 0], data=df, x="education", hue="y").set(ylabel=None)
sns.countplot(ax=axis[1, 1], data=df, x="default", hue="y").set(ylabel=None)
sns.countplot(ax=axis[2, 0], data=df, x="housing", hue="y")
sns.countplot(ax=axis[2, 1], data=df, x="loan", hue="y").set(ylabel=None)
#falta poutcome

plt.tight_layout()

plt.show()

fig, axis = plt.subplots(figsize=(10, 5), ncols=2)

# Primer gráfico
sns.barplot(ax=axis[0], data=df, x="age", y="job", hue="y", orient="h")
axis[0].set(title="Barplot 1")

# Segundo gráfico
sns.barplot(ax=axis[1], data=df, x="emp.var.rate", y="cons.conf.idx", hue="y", orient="h")
axis[1].set(title="Barplot 2", ylabel=None)

plt.tight_layout()
plt.show()

#Correlation Analysis
# aplicar la codificación de etiquetas (Label Encoding) a las variables categóricas para convertir cadenas de texto (String) a flotantes directamente
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Copia del DataFrame original
df_encoded = df.copy()

# Codificar variables categóricas usando Label Encoding
for col in ["job", "marital", "education", "default", "housing", "loan", "poutcome"]:
    df_encoded[col] = pd.factorize(df[col])[0]

# Convertir "y" a valores numéricos (aunque ya parece estar binarizado)
df_encoded["y"] = pd.factorize(df["y"])[0]

# Crear el gráfico de correlación
fig, axis = plt.subplots(figsize=(10, 6))
sns.heatmap(df_encoded[["job", "marital", "education", "default", "housing", "loan", "poutcome", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m"]].corr(), annot=True, fmt=".2f")
plt.tight_layout()
plt.show()

'''Interpretación de la correlación:

✅age vs. emp.var.rate: La correlación es aproximadamente -0.15. Indica una correlación negativa débil entre la edad y la tasa de variación del empleo. Esto podría sugerir que las personas más jóvenes tienden a experimentar mayores variaciones en las tasas de empleo.

✅age vs. euribor3m: La correlación es aproximadamente -0.16. Indica una correlación negativa débil entre la edad y la tasa Euribor a 3 meses. Puede significar que las personas más jóvenes podrían tener tasas Euribor más altas.

✅emp.var.rate vs. euribor3m: La correlación es alta y positiva, alrededor de 0.97. Esto es esperado, ya que la tasa de variación del empleo (emp.var.rate) y la tasa Euribor a 3 meses (euribor3m) están relacionadas en el contexto económico.

✅emp.var.rate vs. y: La correlación es aproximadamente -0.30. Indica una correlación moderadamente negativa entre la tasa de variación del empleo y la variable objetivo "y". Esto sugiere que a medida que la tasa de variación del empleo disminuye, es más probable que la variable objetivo "y" sea positiva (indicando la realización de un depósito a largo plazo).

✅euribor3m vs. y: La correlación es aproximadamente -0.31. Similar a la correlación anterior, sugiere que a medida que la tasa Euribor a 3 meses disminuye, es más probable que la variable objetivo "y" sea positiva.'''

sns.pairplot(data = df)

#Feature Engeneering
#outliers
df.describe()

#pintamos los boxplots
fig, axis = plt.subplots(3, 3, figsize = (15, 10))

sns.boxplot(ax = axis[0, 0], data = df, y = "y")
sns.boxplot(ax = axis[0, 1], data = df, y = "age")
sns.boxplot(ax = axis[0, 2], data = df, y = "campaign")
sns.boxplot(ax = axis[1, 0], data = df, y = "emp.var.rate")
sns.boxplot(ax = axis[1, 1], data = df, y = "cons.price.idx")
sns.boxplot(ax = axis[1, 2], data = df, y = "cons.conf.idx")
sns.boxplot(ax = axis[2, 0], data = df, y = "euribor3m")

plt.tight_layout()

plt.show()

# Variables de interés
variables_interes = ["y", "age", "campaign", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m"]

# Obtener estadísticas descriptivas para cada variable
for variable in variables_interes:
    variable_stats = df[variable].describe()
    print(f"\nEstadísticas descriptivas para {variable}:\n{variable_stats}")

# Variables de interés
variables_interes = ["y", "campaign", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m"]

# Calcular límites superior e inferior para la búsqueda de outliers para cada variable
for variable in variables_interes:
    variable_stats = df[variable].describe()

    iqr = variable_stats["75%"] - variable_stats["25%"]
    upper_limit = variable_stats["75%"] + 1.5 * iqr
    lower_limit = variable_stats["25%"] - 1.5 * iqr

    print(f"\nLímites superior e inferior para la búsqueda de outliers de {variable}:")
    print(f"Superior: {round(upper_limit, 2)}, Inferior: {round(lower_limit, 2)}, Rango intercuartílico: {round(iqr, 2)}")

#Eliminar valores atipicos

df.shape

import pandas as pd

# Crear una copia de seguridad del DataFrame original
df_backup = df.copy()

# Variables de interés
variables_interes = ["y", "campaign", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m"]

# Calcular límites superior e inferior para la búsqueda de outliers para cada variable
for variable in variables_interes:
    variable_stats = df[variable].describe()

    iqr = variable_stats["75%"] - variable_stats["25%"]
    upper_limit = variable_stats["75%"] + 1.5 * iqr
    lower_limit = variable_stats["25%"] - 1.5 * iqr

    # Eliminar outliers y actualizar el DataFrame original
    df = df[(df[variable] >= lower_limit) & (df[variable] <= upper_limit)]

    print(f"\nLímites superior e inferior para la búsqueda de outliers de {variable}:")
    print(f"Superior: {round(upper_limit, 2)}, Inferior: {round(lower_limit, 2)}, Rango intercuartílico: {round(iqr, 2)}")

# Mostrar información sobre la eliminación de outliers
print("\nNúmero de filas antes de eliminar outliers:", len(df_backup))
print("Número de filas después de eliminar outliers:", len(df))

df.shape

#Normalización 👉 La normalización se refiere a cambiar la escala de los atributos numéricos de valor real a un rango de 0 a 1. La normalización de datos se usa en el aprendizaje automático para hacer que el entrenamiento de modelos sea menos sensible a la escala de características. Esto permite que nuestro modelo converja a mejores pesos y, a su vez, conduce a un modelo más preciso.
#Si tras la normalización obtenemos valores negativos debemos usar Escalado Mínimo-Máximo
'''from sklearn.preprocessing import StandardScaler
import pandas as pd

num_variables = ["age", "campaign", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m"]

scaler = StandardScaler()
norm_features = scaler.fit_transform(df[num_variables])
df_norm = pd.DataFrame(norm_features, index=df.index, columns=num_variables)
df_norm["y"] = df["y"]  # Variable objetivo
df_norm.head()'''

#Escalado Minimo-Máximo 👉 El escalado mínimo funciona restando el valor mínimo de cada punto de datos y dividiéndolo por el rango de valores. Esto garantiza que el valor mínimo se transforme en 0 y el valor máximo se transforme en 1, con todos los demás valores escalados proporcionalmente en el medio.

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Variables numéricas de interés
num_variables = ["age", "campaign", "emp.var.rate", "cons.price.idx", "cons.conf.idx", "euribor3m"]

# Crear una instancia de MinMaxScaler
scaler = MinMaxScaler()

# Escalar las variables numéricas y crear un nuevo DataFrame
scaled_features = scaler.fit_transform(df[num_variables])
df_scaled = pd.DataFrame(scaled_features, index=df.index, columns=num_variables)

# Agregar la variable objetivo al DataFrame escalado
df_scaled["y"] = df["y"]

# Mostrar las primeras filas del DataFrame escalado
print(df_scaled.head())

#Feature Selection
from sklearn.feature_selection import chi2, SelectKBest
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder


# Encode categorical variables
le = LabelEncoder()
df_encoded = df.apply(lambda x: le.fit_transform(x) if x.dtype == 'O' else x)

# Divide the dataset into training and test samples.
X = df_encoded.drop("y", axis=1)
y = df_encoded["y"]

# Scale the features to [0, 1] range
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Use random_state to ensure reproducibility
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# With a value of k = 5, we implicitly mean that we want to remove 2 features from the dataset
selection_model = SelectKBest(chi2, k=5)
selection_model.fit(X_train, y_train)

# Get the indices of the selected features
ix = selection_model.get_support()

# Extract the selected features for both training and test sets
X_train_sel = pd.DataFrame(selection_model.transform(X_train), columns=X.columns.values[ix])
X_test_sel = pd.DataFrame(selection_model.transform(X_test), columns=X.columns.values[ix])

# Display the selected features
print(X_train_sel.head())

#heads
X_test_sel.head()

#splitting
X_train_sel["y"] = list(y_train)
X_test_sel["y"] = list(y_test)

X_train_sel.to_csv("clean-bank-marketing-campaign-data.train.csv", index=False)
X_test_sel.to_csv("clean-bank-marketing-campaign-data.test.csv", index=False)

# Guardar los DataFrames en archivos CSV
X_train_sel.to_csv("clean-bank-marketing-campaign-data.train.csv", index=False)
X_test_sel.to_csv("clean-bank-marketing-campaign-data.test.csv", index=False)

#Regression Logistic Model Building
#Import data
import pandas as pd
train_data = pd.read_csv("clean-bank-marketing-campaign-data.train.csv")
test_data = pd.read_csv("clean-bank-marketing-campaign-data.test.csv")
train_data.head()

#Optimización del modelo

#Paso 1 división de variables predictoras según modelos de testeo y modelo de entrenamiento (Hecho arriba)
'''X_train = train_data.drop(["y"], axis = 1)
y_train = train_data["y"]
X_test = test_data.drop(["y"], axis = 1)
y_test = test_data["y"]'''

#Paso 2: Inicialización y entrenamiento del modelo
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Inicializar el modelo de regresión logística
model = LogisticRegression(random_state=42)

# Entrenar el modelo con las características seleccionadas
model.fit(X_train_sel, y_train)

# Predecir en el conjunto de prueba
y_pred = model.predict(X_test_sel)

# Evaluar el rendimiento del modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy del modelo en el conjunto de prueba: {accuracy:.2f}")

# Mostrar el informe de clasificación
print("\nInforme de clasificación:")
print(classification_report(y_test, y_pred))

# Hacer predicciones en el conjunto de prueba original (sin selección de características)
# Aplicar la misma selección de características al conjunto de prueba original
X_test_sel_original = pd.DataFrame(selection_model.transform(X_test), columns=X.columns.values[ix])

# Hacer predicciones en el conjunto de prueba original (con selección de características)
y_pred_original = model.predict(X_test_sel_original)

# Mostrar las predicciones
print("\nPredicciones en el conjunto de prueba original:")
print(y_pred_original)

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)

#Confusion Matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# Calcular la matriz de confusión
conf_matrix = confusion_matrix(y_test, y_pred_original)

# Crear un DataFrame de la matriz de confusión para su visualización
conf_matrix_df = pd.DataFrame(conf_matrix, index=['Actual No', 'Actual Yes'], columns=['Predicted No', 'Predicted Yes'])

# Visualizar la matriz de confusión con seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_df, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

#Interpretación de la matriz de confusion
#✅Verdaderos positivos (TP, True positive): Se corresponde con el número 7125 y son los casos en los que el modelo predijo positivo (no supervivencia) y la clase real también es positiva
#✅Verdaderos negativos (TN, False negative): Se corresponde con el número 250 y son los casos en los que el modelo predijo negativo (supervivencia) y la clase real también es negativa
#⛔Falsos positivos (FP, False positive): Se corresponde con el número 721 y son los casos en los que el modelo predijo positivo y la clase real es negativa.
#⛔Falsos negativos (FN, False negative): Se corresponde con el número 140 y son los casos en los que el modelo predijo negativo y la clase real es positiva. Estas cuatro medidas se utilizan a menudo para calcular métricas más complejas

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Calcular la matriz de confusión
cm = confusion_matrix(y_test, y_pred)

# Descomponer la matriz de confusión en variables
tp, fn, fp, tn = cm.ravel()

# Etiquetas y valores para el gráfico
labels = ['Verdaderos positivos', 'Falsos negativos', 'Falsos positivos', 'Verdaderos negativos']
values = [tp, fn, fp, tn]

# Crear un gráfico de barras con la paleta asignada a la variable de matiz (hue)
plt.figure(figsize=(8, 6))
sns.barplot(x=labels, y=values, hue=labels, palette='viridis', legend=False)

# Añadir etiquetas y título
plt.title('Métricas de la Matriz de Confusión')
plt.xlabel('Métricas')
plt.ylabel('Cantidad')

# Mostrar los valores en las barras
for i, value in enumerate(values):
    plt.text(i, value + 0.1, str(value), ha='center', va='bottom')

# Mostrar el gráfico
plt.show()

#Optimización de hiperparámetros de modelo
#Automático

from sklearn.svm import SVC  # Ejemplo con el clasificador SVM (Support Vector Machine)

# Crear una instancia del clasificador
clf = SVC()

# Obtener los hiperparámetros del clasificador
hyperparams = clf.get_params()

# Mostrar los hiperparámetros
print(hyperparams)

#Optimizacion del modelo con GridSearch encontrando los mejores hiperparámetros
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

# Paso 1: Definir y crear el modelo
model = LogisticRegression()

# Paso 2: Configurar la búsqueda de cuadrícula
hyperparams = {
    'C': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
    'penalty': ['l1', 'l2', 'elasticnet', 'none'],
    'solver': ['newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'],
    'max_iter': [100, 500, 1000],
    'class_weight': [None, 'balanced'],
    'random_state': [None, 42],
}

grid = GridSearchCV(model, hyperparams, scoring="accuracy", cv=5)

# Paso 3: Ajustar la cuadrícula con tus datos de entrenamiento
grid.fit(X_train, y_train)  # Asegúrate de tener X_train e y_train definidos

# Paso 4: Acceder a los resultados
best_model = grid.best_estimator_
best_params = grid.best_params_
best_score = grid.best_score_

# Puedes imprimir o utilizar los resultados como desees
#print("Mejor modelo:", best_model)
print("Mejores hiperparámetros:", best_params)
#print("Mejor puntuación:", best_score)

#Mejora Manual -> Con los mejores hiper parametros que nos devuelva la anterior query hacemos el ajuste manual
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Mejores hiperparámetros: {'C': 1, 'class_weight': None, 'max_iter': 100, 'penalty': 'l1', 'random_state': None, 'solver': 'saga'}

# Divide el conjunto de datos en conjuntos de entrenamiento y prueba con random_state
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Crea y entrena el modelo con parámetros corregidos y random_state
model_manual = LogisticRegression(penalty='l1', C=1, solver='saga', random_state=None, class_weight=None, max_iter=100)  # 'None' como cadena en class_weight
model_manual.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred_manual = model_manual.predict(X_test)

# Calcula la precisión
manual_accuracy = accuracy_score(y_test, y_pred_manual)
print("Precisión del modelo (ajuste manual):", manual_accuracy)

# Valores originales
original_valor = 0.8954589606605148
nuevo_valor = 0.9040796503156873

# Calcular la mejora porcentual
mejora_porcentaje = ((nuevo_valor - original_valor) / original_valor) * 100

print("Mejora porcentual:", mejora_porcentaje)

import matplotlib.pyplot as plt

# Valores originales
original_valor = 0.8954589606605148
nuevo_valor = 0.9040796503156873

# Calcular la mejora porcentual
mejora_porcentaje = ((nuevo_valor - original_valor) / original_valor) * 100

# Crear un gráfico de barras verticales para representar original y mejora
etiquetas = ['Original', 'Mejora']
valores = [original_valor, nuevo_valor]
colores = ['blue', 'green']

plt.bar(etiquetas, valores, color=colores)
plt.ylabel('Valores')
plt.title('Comparación de Valores con Mejora Porcentual')

# Mostrar el porcentaje de mejora en la parte superior de la barra de mejora
plt.text(1, nuevo_valor + 0.0005, f'+{mejora_porcentaje:.2f}%', ha='center', va='bottom', color='black', fontsize=10)

plt.show()

#Guardar modelo tras reajuste manual
import pickle

# Guardar el modelo en un archivo con pickle
with open('modelo_manual.pkl', 'wb') as file:
    pickle.dump(model_manual, file)

#Recuperar modelo
'''# Cargar el modelo desde el archivo con pickle
with open('modelo_manual.pkl', 'rb') as file:
    loaded_model_manual = pickle.load(file)'''

#Mejora Aleatoria
import numpy as np
from sklearn.model_selection import RandomizedSearchCV
from sklearn.linear_model import LogisticRegression  # Debes importar el modelo específico que estás utilizando

# Supongamos que ya has definido y creado una instancia del modelo
model = LogisticRegression()

# Definimos los parámetros que queremos ajustar
hyperparams = {
    "C": np.logspace(-4, 4, 20),
    "penalty": ["l2", "elasticnet", None],  # Excluimos 'l1' para el solver 'sag'
    "solver": ["newton-cg", "lbfgs", "liblinear", "sag", "saga"]
}

# Inicializamos la búsqueda aleatoria
random_search = RandomizedSearchCV(model, hyperparams, n_iter=100, scoring="accuracy", cv=5, random_state=42)

# Ajustamos el modelo utilizando la búsqueda aleatoria
random_search.fit(X_train, y_train)  # Asegúrate de tener X_train e y_train definidos

# Mostramos los resultados de la búsqueda aleatoria
print("Mejores hiperparámetros encontrados:")
print(random_search.best_params_)
print("Mejor puntuación de validación cruzada:")
print(random_search.best_score_)

# Valores originales
original_valor = 0.8954589606605148
nuevo_valor = 0.9116575591985429

# Calcular la mejora porcentual
mejora_porcentaje = ((nuevo_valor - original_valor) / original_valor) * 100

print("Mejora porcentual:", mejora_porcentaje)

import matplotlib.pyplot as plt

# Valores originales
original_valor = 0.8954589606605148
nuevo_valor = 0.9116575591985429

# Calcular la mejora porcentual
mejora_porcentaje = ((nuevo_valor - original_valor) / original_valor) * 100

# Crear un gráfico de barras con colores diferentes para original y mejora
etiquetas = ['Original']
valores = [original_valor]
colores = ['blue']

plt.bar(etiquetas, valores, color=colores, label='Original')
plt.bar('Mejora', nuevo_valor, color='green', label=f'Mejora\n+{mejora_porcentaje:.2f}%')

plt.ylabel('Valores')
plt.title('Comparación de Valores con Mejora Porcentual')
plt.legend()

plt.show()

#Reentrenamiento del modelo con mejora aleatoria
model_random_search = LogisticRegression(penalty = "l2", C = 29.7635, solver = "lbfgs")
model_random_search.fit(X_train, y_train)
y_pred = model_random_search.predict(X_test)

random_search_accuracy = accuracy_score(y_test, y_pred)
random_search_accuracy

#Guardar modelo
import pickle

# Guardar el modelo en un archivo
with open('modelo_entrenado_mejora_aleatoria.pkl', 'wb') as file:
    pickle.dump(random_search, file)

# Puedes cambiar 'modelo_entrenado.pkl' por el nombre que desees para el archivo.

#Recuperar modelo
'''import pickle

# Cargar el modelo desde el archivo
with open('modelo_entrenado_mejora_aleatoria.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Ahora 'loaded_model' contiene tu modelo cargado y puedes usarlo para hacer predicciones'''
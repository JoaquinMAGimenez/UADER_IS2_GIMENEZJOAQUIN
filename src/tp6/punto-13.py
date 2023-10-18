import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Datos proporcionados
dias = np.array([0, 1, 2, 3, 4, 5, 6])
defectos = np.array([9, 18, 5, 7, 23, 2, 8])

# Crear una instancia del modelo de regresión polinómica
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(dias.reshape(-1, 1))

# Ajustar el modelo de regresión polinómica a los datos
model = LinearRegression()
model.fit(X_poly, defectos)

# Predecir el número total de defectos para un día dado (por ejemplo, día 7)
dia_prediccion = 7
defectos_predichos = model.predict(poly.transform(np.array([[dia_prediccion]])))

print(f"El número estimado de defectos en el día {dia_prediccion} es aproximadamente {int(defectos_predichos[0])}.")

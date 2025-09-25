
# Practica del Metodo simbolico

## Instalacion
Intalamos las librerias necesarias para la practica 

<img width="675" height="142" alt="image" src="https://github.com/user-attachments/assets/57c0a391-650b-4ae1-9e48-ec76ab9c55b6" />

### Importamos las librerias al proyecto estas librerías permiten:
<ul>
 <li> -load_wine → cargar la base de datos del vino. </li>
 <li>-DecisionTreeClassifier → crear el clasificador basado en reglas. </li>
 <li> -export_text → visualizar las reglas aprendidas. </li>
  <li> -train_test_split → dividir los datos en entrenamiento y prueba. </li>
</ul>
<img width="675" height="142" alt="image" src="https://github.com/user-attachments/assets/b6c11f76-3f9d-4792-8eaa-b3e47f2f1982" />

### Cargar el dataset del vino:
<ul>
<li> wine = load_wine() </li>
<li> x, y = wine.data, wine.target </li>
</ul>
### Donde:
 "x" contiene las características químicas del vino (ej. alcohol, ácido málico, flavonoides, etc.) 
"y" contiene la clase del vino (0, 1 o 2, que corresponden a 3 tipos de vino). 







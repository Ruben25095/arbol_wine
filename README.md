
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

<img width="582" height="64" alt="image" src="https://github.com/user-attachments/assets/e13849aa-d59f-48de-9b91-0869ad54be2d" />

### Dividir los datos en entrenamiento y prueba
<ul>
<li> 80% de los datos se usan para entrenar.</li>
<li> 20% se reservan para probar la precisión.</li>

</ul>
<img width="784" height="57" alt="image" src="https://github.com/user-attachments/assets/19a6416d-f1af-4021-9122-4c275ea08baf" />

### Crear y entrenar el clasificador
<ul> <li></li> max_depth=2 limita la profundidad del árbol para que las reglas sean más fáciles de interpretar. </li> </ul>

<img width="536" height="61" alt="image" src="https://github.com/user-attachments/assets/88ce8626-4b25-4f0a-98ad-3a2d0c33c36b" />

### Exportar y visualizar las reglas simbólicas

<img width="635" height="93" alt="image" src="https://github.com/user-attachments/assets/357f8530-cf4f-49ac-834d-043e05de563a" />


### Resultado
<img width="783" height="292" alt="image" src="https://github.com/user-attachments/assets/8c5726ad-1b51-4dd0-a342-1d232578d8ed" />


## Actividades
### Cambia el parámetro max_depth de DecisionTreeClassifier y observa cómo cambian las reglas del árbol.

 <img width="728" height="230" alt="image" src="https://github.com/user-attachments/assets/de680145-bf95-47dd-96ce-5b0db3d6aa87" />


### Prueba a entrenar el modelo sin limitar la profundidad (max_depth=None). ¿Qué notas en las reglas?


<img width="785" height="526" alt="image" src="https://github.com/user-attachments/assets/fb813166-240e-4696-9117-93076aa3d858" />


### Evalúa la precisión del modelo en los datos de prueba:
print("Precisión en datos de prueba:", tree.score(X_test, y_test))
Cuales son tus opiniones de los resultados.

<img width="727" height="104" alt="image" src="https://github.com/user-attachments/assets/739f39c5-2bce-4bc7-b01f-bad75811e976" />

<img width="727" height="104" alt="image" src="https://github.com/user-attachments/assets/9dc85d00-ac4a-442b-9348-1b3d1bce7384" />

<img width="729" height="113" alt="image" src="https://github.com/user-attachments/assets/0c11997d-d959-45e4-8169-f534b4c2bd67" />














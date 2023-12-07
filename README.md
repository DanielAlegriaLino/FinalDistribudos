[![Django CI](https://github.com/DanielAlegriaLino/FinalDistribudos/actions/workflows/django.yml/badge.svg)](https://github.com/DanielAlegriaLino/FinalDistribudos/actions/workflows/django.yml)

# Sigma IDE

###### Editor de codigo Javascript facil, online para snippets cortos pero complejos

## Tabla de Contenidos

- [Instalación](#instalación)
- [Uso](#uso)



## Instalación
Para el uso de este proyecto, se requiere que se realizen las siguientes acciones previas.
1. Instalacion de los **requirements.txt** por medio del comando 
`pip install -r requirements.txt`
2. Creacion de un archivo **.env** donde se contenga tu clave de API OpenAI en el siguiente formato: 
`OPENAI_API_KEY= "NbB234hb4BHB.........423k4fNnk"`
3. En la carpeta /LectorEditor ejecutar el comando `python admin.py runserver`
4. Abrir en el navegador el proyecto corriendo, normalmente es el servidor **127.0.0.1:8000/**

## Uso
* Se puede **iniciar sesion, registrarse** para poder tener un historial de tus codigos, en caso de no requerir esta funcion se puede **Acceder como invitado**
* El editor de codigo nos permite ejecutar pequeños snippets de  codigo javascript, siempre y cuando este posea un return de algun valor. Por ejemplo:
```javascript
arr = [1,2,3,4,5,6,7];  
suma = 0;  
for(i = 0; i< arr.length; i++){  
    suma = suma + arr[i];
}
return suma```

* Si se quiere revisar la salida del codigo y ademas ver el feedback de la IA se presiona el boton de play.
* En el historial de codigo se puede observar los codigos hechos con anterioridad, ademas de poder abrirlos y analizarlos.

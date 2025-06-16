El objetivo de este trabajo es comprender cómo se aplican los estándares de interoperabilidad (en particular, FHIR) en sistemas de salud, con foco en la Red Nacional de Salud Digital de Argentina.

# Actividad 1- Creación de un recurso Patient con HAPI FHIR
Se accedió al servidor de prueba HAPI FHIR (versión R4) a través del sitio oficial:
https://hapi.fhir.org/baseR4.

Luego, seleccionamos el recurso Patient y utilizamos la opción POST para crear un nuevo paciente. Enviamos el siguiente JSON:
    {
    "resourceType": "Patient",
    "name": [
      {
        "use": "official",
        "family": "Scalise",
        "given": ["Zarina"]
      }
    ],
    "gender": "female",
    "birthDate": "2000-01-01"
  }

El servidor respondió con HTTP 201 Created, lo que indica que el recurso fue creado correctamente. La URL generada fue:
https://hapi.fhir.org/baseR4/Patient/47884498/_history/1

El recurso creado incluye los siguientes atributos:
- resourceType: Especifica que se trata de un recurso de tipo Patient.
- id: Identificador único del recurso (47884498).
- name: Contiene el nombre del paciente, con nombre "Zarina" y apellido "Scalise".
- gender: Género declarado como female.
- birthDate: Fecha de nacimiento 2000-01-01.

Se adjuntan capturas de pantalla del procedimiento realizado:
![capturas](./CAPTURAS/Ejercicio1PT1.png)
*Figura 1: Actividad 1*

![capturas](./CAPTURAS/Ejercicio1PT3.png)
*Figura 2: Actividad 1*

![capturas](./CAPTURAS/Ejercicio1PT4.png)
*Figura 3: Actividad 1*


# Actividad 2 - Postman
Se utilizó la herramienta Postman, que permite probar la comunicación entre sistemas a través de solicitudes HTTP. Ahí se envió manualmente el mismo formulario JSON con los datos del paciente al mismo servidor que la actividad anterior. Después de hacer el POST, se recibió una respuesta con el código **201 Created**, lo que confirma que el recurso fue almacenado correctamente.

![capturas](./CAPTURAS/Ejercicio2PT1.png)
*Figura 1: Actividad 2*
![capturas](./CAPTURAS/Ejercicio2PT2.png)
*Figura 2: Actividad 2*
![capturas](./CAPTURAS/Ejercicio2PT3.png)
*Figura 3: Actividad 2*
![capturas](./CAPTURAS/Ejercicio2PT4.png)
*Figura 4: Actividad 2*

Luego se verificó la existencia mediante una solicitud GET, a la cual el sistema respondió con un **200 OK**, confirmando lo realizado.
![capturas](./CAPTURAS/Ejercicio2PT5.png)
*Figura 5: Actividad 2*


# Actividad 3
En esta actividad se trabajó con el estándar FHIR utilizando Python, implementando recursos clínicos, enviándolos al servidor HAPI FHIR y estableciendo relaciones entre ellos. La actividad se dividió en tres partes:

## 3a. Crear un recurso patient y enviarlos al servidor
Se implementó en Python una función utilizando la libreria ***fhir.resources*** para crear el recurso patient, que incluye nombre, apellido, genero, fecha de nacimiento y numero de documento como identificador.
El recurso fue enviado exitosamente al servidor público HAPI FHIR (https://hapi.fhir.org/baseR4/Patient) utilizando una solicitud HTTP POST. El servidor devolvió un código 201 Created y un ID asignado, confirmando que el recurso fue almacenado correctamente.

## 3b. Buscar un recurso Patient por número de documento

![capturas](./CAPTURAS/Ejercicio3PT1.png)
*Figura 6: Actividad 3*
![capturas](./CAPTURAS/Ejercicio3PT2.png)
*Figura 7: Actividad 3*


## 3c. Crear un recurso ServiceRequest relacionado con un recurso Observation

![capturas](./CAPTURAS/Ejercicio3PT3.png)
*Figura 8: Actividad 3*
![capturas](./CAPTURAS/Ejercicio3PT4.png)
*Figura 9: Actividad 3*
![capturas](./CAPTURAS/Ejercicio3PT5.png)
*Figura 10: Actividad 3*
![capturas](./CAPTURAS/Ejercicio3PT6.png)
*Figura 11: Actividad 3*

Este trabajo permitió aplicar de forma práctica los conceptos de interoperabilidad en salud mediante la creación, envío y recuperación de recursos FHIR, tanto manualmente como programáticamente. Se logró una mejor comprensión del funcionamiento de los estándares y su implementación en sistemas reales.

Descripcion de calculadora

Integrantes del grupo:
Mariano Capella
Gabriel Osemberg


Empezamos con:

Historias de usuario

1. Suma
Como usuario de la calculadora,
quiero poder ingresar dos números y obtener su suma,
para resolver operaciones aditivas de forma rápida.

2. Resta
Como usuario de la calculadora,
quiero poder ingresar dos números y obtener su diferencia,
para calcular cuánto hay entre un número y otro.

3. Multiplicación
Como usuario de la calculadora,
quiero poder multiplicar dos números,
para realizar cálculos de escalado o productos.

4. División
Como usuario de la calculadora,
quiero poder dividir un número por otro,
para obtener el cociente de una operación.

5. Manejo de errores en división
Como usuario de la calculadora,
quiero recibir un mensaje claro si intento dividir por cero,
para entender que la operación no es válida y evitar errores.

6. Operaciones encadenadas
Como usuario de la calculadora,
quiero realizar múltiples operaciones una tras otra,
para obtener resultados de cálculos más complejos sin reiniciar.

7. Interfaz de uso simple
Como usuario sin conocimientos técnicos,
quiero una interfaz simple para ingresar operaciones,
para poder usar la calculadora sin necesidad de aprender comandos complejos.

8. Historial de operaciones
Como usuario frecuente,
quiero ver el historial de operaciones realizadas,
para poder revisar mis cálculos anteriores.

9. Borrar o reiniciar
Como usuario,
quiero tener la opción de borrar la operación actual o reiniciar la calculadora,
para comenzar desde cero si me equivoco.

10. Resultados claros
Como usuario,
quiero que los resultados de las operaciones se muestren de forma clara y destacada,
para asegurarme de entenderlos correctamente.


criterios de aceptacion

1. Suma
Historia:
Como usuario de la calculadora, quiero poder ingresar dos números y obtener su suma, para resolver operaciones aditivas de forma rápida.

Criterios de aceptación:

El sistema debe permitir ingresar dos números válidos (enteros o decimales).

Al seleccionar la operación de suma, el sistema debe devolver la suma correcta.

El resultado debe mostrarse claramente en la interfaz.

Si los valores ingresados no son números válidos, debe mostrarse un mensaje de error.

2. Resta
Como usuario de la calculadora, quiero poder ingresar dos números y obtener su diferencia, para calcular cuánto hay entre un número y otro.

Criterios de aceptación:

El sistema debe aceptar dos entradas numéricas válidas.

Al seleccionar la operación de resta, se debe mostrar correctamente el resultado de la diferencia (a - b).

El resultado debe poder ser negativo si corresponde.

Errores en el ingreso de datos deben ser gestionados adecuadamente.

3. Multiplicación
Como usuario de la calculadora, quiero poder multiplicar dos números, para realizar cálculos de escalado o productos.

Criterios de aceptación:

El sistema debe aceptar dos números como entrada.

La multiplicación debe calcularse correctamente y mostrarse de forma inmediata.

Debe soportar la multiplicación de números negativos, decimales y cero.

No debe haber fallos en precisión para números decimales estándar.

4. División
Como usuario de la calculadora, quiero poder dividir un número por otro, para obtener el cociente de una operación.

Criterios de aceptación:

El sistema debe aceptar dos números válidos como entrada.

La operación de división debe devolver un resultado correcto (a / b).

Debe soportar división entre enteros y decimales.

Si el divisor es cero, no debe ejecutarse la operación, y debe cumplirse el criterio de la siguiente historia.

5. Manejo de errores en división
Como usuario de la calculadora, quiero recibir un mensaje claro si intento dividir por cero, para entender que la operación no es válida y evitar errores.

Criterios de aceptación:

Si el segundo número ingresado (divisor) es cero, el sistema debe bloquear la operación.

Se debe mostrar un mensaje claro tipo: “Error: División por cero no permitida.”

No debe producirse ninguna excepción técnica visible al usuario.

El sistema debe permitir continuar con otras operaciones tras mostrar el mensaje.

6. Operaciones encadenadas
Como usuario de la calculadora, quiero realizar múltiples operaciones una tras otra, para obtener resultados de cálculos más complejos sin reiniciar.

Criterios de aceptación:

El resultado de una operación debe poder reutilizarse como primer operando en la siguiente sin necesidad de reingresarlo.

Debe existir una forma intuitiva de continuar calculando (por ejemplo, usando el resultado actual automáticamente).

El sistema debe actualizar correctamente los resultados tras cada operación.

El flujo de operaciones debe mantener precisión y consistencia.

7. Interfaz de uso simple
Como usuario sin conocimientos técnicos, quiero una interfaz simple para ingresar operaciones, para poder usar la calculadora sin necesidad de aprender comandos complejos.

Criterios de aceptación:

La interfaz debe mostrar claramente los botones u opciones disponibles (números, operadores, limpiar, resultado).

Debe permitir el ingreso de números y operaciones sin necesidad de conocimientos técnicos o fórmulas.

La experiencia debe ser coherente entre diferentes operaciones.

Todos los textos deben estar en lenguaje natural y sin tecnicismos.

8. Historial de operaciones
Como usuario frecuente, quiero ver el historial de operaciones realizadas, para poder revisar mis cálculos anteriores.

Criterios de aceptación:

El sistema debe guardar un registro cronológico de las operaciones realizadas durante la sesión.

Cada entrada debe mostrar claramente los operandos, la operación y el resultado.

Debe permitir visualizar el historial en una sección accesible.

El historial debe poder borrarse completamente si el usuario lo desea.

9. Borrar o reiniciar
Como usuario, quiero tener la opción de borrar la operación actual o reiniciar la calculadora, para comenzar desde cero si me equivoco.

Criterios de aceptación:

Debe existir un botón o comando para limpiar la operación actual.

Debe existir una opción para reiniciar el sistema (borrar todas las entradas y el historial).

Al borrar, todos los campos visibles deben reiniciarse a su estado original.

El sistema debe confirmar visualmente que el borrado o reinicio fue realizado.

10. Resultados claros
Como usuario, quiero que los resultados de las operaciones se muestren de forma clara y destacada, para asegurarme de entenderlos correctamente.

Criterios de aceptación:

El resultado debe estar visualmente separado del resto de los elementos.

Debe estar resaltado (por tamaño, color u otra técnica) para facilitar su lectura.

Los resultados deben limitar el número de decimales para claridad (por ejemplo, 2 o 3 cifras).

Debe haber una indicación clara de a qué operación corresponde el resultado mostrado.




flujo de tareas

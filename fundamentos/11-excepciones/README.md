# 11. Excepciones

## Concepto

Una excepción señala un error durante la ejecución. try delimita la operación que puede fallar y except maneja un tipo concreto de error.

## Referencia disponible

Errores de conversión y división; manejo por tipo; referencias de else, finally y raise.

Ejecuta `python fundamentos/11-excepciones/main.py` desde la raíz del repositorio.

`main.py` contiene un ejemplo de referencia. Los archivos adicionales, cuando existen, conservan variantes para comparar enfoques.

## Práctica propuesta

Recorre documentos con texto normal, clave texto ausente, espacios solos, un entero como texto y otro texto normal. Maneja KeyError y AttributeError dentro del ciclo y cuenta los estados.

Escribe tu intento en un archivo aparte. Predice la salida antes de ejecutar.

## Comprobación

Comprueba que un documento posterior al error se procesa y que una lista vacía deja los contadores en cero.

## Alcance

El ejemplo principal usa ValueError y ZeroDivisionError. La práctica propuesta introduce KeyError y AttributeError; else, finally y raise amplían el manejo de errores.

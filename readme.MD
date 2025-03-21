
# TDA (Tipo de Dato Abstracto)

Aqui mostraremos la parte teorica de **Listas Doblemente Enlazadas** y **Listas Circulares**



## Autores

| Estudiante | Cedula  |
| :-------- | :------- |
| `Franyer Marin` | `32.293.396` | 
| `Luis Yepez` | `31.` | 


## Listas Enlazadas



- #### 1. ¿Cuál es la diferencia entre una lista simplemente enlazada y una lista doblemente enlazada?: 
  Que en la simplemente enlazada cada nodo tiene un enlace (uno al siguiente), mientras que la doblemente enlazada cada nodo tiene dos enlaces (uno al siguiente y el otro al anterior).


  ![Lista Enlazada](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Frd4zeajh6dqnme4e3uhc.png "Lista Simplemente Enlazada")

  ![Lista Enlazada Dobe](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fbzt4m25cfowzraozktyk.png "Lista Doblemente Enlazada")


- #### 2. ¿Cuáles son las ventajas y desventajas de usar una lista doblemente enlazada en comparación con una lista simplemente enlazada?: 

  | **Característica**               | **Lista Simplemente Enlazada**                       | **Lista Doblemente Enlazada**                     |
  |----------------------------------|-----------------------------------------------------|--------------------------------------------------|
  | **Estructura**                   | Cada nodo tiene un solo puntero al siguiente nodo.  | Cada nodo tiene punteros al siguiente y al anterior. |
  | **Acceso**                       | Acceso secuencial; no se puede acceder al nodo anterior. | Acceso más flexible; se puede acceder a nodos anteriores y siguientes. |
  | **Inserción**                    | Más simple y rápida, solo se necesita cambiar un puntero. | Puede ser más compleja, ya que se deben actualizar dos punteros. |
  | **Eliminación**                  | Requiere más pasos para encontrar el nodo anterior. | Más eficiente al eliminar, ya que se puede acceder al nodo anterior directamente. |
  | **Uso de memoria**               | Menor uso de memoria (un puntero por nodo).        | Mayor uso de memoria (dos punteros por nodo).   |
  | **Complejidad**                  | Menos compleja en términos de implementación.      | Más compleja debido a la gestión de dos punteros. |
  | **Recorridos**                   | Solo en una dirección (del primero al último).     | Se puede recorrer en ambas direcciones.         |



- #### 3. ¿Cómo se realiza la inserción de un nodo en una lista doblemente enlazada?: 
  La creación de un nuevo nodo implica:

   - Solicitar el espacio a la memoria principal

    - Verificar la validez del espacio (la memoria puede no entregarlo)

   - Depositar la información básica del nodo y fijar las referencias inicialmente a NULL

        ![creando nodo](https://conclase.net/imagen/c/edd/id_vacia2.gif "Creando nodo")


    - Insertarlo dentro de la estructura reorganizando referencias (vínculos)
    
        ![creando nodo](https://conclase.net/imagen/c/edd/id_continuacion2.gif "Creando nodo")

- #### 4. ¿Qué cambios deben realizarse en los punteros al eliminar un nodo de una lista doblemente enlazada?: 

  Se actualiza el enlace "siguiente" del nodo anterior para que apunte al nodo posterior al eliminado, y el enlace "anterior" del nodo posterior para que apunte al nodo anterior al eliminado. Si el nodo eliminado era cabeza/cola, se actualizan esos punteros. 
 
   ![Eliminando en Lista Doble](https://conclase.net/imagen/c/edd/bd_intermedio2.gif "Eliminacion en Lista Doblemente Enlazada")

- #### 5. ¿Cuándo es más eficiente utilizar una lista doblemente enlazada en lugar de un array?: 
  Cuando se requieren inserciones/eliminaciones frecuentes en cualquier posición con tiempo O(1), no se conoce el tamaño máximo de antemano, o se necesita recorrido bidireccional sin costo adicional de memoria. Los arrays son eficientes en acceso aleatorio pero ineficientes en modificaciones de elementos intermedios. 

   ![array o lista enlazada](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fi%2Fe65b6pku9i7tstechfnz.jpeg "arrat vs list")  

- ### 6. Ejemplo practico hecho en python archivo: `Lista_doble_enlazada_ejemplo_iphones.py`




## Listas Circulares

- #### 1. ¿Cómo se implementa la inserción de un nodo en una lista circular?: 
   Para insertar un nodo en una lista circular, primero se debe identificar el lugar donde se desea realizar la inserción, ya sea al inicio, al final o en una posición específica. Si se inserta al inicio, se crea el nuevo nodo y se hace que su puntero siguiente apunte al nodo actual que es la cabeza de la lista; luego, se actualiza el último nodo (el que apunta a la cabeza) para que su siguiente apunte al nuevo nodo, y finalmente se actualiza la cabeza para que sea el nuevo nodo. Si la inserción es al final, se crea el nuevo nodo y se hace que su siguiente apunte a la cabeza; después, se busca el último nodo (el que apunta a la cabeza) y se actualiza su siguiente para que apunte al nuevo nodo. En el caso de una inserción en una posición específica, se recorre la lista hasta llegar a la posición deseada, y se ajustan los punteros del nodo anterior y del nuevo nodo para mantener la estructura circular, asegurando que el nuevo nodo apunte al siguiente nodo en la secuencia y que el nodo anterior apunte al nuevo nodo. En todos los casos, es fundamental mantener la propiedad circular de la lista, garantizando que el último nodo siempre apunte al primero.


- #### 2. ¿Cómo se elimina un nodo en una lista circular sin romper su estructura?
  Para eliminar un nodo en una lista circular sin afectar su estructura, se sigue un proceso específico. Primero, se localiza el nodo que se desea eliminar recorriendo la lista desde el nodo cabeza. Una vez identificado el nodo, se ajusta el puntero del nodo anterior para que apunte al nodo siguiente del nodo que se va a eliminar, garantizando así que la estructura circular se mantenga intacta. Si el nodo a eliminar es el cabeza, se debe actualizar el cabeza para que apunte al siguiente nodo y, además, se debe ajustar el último nodo de la lista para que apunte al nuevo cabeza, asegurando que la circularidad de la lista no se pierda. Este proceso es esencial para mantener la integridad de la lista circular durante la eliminación de nodos.

- #### 3. ¿Cómo se puede recorrer una lista circular sin entrar en un bucle infinito?
  Para recorrer una lista circular sin caer en un bucle infinito, se pueden utilizar estrategias como un contador o un marcador. En el enfoque del contador, se lleva un registro del número de nodos visitados durante el recorrido; cuando el contador alcanza el total de nodos en la lista, se detiene el recorrido. Por otro lado, en el enfoque del marcador, se almacena una referencia al nodo cabeza y se detiene el recorrido cuando se vuelve a encontrar este nodo, asegurando que no se continúe indefinidamente. Ambos métodos son efectivos para garantizar que el recorrido de la lista circular sea controlado y no se convierta en un bucle infinito.

- #### 4. ¿En qué tipo de aplicaciones o algoritmos se suelen utilizar las listas circulares?
  Las listas circulares son estructuras de datos muy útiles en diversas aplicaciones y algoritmos. Por ejemplo, en juegos como la "eliminación de José", donde se elimina a cada k-ésimo jugador en un círculo, las listas circulares permiten modelar de manera eficiente este tipo de dinámicas. En el ámbito de la gestión de recursos, como en sistemas operativos, se utilizan para la programación de tareas y el manejo de procesos, ya que permiten un acceso cíclico y ordenado a los recursos. Además, en estructuras de datos como las colas, las listas circulares ofrecen un acceso eficiente y cíclico a los elementos, lo que las hace ideales para implementaciones que requieren un flujo continuo y repetitivo de datos. Estas aplicaciones demuestran la versatilidad y eficiencia de las listas circulares en diferentes contextos.

- #### 5. ¿Cómo hacer que una lista doblemente enlazada se comporte como una lista circular?
  Para hacer que una lista doblemente enlazada se comporte como una lista circular, es necesario realizar dos pasos clave. Primero, se deben conectar los extremos de la lista, es decir, el siguiente puntero del último nodo debe apuntar al primer nodo (cabeza), y el puntero anterior del primer nodo debe apuntar al último nodo. Esto crea un ciclo entre el primer y el último nodo, estableciendo la circularidad. Segundo, todas las operaciones de inserción, eliminación y recorrido deben ajustarse para tener en cuenta esta circularidad, asegurando que, al llegar a un extremo de la lista, se pueda regresar al otro sin problemas. Estas modificaciones garantizan que la lista doblemente enlazada funcione correctamente como una lista circular.

- ### 6. Ejemplo practico hecho en python archivo: `lista circulares.py`

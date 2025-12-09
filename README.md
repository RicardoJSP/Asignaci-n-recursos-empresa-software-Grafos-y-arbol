La estructura de grafo nos permite representar relaciones entre elementos, una herramienta muy útil al momento de modelar las habilidades y 
dependencias de los proyectos en la empresa. Podemos crear un grafo en donde modelemos las habilidades de los trabajadores, donde cada nodo o vértice puede 
representar un lenguaje de programación que el desarrollador maneja con facilidad (Python, HTML, CSS, Base de datos, etc.) y cada desarrollador lo podemos 
vincular a los nodos que representan sus habilidades, de esta manera, podemos identificar directamente y con rapidez qué desarrollador maneja tal lenguaje 
o estructura, evaluar si un proyecto en el cual queremos participar puede ser cubierto con las habilidades existentes o detectar las habilidades frecuentes 
de un trabajador.

Otro ejemplo en el cual podemos utilizar la estructura de grafos, es al momento de modelar dependencias entre proyectos, donde cada proyecto vendría 
siendo un nodo o vértice y las aristas dirigidas representan una dependencia, por ejemplo, si tenemos un proyecto A que depende del proyecto B para terminarse, 
entonces existe: (B ---> A). De esta manera, organizamos mejor la prioridad de la empresa en cuanto a cuál proyecto terminar primero, priorizar asignaciones de
recursos, identificar las mejores rutas de desarrollo, etc. Al momento de realizar estos estudios es importante la aplicación de algoritmos como DFS (Depth-First 
Search) o (Búsqueda en profundidad) el cual nos permite detectar dependencias profundas, ciclos y rutas críticas, empezando por el nodo inicial (raíz), 
luego explorando nodos adyacentes no visitados y guardándolos en una pila tras visitarlos para no volver, si se llega a un “callejón sin salida” se retrocede al
nodo anterior a la pila, y se sigue explorando. El proceso se repite hasta que la pila esta vacía lo que significa que todos los nodos han sido accedidos, 
este algoritmo es útil para poder analizar todos los trabajadores que saben usar un lenguaje en particular.
Otro algoritmo importante es el BFS (Breadth-First Search) o (Búsqueda en anchura), el cual evalúa niveles de dependencias o encuentra proyectos desbloqueados, 
es común al momento de encontrar la ruta más corta, analizar las redes o la detección de ciclos, para nuestro caso en particular, es útil para identificar la 
cadena completa de dependencias de proyectos.

De esta manera, al utilizar la estructura de grafos, tenemos la ventaja de optimizar los procesos de búsqueda en la empresa y visualizar rápidamente qué 
trabajadores son los más adecuados para ciertos proyectos o qué proyectos deben realizarse primero.

DFS = https://www.youtube.com/watch?v=Xb6nY2RXcG0
BFS = https://www.youtube.com/watch?v=gHHAZNuSTII

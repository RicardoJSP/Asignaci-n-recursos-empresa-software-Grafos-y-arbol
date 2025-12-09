import networkx as nx
G = nx.DiGraph()

habilidades = ["Python", "JavaScript", "HTML", "CSS", "PHP"]
devs = {"Ricardo": ["Python", "HTML"],
        "Constanza": ["HTML", "CSS"],
        "Javier": ["JavaScript", "Python"],
        "Snow": ["Python"],
        "Neo": ["PHP"]
        }
proyectos = ["WebAPP", "FrontEndWeb", "BackEndWeb"]

# Agregar nodos de habilidades al grafo:
G.add_nodes_from(habilidades, tipo="habilidad")

# Agregar nodos de desarrolladores al grafo:
# y sus habilidades como aristas:
for dev, dev_habilidad in devs.items(): # Iteramos sobre el diccionario
    G.add_node(dev, tipo="desarrollador") # Agregamos el nodo del desarrollador
    for habilidad in dev_habilidad: # Iteramos sobre las habilidades del desarrollador
        G.add_edge(dev, habilidad) # Agregamos una arista entre el desarrollador y su habilidad.

# Agregamos nodos de proyectos al grafo:
G.add_nodes_from(proyectos, tipo="proyecto")

# Generamos las dependencias, cual proyecto necesita estar listo antes que otro:
dependencias = [("BackEndWeb", "FrontEndWeb"),
                ("BackEndWeb", "WebAPP")]

# Añadimos las dependencias como aristas:
for dep in dependencias:
    G.add_edge(dep[0], dep[1]) 

# Imprimimos información del grafo:
print("Total de nodos:", G.number_of_nodes())
print("Total de aristas:", G.number_of_edges())

print("Dependencias del proyecto:")
for origen, destino in G.edges():
    if origen in proyectos and destino in proyectos:
        print(f"{origen} debe estar listo antes de: {destino}")

# Creamos una clase nodo para representar la jerarquía de la empresa
class Nodo:
    def __init__(self, valor):
        self.valor = valor 
        self.hijos = [] # Lista de nodos hijos, inicialmente vacía

    def agregar_hijo(self, nodo): 
        self.hijos.append(nodo) # Agrega el nodo hijo a la lista de hijos

raiz = Nodo("Empresa de software") # Nodo raíz que representa la empresa

# Asignamos los proyectos al árbol
for proyecto in proyectos: # Iteramos sobre los proyectos.
    nodo_proyecto = Nodo(proyecto) # Creamos un nodo para cada proyecto.

    if proyecto == "BackEndWeb": # Definimos las habilidades requeridas para cada proyecto
        habilidades_requeridas = ["Python", "JavaScript"]
    elif proyecto == "FrontEndWeb":
        habilidades_requeridas = ["HTML", "CSS"]
    else:
        habilidades_requeridas = ["PHP", "JavaScript", "Python"]

    for dev, dev_habilidad in devs.items(): # Iteramos sobre los desarrolladores y sus habilidades:
      if any(habilidad in dev_habilidad for habilidad in habilidades_requeridas): # Si hay alguna habilidad en las habilidades del dev, y en las habilidades requeridas:
        nodo_asignacion = Nodo(dev) # Creamos un nodo para el desarrollador, definiendo la variable asignación.
        nodo_proyecto.agregar_hijo(nodo_asignacion) #  Y agregamos el nodo del desarrollador al nodo del proyecto, llamando al método agregar_hijo.
    raiz.agregar_hijo(nodo_proyecto) # Finalmente, agregamos el nodo del proyecto a la raíz.

# Ahora, creamos algoritmos de búsqueda, partiendo por "DFS", para recorrer y mostrar
# el arbol de asignaciones, como un reporte visual:
def recorrer_arbol_DFS(nodo, nivel=0): 
    print("  " * nivel + nodo.valor) # Imprimimos el valor del nodo, segun su nivel en el árbol con la indentacion correspondiente.
    for hijo in nodo.hijos: # Iteramos sobre los hijos del nodo actual
        recorrer_arbol_DFS(hijo, nivel + 1) # Llamada recursiva para cada hijo, incrementando el nivel.               
print("--------------ARBOL COMPLETO (DFS)------------------") 
recorrer_arbol_DFS(raiz)

# Luego generamos algoritmo de busqueda "BFS" para buscar los desarrolladores capacitados por proyecto
# o para identificar las dependencias de los proyectos:
def buscar_devs_para_proyecto(proyecto): # usamos el proyecto como parámetro de búsqueda.
    if proyecto == "BackEndWeb":
        habilidades_requeridas =  ["Python", "JavaScript"]
    elif proyecto == "FrontEndWeb":
        habilidades_requeridas = ["HTML", "CSS"]
    else:
        habilidades_requeridas = ["PHP", "JavaScript", "Python"]
    devs_encontrados = [] # Lista para almacenar los desarrolladores encontrados.
    for dev, dev_habilidad in devs.items():
        if any(habilidad in dev_habilidad for habilidad in habilidades_requeridas):
            devs_encontrados.append(dev) # Agregamos el desarrollador a la lista si tiene alguna habilidad requerida.
    print(f"Proyecto: {proyecto}")
    print(f"Requiere: {habilidades_requeridas}")
    print(f"Candidatos elegidos: {devs_encontrados}")
    return devs_encontrados

print("-----BUSQUEDA DE DESARROLLADORES POR PROYECTO (BFS)-----")
for proyecto in proyectos:
    buscar_devs_para_proyecto(proyecto)
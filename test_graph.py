class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list() #vertices ligados a esse vertice
		self.discovery = 0
		self.finish = 0
		self.color = 'gray'
	
	def add_adjacency(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v) #adiciona um vizinho ao vertice
			self.neighbors.sort() #ordena
	#def search_vertex(self, index):
	#	print(f"Vertex: {index} - {self.dictionary_vertex}")

class Graph:
	def __init__(self, directed=None, verbose=None):
		self.adjacency = [] # cria lista para adjacencia
		self.directed = directed #flag para saber se eh direcioando ou nao
		self.adjacency_type = verbose # flag para saber eh lista ou matriz
		#self.quantity = quantity #quantidade de vertices
		self.dictionary_vertex = {}
		
		
	time = 0
	
	'''
	If choice is list created a list or a matrix
	'''
	def created_matrix(self):
		vertex_quantity = len(self.dictionary_vertex)
		for i in range(vertex_quantity):
			list_v = []
			for i in range(vertex_quantity):

				list_v.append(0)
			self.adjacency.append(list_v)
				
	def add_vertex(self, vertex):
		#verifica se eh um vertice e se ja nao foi um  vertice inserido
		if isinstance(vertex, Vertex) and vertex.name not in self.dictionary_vertex:
			self.dictionary_vertex[vertex.name] = vertex

			return(True)
		else: # return false if vertex insured
			return(False)

	
	
	
	'''
	First verify if is a object after if is directed and 
	created a list or matrix, if matrix created a matrix with size vertex

	'''
	def add_edge(self, vertex1, vertex2):
		if(isinstance(vertex1, Vertex)) and (isinstance(vertex2, Vertex)): # verify if created vertex
			if(self.adjacency_type):# created matrix
								
				if(self.directed): #if directed or not directed
					self.adjacency[vertex1.name][vertex2.name] = 1
				else:
					self.adjacency[vertex1.name][vertex2.name] = 1
					self.adjacency[vertex2.name][vertex1.name] = 1
			else: # created list
				if(self.directed): #if directed or not directed
					self.dictionary_vertex[vertex1.name].add_adjacency(vertex2.name)
				else:
					self.dictionary_vertex[vertex1.name].add_adjacency(vertex2.name)
					self.dictionary_vertex[vertex2.name].add_adjacency(vertex1.name)

	def print_graph(self, verbose=None):
		if(verbose):
			for i in range(len(self.dictionary_vertex)):
				print(f'{[i]} -> {self.adjacency[i]}')
		else:
			for key in sorted(list(self.dictionary_vertex.keys())):
				print(f"{key} - {self.dictionary_vertex[key].neighbors}")
            	#print(key + str(self.dictionary_vertex[key].neighbors) + " " + str(self.dictionary_vertex[key].discovery))

			

#graph = Graph(True, True)  # matriz direcionada
#graph = Graph(False, True) # matriz nao direcionada
#graph = Graph(False, False) # list adjacency not directed
graph = Graph(True, False)  # list adjacency directed
a = Vertex(0)
b = Vertex(1)
c = Vertex(2)
d = Vertex(3)
e = Vertex(4)


graph.add_vertex(a)
graph.add_vertex(b)
graph.add_vertex(c)
graph.add_vertex(d)
graph.add_vertex(e)

#graph.created_matrix()

###
#print('Matriz criada')
#graph.print_graph(True)
###
#print('Lista de adjacencia')
#graph.print_graph(False)
###

###
graph.add_edge(a, b)
graph.add_edge(a, c)
graph.add_edge(b, c)
graph.add_edge(c, d)
graph.add_edge(e, a)
###

###
#print('Matriz com as adjacencias')
#graph.print_graph(True)
#print("Lista de adjacencia")
#graph.print_graph(False)
###
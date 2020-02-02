from SimpleNode import *

class ListElements:
	def __init__(self):
		self.init = None
		self.amountNodes = 0
	
	def __increment(self):
		self.amountNodes += 1
	
	def __isIndexValid(self, index):
		return True if (index >= 0) and (index <= self.size()) else False
		
	def __isValidNode(self, node):
		return True if node != None else False
	
	def __addRecursive(self, node, index, newNode):
		if index == 1:
			newNode.setNext( node )
			node.setNext( newNode )
		else:
			self.__addRecursive( node.getNext(), index-1, newNode )
		
	def __addPosition(self, index, value):
		newNode = SimpleNode( value )
		
		if index == 0:
			newNode.setNext( self.init )
			self.init = newNode
		else:
			self.__addRecursive( self.init, index, newNode )
		
		self.__increment()
	
	def __getRecursive(self, node, index):
		if index == 0:
			return node.getValue()
		else:
			return self.__getRecursive( node.getNext(), index-1)
	
	def add(self, index, value):
		if self.__isIndexValid( index ):
			self.__addPosition( index, value )
		else:
			raise Exception("Método 'add': Indice inválido.")
	
	def get(self, index):
		if index >= 0 and index < self.size():
			return self.__getRecursive( self.init, index )
		else:
			raise Exception("MIndice inválido.")
		
	def isEmpty(self):
		return True if self.amountNodes == 0 else False
	
	def size(self):
		return self.amountNodes

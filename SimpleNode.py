class SimpleNode:
	def __init__(self, value):
		self.value = value
		self.nextNode = None
	
	def hasNext(self):
		return True if self.getNext() != None else False
	
	def setValue(self, value):
		self.value = value
	
	def setNext(self, newNode):
		self.nextNode = newNode
	
	def getValue(self):
		return self.value
	
	def getNext(self):
		return self.nextNode

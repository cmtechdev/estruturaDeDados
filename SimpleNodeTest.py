'''
	python3 -m pip install pytest
'''

import unittest

from SimpleNode import *

class SimpleNodeTest( unittest.TestCase ):
	def setUp(self):
		self.node = SimpleNode(2)
	
	def testHasNext(self):
		self.assertEqual( self.node.hasNext(), False )
		self.node.setNext( SimpleNode(3) )
		self.assertEqual( self.node.hasNext(), True )
		
	def testHasNotNext(self):
		self.assertEqual( self.node.hasNext(), False )	
	
	def testSetValue(self):
		self.node.setValue(9)
		self.assertEqual( self.node.getValue(), 9 )
		
	def testGetValue(self):
		self.assertEqual( self.node.getValue(), 2 )
	
	def testNextNodeNone(self):
		self.assertIsNone( self.node.getNext() )
	
	def testNextNodeIsNotNone(self):
		self.node.setNext( SimpleNode(7) )
		self.assertIsNotNone( self.node.getNext() )
	
if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	suite = unittest.loadTestsFromTestCase( SimplesNodeTest )
	runnet.run( suite )

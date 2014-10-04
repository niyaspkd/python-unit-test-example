import sort
import unittest
class inputtype(unittest.TestCase):
	def testinput(self):
		self.assertRaises(sort.ElementTypeError,sort.sort,[4,2,"rty",7])
class outputcheck(unittest.TestCase):
	def testoutput(self):
		a=sort.sort([6,3,9,5])
		self.assertEqual([3,5,6,9],a)
	def testtype(self):
		a=sort.sort([5,3,6,1])
		self.assertEqual(list,type(a))
if __name__=="__main__":
unittest.main()
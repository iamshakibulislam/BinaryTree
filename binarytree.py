
class Tree:
	def __init__(self,data=None):
		self.data=data
		self.left=None
		self.right=None



	def add(self,data):
		
		if self.data == data:
			print('already exists')
		if data < self.data :
			if self.left:
				self.left.add(data)

			else :
				self.left =  Tree(data)
				print('added')

		if data > self.data:
			if self.right:
					self.right.add(data)

			else:
				self.right=Tree(data)
				print('added')


				









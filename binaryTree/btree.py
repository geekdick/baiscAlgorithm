from  collections import deque


class Node(object):
	def __init__(self, data):
		self.data = data
		self.lft = None
		self.rgt = None


class BTree(object):
	def __init__(self):
		self._root = None
		self._size = 0
	
	# 二分查找
	def find(self, item):
		
		def recurse(node):
			if node is None:
				return None
			elif item == node.data:
				return node.data
			elif item < node.data:
				return recurse(node.lft)
			else:
				return recurse(node.rgt)
		
		# 从根节点开始查找
		return recurse(self._root)
	
	# 判断节点是否为空
	def isEmpty(self):
		if self._root:
			return False
		else:
			return True
	
	# 增加节点
	def add(self, item):
		'''
		 从根节点判断，根节点为None，赋值给根节点
		 比根节点小，则判断左节点是否为空，为空则赋值给左节点，否则递归左节点
		 比根节点大，则判断右节点是否为空，为空则赋值给右接待你，否则递归右节点
		'''
		
		def recurse(node):
			if item < node.data:
				if node.lft == None:
					node.lft = Node(item)
				else:
					recurse(node.lft)
			else:
				if node.rgt == None:
					node.rgt = Node(item)
				else:
					recurse(node.rgt)
		
		if self.isEmpty():
			self._root = Node(item)
		else:
			recurse(self._root)
		self._size += 1
	
	# 中序遍历
	def inOrder(self):
		'''
		中序遍历顺序：
		1，遍历左子树
		2，根节点
		3，遍历右子树
		'''
		btree = []
		
		def recurse(node):
			if node != None:
				recurse(node.lft)
				btree.append(node.data)
				recurse(node.rgt)
		
		recurse(self._root)
		return btree
	
	def preOrder(self):
		'''
		先遍历顺序：
		1，根节点
		2，遍历左子树
		3，遍历右子树
		'''
		btree = []
		
		def recurse(node):
			if node != None:
				btree.append(node.data)
				recurse(node.lft)
				recurse(node.rgt)
		
		recurse(self._root)
		return btree
	
	# 后序遍历
	def postOrder(self):
		'''
		后序遍历顺序：
		1，遍历左子树
		2，遍历右子树
		3，根节点
		'''
		btree = []
		
		def recurse(node):
			if node != None:
				recurse(node.lft)
				recurse(node.rgt)
				btree.append(node.data)
		
		recurse(self._root)
		return btree
	
	# 层序遍历
	def leverOrder(self):
		q = deque()
		q.append(self._root)
		btree = []
		while q:
			# dque是一个双向队列，先进先出是popleft
			node = q.popleft()
			btree.append(node.data)
			if node.lft:
				q.append(node.lft)
			if node.rgt:
				q.append(node.rgt)
		return btree


if __name__ == "__main__":
	btree = BTree()
	btree.add(4)
	btree.add(2)
	btree.add(1)
	btree.add(3)
	btree.add(6)
	btree.add(5)
	btree.add(7)
	print(btree.inOrder())
	print(btree.preOrder())
	print(btree.leverOrder())

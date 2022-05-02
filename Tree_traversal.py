import sys

class Node:
    def __int__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

def pre_order(node): #부모 - 왼 -오
    print(node.data, end=" ")
    if node.left_node != None:
        pre_order(tree[node.left_node])
    if node.right_node != None:
        pre_order(tree[node.right_node])

def in_oder(node): # 왼 - 부모- 오
    if node.left_node != None:
        in_oder(tree[node.left_node])
    print(node.data, end=" ")
    if node.right_node != None:
        in_oder(tree[node.right_node])

def post_oder(node): # 왼 - 오- 부모
    if node.left_node != None:
        post_oder(tree[node.left_node])

    if node.right_node != None:
        post_oder(tree[node.right_node])
    print(node.data, end=" ")

n = int(input())
tree = {}

for i in range(n):
    data, left, right = input().split()
    if left == 'None':
        left = None
    if right == 'None':
        right = None
    tree[data] = Node(data,left,right)

pre_order(tree['A'])
print()
pre_order(tree['B'])
print()
pre_order(tree['B'])

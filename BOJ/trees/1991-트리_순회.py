'''
# 예제 입력 1
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
'''
import sys
sys.setrecursionlimit(10**6)
def preorder(node):
    if node == '.':
        return
    print(node, end = "")
    preorder(tree[node][0])
    preorder(tree[node][1])

def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end = "")
    inorder(tree[node][1])

def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end = "")

n = int(input())
tree = {}
for _ in range(n):
    root, left, right = input().split()
    tree[root] = (left, right)

preorder('A')
print()
inorder('A')
print()
postorder('A')

'''by hhs666
import sys
sys.setrecursionlimit = 10**9
n = int(input())
tree = [line.split() for line in sys.stdin.read().splitlines()]
tree = {root:(left, right) for root, left, right in tree}

def pre(root):
    left, right = tree[root]
    print(root,end='')
    if left!='.': pre(left)
    if right!='.': pre(right)

def inorder(root):
    left, right = tree[root]
    if left!='.': inorder(left)
    print(root,end='')
    if right !='.' : inorder(right)

def post(root):
    left, right = tree[root]
    if left!='.' : post(left)
    if right!='.': post(right)
    print(root, end='')

for foo in (pre, inorder, post):
    foo('A')
    print()
'''

'''by tjdals4565
left = {}
right = {}

def preorder(root):
  if root == '.':
    return
  print(root, end='')
  preorder(left[root])
  preorder(right[root])

def inorder(root):
  if root == '.':
    return
  inorder(left[root])
  print(root, end='')
  inorder(right[root])

def postorder(root):
  if root == '.':
    return
  postorder(left[root])
  postorder(right[root])
  print(root, end='')

def main():
  global left, right
  n = int(input())
  for i in range(n):
    a,l,r = input().split()
    left[a] = l
    right[a] = r

  preorder('A')
  print()
  inorder('A')
  print()
  postorder('A')
  print()

if __name__ == "__main__":
  main()
'''

'''by sangw0804
def preorder(adj_list, cur):
  print(cur, end='')
  if adj_list[cur][0] != '.': preorder(adj_list, adj_list[cur][0])
  if adj_list[cur][1] != '.': preorder(adj_list, adj_list[cur][1])


def inorder(adj_list, cur):
  if adj_list[cur][0] != '.': inorder(adj_list, adj_list[cur][0])
  print(cur, end='')
  if adj_list[cur][1] != '.': inorder(adj_list, adj_list[cur][1])


def postorder(adj_list, cur):
  if adj_list[cur][0] != '.': postorder(adj_list, adj_list[cur][0])
  if adj_list[cur][1] != '.': postorder(adj_list, adj_list[cur][1])
  print(cur, end='')


n = int(input())
adj_list = {}

for _ in range(n):
  par, lc, rc = input().split()
  adj_list[par] = [lc, rc]

preorder(adj_list, 'A')
print()
inorder(adj_list, 'A')
print()
postorder(adj_list, 'A')
'''
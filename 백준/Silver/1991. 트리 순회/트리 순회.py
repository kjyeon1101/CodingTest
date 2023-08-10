import sys
input = sys.stdin.readline

def preorder(tree, node):
  if node != '.':
    print(node, end='')
    preorder(tree, tree[node][0])
    preorder(tree, tree[node][1])
  return

def inorder(tree, node):
  if node != '.':
    inorder(tree, tree[node][0])
    print(node, end='')
    inorder(tree, tree[node][1])
  return

def postorder(tree, node):
  if node != '.':
    postorder(tree, tree[node][0])
    postorder(tree, tree[node][1])
    print(node, end='')
  return

def main():
  N = int(input())
  tree = dict()
  for _ in range(N):
    node, left, right = input().split()
    tree[node] = (left, right)

  preorder(tree, 'A')
  print()
  inorder(tree, 'A')
  print()
  postorder(tree, 'A')
  print()

main()
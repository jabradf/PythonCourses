class TreeNode:
  def __init__(self, value):
    self.value = value
    self.children = []

  def add_child(self, child_node):
    self.children.append(child_node) 
  
  def traverse(self):
    nodes_to_visit = [self]
    while len(nodes_to_visit) > 0:
      current_node = nodes_to_visit.pop()
      print(current_node.value)
      nodes_to_visit += current_node.children

root = TreeNode("A")
first_child = TreeNode("B")
second_child = TreeNode("C")

root.add_child(first_child)
root.add_child(second_child)

root.traverse()
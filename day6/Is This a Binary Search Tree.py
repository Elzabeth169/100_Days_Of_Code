""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def is_bst_helper(node, min_value, max_value):
    if node is None:
        return True
    if node.data <= min_value or node.data >= max_value:
        return False
    return is_bst_helper(node.left, min_value, node.data) and is_bst_helper(node.right, node.data, max_value)

def check_binary_search_tree_(root):
    return is_bst_helper(root, float('-inf'), float('inf'))
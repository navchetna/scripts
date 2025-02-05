from treeparser import TreeParser
from tree import Tree
import sys

if len(sys.argv) != 2:
    print("Please enter PDF name")
    sys.exit()

pdf_folder = "./input/"

path = pdf_folder + sys.argv[1]

tree = Tree(path)
tree_parser = TreeParser()
tree_parser.populate_tree(tree)
tree_parser.generate_output_text(tree)
# tree_parser.generate_output_json(tree)
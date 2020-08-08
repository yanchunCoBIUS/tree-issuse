

from ete3 import *
import pickle


def read_evolutionary_event():
    with open("./ENSGT00390000009061_transcript_gene_evolutionary_event.pickle", 'rb') as f:
        evolutionary_event = pickle.load(f)
    return evolutionary_event


def check(node: PhyloTree, s: set, grey: set):
    if node in grey:
        if not node.is_leaf():
            left = check(node.children[0], s, grey)
            right = check(node.children[1], s, grey)
            if left and right:
                s.add(node)
                s.discard(node.children[0])
                s.discard(node.children[1])
                return True
            if left != right:
                s.add(node.children[0] if left else node.children[1])
                return False
        else:
            return True
    else:
        for n in node.children:
            check(n, s, grey)
        return False

def main():
    result = []
    _12_grey_node_or_leaf = read_evolutionary_event()["loss"]

    grey_leaf = set(_12_grey_node_or_leaf)
    print("original")
    # for i in grey_leaf:
    #      print(i)


    print("\n---------------\n")

    root = _12_grey_node_or_leaf[0].get_tree_root()

    r = set()
    check(root, r, grey_leaf)


    print("result")
    for i in r:
        print(i)





if __name__ == "__main__":
    main()
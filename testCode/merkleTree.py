import hashlib

def build_merkle_tree(leaves):
    num_leaves = len(leaves)

    if num_leaves == 1:
        return hashlib.sha256(leaves[0].encode()).hexdigest()
    
    if num_leaves % 2 == 1:
        leaves.append(leaves[-1])
        num_leaves += 1
    
    pairs = [leaves[i] + leaves[i+1] for i in range(0, num_leaves, 2)]

    hashes = [hashlib.sha256(pair.encode()).hexdigest() for pair in pairs]

    return build_merkle_tree(hashes)

leaves = ['a']
merkle_root = build_merkle_tree(leaves)
print(merkle_root+'\n')



def print_merkle_tree(node, depth):
    indent = " " * depth * 4
    print(indent + node)
    if len(node) == 64:
        print_merkle_tree(node[:32], depth+1)
        print_merkle_tree(node[32:], depth+1)


print_merkle_tree(merkle_root, 0)



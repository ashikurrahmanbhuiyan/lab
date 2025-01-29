import hashlib

def build_merkle_tree(leaves):
    if len(leaves) == 1:
        return [leaves]
    
    if len(leaves) % 2 == 1:
        leaves.append(leaves[-1])
    
    parent = []
    for i in range(0, len(leaves), 2):
        combined = leaves[i] + leaves[i + 1]
        parent.append(hashlib.sha256(combined.encode()).hexdigest())
    
    return [leaves] + build_merkle_tree(parent)

def print_full_tree(tree):
    depth = len(tree)
    for i, level in enumerate(tree):
        indent = "" * (depth - i) * 4
        print(indent + "\n   ".join(level))


# data
leaves = ['a', 'b', 'c']
hashed_leaves = [hashlib.sha256(leaf.encode()).hexdigest() for leaf in leaves]
merkle_tree = build_merkle_tree(hashed_leaves)

# print(hashed_leaves)
print("Merkle Tree:")
print_full_tree(merkle_tree)

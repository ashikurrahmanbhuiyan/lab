import hashlib

def build_merkle_tree(leaves):
    for leave in leaves:
        print(leave)
    print('\n')

    if len(leaves) == 1:
        return [leaves]
    
    if len(leaves) % 2 == 1:
        leaves.append(leaves[-1])

    parent = []
    for i in range(0, len(leaves), 2):
        combined = leaves[i] + leaves[i + 1]
        parent.append(hashlib.sha256(combined.encode()).hexdigest())
    
    return [leaves] + build_merkle_tree(parent)


# data
n = int(input("ENter the number of element: "))
leaves = []
for i in range(n):
    leaves.append(input(f"Enter the element {i+1} : "))
hashed_leaves = [hashlib.sha256(leaf.encode()).hexdigest() for leaf in leaves]
merkle_tree = build_merkle_tree(hashed_leaves)
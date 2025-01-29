import hashlib


def build_merkle_tree(leaves, flg = True):
    num_leaves = len(leaves)
    if num_leaves == 1:
        if flg == True:
            return hashlib.sha256(leaves[0].encode()).hexdigest()
        else:
            return leaves[0]

    if num_leaves % 2 == 1:
        leaves.append(leaves[-1])
        num_leaves += 1
    pairs = [leaves[i] + leaves[i+1] for i in range(0, num_leaves, 2)]
    hashes = [hashlib.sha256(pair.encode()).hexdigest() for pair in pairs]

    return build_merkle_tree(hashes, False)

leaves = ["apple", "banana", "cherry", "date"]
original = build_merkle_tree(leaves)

leaves = ["apple", "banana", "cherry", "date",]
modified = build_merkle_tree(leaves)

if original == modified:
    print('The transections are not modified')
else:
    print('The transections are modified')
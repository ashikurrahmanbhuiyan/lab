import hashlib

# Function to compute the hash of a value
def hash_data(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

# Function to create a Merkle Tree
def create_merkle_tree(leaf_nodes):
    if len(leaf_nodes) % 2 != 0:  # Ensure even number of nodes
        leaf_nodes.append(leaf_nodes[-1])

    tree = [leaf_nodes]
    current_level = leaf_nodes

    while len(current_level) > 1:
        next_level = []
        for i in range(0, len(current_level), 2):
            combined_hash = hash_data(current_level[i] + current_level[i+1])
            next_level.append(combined_hash)
        tree.append(next_level)
        current_level = next_level

    return tree

# Function to generate proof of membership for a leaf node
def generate_proof(tree, index):
    proof = []
    for level in tree[:-1]:
        sibling_index = index ^ 1  # XOR with 1 to get sibling index
        proof.append(level[sibling_index])
        index //= 2  # Move to the parent index
    return proof

# Function to verify proof of membership
def verify_proof(leaf, proof, root, index):
    current_hash = hash_data(leaf)
    for sibling in proof:
        if index % 2 == 0:  # If current index is even
            current_hash = hash_data(current_hash + sibling)
        else:  # If current index is odd
            current_hash = hash_data(sibling + current_hash)
        index //= 2
    return current_hash == root

# Example usage
if __name__ == "__main__":
    # Step 1: Define 4 leaf nodes
    leaf_nodes = [hash_data(f"Leaf {i}") for i in range(4)]

    # Step 2: Build Merkle Tree
    merkle_tree = create_merkle_tree(leaf_nodes)

    # Step 3: Extract the Merkle Root
    merkle_root = merkle_tree[-1][0]
    print("Merkle Root:", merkle_root)

    # Step 4: Verify proof of membership for a specific leaf
    leaf_index = 2  # Index of the leaf to verify
    proof = generate_proof(merkle_tree, leaf_index)
    print("Proof for Leaf Index", leaf_index, ":", proof)

    is_valid = verify_proof(leaf_nodes[leaf_index], proof, merkle_root, leaf_index)
    print(f"Leaf {leaf_index} is {'valid' if is_valid else 'invalid'} in the Merkle Tree.")


import hashlib
import math

class MerkleTree:
    def __init__(self, data):
        self.data = data
        self.tree = []
        self.build_tree()

    @staticmethod
    def hash_data(data):
        return hashlib.sha256(data.encode()).hexdigest()

    def build_tree(self):
        num_leaves = len(self.data)
        full_size = 2 ** math.ceil(math.log2(num_leaves))  
        leaf_level = []
        for d in self.data:
            leaf_level.append(self.hash_data(d))

        while len(leaf_level) < full_size:
            leaf_level.append(self.hash_data("")) 

        self.tree = [None] * (2 * full_size)

        for i in range(full_size):
            self.tree[full_size + i] = leaf_level[i]

        for i in range(full_size - 1, 0, -1):
            left_child = self.tree[2 * i]
            right_child = self.tree[2 * i + 1]
            self.tree[i] = self.hash_data(left_child + right_child)

    def get_root(self):
        return self.tree[1] 

    def get_proof(self, index,leaf,root):
        num_leaves = len(self.data)
        full_size = 2 ** math.ceil(math.log2(num_leaves))
        array_index = full_size + index
        current_hash = hashlib.sha256(leaf.encode()).hexdigest()

        while array_index > 1:
            print(current_hash)
            if array_index % 2 != 0:
                current_hash = self.hash_data(self.tree[array_index - 1] + current_hash)
            else:
                current_hash = self.hash_data(current_hash + self.tree[array_index + 1])  
            array_index //= 2
            self.tree[array_index] = current_hash

        return current_hash == root



    def print_tree(self):
        print("Binary Tree Representation:")
        for i in range(1, len(self.tree)):
            print(f"Index {i}: {self.tree[i]}")


# Example usage
if __name__ == "__main__":
    data = ["data1", "data2", "data3", "data4"]
    tree = MerkleTree(data)

    print("Merkle Tree:")
    tree.print_tree()

    root = tree.get_root()
    print("\nRoot Hash:", root)

    # Generate proof for the second leaf (index 1, "data2")
    index=1
    is_valid = tree.get_proof(index,"data2",root)
    print("\nProof verification result:", is_valid)
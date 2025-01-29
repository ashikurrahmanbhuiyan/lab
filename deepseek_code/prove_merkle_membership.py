import hashlib

def calculate_hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

def build_merkle_tree(transactions):
    if len(transactions) == 1:
        return transactions[0]

    new_level = []
    for i in range(0, len(transactions) - 1, 2):
        combined = transactions[i] + transactions[i + 1]
        new_level.append(calculate_hash(combined))

    if len(transactions) % 2 != 0:
        new_level.append(transactions[-1])

    return build_merkle_tree(new_level)

def verify_membership(merkle_root, transaction, proof):
    current_hash = calculate_hash(transaction)
    for p in proof:
        if p[1] == 'left':
            current_hash = calculate_hash(p[0] + current_hash)
        else:
            current_hash = calculate_hash(current_hash + p[0])
    return current_hash == merkle_root

transactions = ["tx1", "tx2", "tx3", "tx4"]
merkle_root = build_merkle_tree(transactions)

# Proof for tx2
proof = [("tx1", 'left'), (calculate_hash("tx3" + "tx4"), 'right')]
is_member = verify_membership(merkle_root, "tx2", proof)
print(f"Is 'tx2' a member of the Merkle Tree? {is_member}")

# Proof for non-member "tx5"
proof = [("tx1", 'left'), (calculate_hash("tx3" + "tx4"), 'right')]
is_member = verify_membership(merkle_root, "tx5", proof)
print(f"Is 'tx5' a member of the Merkle Tree? {is_member}")
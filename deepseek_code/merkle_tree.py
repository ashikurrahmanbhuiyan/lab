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

transactions = ["tx1", "tx2", "tx3", "tx4"]
merkle_root = build_merkle_tree(transactions)
print(f"Merkle Root: {merkle_root}")
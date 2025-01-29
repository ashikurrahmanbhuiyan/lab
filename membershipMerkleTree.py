import hashlib

merkle_tree = {
    'root': '0899981ba6c88f9de81fc5475f6fc65db9392cd719deb08cbef448f52d6e2b11',
    'levels': [
        [   'ca978112ca1bbdcafac231b39a23dc4da786eff8147c4e72b9807785afee48bb',
            '3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d',
            '2e7d2c03a9507ae265ecf5b5356885a53393a2029d241394997265a1a25aefc6',
            '18ac3e7343f016890c510e93f935261169d9e3f565436429830faf0934f4f8e4'],
        [
            '62af5c3cb8da3e4f25061e829ebeea5c7513c54949115b1acc225930a90154da',
   '57e65b2997916fb520d5c670b181dadbc7c0824c7973f8d3550a7d74734fbef6'
        ],
        [
            '0899981ba6c88f9de81fc5475f6fc65db9392cd719deb08cbef448f52d6e2b11'
        ]
    ]
}


def generate_merkle_proof(element_hash, merkle_tree):
    proof = []
    current_hash = element_hash

    for level in merkle_tree['levels']:
        if len(level) == 1:  # Only the root remains
            break
        if current_hash in level:
            index = level.index(current_hash)
            sibling_index = index - 1 if index % 2 else index + 1

            if sibling_index < len(level):  # Ensure sibling exists
                sibling_hash = level[sibling_index]
                proof.append(sibling_hash)

            # Concatenate the current hash and sibling hash (in correct order)
            if index % 2 == 0:  # If current hash is a left child
                current_hash = hashlib.sha256((current_hash + sibling_hash).encode()).hexdigest()
            else:  # If current hash is a right child
                current_hash = hashlib.sha256((sibling_hash + current_hash).encode()).hexdigest()
    return proof

element = 'c'
element_hash = hashlib.sha256(element.encode()).hexdigest()
proof = generate_merkle_proof(element_hash, merkle_tree)

# Verifying the Merkle proof
current_hash = element_hash
for sibling_hash in proof:
    if proof.index(sibling_hash) % 2 == 0:
        current_hash = hashlib.sha256((current_hash + sibling_hash).encode()).hexdigest()
    else:
        current_hash = hashlib.sha256((sibling_hash + current_hash).encode()).hexdigest()

if current_hash == merkle_tree['root']:
    print('Merkle Proof is valid')
else:
    print('Merkle Proof is invalid')

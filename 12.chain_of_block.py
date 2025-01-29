import hashlib
import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        hash_string = str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(hash_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    # def traverse(self):
    #     for block in self.chain:
    #         print(f"Timestamp: {block.timestamp}")
    #         print(f"Data: {block.data}")
    #         print(f"Previous Hash: {block.previous_hash}")
    #         print(f"Hash: {block.hash}")
    #         print()

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True

blockchain = Blockchain()
blockchain.add_block(Block(datetime.datetime.now(), "Block 1", ""))
blockchain.add_block(Block(datetime.datetime.now(), "Block 2", ""))
blockchain.add_block(Block(datetime.datetime.now(), "Block 3", ""))

# blockchain.traverse()

print("Is blockchain valid?", blockchain.is_valid())

blockchain.chain[1].data = "Modified Block"

print("Is manipulated blockchain valid?", blockchain.is_valid())

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, transactions, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.transactions = transactions
        self.hash = hash


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        # Create the first block (genesis block)
        genesis_block = Block(0, "0", time.time(), [], self.calculate_hash(0))
        self.chain.append(genesis_block)

    def add_block(self, transactions):
        # Add a new block to the blockchain
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        hash_value = self.calculate_hash(index)

        new_block = Block(index, previous_block.hash, timestamp, transactions, hash_value)
        self.chain.append(new_block)

    def calculate_hash(self, index):
        # Calculate the hash for the block
        return hashlib.sha256(str(index).encode('utf-8')).hexdigest()


python
Copy code
# Sample data
transactions_data = [
    {"TransactionNo": 581482, "Date": "12-09-2019", "ProductNo": 22485, "ProductName": "Set Of 2 Wooden Market Crates", "Price": 21.47, "Quantity": 12, "CustomerNo": 17490, "Country": "United Kingdom"},
    # ... Add more transactions as needed
]

# Create a blockchain instance
blockchain = Blockchain()

# Process transactions and add blocks to the blockchain
for transaction in transactions_data:
    blockchain.add_block(transaction)
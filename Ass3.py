import hashlib
import json
from datetime import datetime


# Create a block
def create_block(transaction_data, previous_block_hash):
    """Create and return a blockchain block for the given data."""
    block = {
        "index": len(blockchain) + 1,
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "data": transaction_data,
        "previous_hash": previous_block_hash
    }

    block["hash"] = calculate_hash(block)
    return block


# Calculate SHA-256 hash of a block
def calculate_hash(block_to_hash):
    """Calculate and return the SHA-256 hash of a block."""
    block_data = {
        key: value
        for key, value in block_to_hash.items()
        if key != "hash"
    }

    encoded_data = json.dumps(
        block_data, sort_keys=True
    ).encode("utf-8")

    return hashlib.sha256(encoded_data).hexdigest()


# Create the blockchain list
blockchain = []

# Create the Genesis Block
genesis_block = create_block(
    "Genesis Block", "0"
)
blockchain.append(genesis_block)


# Add new blocks using user input
while True:
    data = input(
        "\nEnter transaction data (or 'exit' to stop): "
    )

    if data.lower() == "exit":
        break

    previous_hash = blockchain[-1]["hash"]

    new_block = create_block(data, previous_hash)
    blockchain.append(new_block)

    print("\nBlock added successfully!")


# Display the blockchain
print("\n========== BLOCKCHAIN ==========")

for block in blockchain:
    print("\nBlock Index:", block["index"])
    print("Timestamp:", block["timestamp"])
    print("Data:", block["data"])
    print("Previous Hash:", block["previous_hash"])
    print("Block Hash:", block["hash"])


# Verify the blockchain
print("\n========== VERIFICATION ==========")

valid = True

for i in range(1, len(blockchain)):
    current = blockchain[i]
    previous = blockchain[i - 1]

    if current["previous_hash"] != previous["hash"]:
        valid = False
        break

    if current["hash"] != calculate_hash(current):
        valid = False
        break

if valid:
    print("Blockchain is VALID.")
else:
    print("Blockchain is INVALID.")

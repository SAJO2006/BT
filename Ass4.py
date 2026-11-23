
from web3 import Web3
from getpass import getpass

# Connect to Sepolia Test Network
rpc_url = input("Enter Alchemy Sepolia RPC URL: ")
web3 = Web3(Web3.HTTPProvider(rpc_url))

if not web3.is_connected():
    print("Connection Failed!")
    exit()

print("Connected to Sepolia Testnet")

# Enter private key securely
private_key = getpass("Enter test wallet private key: ")

# Get sender address automatically
account = web3.eth.account.from_key(private_key)
sender = account.address

print("Sender Address:", sender)

# Enter receiver address
receiver = input("Enter receiver wallet address: ")

# Check balance
balance = web3.from_wei(
    web3.eth.get_balance(sender), "ether"
)

print("Wallet Balance:", balance, "Sepolia ETH")

# Transfer amount
amount = web3.to_wei(0.001, "ether")

if balance < web3.from_wei(amount, "ether"):
    print("Insufficient balance!")
    exit()

# Create transaction
transaction = {
    "nonce": web3.eth.get_transaction_count(sender),
    "to": receiver,
    "value": amount,
    "gas": 21000,
    "gasPrice": web3.eth.gas_price,
    "chainId": 11155111
}

# Sign transaction
signed_txn = account.sign_transaction(transaction)

# Send transaction
tx_hash = web3.eth.send_raw_transaction(
    signed_txn.raw_transaction
)

print("Transaction Hash:", web3.to_hex(tx_hash))

# Wait for confirmation
receipt = web3.eth.wait_for_transaction_receipt(tx_hash)

if receipt.status == 1:
    print("Transaction Successful!")
else:
    print("Transaction Failed!")

print("Block Number:", receipt.blockNumber)
print("Gas Used:", receipt.gasUsed)
print("Verify at: https://sepolia.etherscan.io/tx/" + web3.to_hex(tx_hash))

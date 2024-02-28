from bottle import Bottle, run, template
from web3 import Web3

app = Bottle()

# Connect to a local Ethereum node
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/4b967b642e0d41ff842b642bb2f9d701'))

@app.route('/')
def index():
    # Check if connected to Ethereum node
    if w3.isConnected():
        block_number = w3.eth.blockNumber
        return template("Connected to Ethereum node. Latest block number: {{block_number}}", block_number=block_number)
    else:
        return "Not connected to an Ethereum node."

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)

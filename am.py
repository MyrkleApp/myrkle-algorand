from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

algod_address = "https://node.testnet.algoexplorerapi.io"
algod_token = ""

# algod_client = AlgodClient(algod_token, algod_address)
# print(algod_client.status())



indexe = IndexerClient(indexer_address="https://testnet-idx.algonode.cloud", indexer_token="")
print(indexe.health())
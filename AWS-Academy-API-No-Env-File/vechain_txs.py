from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract
from decouple import config
import boto3
import base64
from botocore.exceptions import ClientError
import time
import os

#Connect to Veblocks and import the DHN contract
def init():
    print("------------------Connect to Veblocks------------------\n")
    #https://mainnet.veblocks.net
    #SayNode testnet node : http://3.71.71.72:8669/doc/swagger-ui/
    #SayNode mainnet node : http://3.124.193.149:8669/doc/swagger-ui/
    connector = Connect("http://3.71.71.72:8669")
    print("------------------IMPORT DHN CONTRACT------------------\n")
    _contract = Contract.fromFile("./build/contracts/DHN.json")
    DHN_contract_address = '0x0867dd816763BB18e3B1838D8a69e366736e87a1'
    return connector, _contract, DHN_contract_address

#Import wallets from mnemonic (this should be only one, but for know we need 2 for testing)
def wallet_import_1(connector):
    #MNEMONIC_1 = config('MNEMONIC_1')
    MNEMONIC_1 = os.environ['MNEMONIC_1']
    testwallet1 = Wallet.fromMnemonic(MNEMONIC_1.split(', '))
    testWallet1_address= testwallet1.getAddress()
    print("Wallet address: " + testWallet1_address)
    print("Wallet VET balance: " + str(connector.get_vet_balance(testWallet1_address)))
    print("Wallet VTHO balance: " + str(connector.get_vtho_balance(testWallet1_address)))
    return testwallet1, testWallet1_address

#Get wallet balances, we use "call" in order to not waste any gas (once again this should be separated, but it will be done when ready 
# to deploy)
def wallet_balance(connector,_contract, DHN_contract_address, testWallet1_address, testWallet2_address):
    print("Wallet1:")
    balance_one = connector.call(
        caller=testWallet1_address, # fill in your caller address or all zero address
        contract=_contract,
        func_name="balanceOf",
        func_params=[testWallet1_address],
        to=DHN_contract_address,
    )
    print(balance_one["decoded"]["0"])

    print("Wallet2:")
    balance_two = connector.call(
        caller=testWallet2_address, # fill in your caller address or all zero address
        contract=_contract,
        func_name="balanceOf",
        func_params=[testWallet2_address],
        to=DHN_contract_address,
    )
    print(balance_two["decoded"]["0"]) 

#Transfer DHN tokens
def transfer_DHN(connector, DHN_contract_address, testwallet1, receiver_address, amount):
    connector.transfer_token(
        testwallet1, 
        to=receiver_address,
        token_contract_addr= DHN_contract_address, 
        amount_in_wei=amount
    ) 

def balances(wallet_id_one, wallet_id_two):
    print("------------------Connect to Veblocks------------------")
    print("------------------IMPORT DHN CONTRACT------------------\n")
    (connector, _contract, DHN_contract_address)=init()

    balance_one = connector.call(
        caller=wallet_id_one, # fill in your caller address or all zero address
        contract=_contract,
        func_name="balanceOf",
        func_params=[wallet_id_one],
        to=DHN_contract_address,
    )
  
    balance_two = connector.call(
        caller=wallet_id_two, # fill in your caller address or all zero address
        contract=_contract,
        func_name="balanceOf",
        func_params=[wallet_id_two],
        to=DHN_contract_address,
    )
    
    return balance_one["decoded"]["0"], balance_two["decoded"]["0"]

def main(wallet_id,reward):
    reward = float(reward)
    reward = int(reward*(10**18))
    print("------------------Connect to Veblocks------------------")
    print("------------------IMPORT DHN CONTRACT------------------\n")
    (connector, _contract, DHN_contract_address)=init()
    print("------------------WALLET 1------------------\n")
    (testwallet1, testWallet1_address)=wallet_import_1(connector)

    print("------------------DHN Balances Before Transfer------------------\n")
    wallet_balance(connector,_contract, DHN_contract_address, testWallet1_address, wallet_id)
    print("------------------Transfer DHN Tokens------------------\n")
    transfer_DHN(connector, DHN_contract_address, testwallet1, wallet_id, reward)
    print("------------------DHN Balances After Transfer------------------\n")
    wallet_balance(connector,_contract, DHN_contract_address, testWallet1_address, wallet_id) 

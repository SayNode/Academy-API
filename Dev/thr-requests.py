from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract
from thor_devkit import cry
from thor_devkit.cry import hdnode
import os
from decouple import config


connector = Connect("https://testnet.veblocks.net")

print("------------------WALLET 1------------------\n")
MNEMONIC_1 = config('MNEMONIC_1')
testwallet1 = Wallet.fromMnemonic(MNEMONIC_1.split(', '))
testWallet1_address= testwallet1.getAddress()
print("Wallet address: " + testWallet1_address)
print("Wallet VET balance: " + str(connector.get_vet_balance(testWallet1_address)))
print("Wallet VTHO balance: " + str(connector.get_vtho_balance(testWallet1_address)))

print("------------------WALLET 2------------------\n")
MNEMONIC_2 = config('MNEMONIC_2')
testwallet2 = Wallet.fromMnemonic(MNEMONIC_2.split(', '))
testWallet2_address= testwallet2.getAddress()
print("Wallet address: " + testWallet2_address)
print("Wallet VET balance: " + str(connector.get_vet_balance(testWallet2_address)))
print("Wallet VTHO balance: " + str(connector.get_vtho_balance(testWallet2_address)))

print("------------------DEPLOY DHN CONTRACT------------------\n")
_contract = Contract.fromFile("./build/contracts/MyToken.json")

print("------------------Transfer DHN Tokens------------------\n")
connector.transfer_token(
    testWallet1_address, 
    to=testWallet2_address,
    #token_contract_addr= #insert token address, 
    amount_in_wei=10 * (10 ** 18)
)
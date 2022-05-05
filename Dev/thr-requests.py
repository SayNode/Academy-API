from thor_requests.connect import Connect
from thor_requests.wallet import Wallet
from thor_requests.contract import Contract
from thor_devkit import cry
from thor_devkit.cry import hdnode
import os
from decouple import config
import time


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
DHN_contract_address = '0x299fBe0c9f605d7897694413c774c60892DB631f'

print("------------------Mint tokens to Wallet One------------------\n")
""" get_tokens = connector.transact(
    testwallet1, # fill in your caller address or all zero address
    _contract,
    "mint",
    [testWallet1_address],
    to=DHN_contract_address,
    value=0
)
print(get_tokens) """


print("------------------DHN Balances Before Transfer------------------\n")
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

print("------------------Transfer DHN Tokens------------------\n")
connector.transfer_token(
    testwallet1, 
    to=testWallet2_address,
    token_contract_addr= DHN_contract_address, 
    amount_in_wei=1
) 

#Sleep for 10 seconds to allow for the tx to be processed
time.sleep(10)

print("------------------DHN Balances After Transfer------------------\n")
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
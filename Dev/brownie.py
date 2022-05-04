from brownie import accounts, config, chain, Contract, DHN 
import time
import os

def deploy():
    #A)For local ganache
        #dohrnii_account = accounts[0] 

    #B)To import a wallet you need to do on the terminal:
        #1)brownie accounts new <name of the account>
        #2)Enter "0x"+ the private key you wish to import
        #3)Enter a password of your choosing to encrypt the account
        #To load account in this code: account = accounts.load("SAYNODE")

    #C)If we want to use .env
        #1)Create a .env file
        #2)Add "export PRIVATE_KEY = <wallet private key>" to it
        #3)Use the code bellow:
    SayNode_account = accounts.add(os.getenv("PRIVATE_KEY"))
    #D)Using "wallets" section in brownie-config.yaml:
        #1)Define the wallets in the brownie-config.yaml
        #2)Do the code bellow:
        #account = accounts.add(config["wallets"]["from_key"])
    
    #Deployment
    dohrnii_token_contrat = DHN.at("0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87")


    return SayNode_account, dohrnii_token_contrat

#Testing createDS() from DataSetFactory.sol
def transferRewards(dec_fit, DHN, SayNode_account, wallet_id, reward):
    print("------------------Transfer------------------")
    DHN.transfer(wallet_id, reward*dec_fit, {"from": SayNode_account}) #creator approves that the DSF contract 
                                                       #can send tokens to the DS contract (amount = stakeAmount)



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
        account = accounts.add(os.getenv("PRIVATE_KEY"))
    #D)Using "wallets" section in brownie-config.yaml:
        #1)Define the wallets in the brownie-config.yaml
        #2)Do the code bellow:
        #account = accounts.add(config["wallets"]["from_key"])
    
    #Deployment
    #Call existing contract:dohrnii_token_contrat = DHN.at("0x3194cBDC3dbcd3E11a07892e7bA5c3394048Cc87")(dohrnii_account,{"from": dohrnii_account})
    dohrnii_token_contrat = DHN.deploy(dohrnii_account,{"from": dohrnii_account})


    return dohrnii_token_contrat

#Testing createDS() from DataSetFactory.sol
def createDS(dec_fit, DHN, DSF, ds_creator_account, DS_name, DS_IPFS_link, ds_category, ds_desc, ds_sub_price, update_freq, penalty):
    print("------------------Creating a DS------------------")
    DHN.approve(DSF,30*dec_fit, {"from": ds_creator_account}) #creator approves that the DSF contract 
                                                       #can send tokens to the DS contract (amount = stakeAmount)

    DSF.createDS(DS_name, DS_IPFS_link, ds_category, ds_desc, ds_sub_price, update_freq, penalty, 
                {"from": ds_creator_account}) #DS created


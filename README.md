# Academy-API
## Instructions
> pip install -r requirments.txt

## Prerequisites
Please install or have installed the following:

- nodejs and npm
- python

## Installation
1) Install Brownie, if you haven't already. Here is a simple way to install brownie.
   
> pip install eth-brownie

Or, if that doesn't work, via pipx

> pip install --user pipx
> 
> pipx ensurepath
> 
> #restart your terminal
> 
> pipx install eth-brownie

1) For local testing install ganache-cli
> npm install -g ganache-cli

or

> yarn add global ganache-cli

3) Download the mix and install dependancies.
> brownie bake upgrades-mix

> cd upgrades

## Use rinkeby
- Simply define WEB3_INFURA_PROJECT_ID on the .env file and run:
    > brownie run ./Dev/brownie.py --network rinkeby

- If Brownie does not regognize the WEB3_INFURA_PROJECT_ID variable, than there are two options:
    1) Create a new network equal to rinkeby, manually:
        > brownie networks add live *NetworkName* host=*hostlink* chainid=*chainID*

        > brownie run *FileName* --network *NetworkName*

    2) Add the WEB3_INFURA_PROJECT_ID to your user enviornment variables:
      https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

## Use vechain
- We need to add the vechain network manually, as it is not pre-programmed into the brownie networks
    > brownie networks add live Vechain host=*LocalNodeLink* chainid=*random*

    > brownie run *FileName* --network Vechain
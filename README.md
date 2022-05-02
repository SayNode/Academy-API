# Academy-API
## Instructions
> pip install -r requirments.txt
## Main components:
- **RewardValue variable**: kept in the backend. It can be altered by the Dohrnii foundation. State sthe amount of tokens to be received currently, for answering a quesionnaire;
- **Database for user/questionnaire interactions**: This DB keeps a record of every questionnaire each user has interacted with (clicked the button which links to it). This makes it easier for API access because we can just request "/UserId" or "/QuestID" if we want to get just specific data. 
This DB has 4 fields:
    1) User ID(most likely the wallet address)
    2) Questionnaire ID
    3) Status of the questionnaire (*clicked on*, *answered*, *reward collected*)
    4) Amount of DHN tokens rewarded (this depends on the **RewardValue** at the time of *reward collected* status update)
- **Brownie backend**: to trigger the transaction from the foundation to the user
- **A Vechain Wallet Reserve**: to fund the transactions. This may require a **DHN/VET Pool** for automated funding
- **Flask API**: to connect the Dohrnii server (all the previously described functionalities) to the user
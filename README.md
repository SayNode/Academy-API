# Academy-API
## Main components:
- **RewardValue** variable kept in the backend. It can be altered by the Dohrnii foundation. State sthe amount of tokens to be received currently, for answering a quesionnaire;
- Database for user/questionnaire interactions. This DB keeps a record of every questionnaire each user has interacted with (clicked the button which links to it). This makes it easier for API access because we can just request "/UserId" or "/QuestID" if we want to get just specific data. 
This DB has 4 fields:
    1) User ID
    2) Questionnaire ID
    3) Status of the questionnaire (*clicked on*, *answered*, *reward collected*)
    4) Amount of DHN tokens rewarded (this depends on the **RewardValue** at the time of *reward collected* status update)
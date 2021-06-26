from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer





chatbot = ChatBot(
    'chatGO',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='postgresql://postgres:data123@127.0.0.1:5432/chatGO_DB'
)

conv = [
'restaurants?',
'type the area you are in',
'Are you a robot?',
'Yes, My name is chatGO', 
'Are you a bot?',
'Yes, My name is chatGO',
'Are you a chatbot?',
'Yes, My name is chatGO',
'Are you real?',
'I am a ChatBot, My name is chatGO',
'What is your name?',
'My name is chatGO',
'Who made you?',
'Yigal Salem made me',
'What do you do?',
'I am made to give local info']


trainer = ListTrainer(chatbot)

trainer.train(conv)




while True:
    request = input('You: ')
    response = chatbot.get_response(concierge.google_API.GoogleMapsClient)
    print('Bot: ', response)






from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


class TrainChatBot:
    def __init__(self):
        chatbot = ChatBot(
            'SmallDay',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Sorry, I did not understand your problem. Please select any of the following'
                                        '\n1. Email'
                                        '\n2. Os'
                                        '\n3. Support',
                    'maximum_similarity_threshold': 0.90
                }
            ]
        )
        trainer = ListTrainer(chatbot)
        trainer.train([
            "Good Morning",
            "How Can i help you?",
            "Hi",
            "Hello, How are you?",
            "Good",
            "Thank you",
            "Thank you",
            "Your Welcome",
            "I need help",
            "How can i help you?",
            "email not working",
            "I will help you to fix this issue",
            "My email is not working",
            "Did you check Internet connection?",
            "Email Configuration",
            "Please visit www.smalldaytech.com to email Configuration",
            "Outlook Configuration",
            "Please visit www.smalldaytech.com to email Configuration",
            "Why email is not working",
            "Please click on the link below to fix your problem\n <a href ='https://www.smalldaytech.com' target='_blank'>"
            " click here</a>"
        ])



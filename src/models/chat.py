from chatterbot import ChatBot


class Chat(object):
    def __init__(self):
        pass

    def train_data(self, client_data):
        chatbot = ChatBot(
            'SmallDay',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'Sorry, I did not understand your problem, <br/>I will learn it.<br/> Please select any of the following'
                                        '<br/>1. Email'
                                        '<br/>2. Os'
                                        '<br/>3. Support',
                    'maximum_similarity_threshold': 0.90
                }
            ]
        )

        return chatbot.get_response(client_data)






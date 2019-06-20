import pickle

# from sklearn.externals import joblib


class Helper:
    def __init__(self):
        self.file_name = 'training_data.sd'

    def save_train_data(self, train_data):
        pickle.dump(train_data, open(self.file_name, "wb"))
        # with open(self.file_name, 'wb') as f:
        #     pickle.dump(train_data, f)

    def get_train_data(self):
        with open(self.file_name, 'rb') as f:
            return pickle.load(f)

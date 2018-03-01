import fasttext

class FasttextClassifier(object):
    
    def __init__(self):

        """ You can load your pre-trained model in here. The instance will be created once when the docker container starts running on the cluster. """
        self.model = fasttext.load_model('fasttext_py_model.bin')

    def predict(self, texts):
        "texts is a python list of amazon reviews" 
        return self.model.predict(texts)
        
        
    
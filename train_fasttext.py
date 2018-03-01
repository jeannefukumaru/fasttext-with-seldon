import fasttext

def main():
    # train a supervised text classification model. 
    # returns two output files fasttext_py_model.bin and fasttext_py_model.vec 
    classifier = fasttext.supervised('amzn-data/train.ft.txt', 'fasttext_py_model')
    print("training and saving done!")

    print('testing model on new data')
    result = classifier.test('amzn-data/test.ft.txt')
    print('P@1:', result.precision)
    print('R@1:', result.recall)
    print('Number of examples:', result.nexamples)
    
if __name__ == "__main__":
    main()


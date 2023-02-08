import pickle
import sys
util_path = './utils'
sys.path.insert(0, util_path)
import util
from sklearn.feature_extraction.text import TfidfVectorizer

# load the model
filename = './result/model1/Random Forest/RandomForest_model.sav'

loaded_model = pickle.load(open(filename, 'rb'))

# prediction function
def predict_sexism(text, model, tfidf):
    text = util.process_text(text, model=1)
    text_vec = tfidf.transform([text]) # transform or fit_transform
    prediction = model.predict(text_vec)
    return prediction[0]

# test the function
example_text = "I was told no woman who had children under the age of 6 had any business being outside the home."
loaded_vectorizer = pickle.load(open("./result/model1/Random Forest/vectorizer.pickle", 'rb'))
pred = predict_sexism(example_text, loaded_model, loaded_vectorizer)
print(pred) # should print 'not sexist' or 'sexist'

import pickle
import sys
util_path = '../models/utils'
sys.path.insert(0, util_path)
import util
from sklearn.feature_extraction.text import TfidfVectorizer

# save the model
filename = '../result/model1/Logistic Regression/logistic_regression_model.sav'

# load the model
loaded_model = pickle.load(open(filename, 'rb'))

# prediction function
def predict_sexism(text, model, tfidf):
    text = util.process_text(text, model=1)
    text_vec = tfidf.transform([text]) # transform or fit_transform
    prediction = model.predict(text_vec)
    return prediction[0]

# test the function
example_text = "I was told no woman who had children under the age of 6 had any business being outside the home."
tfidf = TfidfVectorizer()
pred = predict_sexism(example_text, loaded_model, tfidf)
print(pred) # should print 'not sexist' or 'sexist'

# pickle.dump(vectorizer, open("vectorizer.pickle", "wb")) //Save vectorizer
# pickle.load(open("vectorizer.pickle", 'rb'))     // Load vectorizer
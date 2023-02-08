import pickle
import sys
util_path = '/content/drive/MyDrive/markov/utils'
sys.path.insert(0, util_path)
import util
from sklearn.feature_extraction.text import TfidfVectorizer

# load the model
filename = '/content/drive/MyDrive/markov/result/model1/Logistic Regression/logistic_regression_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# prediction function
def predict_sexism(text, model, tfidf):
    text = util.process_text(text, model=1)
    text_vec = tfidf.transform([text]) # transform or fit_transform
    prediction = model.predict(text_vec)
    return prediction[0]

# test the function
example_text = "I was told no woman who had children under the age of 6 had any business being outside the home."
loaded_vectorizer = pickle.load(open("/content/drive/MyDrive/markov/vectorizer.pickle", 'rb'))
pred = predict_sexism(example_text, loaded_model, loaded_vectorizer)
print(pred) # should print 'not sexist' or 'sexist'


# x_train_a, x_test_a, y_train_a, y_test_a = train_test_split(df_under.processed_text, df_under['label_sexist'], test_size=0.05, train_size=0.95, random_state=5, shuffle=True)
# pred_test = df_pred.processed_text
# # this one better for vectors
# tfidf_vectorizer = TfidfVectorizer() 
# train_vectors = tfidf_vectorizer.fit_transform(x_train_a)
# pickle.dump(vectorizer, open("vectorizer.pickle", "wb")) //Save vectorizer
# train fit model classifier function()
# pickle dump the model

# pickle.load(open("vectorizer.pickle", 'rb'))     // Load vectorizer
# test_vectors = tfidf_vectorizer.transform(pred_test)
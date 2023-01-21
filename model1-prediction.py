import pickle

# save the model
filename = 'logistic_regression_model.sav'
pickle.dump(lrm, open(filename, 'wb'))

# load the model
loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(x_test_a, y_test_a)
print(result)

# prediction function
def predict_sexism(text, model, tfidf, lemmatizer, stop_words):
    text = process_text(text, lemmatizer, stop_words)
    text_vec = tfidf.transform([text])
    prediction = model.predict(text_vec)
    return prediction[0]

# test the function
example_text = "I was told no woman who had children under the age of 6 had any business being outside the home."
pred = predict_sexism(example_text, loaded_model, tfidf, lemmatizer, stop_words)
print(pred) # should print 'not sexist' or 'sexist'

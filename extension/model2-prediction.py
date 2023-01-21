import torch

# saving the model
torch.save(model.state_dict(), 'MLP_model.pth')

# prediction function
def predict_sexism(x):
  x = tfidfvectorizer.transform([x]).toarray()
  x = torch.tensor(x, dtype=torch.float64)
  model.load_state_dict(torch.load('MLP_model.pth'))
  pred = model(x_in=x.float().to(device))
  y_1 = (pred).to('cpu').detach().numpy()
  ind=(y_1).argmax(axis = 1)
  y_dim = y_1.shape[1]
  l = [0 for i in range(y_dim)]
  for i in range(y_dim):
      if i==ind:
          l[i] = 1
  y_1 = mlb.inverse_transform(np.array(l).reshape(1,2))
  return y_1

# testing
text = "women are weak and inferior"
test_pred=predict_sexism(text)
print(test_pred)

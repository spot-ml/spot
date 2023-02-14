import numpy as np
import pickle
import sys
util_path = '../models/utils'
sys.path.insert(0, util_path)
import util
import torch
import torch.nn as nn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MultiLabelBinarizer

class MLP(nn.Module):
  '''Multi-layered perceptron based classifier'''
  def __init__(self, num_features,out_features):
    """
    Args:
        num_features (int): the size of the input feature vector
    """
    super(MLP, self).__init__()
    self.fc1 = nn.Linear(in_features=num_features, out_features=64)
    print("num f:", num_features)
    self.fc2 = nn.Linear(in_features=64,out_features=32)
    self.fc3 = nn.Linear(in_features=32,out_features=out_features)

  def forward(self, x_in, apply_softmax=False):
    """The forward pass of the classifier
    
    Args:
        x_in (torch.Tensor): an input data tensor. 
            x_in.shape should be (batch, num_features)
        apply_softmax (bool): a flag for the sigmoid activation
            should be false if used with the Cross Entropy losses
    Returns:
        the resulting tensor. tensor.shape should be (batch,)
    """
    y_out_1 = torch.relu(self.fc1(x_in))
    y_out_2 = self.fc2(y_out_1)
    y_out = self.fc3(y_out_2)
    return y_out 

def predict_sexism(x):
  x = util.process_text(x, model=1)
  x = loaded_vectorizer.transform([x]).toarray()
  x = torch.tensor(x, dtype=torch.float64)
  device = torch.device("cpu")
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


loaded_vectorizer = pickle.load(open("../result/model2/vectorizer.pickle", 'rb'))
mlb = pickle.load(open("../result/model2/mlbinarizer.pickle", "rb"))
model = MLP(1988, 2)
model.load_state_dict(torch.load('../result/model2/trained_model2.pth', map_location=torch.device('cpu')))

text = "Women are weak and inferior"
test_pred=predict_sexism(text)
print(test_pred)

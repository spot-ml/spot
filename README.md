# spot

Project SPOT: Sexist Profane Offensive Texts

## Aim

This project aims to battle online hate speech. Through this project we can sucessfully detect the sexist text from the input text comments. This project will be useful for researchers and practitioners interested in developing systems for filtering online hate speech. The ML models will be deployed through the medium of a Chrome extension which can be used to see if a certain piece of text online is hateful or not.

## Contents

- **[Datasets](./datasets/)**: This folder contains all the different dataset files which will be used to create a master dataset for training our models
- **[Extension](./extension/)**: This folder contains all the code for developing and deploying a chrome extension
- **[Models](./models/)**: This folder contains all the different machine learning models used for the project ranging from simple regression techniques to NLP-heavy models
- **[Result](./result/)**: This folder contains all the different machine learning models's classification report and their important checkpoint files of their best version
- **[Test](./test/)**: This folder files for testing the functionality of different models when predicting a piece of text 'sexist' or 'not sexist'

## Installation
### For training 
- Firstly clone the repository by `git clone https://github.com/spot-ml/spot.git`
- Run the python notebook file in the models repository, There were two python notebook file first is the **[Model1_Conventional.ipynb](./models/)** in which there are 4 traditional classifier are used and in the second file the MLP classifier **[Model2_MLP.ipynb](./models/)** is used to detect the sexist text.
- Once verify the file path of dataset, utils and result saving.

### Testing purpose
- Firstly clone the repository by `git clone https://github.com/spot-ml/spot.git`
- Run the **[test_model1.py](./test/)** file for test the model-1
- Run the **[test_model2.py](./test/)** file for test the model-2
- For testing the sentence of your choice, then set the sentence in the example_text variable of the testing files.
- Once verify the file path of utils, loaded model and loaded vectorizer path.

## Contribution 
- Create a feature branch, preferably with the name `feature/<small-description>` and commit your features into it.
- Create a merge request to push code from your feature branch into `main` branch which will be reviewed.
- Once the code is reviewed and approved by atleast one developer, it would be merged to `main`.

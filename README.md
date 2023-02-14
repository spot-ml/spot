# spot

Project SPOT: Sexist Profane Offensive Texts

## Aim

This project aims to battle online hate speech. The ML models will be deployed through the medium of a Chrome extension which can be used to see if a certain piece of text online is hateful or not.

## Contents

- **[Datasets](./datasets/)**: This folder contains all the different dataset files which will be used to create a master dataset for training our models
- **[Extension](./extension/)**: This folder contains all the code for developing and deploying a chrome extension
- **[Models](./models/)**: This folder contains all the different machine learning models used for the project ranging from simple regression techniques to NLP-heavy models
- **[Result](./result/)**: This folder contains all the different machine learning models's classification report and their important checkpoint files of their best version
- **[Test](./test/)**: This folder files for testing the functionality of different models when predicting a piece of text 'sexist' or 'not sexist'

## Contribution

- Create a feature branch, preferably with the name `feature/<small-description>` and commit your features into it.
- Create a merge request to push code from your feature branch into `main` branch which will be reviewed.
- Once the code is reviewed and approved by atleast one developer, it would be merged to `main`.

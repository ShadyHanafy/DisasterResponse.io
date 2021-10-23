
### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Instructions](#instructions)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The code should run with no issues using Python versions 3. The libraries to run the code here beside the Anaconda distribution of Python as as follow:
* sqlalchemy
* nltk
* re
* pandas
* sklearn
* pickle
* sys

## Project Motivation<a name="motivation"></a>

For this project, the goal is to analyze disaster response data and classifiy the messages into categories for fast response detection from Figure Eight to build a model for that purpose over 3 steps:

1. Use ETL Pipeline to explore, clean and analyze the data then store that final table in sql DB
2. Use ML Pipeline to load the stored data, build a classifier model, train it and predict till the highest accuracy
3. Store the Model into a pickle file to be used by Flask Web APP to view the categories of the messages


## File Descriptions <a name="files"></a>

There are 2 notebooks and 2 datasets available here to showcase work related to the above steps. Markdown cells were used to assist in walking through the thought process for individual steps.  
1. ETL Pipeline Preparation.ipynb : Explore the  dataset and understand the messages classification
2. ML Pipeline Preparation.ipynb : Build classifier model to predict the messages categories
3. workspace
	- \data
		* disaster_categories.csv: categories dataset
		* disaster_messages.csv: messages dataset
		* DisasterResponse.db: disaster response database
		* process_data.py: built using ETL Pipeline.ipyb code
		
	- \models
		* train_classifier.py: built using ML Pipeline.ipyb code


## Results<a name="results"></a>

### FlaskAPP Visualization : http://0.0.0.0:3001/
![This is an image](https://github.com/ShadyHanafy/DisasterResponse.io/blob/main/FlaskApp.png)

# Classification Model Accuracy		
![image](https://github.com/ShadyHanafy/DisasterResponse.io/blob/main/visualize3.png)

## Instructions<a name="instructions"></a>	

Run the following commands in the project's root directory to set up your database and model.

1. To run ETL pipeline that cleans data and stores in database python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/drpdb.db
2. To run ML pipeline that trains classifier and saves python models/train_classifier.py data/drpdb.db models/classifier.pkl
3. Run the following command in the app's directory to run your web app. python run.py
4. Go to http://0.0.0.0:3001/

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Figure Eight for the data.  You can find the Licensing for the data and other descriptive information at the link available [here](https://appen.com/). 

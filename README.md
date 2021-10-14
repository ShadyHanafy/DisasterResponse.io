
### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

There should be no necessary libraries to run the code here beyond the Anaconda distribution of Python.  The code should run with no issues using Python versions 3.*.

## Project Motivation<a name="motivation"></a>

For this project, the goal is to analyze disaster data and classifiy the messages into categories for fast response detection from Figure Eight to build a model for that purpose over 3 steps:

1. Use ETL Pipeline to explore, clean and analyze the data then store that final table in sql DB
2. Use ML Pipeline to load the stored data, build a classifier model, train it and predict till the highest accuracy
3. Store the Model into a pickle file to be used by Flask Web APP to view the categories of the messages


## File Descriptions <a name="files"></a>

There are 2 notebooks and 2 datasets available here to showcase work related to the above steps. Markdown cells were used to assist in walking through the thought process for individual steps.  
1. ETL Pipeline Preparation.ipynb : Explore the  dataset and understand the messages classification
2. ML Pipeline Preparation.ipynb : Build classifier model to predict the messages categories
3. Price_Predict.ipynb : Model to try to predict the prices
4. disaster_messages.csv: The disaster response messages
5. disaster_categories.csv: The messages categories
6. workspace
	- \data
		--disaster_categories.csv: categories dataset
		--disaster_messages.csv: messages dataset
		--DisasterResponse.db: disaster response database
		--process_data.py: built using ETL Pipeline.ipyb code
	- \models
		--train_classifier.py: built using ML Pipeline.ipyb code


## Results<a name="results"></a>

# Visualization for Genre Distribution
![This is an image](https://github.com/ShadyHanafy/DisasterResponse.io/blob/main/visualize1.png)

# Visualization for Top Categories Distribution
![This is an image](https://github.com/ShadyHanafy/DisasterResponse.io/blob/main/visualize2.png)

# Classification Model Accuracy
Category	precision	recall	f1-score	support
related	0.78	0.8	0.78	18352
request	0.85	0.86	0.85	18352
offer	0.98	0.98	0.98	18352
aid_related	0.72	0.73	0.72	18352
medical_help	0.87	0.91	0.88	18352
medical_produ	0.93	0.94	0.93	18352
search_and_re	0.95	0.97	0.95	18352
security	0.96	0.97	0.96	18352
military	0.95	0.96	0.95	18352
child_alone	0.99	0.98	0.98	18352
water	0.93	0.94	0.93	18352
food	0.92	0.93	0.92	18352
shelter	0.92	0.93	0.91	18352
clothing	0.97	0.98	0.97	18352
money	0.96	0.97	0.96	18352
missing_peop	0.97	0.97	0.97	18352
refugees	0.93	0.95	0.94	18352
death	0.92	0.94	0.93	18352
other_aid	0.78	0.85	0.8	18352
infrastructu	0.87	0.92	0.89	18352
transport	0.93	0.95	0.93	18352
buildings	0.92	0.94	0.92	18352
electricity	0.97	0.97	0.96	18352
tools	0.98	0.98	0.98	18352
hospitals	0.97	0.97	0.97	18352
shops	0.98	0.99	0.98	18352
aid_centers	0.97	0.98	0.97	18352
other_infras	0.91	0.94	0.92	18352
weather_rela	0.84	0.84	0.84	18352
floods	0.92	0.93	0.91	18352
storm	0.91	0.92	0.91	18352
fire	0.97	0.98	0.97	18352
earthquake	0.95	0.95	0.95	18352
cold	0.96	0.96	0.96	18352
precision	0.9	0.93	0.91	18352
direct_repor	0.8	0.82	0.79	18352
Model Accuracy	0.931			
![image](https://user-images.githubusercontent.com/48498548/137370551-7856eb70-440c-4497-9625-727f28b1dd77.png)

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Must give credit to Figure Eight for the data.  You can find the Licensing for the data and other descriptive information at the link available [here](https://appen.com/). 

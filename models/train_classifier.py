import sys
from sqlalchemy import create_engine
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
import re
import pandas as pd
from sklearn.multioutput import MultiOutputClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier 
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import nltk
nltk.download(['punkt', 'wordnet'])
nltk.download('stopwords')
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
import pickle


def load_data(database_filepath):
    # load data from database
    engine = create_engine('sqlite:///' + database_filepath)
    df = pd.read_sql_table('clean', engine)
    
    print (df.head())
    #Create X & Y
    X = df["message"]
    Y = df[df.columns[4:]]
    
    #Rename one value in column to ensure the column has only 2 unique values like other columns
   # Y.loc[Y['related'] == 2] = 1
    category_names = Y.columns
    
    return X, Y, category_names
  

def tokenize(text):
    text = re.sub(r"[^a-zA-Z0-9]", " ", text.lower())
    
    # Tokenize text
    words = word_tokenize(text)
    
    # Remove stop words
    stop = stopwords.words("english")
    words = [t for t in words if t not in stop]
    
    # Lemmatization
    lemm = [WordNetLemmatizer().lemmatize(w) for w in words]
    return lemm


def build_model():
    
    pipeline =Pipeline([
    ('vect', CountVectorizer(tokenizer=tokenize)),
    ('tfidf', TfidfTransformer()),
    ('clf', MultiOutputClassifier(RandomForestClassifier()))])
    
    parameters = {
    'clf__estimator__n_estimators': [50, 100],
    'clf__estimator__max_features': ['auto', 'log2'],
    'clf__estimator__bootstrap': [False, True],
    'clf__estimator__max_depth':[5, 10]}
        
    '''
    parameters = {
    'clf__estimator__n_estimators': [5, 10, 50, 100],
    'clf__estimator__max_features': ['auto', 'log2', 'sqrt'],
    'clf__estimator__bootstrap': [False, True],
    'clf__estimator__max_depth':[5, 10, 20]}
    '''
    cv = GridSearchCV(estimator=pipeline,
            param_grid=parameters,
            verbose=2)
    return cv

def evaluate_model(model, X_test, Y_test, category_names):
    y_pred = model.predict(X_test)
    
    #Evaluate the accuracy in each run
    
    i=0
    for col in Y_test:
        print('Feature {}: {}'.format(i+1, col))
        print(classification_report(Y_test[col], y_pred[:, i]))
        i = i + 1
        accuracy = (y_pred == Y_test.values).mean()
        print('Model accuracy is {:.3f}'.format(accuracy))       



def save_model(model, model_filepath):
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)
        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()
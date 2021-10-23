# import libraries
import sys
import pandas as pd
from sqlalchemy import create_engine

def load_data(messages_filepath, categories_filepath):
'''
   Function:
      load the data from two csv files and then merge them
   Args:
      messages_filepath: the file path of disaster messages csv file
      categories_filepath: the file path of disaster categories csv file
   Return:
      df : The merged dataframe
 '''
    # load datasets
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    
    # merge datasets
    df = messages.merge(categories, how='outer', on=['id'])
    
    return df

def clean_data(df):
    
  '''
  Function:
      clean the dataframe
  Args:
      df : The dataframe to be cleaned
  Return:
      df : The cleaned dataframe
   '''

        
    # create a dataframe for the columns
    categories = df['categories'].str.split(";", expand=True)
    
    # select the first row of the categories dataframe to rename the columns
    row = categories[0:1]
    category_col = row.apply(lambda x: x.str[0:-2]).values.tolist()
    category_colnames = [item for sublist in category_col for item in sublist]
    
    # rename the columns of `categories`
    categories.columns = category_colnames
    
    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].astype(str).str[-1]

        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])
    
    # drop the original categories column from `df`

    df.drop("categories", axis=1, inplace=True)
    
    # concatenate the original dataframe with the new `categories` dataframe
    frames = [df, categories]
    df = pd.concat(frames, axis=1)
    
    # drop duplicates
    df["related"].replace({2: 1}, inplace=True)
    df=df.drop_duplicates()
    
    return df


def save_data(df, database_filename):
    
 '''
  Function:
       Save the dataframe to a database
  Args:
       df: The merged dataframe
       database_filename: The name of the database
  '''
        
    engine = create_engine('sqlite:///' + database_filename)
    df.to_sql('clean', engine,if_exists='replace', index=False)    


def main():
    
   '''
    Function:
       Run the main function of script
    '''
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '\
              'datasets as the first and second argument respectively, as '\
              'well as the filepath of the database to save the cleaned data '\
              'to as the third argument. \n\nExample: python process_data.py '\
              'disaster_messages.csv disaster_categories.csv '\
              'DisasterResponse.db')


if __name__ == '__main__':
    main()

'''
Module description
------------------
This module sets and example of logging with a demo function
'''
import pandas as pd
import logging

# logging basic config
logging.basicConfig(
    filename = './results.log',
    level = logging.INFO,
    filemode = 'w',
    format = '%(name)s - %(levelname)s - %(message)s'
)

def read_data(file_path):
    '''
    function to read a csv file with logging options
    PARAMS:
    file_path: (str) file path
    OUTPUT:
    df: (dataframe) pandas dataframe
    '''
    try:
        df = pd.read_csv(file_path)
        logging.info('SUCCESS: There are {} rowns and {} columns in your dataframe'.format(df.shape[0], df.shape[1]))
        logging.info('SUCCESS: Your file was successfully read in')
        return df
    except FileNotFoundError:
        logging.error('ERROR: We were not able to find that file')

if __name__ == '__main__':
    df = read_data('some_path')
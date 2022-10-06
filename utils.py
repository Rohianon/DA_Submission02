import gc
import missingno
import matplotlib.pyplot as plt
import pandas as pd
from IPython.display import display
import calendar
from IPython.display import clear_output, Image, display, HTML
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import StandardScaler
import seaborn as sns
from datetime import datetime
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")

plt.style.use('fivethirtyeight')

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.options.display.float_format = '{:.4f}'.format
#######################################################################


# Read the Data
def read_df(path, name='pharmaceutical-sales-demand', format="excel"):
    """
    Helper function to read the dataset and display particular aspects

    Parameters:
    -----------
        path: str
            The file location where the data is located

        name: str
            the name of the data to be read

        format: str
            One of the data format to be read by pandas, i.e. excel, csv, pickle etc

    Returns:
    --------
        data: pd.Dataframe Object
            returns the df that has been read


    """
    reader = eval("pd.read_"+format)
    data = reader(path)
    print(name)
    display(data_characterization(data))

    return data


# display some few elements about the data
#########################################################################
def data_characterization(data) -> None:
    """
    Helper function to get a few statistics and information regarding the data

    Parameters:
    -----------
        data: pd.Dataframe object
            the data that has been read from the file

    Returns:
    --------
        None
        Does not return any object
    """

    print("shape of data : "+str(data.shape))
    data_characterization = pd.DataFrame()
    columns = data.columns
    Type, Count = [], []
    unique_values, Max = [], []

    Min, Mean = [], []
    Nan_counts = data.isnull().sum().tolist()
    Nan_ratio = (data.isnull().sum()/len(data)).values

    Type = data.dtypes.tolist()
    J = 0
    for i in columns:
        unique = list(data[i].unique())
        unique_values.append(unique)
        Count.append(len(unique))

        if (data[i].dtypes.name == 'object'):
            Max.append(0)
            Min.append(0)
            Mean.append(0)
        elif ((data[i].dtypes == '<M8[ns]')):
            Max.append(0)
            Min.append(0)
            Mean.append(0)
        elif ((data[i].dtype.name == "category")):
            Max.append(0)
            Min.append(0)
            Mean.append(0)

        else:
            Max.append(data[i].max())
            Min.append(data[i].min())
            Mean.append(data[i].mean())

    data_characterization["Columns name"] = columns
    data_characterization["Type "] = data.dtypes.tolist()
    data_characterization["Count unique values"] = Count
    data_characterization["Count Nan values"] = Nan_counts
    data_characterization["Ratio Nan values"] = Nan_ratio

    data_characterization["Unique   values"] = unique_values
    data_characterization["Max"] = Max
    data_characterization["Min"] = Min
    data_characterization["Mean"] = Mean

    return data_characterization


# Get rid of -ve values from the data
#########################################################################
def clean_negatives(data):
    """
    Helper function to only get positive stock quantities
    Parameters:
    -----------
        data: pd.Dataframe object
            the data that has been read from the file

    Returns:
    --------
        returns data with only positive stock quantity
    """
    return data[data.stock_demand > 0]


# Clean the column names for easy usage
#########################################################################
def clean_cols(data):
    """
    Helper function to clean the column names from the data

    Parameters:
    -----------
        data: pd.Dataframe object
            the data that has been read from the file

    Returns:
    --------
        data with clean column names (snake_case)
    """
    return data.columns.str.strip().str.lower().\
        str.replace(' ', '_').str.replace('(', '').\
        str.replace(')', '')

# visualize missing values
#########################################################################


def visualize_missingness(data):
    """
    Helper function to get a visualize distribution of missing values

    Parameters:
    -----------
        data: pd.Dataframe object
            the data that has been read from the file

    Returns:
    --------
        Bar plot of the missing values
    """
    return missingno.bar(data)


# Drop the duplicate and keep the first row
#########################################################################


def drop_dups(data):
    """
    Helper function to get a visualize distribution of missing values

    Parameters:
    -----------
        data: pd.Dataframe object
            the data that has been read from the file

    Returns:
    --------
        unique values from the dataset
    """

    return data.loc[~data.duplicated(), :]


# Delete outliers from the data
#########################################################################


def detect_outliers(col):
    """
    Helper function to display information related to outlier thresholds in the data

    Parameters:
    -----------
        column: pd.Series object
            A particular column in the data

    Returns:
    --------
        lower and upper threshold within which the data should lie
    """
    values = col.sort_values()
    # first quartile
    Q1 = values.quantile(0.25)
    # 3rd quartile
    Q3 = values.quantile(0.75)
    # interquartile range
    IQR = Q3 -  Q1

    return Q1 - (1.5*IQR), Q3 + (1.5*IQR)
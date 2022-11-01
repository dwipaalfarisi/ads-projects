import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from matplotlib import rcParams

def print_format(data, format):
    '''
    Format a number's digit
    '''
    print(f"{data:.{format}f}")

def addlabels(x,y):
    '''
    Add labels to the given bar chart
    '''
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center')

def prob(A):
    """Computes the probability of a proposition, A."""    
    return A.mean()

def conditional(proposition, given):
    """Probability of A conditioned on given."""
    return prob(proposition[given])

def correlation(dataset, threshold):
    """returns column names with according to given threshold."""
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr

def get_corr_cols(df, threshold):
    """returns correlation column names by the given threshold."""
    cols_corr = set()
    corr_matrix = df.corr()
    for i in range(len(corr_matrix)):
        if abs(corr_matrix.iloc[2, i]) > threshold:
            colsname = corr_matrix.columns[i]
            if colsname == 'charges':
                pass
            else:
                cols_corr.add(colsname)
        else: 
            pass   
    return cols_corr

def load_roboto():
    font_path = 'C:/Users/ASUS/AppData/Local/Microsoft/Windows/Fonts/Roboto-Regular.ttf' 
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = prop.get_name()
    return rcParams['font.sans-serif']

def load_roboto_var():
    font_path = 'C:/Users/ASUS/AppData/Local/Microsoft/Windows/Fonts/RobotoFlex-VariableFont_GRAD,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght.ttf'
    font_manager.fontManager.addfont(font_path)
    prop = font_manager.FontProperties(fname=font_path)

    rcParams['font.family'] = 'sans-serif'
    rcParams['font.sans-serif'] = prop.get_name()
    return rcParams['font.sans-serif']

def bmi_category(bmi):
    """Return bmi category"""
    if bmi < 18.5:
        return 'underweight'
    elif bmi >= 18.5 and bmi <25:
        return 'healthy weight'
    elif bmi >= 25 and bmi < 30:
        return 'overweight'
    elif bmi > 30:
        return 'obesity'

def df_without_outlier(df, col: str):
    '''
    Handle outliers on a given column of a dataframe and return df without outliers
    '''
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)
    iqr = q3 - q1 
    lower_lim = q1 - 1.5 * iqr
    upper_lim = q3 + 1.5 * iqr
    outlier_low = (df[col] < lower_lim)
    outlier_up = (df[col] > upper_lim)
    df = (df[~(outlier_low | outlier_up)])

    return df

def chance(df, condition: int, high_or_low: str):
    try: 
        if high_or_low.lower() == 'high':
            return df.iloc[condition-1, 0]
        elif high_or_low.lower() == 'low':
            return df.iloc[condition-1, 1]
        else:
            pass
    except (RuntimeError, TypeError, NameError, AttributeError):
        pass

def get_bmi_more_less(dummy_df):
    bmiM25 = []
    for index, row in dummy_df.iterrows():
        if row.bmi > 25:
            bmiM25.append(1)
        elif row.bmi <= 25:
            bmiM25.append(0)

    bmiL25 = []
    for index1, row1 in dummy_df.iterrows():
        if row1.bmi < 25:
            bmiL25.append(1)
        elif row.bmi >= 25:
            bmiL25.append(0)
    dummy_df['bmi_m25'] = bmiM25
    dummy_df['bmi_l25'] = bmiL25

    return dummy_df

def get_bmi_status(df):
    '''Using bmi_category function to deter bmi_status and return df with a new colun (bmi_status)'''
    bmi_status = []
    for index, row in df.iterrows():
        bmi_status.append(bmi_category(row['bmi']))
    df['bmi_status'] = bmi_status
    
    return df

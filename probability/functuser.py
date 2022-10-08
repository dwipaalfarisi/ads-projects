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
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr
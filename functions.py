def eda(df):
    """Function to perform some basic EDA on my datasets"""
    
    #Inspect the first 5 rows
    display(df.head())
    print("\n")
    
    # Count of non-null values, datatypes, and total entries
    display(df.info())
    print("\n")
    
    # Check descriptive statistics
    display(df.describe())
    print("\n")
    
    # Check value counts
    for c in df.columns:
        print ("---- %s ----" % c)
        print (df[c].value_counts())
        print("\n")
    
    # Print null values
    display(df.isna().sum())
    print('Total Null Count:', df.isna().sum().sum())
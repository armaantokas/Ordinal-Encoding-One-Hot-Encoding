import pandas
import numpy

def ordinal_encode(dataframe):
    print("Original DataFrame:")
    print(dataframe)
    changed=dataframe.copy()
    columns = changed.select_dtypes(include=['object', 'category']).columns.tolist()
    print("Categorical columns:", columns)
    for i in columns:
        unique = sorted(changed[i].unique())
        category_iteration = {category:index
                            for index, category in enumerate(unique)}
        changed[i + '_ordinal'] = changed[i].map(category_iteration)
    changed.drop(columns=columns, inplace=True)
    print("DataFrame after Ordinal Encoding:")
    print(changed)
    return changed

def one_hot_encode(dataframe):
    print("Original DataFrame:")
    print(dataframe)
    changed=dataframe.copy()
    columns = changed.select_dtypes(include=['object', 'category']).columns.tolist()
    print(columns)
    for i in columns:
        unique_arg = changed[i].unique()
        for j in unique_arg:
            changed[f'{i}_{j}'] = numpy.where(changed[i] == j, 1, 0)
    print("DataFrame after One Hot Encoding:")
    print(changed)
    return changed
def create_vectors(df, main_col, cols=None, lag=6):
    if main_col not in df:
        raise ValueError
    X = []
    y = []
    for window in df[main_col].rolling(window=lag):
        if len(window) == lag:
            vector = window.to_list()
            X.append(vector[:-1])
            y.append(vector[-1])
    if cols is not None:
        for col in cols:
            i = 0
            for window in df[col].rolling(window=lag - 1):
                if len(window) == lag - 1:
                    vector = window.to_list()
                    if i < len(X):
                        X[i].extend(vector)
                    i += 1

    return X, y

import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error

def read_dataset(n,j,p,q,r,s):
    rand_state = {
        'Rice': 83,
        'Maize': 24,
        'Groundnut':208,
        'Moong':179,
        'Urad':130,
        'Soyabean':255,
        'Jowar':244,
        'Tur':102,
        'Cotton':244

    }

    crop={
        1:'Rice',
        2:'Maize',
        3:'Groundnut',
        4:'Moong',
        5:'Urad',
        6:'Soyabean',
        7:'Jowar',
        8:'Tur',
        9:'Cotton'

    }


    df = pd.read_csv(n)

    all_Crops = {}
    cnt = 0

    for i in range(len(df)):
        if df.loc[i]['Crops'] not in all_Crops:
            all_Crops[df.loc[i]['Crops']] = cnt
            cnt += 1

    all_Years = {}
    cnt = 0

    for i in range(len(df)):
        if df.loc[i]['Year'] not in all_Years:
            all_Years[df.loc[i]['Year']] = cnt
            cnt += 1

    all_Cost_Production = {}
    cnt = 0

    for i in range(len(df)):
        if df.loc[i]['Cost_Production'] not in all_Cost_Production:
            all_Cost_Production[df.loc[i]['Cost_Production']] = cnt
            cnt += 1

    all_Domastic_Price = {}
    cnt = 0

    for i in range(len(df)):
        if df.loc[i]['Domastic_Price'] not in all_Domastic_Price:
            all_Domastic_Price[df.loc[i]['Domastic_Price']] = cnt
            cnt += 1

    all_International_Price = {}
    cnt = 0

    for i in range(len(df)):
        if df.loc[i]['International_Price'] not in all_International_Price:
            all_International_Price[df.loc[i]['International_Price']] = cnt
            cnt += 1
    print("\n")
    print("all_Crops")
    print(all_Crops)
    print("\n")
    print("all_Years")
    print(all_Years)
    print("\n")
    print("all_Cost_Production")
    print(all_Cost_Production)
    print("\n")
    print("all_Domastic_Price")
    print(all_Domastic_Price)
    print("\n")
    print("all_International_Price")
    print(all_International_Price)
    print("\n")

    x = df[['Crops', 'Year', 'Cost_Production', 'Domastic_Price', 'International_Price']]  # input features
    y = df[['MSP']]  # to be predicted by model

    x = np.array(x)
    y = np.array(y)

    for i in range(len(x)):
        x[i][0] = all_Crops[x[i][0]]
        x[i][1] = all_Years[x[i][1]]
        x[i][2] = all_Cost_Production[x[i][2]]
        x[i][3] = all_Domastic_Price[x[i][3]]
        x[i][4] = all_International_Price[x[i][4]]

    x = np.array(x, dtype='int32')
    y = np.array(y, dtype='int32')

    from sklearn.model_selection import train_test_split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=rand_state[crop[j]])
    from sklearn.linear_model import LinearRegression
    lr = LinearRegression()
    lr.fit(x, y)
    y_pred = lr.predict(x_test)
    R2 = lr.score(x_test, y_test)
    print("\n R2:", R2)
    print("\n MSE:", mean_squared_error(y_test, y_pred))
    print("\n RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))

    test = np.array([0, p, q, r, s]).reshape(1, -1)
    print(lr.predict(test))
    return lr.predict(test)
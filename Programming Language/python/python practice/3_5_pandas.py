import pandas as pd


def show_series():
    s = pd.Series([3, 2, 7, 5])
    # print(s, end='\n\n')

    # print(s.index)
    # print(s.values)

    # print(s[0], s[3])

    # # s.index = range(5,9)
    s.index = list('abcd')
    # print(s, end='\n\n')

    # print(s[0], s[-1])
    # print(s['a'], s['d'])

    print(s[2:].values)
    print(s['c':].values)


def show_dataframe():
    data = {
        'year': [2016, 2017, 2018, 2019, 2016, 2017, 2018, 2019],
        'city': ['pusan', 'pusan', 'pusan', 'pusan', 'yeosoo', 'yeosoo', 'yeosoo', 'yeosoo'],
        'population': [200, 250, 230, 220, 130, 160, 170, 180],
    }

    df = pd.DataFrame(data)
    # print(df)

    # print(df.index)
    # print(df.columns)
    # print(df.values)
    # print(df.values.dtype, end='\n\n')

    # print(df.head(), end='\n\n')
    # print(df.tail(), end='\n\n')

    # print(df.head(2), end='\n\n')
    # print(df.tail(2), end='\n\n')

    # print(df['year'])
    # print(df.year, end='\n\n')

    # 도시가 여수인 행의 인구만 출력
    # print(df.population[df.city == 'yeosoo'], end='\n\n')

    df.index = list('abcdefgh')
    # print(df, end='\n\n')

    # print(df.loc['a':'c'])
    # print(df.loc[['a', 'c']])
    # print(df.loc['a':'c', 'year':'city'])
    # print(df.loc['a':'c', ['year', 'city']])
    # print(df.iloc[0:3])
    # print(df.iloc[[0, 2]])

    print(df.loc['e':].population.values)









# show_series()
show_dataframe()
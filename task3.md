# Задание 3 (Вариант 2)

## Вопросы

1. Дайте определение объекту библиотеки Index?
2. Какие параметры у функции Series?
3. Каков тип DataFrame.values?
4. В чем особенность среза для объекта DataFrame?

## Ответы

1. Index - объект, ссылающийся на значение в датафрейме

2. [Series documentation](https://pandas.pydata.org/docs/reference/series.html#constructor)

   ```python
   class pandas.Series(data=None, index=None, dtype=None, name=None, copy=None, fastpath=<no_default>)
   ```

3. `DataFrame.values` возвращает многомерный массив без заголовков датафрейма:

   ```python
   df = pd.DataFrame({
       'age': [3, 29],
       'height': [94, 170],
       'weight': [31, 115]
   })

   df.values # [[3, 94, 31], [29, 170, 115]]
   ```

4. В отличие от классического среза для массивов, который вовзращает подмассив - срез для `DataFrame` возвращает подмножество `DataFrame`

   ```python
    import pandas as pd

    df = df = pd.DataFrame({
        "age": [x for x in range(20)],
        "height": [x for x in range(160, 180)],
        "weight": [x for x in range(60, 80)],
    })

    print(df[:5])
    print(type(df[:5]))

    """
    Output:
       age  height  weight
    0    0     160      60
    1    1     161      61
    2    2     162      62
    3    3     163      63
    4    4     164      64
    <class 'pandas.core.frame.DataFrame'>
    """
   ```

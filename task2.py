import pandas as pd

"""
Задание 2 (Вариант 2)

Используя набор данных (датасет) HousePrice1 реализуйте следующее:
- Функция возвращающая DataFrame по указанному пути к датасету.
Причем загруженный DataFrame остается в памяти для последующей
обработки.
- Функция возвращающая первые десять самых старых домов.
- Функция возвращающая записи, у которых стоимость дома больше
средней цены.
- Функция возвращающая записи, у которых размер дома меньше
медианного значения.
- Функция возвращающая количество домов, которые сгруппированы
по количеству ванных комнат.
- Функция возвращающая новый DataFrame, в котором: в новой
колонке "num_rooms" записана сумма спальных и ванных комнат;
исключены записи, у которых есть отрицательные значения в поле
"Price"; изменен тип данных в колонке "Price" на целочисленный по
правилам округления; в новой колонке "factor" записан результат
деления колонки "Price" на колонку "SquareFeet" до двух чисел после
запятой. В качестве дополнительных параметров указывается
выходной путь для сохранения измененного датасета
"""


def read_csv_as_dataframe_by_path(path: str) -> pd.DataFrame:
    return pd.read_csv(path)


def get_ten_oldest_houses(df: pd.DataFrame, col: str) -> pd.DataFrame:
    return df.sort_values(by=col, ascending=True)[:10]


def get_houses_above_average_price(
    df: pd.DataFrame, col: str
) -> tuple[pd.DataFrame, float]:
    arithmetic_mean = df[col].mean()
    return df[df[col] > arithmetic_mean], arithmetic_mean


def get_houses_with_less_than_median_size(
    df: pd.DataFrame, col: str
) -> tuple[pd.DataFrame, float]:
    median = df[col].median()
    return df[df[col] < median], median


def get_houses_groupped_by_bathrooms_count(df: pd.DataFrame, col: str) -> pd.DataFrame:
    return df.groupby(col).sum()


def new_filtered_houses_dataframe_from_existing(
    df: pd.DataFrame, df_save_path: str | None = None
) -> pd.DataFrame:
    new_df = df.copy(deep=True)
    new_df["num_rooms"] = new_df["Bathrooms"] + new_df["Bedrooms"]
    new_df = new_df[new_df["Price"] >= 0]
    new_df["Price"] = new_df["Price"].round().astype("int")
    new_df["factor"] = (new_df["Price"] / new_df["SquareFeet"]).round(2)

    if df_save_path is not None:
        new_df.to_csv(df_save_path)

    return new_df.sort_values(by="Price", ascending=True)


def main():
    dframe = read_csv_as_dataframe_by_path("dataset_house_price1.csv")

    print(get_ten_oldest_houses(dframe, col="YearBuilt"))

    houses, avg_price = get_houses_above_average_price(dframe, col="Price")
    print(houses.sort_values(by="Price", ascending=True))
    print(f"Average price: {avg_price}")

    houses, median = get_houses_with_less_than_median_size(dframe, col="SquareFeet")
    print(houses.sort_values(by="SquareFeet", ascending=True))
    print(f"Median: {median}")

    print(get_houses_groupped_by_bathrooms_count(dframe, "Bathrooms"))

    new_filtered_houses_dataframe_from_existing(dframe, df_save_path="new_frame.csv")


if __name__ == "__main__":
    main()

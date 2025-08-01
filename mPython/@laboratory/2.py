import pandas as pd

# Загрузка данных из файла .xlsx
def load_data(file_path):
    return pd.read_excel(file_path)

# Фильтрация данных
def filter_data(df, filters):
    for column, values in filters.items():
        df = df[df[column].isin(values)]
    return df

# Получение фильтров от пользователя
def get_filters(df):
    filters = {}
    print("Доступные столбцы:")
    print(df.columns.tolist())
    
    while True:
        column = input("Введите название столбца для фильтрации (или 'exit' для выхода): ")
        if column.lower() == 'exit':
            break
        if column not in df.columns:
            print("Такого столбца нет. Попробуйте снова.")
            continue
        
        values = input(f"Введите значения для фильтрации в столбце '{column}' (через запятую): ")
        values_list = [value.strip() for value in values.split(',')]
        filters[column] = values_list
    
    return filters

# Запись отфильтрованных данных в .txt файл
def save_to_txt(df, output_file):
    df.to_csv(output_file, sep='\t', index=False)  # Используем табуляцию в качестве разделителя

# Основная функция
def main():
    # Путь к вашему файлу .xlsx
    file_path = 'z/input/data.xlsx'
    
    # Загрузка данных
    data = load_data(file_path)
    
    # Получение фильтров от пользователя
    filters = get_filters(data)
    
    # Фильтрация данных
    filtered_data = filter_data(data, filters)
    
    # Вывод отфильтрованных данных
    print("Отфильтрованные данные:")
    print(filtered_data)
    
    # Запись в .txt файл
    output_file = 'z/output/output2.txt'
    save_to_txt(filtered_data, output_file)
    print(f"Отфильтрованные данные сохранены в '{output_file}'.")

if __name__ == "__main__":
    main()

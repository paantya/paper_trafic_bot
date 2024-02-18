import json


def load_file(file_path):
    """
    Загружает данные из JSON-файла.

    Args:
        file_path (str): Путь к файлу, который необходимо загрузить.

    Returns:
        dict: Данные, загруженные из JSON-файла.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_file(data, file_path):
    """
    Сохраняет данные в JSON-файл с форматированием.

    Args:
        data (dict): Данные для сохранения в файл.
        file_path (str): Путь к файлу, в который необходимо сохранить данные.

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

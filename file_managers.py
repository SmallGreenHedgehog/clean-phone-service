from os.path import isfile


class FileManager:
    _file_path = None

    def set_file_path(self, file_path: str):
        """Сеттер пути к файлу"""
        self._file_path = file_path

    @property
    def file_path(self):
        """Возвращает путь к файлу"""
        return self._file_path

    def __init__(self, file_path):
        self.set_file_path(file_path=file_path)

    def write_text_to_file(self, text: str):
        """Записывает указанный текст в файл"""
        with open(self.file_path, 'a+') as file:
            file.write(text)

    def erase_file(self):
        """Очищает указанный файл"""
        open(self.file_path, 'w').close()

    @property
    def file_text(self) -> str:
        """Возвращает текст файла"""
        result = ''
        if isfile(self.file_path):
            with open(self.file_path, 'r') as file:
                result = file.read()
        return result

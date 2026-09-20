from abc import ABC, abstractmethod

class File(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def get_file_info(self):
        pass

class TextFile(File):
    def open(self):
        print("Открываем текстовый файл:")
        print("Ассалам Алейкум, меня зовут Азим")

    def get_file_info(self):
        print("Тип файла: Текст")

class ImageFile(File):
    def open(self):
        print("Открываем изображение:")
        print("------------>>>>>>><<<<<<<<______________")
    def get_file_info(self):
        print("Тип файла: Изображение")

class AudioFile(File):
    def open(self):
        print("Воспроизводим аудиозапись: ")

    def get_file_info(self):
        print("Тип файла: Аудио")

class VideoFile(File):
    def open(self):
        print("Воспроизводим видеозапись: ")

    def get_file_info(self):
        print("Тип файла: Видео")

class ArhiveFile(File):
    def open(self):
        print("Открываем архив:")

files = [
    TextFile(),
    ImageFile(),
    AudioFile(),
    VideoFile(),
]

for file in files:
    file.open()
    file.get_file_info()
    print()

try:
    file = File()
except TypeError as e:
    print("Ошибка")

try:
    arсhive = ArhiveFile()
except TypeError as e:
    print("Ошибка")



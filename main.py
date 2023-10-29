from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler
import zipfile

class Sort(FileSystemEventHandler):
    def __init__(self, folger_trash, folger_images, folger_videos, folger_music, folger_other):
        self.folger_trash = folger_trash
        self.folger_images = folger_images
        self.folger_videos = folger_videos
        self.folger_music = folger_music
        self.folger_other = folger_other

    def on_modified(self, event):
        for filename in os.listdir(self.folger_trash):
            file = os.path.join(self.folger_trash, filename)
            if os.path.isfile(file):
                ext = filename.split('.')[-1].lower()
                if ext in ['jpg', 'png', 'svg', 'jpeg', 'gif']:
                    new_path = os.path.join(self.folger_images, filename)
                elif ext in ['wmv', 'mp4', 'avi']:
                    new_path = os.path.join(self.folger_videos, filename)
                elif ext in ['mp3', 'wav']:
                    new_path = os.path.join(self.folger_music, filename)
                else:
                    new_path = os.path.join(self.folger_other, filename)
                try:
                    os.rename(file, new_path)
                except FileExistsError:
                    print(f"Файл '{new_path}' вже існує. Перейменування не виконано.")
                except FileNotFoundError:
                    print(f"Файл '{file}' не знайдено.")
                except Exception as e:
                    print(f"Помилка: {str(e)}")


folger_trash = 'D:/програмування/Проекти/Сортіровка-файлів/Trash'
folger_videos = 'D:/програмування/Проекти/Сортіровка-файлів/sorted/Video'
folger_music = 'D:/програмування/Проекти/Сортіровка-файлів/sorted/Musik'
folger_images = 'D:/програмування/Проекти/Сортіровка-файлів/sorted/Images'
folger_other = 'D:/програмування/Проекти/Сортіровка-файлів/sorted/Other'

print("1 - Sort")
print("2 - Archiving")
mode = int(input("Mode: "))

if mode == 1:
    sort = Sort(folger_trash, folger_images, folger_videos, folger_music, folger_other)
    observer = Observer()
    observer.schedule(sort, folger_trash, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

elif mode == 2:
    print("Створення архіву...")
    name = str(input('Project name: '))

    zip_file = zipfile.ZipFile(name + '.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk('sorted'):
        for file in files:
            zip_file.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), 'sorted'))
    zip_file.close()

    print("Очищення каталогів...")
    for root, dirs, files in os.walk('sorted'):
        for file in files:
            os.remove(os.path.join(root, file))
    print("Готово!")

else:
    print('Виберіть 1 або 2.')

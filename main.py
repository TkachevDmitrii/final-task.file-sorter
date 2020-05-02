import os
import click
from utils import mp3
from utils import directory


@click.command()
@click.option('-s', '--src-dir', default='.', help='Source directory.')
@click.option('-d', '--dst-dir', default='.', help='Destination directory.')
def sorter(src_dir, dst_dir):
    while True:
        if os.path.isdir(src_dir):
            # Проверка доступа src_dir
            try:
                scan = os.scandir(src_dir)
            # Обработка ошибки доступа, есть возможность сменить директорию без выхода из программы
            except PermissionError:
                print('Введите другой путь или нажмите "q" для выхода')
                src_dir = input()
                if src_dir == 'q':
                    break
            # Скан файлов
            else:
                with scan:
                    for file in scan:
                        if not file.name.startswith('.') and file.name.lower().endswith(
                                '.mp3') and file.is_file():

                            # Обработка mp3 файла, функция обработки в mp3.py
                            try:
                                mp3_val = mp3.parse(file)
                                # Если mp3_val вернул значения, то распределяет их по переменным
                                if mp3_val:
                                    new_file_name, old_file_name, artist, album = mp3.parse(file)
                                # Если он пуст, значит обработка выявила отсутствие тегов "Альбом" или "Исполнитель"
                                elif not mp3_val:
                                    print(f'Отсутствуют теги "Альбом" или "Исполнитель" в {file.name}')
                                    continue
                            # Обработка ошибок при работе с mp3 - файлом
                            except AttributeError:
                                print(f'Что-то не так с файлом: {file.name} AttributeError')
                                continue
                            except NotImplementedError:
                                print(f'Что-то не так с файлом: {file.name} AttributeError')
                                continue
                            except PermissionError:
                                print(f'Нет прав на изменение файла: {file.name}')
                                continue

                            # Создание директории и перемещение файла
                            else:
                                if os.path.exists(os.path.join(dst_dir, artist, album)):
                                    # Функция для создания директории лежит в directory.py
                                    directory.move_to(src_dir, dst_dir, old_file_name, new_file_name, artist, album)
                                else:
                                    # Попытка создать директорию, если есть права доступа
                                    try:
                                        os.makedirs(os.path.join(dst_dir, artist, album))
                                    except PermissionError:
                                        print(f'Введите другой путь или нажмите "q" для выхода')
                                        dst_dir = input()
                                        if dst_dir == 'q':
                                            break
                                    else:
                                        directory.move_to(src_dir, dst_dir, old_file_name, new_file_name, artist, album)

                            print(f'{old_file_name} --> {new_file_name}')

                print('Done.')
                break


if __name__ == '__main__':
    sorter()

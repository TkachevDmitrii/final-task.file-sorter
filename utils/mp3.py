import eyed3
from utils import rpls


# Функция обработкти mp3 файлов
def parse(file):

    mp3_file = eyed3.load(file)

    # Для нового названия и дальнейшего перемещения
    old_file_name = file.name

    artist = mp3_file.tag.artist
    album = mp3_file.tag.album
    title = mp3_file.tag.title

    # Убераем недопусимые символы
    if not mp3_file.tag.title:
        title = old_file_name.replace('.mp3', '')
    if artist and album:
        title = rpls.multi_replace(title, rpls.values)
        artist = rpls.multi_replace(artist, rpls.values)
        album = rpls.multi_replace(album, rpls.values)
    if not artist or not album:
        return

    mp3_file.tag.save()
    new_file_name = f'{title} - {artist} - {album}.mp3'
    all_val = (new_file_name, old_file_name, artist, album)

    return all_val

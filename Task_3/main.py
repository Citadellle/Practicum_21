from album import Album
from track import Track

def main() -> None:
    album = Album('Мой альбом')

    # Adding initial tracks to the album
    album.add_track(Track('Трек 1', 182, 'Исполнитель 1', 2000))
    album.add_track(Track('Трек 2', 1523, 'Исполнитель 1', 1636))
    album.add_track(Track('Трек 3', 132, 'Исполнитель 2', 1))

    finish_listening = False
    while not finish_listening:
        print('\nМеню:')
        print('1. Показать треки')
        print('2. Воспроизвести трек')
        print('3. Следующий трек')
        print('4. Предыдущий трек')
        print('5. Пауза')
        print('6. Стоп')
        print('7. Удалить трек ')
        print('0. Выход')

        choice = input('\nВыберите действие: ')

        match choice:
            case '1':
                album.show_tracks()

            case '2':
                album.show_tracks()
                try:
                    index = int(input('Введите номер трека: ')) - 1
                    album.play_track(index)
                except ValueError:
                    print('Ошибка, неверный индекс')

            case '3':
                album.next_track()

            case '4':
                album.prev_track()

            case '5':
                album.pause()

            case '6':
                album.stop()
            
            case '7':
                album.show_tracks()
                try:
                    index = int(input('Введите номер трека: ')) - 1
                    album.remove_track(index)
                except ValueError:
                    print('Ошибка, неверный индекс')

            case '0':
                print('Выход')
                finish_listening = True

            case _:
                print('Неверный ввод')


if __name__ == '__main__':
    main()
class Track:
    '''
    Represents a musical track with metadata and playback status.

    Handles track information (title, duration, artist, year) and controls
    the state of playback (play, pause, stop).
    '''

    def __init__(self, 
                 title: str, 
                 duration: int, 
                 artist: str, 
                 year: int) -> None:
        '''
        Initialize a new Track instance.

        :param title: The title of the track.
        :param duration: Duration of the track in seconds.
        :param artist: The name of the artist.
        :param year: The release year of the track.
        '''
        self.__title = title
        self.__duration = duration
        self.__artist = artist
        self.__year = year
        self.__is_playing = False
        self.__is_pausing = False

    def __str__(self) -> str:
        '''
        Return a string representation of the track with its current status.

        :return: A formatted string showing play status, 
        artist, title, and metadata.
        '''
        status = '▶' if self.__is_playing else '⏸' if self.__is_pausing else ''
        return (f'{status} {self.__artist} - {self.__title} '
                f'({self.__year}, {self.__duration} сек)')

    def play(self) -> None:
        '''
        Start or resume playback of the track.

        Displays an error if the track is already playing.
        '''
        if self.__is_playing:
            print(f'Ошибка. Трек {self.__artist} - {self.__title} '
                  f'({self.__year}) уже играет')
            return
        
        if self.__is_pausing:
            print(f'▶ Возобновление воспроизведения трека '
                  f'{self.__artist} - {self.__title} ({self.__year})')
            self.__is_pausing = False
            self.__is_playing = True
            return
        
        print(f'▶ Воспроизведение трека: {self.__artist} - {self.__title} '
              f'({self.__year})')
        self.__is_playing = True

    def pause(self) -> None:
        '''
        Pause the track playback.

        Displays an error if the track is not currently playing.
        '''
        if not self.__is_playing or self.__is_pausing:
            print('Ошибка. Трек не воспроизводится, '
                  'нельзя поставить на паузу')
            return
        
        print(f'⏸ Трек {self.__artist} - {self.__title} на паузе')
        self.__is_pausing = True
        self.__is_playing = False

    def stop(self) -> None:
        '''
        Stop the track playback entirely.

        Displays an error if the track is already stopped.
        '''
        if not self.__is_playing and not self.__is_pausing:
            print(f'Ошибка. Трек {self.__artist} - {self.__title} '
                  f'({self.__year}) уже остановлен')
            return
        
        print(f'⏹ Трек {self.__artist} - {self.__title}'
              f'({self.__year}) остановлен')
        self.__is_pausing = False
        self.__is_playing = False
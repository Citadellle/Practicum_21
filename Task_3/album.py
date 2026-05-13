from track import Track

class Album:
    '''
    Represents a music album containing a collection of tracks.

    Manages track storage, selection, and playback controls such as play,
    pause, stop, and navigation between tracks.
    '''

    def __init__(self, title: str) -> None:
        '''
        Initialize an Album instance.

        :param title: The title of the album.
        '''
        self.__title = title
        self.__tracks = []
        self.__current_index = -1

    def __str__(self) -> str:
        '''
        Return a string representation of the album.

        :return: A string with the album title.
        '''
        return f'Альбом: {self.__title}'

    def add_track(self, track: Track) -> None:
        '''
        Add a track to the album.

        :param track: An instance of the Track class.
        '''
        if not isinstance(track, Track):
            print('Можно добавлять только объекты Track')
            return
        
        self.__tracks.append(track)
        print(f'Добавлен трек {track} в альбом {self.__title}')

    def remove_track(self, index: int) -> None:
        '''
        Remove a track by its index.

        Adjusts the current playback index if the removed track affects it.

        :param index: The position of the track to remove.
        '''
        if not (0 <= index < len(self.__tracks)):
            print('Введен неверный индекс')
            return
        
        removed = self.__tracks.pop(index)
        print(f'Удален трек {removed}')
        
        if self.__current_index == index:
            self.__current_index = -1
        elif self.__current_index > index:
            self.__current_index -= 1

    def show_tracks(self) -> None:
        '''Display all tracks currently in the album.'''
        for i, track in enumerate(self.__tracks, 1):
            print(f'{i}) {track}')

    def play_track(self, index: int) -> None:
        '''
        Start playback of a specific track.

        :param index: The index of the track to play.
        '''
        if not (0 <= index < len(self.__tracks)):
            print('Введен неверный индекс')
            return
        
        self.stop()
        self.__current_index = index
        self.__tracks[index].play()

    def pause(self) -> None:
        '''Pause the currently playing track.'''
        if self.__current_index != -1:
            self.__tracks[self.__current_index].pause()
        else:
            print('Нет воспроизводящегося трека')

    def stop(self) -> None:
        '''Stop the playback and reset the track index.'''
        if self.__current_index != -1:
            self.__tracks[self.__current_index].stop()
            self.__current_index = -1
        else:
            print('Нет воспроизводящегося трека')

    def next_track(self) -> None:
        '''Navigate to and play the next track in the list.'''
        if self.__current_index + 1 < len(self.__tracks):
            self.play_track(self.__current_index + 1)
            return
        
        print('Это последний трек')

    def prev_track(self) -> None:
        '''Navigate to and play the previous track in the list.'''
        if self.__current_index > 0:
            self.play_track(self.__current_index - 1)
            return
        
        print('Это первый трек')
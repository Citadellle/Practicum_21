from pair import Pair

class Schedule:
    '''
    Represents a student group schedule.

    Handles loading class data from a file, filtering by group, and 
    displaying the schedule in a structured format by days and time slots.
    '''

    def __init__(self, group: str) -> None:
        '''
        Initialize the Schedule instance for a specific group.

        :param group: The identifier of the target student group.
        '''
        self.our_group = group
        self.our_lessons = []

    def load_data(self, file_path: str) -> None:
        '''
        Load class data from a .txt file.

        Parses lines delimited by semicolons and adds matching entries
        to the internal lessons list.

        :param file_path: Path to the schedule data file.
        '''
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                day, time, subject, teacher, room, group = \
                line.strip().split(';')

                if group == self.our_group:
                    self.our_lessons.append(Pair(day,
                                             time,
                                             subject,
                                             teacher,
                                             room,
                                             group))

    def display_schedule(self) -> None:
        '''
        Organize and print the schedule grouped by day and sorted by time.
        '''
        if not self.our_lessons:
            print('Расписание не найдено.')
            return
        
        days_order = {
            'Понедельник': 1, 'Вторник': 2, 'Среда': 3, 
            'Четверг': 4, 'Пятница': 5, 'Суббота': 6, 'Воскресенье': 7
        }
        pairs_order = {
            '09:00': 1, '10:50': 2, '12:40': 3,
            '14:30': 4, '16:20': 5, '18:10': 6
        }
        schedule = {}

        for lesson in self.our_lessons:
            if lesson.day not in schedule:
                schedule[lesson.day] = []
            schedule[lesson.day].append(lesson)

        sorted_days = sorted(schedule.keys(), 
                             key=lambda day: days_order.get(day.title(), 99))

        print(f'\nРасписание группы {self.our_group}:')
        for day in sorted_days:
            print(day.title())
            sorted_lessons = sorted(schedule[day], 
                                    key=lambda x: pairs_order.get(x.time, 99))

            for lesson in sorted_lessons:
                # Get the pair number from the dictionary or 
                # put a dash if the time is non-standard
                pair_num = pairs_order.get(lesson.time, '-')
                print(f'{pair_num}: {lesson}')
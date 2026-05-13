class Pair:
    '''
    Represents a single academic class (pair) in a schedule.

    Stores information about the day, time, subject, teacher, 
    classroom, and the student group.
    '''

    def __init__(self,
        day: str,
        time: str,
        subject: str,
        teacher: str,
        room: str,
        group: str
    ) -> None:
        '''
        Initialize the Pair instance.

        :param day: The day of the week (e.g., 'Monday').
        :param time: The time slot of the class.
        :param subject: The name of the subject.
        :param teacher: The name of the lecturer or teacher.
        :param room: The room or lecture hall number.
        :param group: The student group identifier.
        '''
        self.day = day
        self.time = time
        self.subject = subject
        self.teacher = teacher
        self.room = room
        self.group = group

    def __str__(self) -> str:
        '''
        Return a string representation of the class details.

        :return: Formatted string containing time, subject, teacher, and room.
        '''
        return (f'{self.time} - {self.subject} - '
                f'{self.teacher} - ауд. {self.room}')


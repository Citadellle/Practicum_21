from schedule import Schedule

def main() -> None:
    group = input('Введите номер группы (например 24704, 24702 или 24709): ')

    schedule = Schedule(group)
    schedule.load_data('schedule.txt')
    schedule.display_schedule()


if __name__ == '__main__':
    main()
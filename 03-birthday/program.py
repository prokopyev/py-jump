import datetime

print('---------------------------------------')
print('Birthday App')
print('---------------------------------------')
print()


def print_header():
    pass


def get_birthday_from_user():
    print('When were you born? ')
    year = int(input('Year [YYYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year, month, day)
    return birthday


def compute_day_between_dates(original_date, target_date):
    this_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = this_year - target_date
    return dt.days

1963
def print_birthday_info(days):
    if days < 0:
        print('You had your birthday {} days ago this year.'.format(-days))
    elif days > 0:
        print('Your birthday is in {} days!'.format(days))
    else:
        print('Today is your birthday!')


def main():
    print_header()
    bday = get_birthday_from_user()
    today = datetime.date.today()
    number_of_days = compute_day_between_dates(bday, today)
    print_birthday_info(number_of_days)

main()
import datetime

date_now = datetime.datetime.now()
years_old = date_now.year - 1920


def get_number_end(num) -> str:
    end_numbers = {
        'год': [1],
        'года': [2, 3, 4],
        'лет': [11, 12, 13, 14]  # Exceptions from russian language:)
    }
    if num % 100 in end_numbers['лет']:
        return 'лет'

    if num % 10 in end_numbers['год']:
        return 'год'
    elif num % 10 in end_numbers['года']:
        return 'года'

    return 'лет'




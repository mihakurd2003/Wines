import datetime


def validate_form(num) -> str:
    dict_of_end_numbers = {
        'год': [1],
        'года': [2, 3, 4],
        'лет': [11, 12, 13, 14]  # Exceptions from russian language:)
    }
    if num % 100 in dict_of_end_numbers['лет']:
        return 'лет'

    if num % 10 in dict_of_end_numbers['год']:
        return 'год'
    elif num % 10 in dict_of_end_numbers['года']:
        return 'года'

    return 'лет'


date_now = datetime.datetime.now()
years_old = date_now.year - 1920

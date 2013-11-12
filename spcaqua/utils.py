from django.utils.timezone import now


def today():
    return now().date()

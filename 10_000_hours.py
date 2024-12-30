import math


def working_days(days=365.25):
    return days * 5 / 7


def hours_to_years(sme_hours=10_000, daily_hrs=8, days=working_days(), days_off=10):
    return sme_hours / ((days - days_off) * daily_hrs)


print(hours_to_years(10_000, daily_hrs=7.5 * 0.7, days_off=30))

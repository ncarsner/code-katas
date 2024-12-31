"""How long does it take to become an expert?"""

PRIVATE_HOURS = 40
PUBLIC_HOURS = 37.5
FULL_ALLOCATION = 0.8
PARTIAL_ALLOCATION = 0.7


def working_days(days=365.25):
    return days * 5 / 7


def hours_to_years(expert_hours=10_000, daily_hrs=8, days=working_days(), days_off=10):
    return expert_hours / ((days - days_off) * daily_hrs)


working_styles = [
    {
        "role": "40-hour week @ 80%",
        "weekly_hours": PRIVATE_HOURS,
        "allocation": FULL_ALLOCATION,
    },
    {
        "role": "40-hour week @ 70%",
        "weekly_hours": PRIVATE_HOURS,
        "allocation": PARTIAL_ALLOCATION,
    },
    {
        "role": "37.5-hour week @ 80%",
        "weekly_hours": PUBLIC_HOURS,
        "allocation": FULL_ALLOCATION,
    },
    {
        "role": "37.5-hour week @ 70%",
        "weekly_hours": PUBLIC_HOURS,
        "allocation": PARTIAL_ALLOCATION,
    },
]

for style in working_styles:
    daily_hrs = (style["weekly_hours"] / 5) * style["allocation"]
    years = hours_to_years(10_000, daily_hrs=daily_hrs, days_off=30)
    print(f"{style['role']}: {years:.1f} years")

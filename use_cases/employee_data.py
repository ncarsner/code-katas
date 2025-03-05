from datetime import datetime, date


class Employee:
    def __init__(
        self, first_name, last_name, date_of_birth, department=None, job_title=None
    ):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.date_of_birth = self.parse_birthdate(date_of_birth)
        self.department = department
        self.job_title = job_title

    def parse_birthdate(self, birthdate):
        # Assuming birthdate is in format with leading Month and trailing Year
        try:
            birthdate = datetime.strptime(birthdate, "%m/%d/%y")
            birth_year = (
                birthdate.year
                if birthdate.date() <= datetime.now().date()
                else birthdate.year - 100
            )
        except ValueError:
            birthdate = datetime.strptime(birthdate, "%m/%d/%Y")
            birth_year = birthdate.year

        birth_day = birthdate.day
        birth_month = birthdate.month

        return date(birth_year, birth_month, birth_day)

    def age(self):
        today = date.today()
        dob = self.date_of_birth
        if not (today.month >= dob.month and today.day >= dob.day):
            age_offset = -1
        else:
            age_offset = 0
        age = today.year - dob.year + age_offset
        return age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# Example usage:
employee1 = Employee("Aaron", "anderson", "2/12/42")
# print(employee1.first_name)  # Output: Aaron
# print(employee1.last_name)  # Output: Anderson
print(employee1.full_name())  # Output: Aaron Anderson
print(employee1.date_of_birth, type(employee1.date_of_birth))
print(employee1.age())  # Output: 82 (or appropriate age based on current date)


# Example usage:
birthdate_list = [
    "01/15/98",  # 2-digit year (prior to current date)
    "03/10/2000",  # 4-digit year
    "05/20/90",  # 2-digit year (prior to current date)
    "06/30/2025",  # 4-digit year (in the future)
    "06/30/25",  # 2-digit year (in the past)
    "2/24/42",  # 2-digit year (prior to current date)
    "12/21/1987",
    "9/12/2055",
    "2/28/24",
    "2/29/24",
]

def parse_birthdate(birthdate):
    # Assuming birthdate is in format with leading Month and trailing Year
    try:
        birthdate = datetime.strptime(birthdate, "%m/%d/%y")
        birth_year = (
            birthdate.year
            if birthdate.date() <= datetime.now().date()
            else birthdate.year - 100
        )
    except ValueError:
        birthdate = datetime.strptime(birthdate, "%m/%d/%Y")
        birth_year = birthdate.year

    birth_day = birthdate.day
    birth_month = birthdate.month

    return date(birth_year, birth_month, birth_day)

# Test the function with the example birthdates
for birthdate in birthdate_list:
    parsed_birthdate = parse_birthdate(birthdate)
    print(f"Parsed birthdate for {birthdate}: {parsed_birthdate}")

from faker import Faker
# from faker import providers
# from faker.providers import internet

# call an instance of Faker
fake = Faker()

# for _ in range(5):
#     print(fake.ascii_company_email())

# fake.ascii_company_email()
# fake.ascii_email()
# fake.ascii_free_email()
# fake.ascii_safe_email()

fake.profile() # complete profile as json object
fake.simple_profile() # basic profile with personal info
fake.first_name()
fake.last_name()
fake.ssn()
# fake.file_name() # (category: Optional[str]=None, extension: Optional[str] = None)

# fake.address().split('\n')
fake.street_address()

# fake.building_number()
# fake.street_name()
# fake.street_suffix()
fake.city()
# fake.city_suffix()
# fake.country()

fake.company()
# fake.company_suffix()
fake.job()

# fake.date()
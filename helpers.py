from faker import Faker


fake = Faker('ru_RU')

def generate_random_courier_body():
    return {
        "login": fake.user_name(),
        "password": fake.password(length=10, upper_case=False, lower_case=True),
        "firstName": fake.name()
    }

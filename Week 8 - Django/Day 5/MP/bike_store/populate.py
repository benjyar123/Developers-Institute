from faker import Faker
from .models import Customer

fake = Faker()
customer = Customer()

print (fake)
print (customer)

customer.first_name = fake.first_name()
customer.last_name = fake.email()
customer.phone_number = fake.phone_number()
customer.address = fake.address()
customer.city = fake.city()
customer.country = fake.county()

print (fake)
print (customer)
#
print("hello")
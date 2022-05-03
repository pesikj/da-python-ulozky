import json
from faker import Faker
import random
fake = Faker(["cs-CZ"])
Faker.seed(0)

data = []

for _ in range(10):
    row = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "birth_number": fake.birth_number(),
        "friends": ", ".join([fake.first_name() for _ in range(0, random.randint(1, 5))]),
        "permanent_address": fake.address(),
        "phone_number": fake.phone_number(),
    }
    if random.uniform(0, 1) > 0.8:
        row["mail_address"] = fake.address()
    data.append(row)

with open("people.json", mode="w") as people:
    json.dump(data, people, indent=4, ensure_ascii=False)



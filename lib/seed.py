#!/usr/bin/env python3

from db import session
from models import Company, Dev, Freebie

# Script goes here!
company1 = Company(name="Google", founding_year=1998)
company2 = Company(name="Amazon", founding_year=1994)
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")

freebie1 = Freebie(item_name="Sticker", value=1, dev=dev1, company=company1)
freebie2 = Freebie(item_name="T-shirt", value=10, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Mug", value=5, dev=dev2, company=company1)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2, freebie3])
session.commit()


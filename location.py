# Project to find the country of a number.

import phonenumbers
from phonenumbers import geocoder
phone_number = phonenumbers.parse("+43 7738779076")
print(geocoder.description_for_number(phone_number, 'en'))
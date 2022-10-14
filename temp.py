import phonenumbers
import time
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type

def phone_catcher():
    try:
        #number = "+447939418683"
        number = input("Please enter courier mobile phone number by beginning with the country code\neg: +447123456789\n")
        mobile_number = carrier._is_mobile(number_type(phonenumbers.parse(number)))
    except Exception as e:
        print(f"Error with phone number, error code: {e}")
        time.sleep(2)
        phone_catcher()
    if mobile_number is True:
        number = number.replace(" ","")
        print(number)
        return number
    else:
        print(f"The phone number you have entered is not a valid mobile number, please re-enter\nEntry screen will reload shortly...")
        time.sleep(2)
        phone_catcher()

phone_catcher()
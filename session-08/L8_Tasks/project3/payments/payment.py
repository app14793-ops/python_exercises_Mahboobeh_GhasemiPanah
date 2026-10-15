from .fee import calculate_fee
from accounts.authentication import login

def make_payment():
    login()
    calculate_fee()
    pass
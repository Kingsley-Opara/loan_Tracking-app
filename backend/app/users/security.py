from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def generate_hash(password):
    ph = PasswordHasher()
    return ph.hash(password)


def verify_hash(pw_hash, pw_raw):
    ph = PasswordHasher()
    verifield = False
    msg = None

    try:
        
        verifield = ph.verify(pw_hash, pw_raw)

    except VerifyMismatchError as e:
        msg = f'Invalid Password and Email {e}'
        verifield = False
    except Exception as e:
        msg = f'Invalid Password and Email {e}'
        verifield = False
    return verifield, msg


        
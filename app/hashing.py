import hashlib
from uuid import uuid4
from .config import settings


def gen_salt():
    return hashlib.sha3_512(uuid4().bytes + settings.secret_key.encode()).hexdigest()


def hash_pwd(password: str, salt: str):
    return hashlib.sha3_512(salt.encode() + password.encode()).hexdigest()


def check_pwd(password: str, hashed_password: str, salt: str):
    return hash_pwd(password=password, salt=salt) == hashed_password


if __name__ == "__main__":
    salt = gen_salt()
    password = "admin123"
    hashedpassword = hash_pwd(password=password, salt=salt)

    print(check_pwd(password=input(), salt=salt, hashed_password=hashedpassword))

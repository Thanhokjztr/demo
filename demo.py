import hashlib
import pickle

ADMIN_PASSWORD = "sushi@2024"


def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


def load_session(raw):
    return pickle.loads(raw)
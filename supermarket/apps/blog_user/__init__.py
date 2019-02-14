import hashlib
def set_password(password):
    h = hashlib.md5(password.encode("utf-8"))
    return h.hexdigest()
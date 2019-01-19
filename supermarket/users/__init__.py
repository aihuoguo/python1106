import hashlib


def set_password(password):
    # 加密方法
    h = hashlib.md5(password.encode('utf-8'))
    return h.hexdigest()
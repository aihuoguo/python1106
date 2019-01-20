import hashlib
from supermarket.settings import SECRET_KEY

def set_password(password):
    # 循环加密+加盐
    for v in  range(1000):
        pwd_str='{},{}'.format(password,SECRET_KEY)
        h = hashlib.md5(pwd_str.encode('utf-8'))
        return h.hexdigest()
import hashlib


def key_md5(string):
    md5 = hashlib.md5()
    md5.update(string.encode())
    key=str(md5.hexdigest())
    return key

#coding:utf8

import hashlib

db = {}

def register(username,password):
    db[username] = get_md5(password + username + 'Salt')


def get_md5(passwd):
    md5 = hashlib.md5()
    md5.update(passwd)
    return md5.hexdigest()


def login(username,password):
    if db[username] == get_md5(password + username + 'Salt'):
        return True
    else:
        return False


if __name__ == '__main__':
    register('fred','123456')
    register('tom','1234aed56')
    register('mike','12w3eds')
    register('song','1qaz2wsx')
    print db
    print login('fred','123456')
    print login('song','1qaz2wsx')
import pyotp
import qrcode
import Constants as keys

def gen_key():
    key = pyotp.random_base32()
    return key

def gen_url(key: str):
    return pyotp.totp.TOTP(key).provisioning_uri(name='TelegramBot', issuer_name=keys.bot_name)

def gen_code(key: str):
    totp = pyotp.TOTP(key)
    return totp.now()

def verify_code(key: str, code: str):
    totp = pyotp.TOTP(key)
    return totp.verify(code)

def gen_qr(uri):
    qr = qrcode.make(uri)
    qr.save('qr.png')

def createKey():
    key = gen_key()
    uri = gen_url(key)
    gen_qr(uri)
    code = gen_code(key)
    verify_code(key, code)
    return key

def check2fa(key, text):
    code = gen_code(key)
    verify_code(key, code)
    if text == code:
        correct = "True"
    else:
        correct = "False"
    return correct
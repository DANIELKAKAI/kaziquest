from django.core.mail import send_mail


def send_verify_code(user_email):
	code  = encrypt(plaintext=user_email)
	msg = "Click the following link to verify email:\n http://localhost:8000/verify-email/?code={}".format(code)
	send_mail('Confirm email', msg, 'Unkown  <devemail359@gmail.com>', [user_email], fail_silently=True)


key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n=1, plaintext=''):
    """Encrypt the string and return the ciphertext"""
    result = ''

    for l in plaintext.lower():
        try:
            i = (key.index(l) + n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result.lower()


def decrypt(n=1, ciphertext=''):
    """Decrypt the string and return the plaintext"""
    result = ''

    for l in ciphertext:
        try:
            i = (key.index(l) - n) % 26
            result += key[i]
        except ValueError:
            result += l

    return result


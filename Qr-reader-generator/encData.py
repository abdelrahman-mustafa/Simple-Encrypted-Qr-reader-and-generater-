import sys
import os
import base64
from Crypto.Cipher import AES
import hashlib

class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        key = hashlib.sha256(key.encode()).digest()
        self.key = key
        self.iv = os.urandom(16)

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = os.urandom(16)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        encrypted = cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        aes = AES.new(self.key, AES.MODE_CBC, self.iv)
        decrypted = aes.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * bytes(chr(self.bs - len(s) % self.bs), 'utf-8')

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


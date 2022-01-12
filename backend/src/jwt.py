import secrets
import time

class Token:
    expiration_time = None

    def __init__(self):
        self.token_string = secrets.token_hex(20)
        self.expiration_time = time.time() + 30

class TokenStorage:
    def __init__(self):
        self.tokens = []

    def create_token(self):
        token = Token()
        self.tokens.append(token)
        return token.token_string

    def refresh_token(self, token_index):
       self.tokens[token_index].expiration_time = time.time() + 30

    def token_expired(self, token):
        print(time.time())
        print(token.expiration_time)
        if token.expiration_time > time.time():
            return False
        return True

    def token_exists(self, token_string):
        for i in range(len(self.tokens)):
            if self.tokens[i].token_string == token_string:
                if self.token_expired(self.tokens[i]):
                    return False
                else:
                    self.refresh_token(i)
                return True
        return False
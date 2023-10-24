from random import randint

def private_key(p) -> int:
    random_key = randint(2, p-1)    
    return random_key



def public_key(p, g, private):
    public = pow(g, private, p)
    return public


def secret(p, public, private):
    secret = pow(public, private, p)
    return secret

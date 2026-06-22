from pwdlib import PasswordHash


pwd_hasher = PasswordHash.recommended()

#################################################
################ utils functions ################
#################################################
def hash_password(password_: str) -> str :
    return pwd_hasher.hash(password_)

def verify_password(input_password_: str, hashed_password_: str) -> bool :
    return pwd_hasher.verify(input_password_, hashed_password_)

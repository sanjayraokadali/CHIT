from Root import *

crypter = EncryptDecrypt()

message = "Some message"

En_message = crypter.string_encrypter(message)
print(En_message)

De_message = crypter.string_decrypter(En_message)
print(De_message)
"""
    This project is for testing money transfer using razorpay

"""
import pandas as pd
import pyAesCrypt as crypt
import numpy as np
import pyrebase


class Chit:  

    def __init__(self):
        pass


class User(Chit):

    def __init__(self,
                first_name,
                last_name,
                username,
                password,
                email,
                phone
                ):

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
    
    def sign_up(self):

        pass

    def show_details(self):

        return f"""
                {self.first_name} {self.last_name}
                {self.username} {self.email}
                """


class EncryptDecrypt(Chit):

    def data_encrypter(self):

        return crypt.encryptFile("some data")

    def data_decrypter(self):

        return crypt.decryptFile("some data")

class UpCloud(Chit):

    def __init__(self,configs):

        self.configs = configs
    
    def setup_connection(self):

        firebase = pyrebase.initialize_app(self.configs)



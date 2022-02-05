"""
    This project is for testing money transfer using razorpay

"""
from dataclasses import dataclass
from email import header
import pandas as pd
import pyAesCrypt as crypt
import numpy as np
# import pyrebase
import os
import csv

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
                {self.first_name} {self.last_name}: {self.username}, {self.email}
                """


class EncryptDecrypt(Chit):

    def data_encrypter(self):

        return crypt.encryptFile("some data")

    def data_decrypter(self):

        return crypt.decryptFile("some data")

class UpCloud(Chit):

    def __init__(self,configs):

        self.configs = configs
    
    def __call__(self):

        return pyrebase.initialize_app(self.configs)
            
    def upload(self):
        pass

    def download(self):
        pass

class Data(Chit):

    def __init__(self,
                 file_path,
                 file_name,
                 data):
        
        self.file_path = file_path
        self.file_name = file_name
        self.data = data

    def write_to_csv(self):

        if len(os.listdir(self.file_path)) == 0:
            header = ['First Name','Last Name','Username','Password','Email','Phone','File Location']
            with open(f"{self.file_path}/{self.file_name}", "w") as file:

                writer = csv.writer(file)

                writer.writerow(header)
                writer.writerow(self.data)
        else:

            with open(f"{self.file_path}/{self.file_name}", "a") as file:

                writer = csv.writer(file)

                writer.writerow(self.data)

class StructData():

    def read_data_frame(self,file_loc):

        return pd.read_csv(file_loc)

        

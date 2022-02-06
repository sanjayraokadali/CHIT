from Root import *

crypter = EncryptDecrypt()

user = User(first_name='Dom',
            last_name='Wills',
            username='dom.wills',
            password= 'Dom@123',
            email="dom.w@chit.com",
            phone='+919804003214')


user_data = [user.first_name,
             user.last_name,
             user.username,
             user.password,
             user.email,
             user.phone,
             'C:/Users/91701/Documents/GitHub/CHIT/Data/UserData']

data = Data(file_path=user_data[-1],
            file_name='user.csv',
            data=user_data
            )

sqldb = SqlDB("localhost", "sanjayraokadali", "23March_an", "UserDB")

insertion = sqldb.insert_user(obj = sqldb, data = user, file_loc = user_data[-1])

if insertion:

    print("User inserted to Database")
else:

    print("User data not inserted to the Database")
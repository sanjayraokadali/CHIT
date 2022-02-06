from Root import *


user = User(first_name='Alice',
            last_name='Fisher',
            username='alice.fisher',
            password='Alice@123',
            email="alice.f@chit.com",
            phone='+917894561230')


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

data.write_to_csv()

struct_data = StructData()

print(struct_data.read_data_frame(f"{data.file_path}/{data.file_name}"))

sqldb = SqlDB("localhost", "sanjayraokadali", "23March_an", "UserDB")


insertion = sqldb.insert_user(obj = sqldb, 
                             data = user, 
                             file_loc = user_data[-1]
                             )

if insertion:

    print("User inserted to Database")
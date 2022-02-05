

configs = {    
  "apiKey": "AIzaSyB5tPj6I6W6th5zQlo7JG1fNgnuIyhw8O0",
  "authDomain": "chit-f086e.firebaseapp.com",
  "databaseURL": "https://chit-f086e-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "chit-f086e",
  "storageBucket": "chit-f086e.appspot.com",
  "messagingSenderId": "1097752869866",
  "appId": "1:1097752869866:web:5fcbafe4c8c8e503271093",
  "measurementId": "G-X9YP74776V"
}


firebase = pyrebase.initialize_app(configs)

db = firebase.database()

print(db)
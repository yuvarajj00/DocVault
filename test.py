import pyrebase

# Firebase configuration
Config = {
    "apiKey": "AIzaSyB6Ey-wlu-9xgOqn2CPEP6myZMKcUjOXFM",
    "authDomain": "pbl-project-3ef8d.firebaseapp.com",
    "projectId": "pbl-project-3ef8d",
    "storageBucket": "pbl-project-3ef8d.appspot.com",
    "messagingSenderId": "873183429790",
    "appId": "1:873183429790:web:4eb49025fb7e43b876278f",
    "measurementId": "G-FVXBQJGMZS",
    "databaseURL": "https://pbl-project-3ef8d-default-rtdb.firebaseio.com/"
}

# Initialize the app with the configuration
firebase = pyrebase.initialize_app(Config)
db = firebase.database()

data = {
    'name' : 'john',
    'age' : 20
}

# for i in range(7):
#     db.push({
#         'name' : 'john_' +str(i+1),
#         'roll' : i+1
#     })

user = db.get()
print(user.val())
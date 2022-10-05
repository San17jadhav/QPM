import pyrebase

firebaseConfig={
    'apiKey': "AIzaSyAdr1jjvwuueiNe2ZkpWSTkfala3b6lHBo",
    'authDomain': "qpmauth.firebaseapp.com",
    'projectId': "qpmauth",
    'storageBucket': "qpmauth.appspot.com",
    'messagingSenderId': "559723322830",
    'appId': "1:559723322830:web:24097fabab5011b213df9f",
    'measurementId': "G-4Q5822MEGE"
    }
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
print('so')

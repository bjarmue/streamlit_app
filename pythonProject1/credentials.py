import pickle
from pathlib import Path

file_path= Path(__file__).parent/ "hashed_pw.pkl"
with file_path.open("rb") as file:
    hashed_passwords=pickle.load(file)
def data():
    credentials = {
            "usernames":{
                "test1":{
                    "name":"1",
                    "password":str(hashed_passwords[0])
                    },
                "test2":{
                    "name":"2",
                    "password": str(hashed_passwords[1])
                    }            
                }
            }
    return credentials

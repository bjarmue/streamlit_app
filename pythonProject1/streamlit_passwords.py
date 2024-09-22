import pickle
from pathlib import Path
from streamlit_authenticator.utilities.hasher import Hasher


names = ["User1", "User2"]
usernames = ["user1","user2"]
passwords = ["XXX","XXX"]

hashed_passwords= Hasher(passwords).generate()

file_path =Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)


import json


def read_credentials(path: str = "auth.json"):
    with open(path, 'r') as file:
        creds = json.loads(file.read())
        print(creds)
        return creds

def check_password(username, password):
    creds = read_credentials()
    for i in creds:
        if i['user']==username:
            if i['password']==password:
                return True
    return False

def update_score(submission_time,score,username, path = "auth.json"):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            dict["score"] = score
            dict["submission_time"] = submission_time
    with open(path, 'w+') as f:
        f.write(json.dumps(creds, indent=4))

def check_score(username):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            if dict['score'] > 0:
                return False
            else:
                return True


def update_starting_time(starting_time,username, path = 'auth.json'):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            dict["starting_time"] = starting_time
    with open(path, 'w+') as f:
        f.write(json.dumps(creds, indent=4))








if __name__ == '__main__':
    user = input("Dati userul:")
    password=input("Dati parola:")
    if check_password(user,password)==True:
        print("corect")
    else:
        print("nu")
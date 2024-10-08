import json


def read_credentials(path: str = "auth.json"):
    with open(path, 'r') as file:
        creds = json.loads(file.read())
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

def read_score(username):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            return dict['score']

def read_start_time(username):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            return dict['starting_time']

def read_end_time(username):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            return dict['submission_time']




def update_starting_time(starting_time,username, path = 'auth.json'):
    creds = read_credentials()
    for dict in creds:
        if dict["user"] == username:
            dict["starting_time"] = starting_time
    with open(path, 'w+') as f:
        f.write(json.dumps(creds, indent=4))

def reset_score_and_time(path = 'auth.json'):
    creds = read_credentials()
    for dict in creds:
        dict["score"]=0
        dict["starting_time"] = ""
        dict["submission_time"] = ""
    with open(path, 'w+') as f:
        f.write(json.dumps(creds, indent=4))





if __name__ == '__main__':
   reset_score_and_time()
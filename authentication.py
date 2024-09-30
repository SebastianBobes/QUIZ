import json


def read_credentials(path: str = "auth.json"):
    with open(path, 'r') as file:
        creds = json.loads(file.read())['teams']
        return creds
        # print(creds)

def check_password(creds: list):
    name = request.form["name"]
    password = "TaviMatei"
    for i in creds:
        if password==i['password']:
            print("Bravo!")


if __name__ == '__main__':
    creds = read_credentials()
    check_password(creds)
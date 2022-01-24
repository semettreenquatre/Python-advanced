def user_connection(username):
    import random
    for i in range(random.randint(10, 20)):
        yield f"{username} message{i}"

def establish_connection(auth=True):
    import random
    id = f"{random.randint(0,100000000):010}"
    if auth:
        yield f"auth {id}"
    yield from user_connection(id)
    if auth:
        yield f"disconnect {id}"

def connection():
    import random
    connections = [establish_connection(True) for i in range(10)]
    connections.append(establish_connection(False))
    connections.append(establish_connection(False))
    while len(connections):
        conn = random.choice(connections)
        try:
            yield next(conn)
        except StopIteration:
            del connections[connections.index(conn)]

class Is_User(Exception):
    pass

class Disconnection(Exception):
    pass

class Message(Exception):
    pass

def connect_user():
    users = []
    user_coroutines = []
    while True:
        try:
            user = yield
            users.append(user)
            file_name = user + ' messages.txt'
            file = open(file_name, 'w')
            cor = write_to_file(file)
            user_coroutines.append(cor)
            next(cor)
        except Is_User:
            user = yield
            if user in users:
                yield True
            else:
                yield False
        except Message:
            Input = yield
            user = Input[0]
            message = ''
            for i in range(1, len(Input)):
                message = message + '\n' + Input[i]
            user_coroutines[users.index(user)].send(message)
        except Disconnection:
            user = yield
            user_coroutines[users.index(user)].throw(Disconnection)
            user_coroutines[users.index(user)].close()
            user_coroutines.pop(users.index(user))
            users.pop(users.index(user))

def write_to_file(file):

    while True:
        try:
            message = yield
            file.write(message)
        except Disconnection:
            file.close()
            yield

connect_user = connect_user()
next(connect_user)
for el in connection():
    print(el)
    Input = list(el.split())
    if Input[0] == 'auth':
        connect_user.send(Input[1])
    elif Input[0] == 'disconnect':
        connect_user.throw(Disconnection)
        connect_user.send(Input[1])
    else:
        connect_user.throw(Is_User)
        flag = connect_user.send(Input[0])
        next(connect_user)
        if flag:
            connect_user.throw(Message)
            connect_user.send(Input)


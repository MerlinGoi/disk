from numspy import Way2sms

def send_sms():
    username = input("your username: ")
    password = input("password: ")
    print("=====+=======+=====")
    phone_no = input("victims phone: ")
    msg = input("massage: ")
    w2s = Way2sms()
    w2s.login(username, password)
    w2s.send(phone_no, msg)
    w2s.logout()
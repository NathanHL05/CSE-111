import webbrowser
with open('passwords.txt', 'w') as file:
    pass
with open('passwords.txt', 'r') as file:
    pass_content = file.readlines()
passwords = [line.strip() for line in pass_content]
# with open('info.txt', 'r') as file:
#     info_content = file.read()
# info = [item.strip() for item in info_content.split('"')]


def make_pass():
    new = input("What is your new password: ")
    passwords.append(new)
    with open("passwords.txt","a") as f:
        f.write(f"{new} \n")


def check_pass(password):
    if password in passwords:
        return True
    else:
        print("This password is incorrect")
        return False



#def add_pass():



#def add_info(list = info):
    new = input("What do you want to add to your saved content?: ")



#def get_info(password, list = info):


def main():
    if not passwords:
        print("It looks like you don't have a password")
        make_pass()
    new = input("do you want to make a new password? (Y/N): ")
    if new in ('y','Y'):
        make_pass()
    correct = False
    while correct == False:
            code = input("What is your password?: ")
            correct = check_pass(code)
            if correct == True:
                print("Your password is correct")
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&list=RDdQw4w9WgXcQ&start_radio=1")
            else:
                print("your password is incorrect, try again")

   
       
        
main()

with open('passwords.txt', 'a') as file:
    for item in passwords:
        file.write(item + '\n')

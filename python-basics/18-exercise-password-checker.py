#18-exercise-password-checker.py

uname = input('Enter username: ')
password = input('Enter password:')
pass_len = len(password)
print(f"{uname}, your password {'*' * pass_len} is {pass_len} letters long")
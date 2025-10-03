import keyring  

keyring.set_password(
    'my_awesome_app', 
    'my_user', 
    'my_secret_password123')

password = keyring.get_password('my_awesome_app', 'my_user')
if password:
    print(f'The password is: {password}')
else:
    print('Password not found.')

try:     
    keyring.delete_password('my_awesome_app', 'my_user')     
    print('Password deleted.') 
except keyring.errors.PasswordDeleteError:     
    print('Password not found or could not be deleted.') 
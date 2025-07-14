import os
file_path= 'text/text.txt' #Relative path
file_path1= 'C:/Users/sneha/OneDrive/Desktop'#Absolute path
if os.path.exists(file_path1):
    print(f'location {file_path1} is exist')
    if os.path.isfile(file_path1): # another is isdir()
        print('its a file')
    else:
        print('its not a file')
else:
    print(f'location {file_path1} is not exist')
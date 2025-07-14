#creating file 
# 'w'= write, 'x'=write if not exsist, a=add info in file
text='HI... Im sneha, i created this file in desktop'
file_path2= '"C:\\Users\\sneha\\OneDrive\\Desktop\\aiss\\New Text Document.txt'
with open(file_path2,'w') as file:
    file.write(text)
    print(f"the text file {file_path2} is created ")

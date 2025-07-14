#Tips=' Drink water daily '
employees=['sneha','aishu', 'vazu','sudi']
myfile="C:\\Users\\sneha\\OneDrive\\Desktop\\page.txt"
with open(myfile, 'a') as File:
    for employee in employees:
        File.write('\n'+employee)
    print('file has created')
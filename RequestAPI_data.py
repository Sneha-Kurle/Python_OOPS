import requests
url='https://pokeapi.co/api/v2/'
def get_info(name):
    main_url=f'{url}/pokemon/{name}'
    response=requests.get(main_url)
    if response.status_code==200:
        info=response.json()
        return info
    else:
        print('not able to retrive')
name='ditto'
retrive=get_info(name)
if retrive:
    print(f"{retrive['name']}")
    print(f'{retrive['id']}')
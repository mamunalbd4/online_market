import requests

url = 'https://drrabangladesh-my.sharepoint.com/:x:/g/personal/mamun_arktechbd_org/EeUPMTenrYNFh4YechyHKAUBaUadsZ7MtOboEDv5zVdAIQ?e=MZgv4C'
response = requests.get(url)

with open('data.xlsx', 'wb') as f:
    f.write(response.content)

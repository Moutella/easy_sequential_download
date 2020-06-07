import requests
from decouple import config
import os
#Getting configs
url = config('url')
min_value = int(config('min_value'))
max_value = int(config('max_value'))
file_format = config('file_format')
num_pad = int(config('num_pad'))

#create downloads folder
if not os.path.isdir('downloads'):
    os.mkdir('downloads')

for current_value in range(min_value, max_value+1):
    
    if(num_pad):
        current_value = str(current_value).zfill(num_pad)
    r = requests.get(url.format(current_value))
    open('downloads/{}.{}'.format(current_value, file_format), 'wb').write(r.content)
    print("downloaded {}.{}".format(current_value, file_format))
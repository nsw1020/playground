from PIL import Image
from io import BytesIO
import urllib3

http = urllib3.PoolManager()

image_url = 'URL'

r = http.request('GET', image_url, preload_content=False)
image = Image.open(BytesIO(r.read()))
r.release_conn()

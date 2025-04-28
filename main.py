import requests
from random import choice

from tkinter import Tk, Label, Button
from PIL     import Image, ImageTk
from io      import BytesIO

base_url = 'https://api.unsplash.com'
api_key = '_oED5ZIDWwfgdYKfSFKTH7_ceenn9Jpb9W3ykoeKGDA'
api_url = f'{base_url}/search/photos?client_id={api_key}&query=bird&per_page=1000'

root = Tk()

def show_rand_img() -> None:

    res = requests.get(api_url)

    if res.status_code != 200:
        img_label.config(text=f'Couldn\'n get an image\nError: {res.status_code}'); return

    data = res.json()

    img_url = choice(data['results'])['urls']['regular']
    img_res = requests.get(img_url)

    if img_res.status_code != 200:
        img_label.config(text=f'Couldn\'n get an image\nError: {img_res.status_code}'); return

    img_bin = img_res.content
    image_stream = BytesIO(img_bin)

    img = Image.open(image_stream)
    resize_factor = max(img.size)/400
    new_x, new_y = int(img.size[0]/resize_factor), int(img.size[1]/resize_factor)
    img = img.resize((new_x, new_y))

    img = ImageTk.PhotoImage(img)
    img_label.config(text='', image=img)
    img_label.image = img

img_label = Label()

Button(text='Get random bird image', command=show_rand_img).pack(fill='x')
img_label.pack(fill='x')

root.title('Random bird images')
root.geometry('400x400')
root.mainloop()

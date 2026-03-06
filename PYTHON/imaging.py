from PIL import Image

with Image.open("C:/Users/dbda.STUDENTSDC/Pictures/WALLPAPER/spdmn.jpg") as img:
    img.load()
    # img.show()
l = img.convert('L')
#l.show( )

red, green, blue = img.split()
zero_band = blue.point(lambda _:30)
red_img = Image.merge('RGB', (blue, zero_band, zero_band))
red_img.show()
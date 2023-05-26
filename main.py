from PIL import Image, ImageFilter
def proc1():
    a = Image.open('1.jpg')
    a.show()

    widht, height = a.size
    format = a.format
    mode = a.mode

    print('Ширина: ', widht)
    print('Высота: ', height)
    print('Формат: ', format)
    print('цветовая модель: ', mode)

def proc2():
    a = Image.open('2.jpg')
    a.show()

    b = a.resize((a.width // 3, a.height // 3))
    b.show()

    c = b.rotate(180)
    c.save('2.1.jpg')
    c.show()

    d = b.transpose(Image.FLIP_LEFT_RIGHT)
    d.save('2.2.jpg')
    d.show()

def proc3():
    a = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for x in a:
        with Image.open(x) as b:
            b.load()
            c = b.filter(ImageFilter.SMOOTH)
            d = c.filter(ImageFilter.FIND_EDGES)
            d.show()
            d.save("3.1" + x)

def proc4():
    a = Image.open("5.jpg")
    b = Image.open("6.jpg")

    b = b.resize([1920, 1200])
    a.paste(b, [300, 300], mask = b)
    a.show()

proc1()
proc2()
proc3()
proc4()
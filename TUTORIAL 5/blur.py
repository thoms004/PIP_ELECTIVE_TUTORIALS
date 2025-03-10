from images import Image
from functools import reduce

image = Image(r"D:\Python\IMG.gif")  

def blur(image):
    def tripleSum(triple1, triple2):
        (r1, g1, b1) = triple1
        (r2, g2, b2) = triple2
        return (r1 + r2, g1 + g2, b1 + b2)

    new = image.clone()

    width, height = image.getWidth(), image.getHeight()
    
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            oldP = image.getPixel(x, y)
            left = image.getPixel(x - 1, y)
            right = image.getPixel(x + 1, y)
            top = image.getPixel(x, y - 1)
            bottom = image.getPixel(x, y + 1)
            
            sums = reduce(tripleSum, [oldP, left, right, top, bottom])
            averages = tuple(map(lambda x : x // 5, sums))
            new.setPixel(x, y, averages)
    return new
            
blurred_image = blur(image)
blurred_image.draw()
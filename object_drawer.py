from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown

def draw_شیر(pdf, x=100, y=700):
    # شیر (Lion) - simple lion face
    pdf.setFillColor(yellow)
    pdf.circle(x, y, 40, stroke=1, fill=1)  # face
    pdf.setFillColor(brown)
    pdf.circle(x, y, 50, stroke=1, fill=0)  # mane
    pdf.setFillColor(black)
    pdf.circle(x-15, y+10, 5, stroke=1, fill=1)  # left eye
    pdf.circle(x+15, y+10, 5, stroke=1, fill=1)  # right eye
    pdf.setFillColor(pink)
    pdf.circle(x, y-10, 6, stroke=1, fill=1)  # nose
    pdf.setStrokeColor(black)
    pdf.arc(x-10, y-20, x+10, y-10, startAng=200, extent=140)  # mouth

def draw_مرغ(pdf, x=200, y=700):
    # مرغ (Chicken) - simple chicken
    pdf.setFillColor(white)
    pdf.circle(x, y, 30, stroke=1, fill=1)  # body
    pdf.setFillColor(yellow)
    pdf.circle(x, y+30, 15, stroke=1, fill=1)  # head
    pdf.setFillColor(red)
    pdf.circle(x, y+45, 5, stroke=1, fill=1)  # comb
    pdf.setFillColor(black)
    pdf.circle(x+5, y+35, 2, stroke=1, fill=1)  # eye
    pdf.setFillColor(yellow)
    pdf.line(x+10, y+30, x+20, y+25)  # beak

def draw_پنیر(pdf, x=300, y=700):
    # پنیر (Cheese) - simple cheese wedge
    pdf.setFillColor(yellow)
    pdf.rect(x, y, 40, 20, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.circle(x+10, y+10, 3, stroke=1, fill=1)
    pdf.circle(x+25, y+15, 2, stroke=1, fill=1)
    pdf.circle(x+35, y+5, 2, stroke=1, fill=1)

def draw_نان(pdf, x=400, y=700):
    # نان (Bread) - simple bread loaf
    pdf.setFillColor(brown)
    pdf.roundRect(x, y, 50, 25, 10, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.circle(x+15, y+12, 3, stroke=1, fill=1)
    pdf.circle(x+35, y+18, 2, stroke=1, fill=1)

def draw_شکر(pdf, x=500, y=700):
    # شکر (Sugar) - simple sugar cubes
    pdf.setFillColor(white)
    pdf.rect(x, y, 15, 15, stroke=1, fill=1)
    pdf.rect(x+10, y+10, 15, 15, stroke=1, fill=1)

# ...continue for other words...

# Example usage:
def create_sample_pdf(filename):
    c = canvas.Canvas(filename)
    draw_شیر(c)
    draw_مرغ(c)
    draw_پنیر(c)
    draw_نان(c)
    draw_شکر(c)
    c.save()

create_sample_pdf("sample_icons.pdf")

from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown, orange

def draw_نمک(pdf, x=100, y=600):
    # نمک (Salt) - salt shaker
    pdf.setFillColor(gray)
    pdf.rect(x, y, 20, 30, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x, y+30, 20, 10, stroke=1, fill=1)
    pdf.setFillColor(black)
    for i in range(3):
        pdf.circle(x+5+i*5, y+35, 1, stroke=1, fill=1)

def draw_قهوه(pdf, x=160, y=600):
    # قهوه (Coffee) - coffee cup
    pdf.setFillColor(white)
    pdf.rect(x, y, 25, 20, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.rect(x+2, y+2, 21, 10, stroke=0, fill=1)
    pdf.setFillColor(black)
    pdf.arc(x+20, y+5, x+30, y+15, 0, 180)  # handle

def draw_چای(pdf, x=220, y=600):
    # چای (Tea) - tea cup
    pdf.setFillColor(white)
    pdf.circle(x, y+10, 12, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.circle(x, y+10, 8, stroke=0, fill=1)
    pdf.setFillColor(black)
    pdf.arc(x+8, y+10, x+18, y+20, 0, 180)  # handle

def draw_آب(pdf, x=280, y=600):
    # آب (Water) - water drop
    pdf.setFillColor(blue)
    path = pdf.beginPath()
    path.moveTo(x, y)
    path.curveTo(x-10, y+20, x+10, y+20, x, y)
    path.lineTo(x, y+25)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_شیرینی(pdf, x=340, y=600):
    # شیرینی (Pastry) - simple cookie
    pdf.setFillColor(yellow)
    pdf.circle(x, y+10, 12, stroke=1, fill=1)
    pdf.setFillColor(pink)
    pdf.circle(x, y+10, 5, stroke=1, fill=1)

def draw_کیک(pdf, x=400, y=600):
    # کیک (Cake) - slice of cake
    pdf.setFillColor(pink)
    pdf.rect(x, y, 25, 15, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x, y+15, 25, 5, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.circle(x+12, y+22, 3, stroke=1, fill=1)

def draw_بستنی(pdf, x=460, y=600):
    # بستنی (Ice cream) - cone with scoop
    pdf.setFillColor(orange)
    path = pdf.beginPath()
    path.moveTo(x, y)
    path.lineTo(x+10, y)
    path.lineTo(x+5, y-20)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)
    pdf.setFillColor(pink)
    pdf.circle(x+5, y+7, 7, stroke=1, fill=1)

def draw_پیتزا(pdf, x=520, y=600):
    # پیتزا (Pizza) - pizza slice
    pdf.setFillColor(yellow)
    path = pdf.beginPath()
    path.moveTo(x, y)
    path.lineTo(x+20, y)
    path.lineTo(x+10, y+25)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)
    pdf.setFillColor(red)
    pdf.circle(x+7, y+10, 2, stroke=1, fill=1)
    pdf.circle(x+13, y+15, 2, stroke=1, fill=1)

def draw_همبرگر(pdf, x=100, y=540):
    # همبرگر (Hamburger)
    pdf.setFillColor(brown)
    pdf.ellipse(x, y+10, x+40, y+25, stroke=1, fill=1)  # top bun
    pdf.setFillColor(green)
    pdf.rect(x+5, y+10, 30, 5, stroke=0, fill=1)  # lettuce
    pdf.setFillColor(brown)
    pdf.rect(x+5, y+5, 30, 5, stroke=0, fill=1)  # patty
    pdf.setFillColor(yellow)
    pdf.ellipse(x, y, x+40, y+10, stroke=1, fill=1)  # bottom bun

def draw_ساندویچ(pdf, x=160, y=540):
    # ساندویچ (Sandwich)
    pdf.setFillColor(yellow)
    pdf.rect(x, y+10, 40, 10, stroke=1, fill=1)  # bread
    pdf.setFillColor(green)
    pdf.rect(x, y+5, 40, 5, stroke=0, fill=1)  # lettuce
    pdf.setFillColor(red)
    pdf.rect(x, y, 40, 5, stroke=0, fill=1)  # tomato

def draw_نودل(pdf, x=220, y=540):
    # نودل (Noodle) - bowl with noodles
    pdf.setFillColor(white)
    pdf.ellipse(x, y, x+30, y+10, stroke=1, fill=1)  # bowl
    pdf.setFillColor(yellow)
    for i in range(3):
        pdf.arc(x+5+i*7, y+2, x+10+i*7, y+8, 0, 180)

def draw_میوه(pdf, x=280, y=540):
    # میوه (Fruit) - apple
    pdf.setFillColor(red)
    pdf.circle(x, y+10, 10, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.line(x, y+20, x, y+25)

def draw_سبزی(pdf, x=340, y=540):
    # سبزی (Vegetable) - carrot
    pdf.setFillColor(orange)
    pdf.rect(x, y, 10, 25, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.line(x+5, y+25, x+5, y+35)

def draw_کفش(pdf, x=400, y=540):
    # کفش (Shoe)
    pdf.setFillColor(brown)
    pdf.ellipse(x, y, x+30, y+10, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.rect(x+20, y, 10, 5, stroke=1, fill=1)

def draw_کلاه(pdf, x=460, y=540):
    # کلاه (Hat)
    pdf.setFillColor(blue)
    pdf.ellipse(x, y, x+30, y+10, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.ellipse(x+5, y+10, x+25, y+25, stroke=1, fill=1)

def draw_عینک(pdf, x=520, y=540):
    # عینک (Glasses)
    pdf.setFillColor(black)
    pdf.circle(x, y+10, 8, stroke=1, fill=0)
    pdf.circle(x+20, y+10, 8, stroke=1, fill=0)
    pdf.line(x+8, y+10, x+12, y+10)

def draw_چتر(pdf, x=100, y=480):
    # چتر (Umbrella)
    pdf.setFillColor(blue)
    pdf.arc(x, y, x+30, y+20, 0, 180)
    pdf.setFillColor(black)
    pdf.line(x+15, y, x+15, y-20)

def draw_کیف(pdf, x=160, y=480):
    # کیف (Bag)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 30, 20, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.arc(x+5, y+20, x+25, y+30, 0, 180)

def draw_ساعت(pdf, x=220, y=480):
    # ساعت (Watch)
    pdf.setFillColor(white)
    pdf.circle(x, y+10, 10, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.line(x, y+10, x+10, y+10)
    pdf.line(x, y+10, x, y+20)

# Example usage for these 20:
def create_next20_pdf(filename):
    c = canvas.Canvas(filename)
    draw_نمک(c)
    draw_قهوه(c)
    draw_چای(c)
    draw_آب(c)
    draw_شیرینی(c)
    draw_کیک(c)
    draw_بستنی(c)
    draw_پیتزا(c)
    draw_همبرگر(c)
    draw_ساندویچ(c)
    draw_نودل(c)
    draw_میوه(c)
    draw_سبزی(c)
    draw_کفش(c)
    draw_کلاه(c)
    draw_عینک(c)
    draw_چتر(c)
    draw_کیف(c)
    draw_ساعت(c)
    c.save()

# create_next20_pdf("next20_icons.pdf")

from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown, orange

def draw_لباس(pdf, x=100, y=400):
    # لباس (Clothes) - simple shirt
    pdf.setFillColor(blue)
    pdf.rect(x+10, y+10, 20, 20, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x, y+20, 10, 10, stroke=1, fill=1)
    pdf.rect(x+30, y+20, 10, 10, stroke=1, fill=1)

def draw_جوراب(pdf, x=160, y=400):
    # جوراب (Socks)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 8, 20, stroke=1, fill=1)
    pdf.rect(x, y, 15, 8, stroke=1, fill=1)

def draw_دمپایی(pdf, x=220, y=400):
    # دمپایی (Slippers)
    pdf.setFillColor(brown)
    pdf.ellipse(x, y, x+20, y+8, stroke=1, fill=1)
    pdf.ellipse(x+25, y, x+45, y+8, stroke=1, fill=1)

def draw_کمربند(pdf, x=280, y=400):
    # کمربند (Belt)
    pdf.setFillColor(brown)
    pdf.rect(x, y+10, 40, 8, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+35, y+10, 8, 8, stroke=1, fill=1)

def draw_دکمه(pdf, x=340, y=400):
    # دکمه (Button)
    pdf.setFillColor(gray)
    pdf.circle(x, y+10, 8, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x, y+10, 1, stroke=1, fill=1)
    pdf.circle(x+3, y+13, 1, stroke=1, fill=1)
    pdf.circle(x-3, y+7, 1, stroke=1, fill=1)

def draw_زیپ(pdf, x=400, y=400):
    # زیپ (Zipper)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 8, 30, stroke=1, fill=1)
    pdf.setFillColor(black)
    for i in range(5):
        pdf.line(x, y+5+i*5, x+8, y+5+i*5)

def draw_حوله(pdf, x=460, y=400):
    # حوله (Towel)
    pdf.setFillColor(green)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x, y, 30, 3, stroke=1, fill=1)

def draw_شانه(pdf, x=520, y=400):
    # شانه (Comb)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 30, 5, stroke=1, fill=1)
    pdf.setFillColor(black)
    for i in range(6):
        pdf.line(x+3+i*5, y, x+3+i*5, y-8)

def draw_مسواک(pdf, x=100, y=340):
    # مسواک (Toothbrush)
    pdf.setFillColor(blue)
    pdf.rect(x, y, 25, 4, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x+20, y, 5, 4, stroke=1, fill=1)

def draw_خمیردندان(pdf, x=160, y=340):
    # خمیردندان (Toothpaste)
    pdf.setFillColor(white)
    pdf.rect(x, y, 20, 8, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x+18, y+2, 4, 4, stroke=1, fill=1)

def draw_صندلی(pdf, x=220, y=340):
    # صندلی (Chair)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 20, 20, stroke=1, fill=1)
    pdf.rect(x, y-10, 5, 10, stroke=1, fill=1)
    pdf.rect(x+15, y-10, 5, 10, stroke=1, fill=1)

def draw_میز(pdf, x=280, y=340):
    # میز (Table)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 30, 8, stroke=1, fill=1)
    pdf.rect(x, y-15, 5, 15, stroke=1, fill=1)
    pdf.rect(x+25, y-15, 5, 15, stroke=1, fill=1)

def draw_لامپ(pdf, x=340, y=340):
    # لامپ (Lamp)
    pdf.setFillColor(yellow)
    pdf.circle(x, y+10, 8, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x-3, y, 6, 8, stroke=1, fill=1)

def draw_بالش(pdf, x=400, y=340):
    # بالش (Pillow)
    pdf.setFillColor(white)
    pdf.roundRect(x, y, 25, 15, 5, stroke=1, fill=1)

def draw_پتو(pdf, x=460, y=340):
    # پتو (Blanket)
    pdf.setFillColor(blue)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x, y, 30, 3, stroke=1, fill=1)

def draw_ظرف(pdf, x=520, y=340):
    # ظرف (Dish)
    pdf.setFillColor(white)
    pdf.ellipse(x, y, x+25, y+10, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.ellipse(x+5, y+2, x+20, y+8, stroke=1, fill=1)

def draw_چاقو(pdf, x=100, y=280):
    # چاقو (Knife)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 18, 4, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.rect(x+18, y, 6, 4, stroke=1, fill=1)

def draw_چنگال(pdf, x=160, y=280):
    # چنگال (Fork)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 4, 20, stroke=1, fill=1)
    for i in range(3):
        pdf.rect(x-2+i*3, y+18, 2, 6, stroke=1, fill=1)

def draw_قاشق(pdf, x=220, y=280):
    # قاشق (Spoon)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 4, 15, stroke=1, fill=1)
    pdf.ellipse(x-4, y+12, x+8, y+20, stroke=1, fill=1)

def draw_لیوان(pdf, x=280, y=280):
    # لیوان (Cup)
    pdf.setFillColor(white)
    pdf.rect(x, y, 15, 20, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.arc(x+12, y+5, x+22, y+15, 0, 180)

# Example usage for these 20:
def create_next20b_pdf(filename):
    c = canvas.Canvas(filename)
    draw_لباس(c)
    draw_جوراب(c)
    draw_دمپایی(c)
    draw_کمربند(c)
    draw_دکمه(c)
    draw_زیپ(c)
    draw_حوله(c)
    draw_شانه(c)
    draw_مسواک(c)
    draw_خمیردندان(c)
    draw_صندلی(c)
    draw_میز(c)
    draw_لامپ(c)
    draw_بالش(c)
    draw_پتو(c)
    draw_ظرف(c)
    draw_چاقو(c)
    draw_چنگال(c)
    draw_قاشق(c)
    draw_لیوان(c)
    c.save()

# create_next20b_pdf("next20b_icons.pdf")


from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown, orange

def draw_گلدان(pdf, x=100, y=200):
    # گلدان (Vase)
    pdf.setFillColor(brown)
    pdf.ellipse(x, y, x+20, y+10, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.line(x+10, y+10, x+10, y+30)
    pdf.setFillColor(red)
    pdf.circle(x+10, y+32, 4, stroke=1, fill=1)

def draw_صابون(pdf, x=160, y=200):
    # صابون (Soap)
    pdf.setFillColor(pink)
    pdf.roundRect(x, y, 25, 12, 6, stroke=1, fill=1)

def draw_شامپو(pdf, x=220, y=200):
    # شامپو (Shampoo)
    pdf.setFillColor(blue)
    pdf.rect(x, y, 12, 28, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x, y+28, 12, 4, stroke=1, fill=1)

def draw_کبریت(pdf, x=280, y=200):
    # کبریت (Matchbox)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 20, 10, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.rect(x+2, y+2, 16, 6, stroke=1, fill=1)

def draw_شمع(pdf, x=340, y=200):
    # شمع (Candle)
    pdf.setFillColor(white)
    pdf.rect(x, y, 6, 20, stroke=1, fill=1)
    pdf.setFillColor(yellow)
    pdf.circle(x+3, y+22, 3, stroke=1, fill=1)

def draw_تلویزیون(pdf, x=400, y=200):
    # تلویزیون (TV)
    pdf.setFillColor(black)
    pdf.rect(x, y, 30, 18, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+12, y-4, 6, 4, stroke=1, fill=1)

def draw_موبایل(pdf, x=460, y=200):
    # موبایل (Mobile)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 10, 25, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+5, y+2, 1, stroke=1, fill=1)

def draw_باتری(pdf, x=520, y=200):
    # باتری (Battery)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 20, 8, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.rect(x+20, y+2, 3, 4, stroke=1, fill=1)

def draw_سیم(pdf, x=100, y=140):
    # سیم (Wire)
    pdf.setFillColor(black)
    pdf.setStrokeColor(black)
    pdf.setLineWidth(2)
    pdf.line(x, y, x+30, y+20)
    pdf.setLineWidth(1)

def draw_پیچ(pdf, x=160, y=140):
    # پیچ (Screw)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 5, 18, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.line(x, y+9, x+5, y+9)

def draw_مهره(pdf, x=220, y=140):
    # مهره (Nut)
    pdf.setFillColor(gray)
    pdf.circle(x+8, y+8, 8, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.circle(x+8, y+8, 3, stroke=1, fill=1)

def draw_چسب(pdf, x=280, y=140):
    # چسب (Glue)
    pdf.setFillColor(yellow)
    pdf.rect(x, y, 8, 20, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x, y+20, 8, 4, stroke=1, fill=1)

def draw_نوار(pdf, x=340, y=140):
    # نوار (Tape)
    pdf.setFillColor(yellow)
    pdf.circle(x+10, y+10, 10, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.circle(x+10, y+10, 5, stroke=1, fill=1)

def draw_قیچی(pdf, x=400, y=140):
    # قیچی (Scissors)
    pdf.setFillColor(gray)
    pdf.circle(x+5, y+10, 5, stroke=1, fill=0)
    pdf.circle(x+15, y+10, 5, stroke=1, fill=0)
    pdf.line(x+5, y+10, x+20, y+20)
    pdf.line(x+15, y+10, x+0, y+20)

def draw_سوزن(pdf, x=460, y=140):
    # سوزن (Needle)
    pdf.setFillColor(gray)
    pdf.setLineWidth(2)
    pdf.line(x, y, x+20, y+20)
    pdf.setLineWidth(1)
    pdf.setFillColor(black)
    pdf.circle(x+20, y+20, 2, stroke=1, fill=1)

def draw_نخ(pdf, x=520, y=140):
    # نخ (Thread)
    pdf.setFillColor(black)
    pdf.setStrokeColor(black)
    pdf.setLineWidth(1)
    pdf.arc(x, y, x+20, y+10, 0, 180)
    pdf.arc(x+5, y+5, x+25, y+15, 0, 180)

def draw_پارچه(pdf, x=100, y=80):
    # پارچه (Cloth)
    pdf.setFillColor(green)
    pdf.rect(x, y, 25, 15, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.line(x, y, x+25, y+15)
    pdf.line(x+25, y, x, y+15)

def draw_کوله(pdf, x=160, y=80):
    # کوله (Backpack)
    pdf.setFillColor(blue)
    pdf.rect(x, y, 20, 25, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.arc(x-5, y+20, x+25, y+35, 0, 180)

def draw_چمدان(pdf, x=220, y=80):
    # چمدان (Suitcase)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 25, 18, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+8, y+18, 9, 4, stroke=1, fill=1)

# Example usage for these 20:
def create_next20c_pdf(filename):
    c = canvas.Canvas(filename)
    draw_گلدان(c)
    draw_صابون(c)
    draw_شامپو(c)
    draw_کبریت(c)
    draw_شمع(c)
    draw_تلویزیون(c)
    draw_موبایل(c)
    draw_باتری(c)
    draw_سیم(c)
    draw_پیچ(c)
    draw_مهره(c)
    draw_چسب(c)
    draw_نوار(c)
    draw_قیچی(c)
    draw_سوزن(c)
    draw_نخ(c)
    draw_پارچه(c)
    draw_کوله(c)
    draw_چمدان(c)
    c.save()

# create_next20c_pdf("next20c_icons.pdf")


from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown, orange

def draw_ماهی(pdf, x=100, y=600):
    # ماهی (Fish)
    pdf.setFillColor(blue)
    pdf.ellipse(x, y, x+30, y+15, stroke=1, fill=1)
    pdf.setFillColor(orange)
    path = pdf.beginPath()
    path.moveTo(x+30, y+7)
    path.lineTo(x+40, y+15)
    path.lineTo(x+40, y)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)
    pdf.setFillColor(black)
    pdf.circle(x+8, y+8, 2, stroke=1, fill=1)

def draw_طوطی(pdf, x=160, y=600):
    # طوطی (Parrot)
    pdf.setFillColor(green)
    pdf.circle(x+10, y+15, 10, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.circle(x+20, y+20, 5, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+13, y+20, 2, stroke=1, fill=1)

def draw_سگ(pdf, x=220, y=600):
    # سگ (Dog)
    pdf.setFillColor(brown)
    pdf.circle(x+15, y+15, 12, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.ellipse(x+5, y+20, x+10, y+30, stroke=1, fill=1)
    pdf.ellipse(x+20, y+20, x+25, y+30, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+11, y+18, 2, stroke=1, fill=1)
    pdf.circle(x+19, y+18, 2, stroke=1, fill=1)

def draw_گربه(pdf, x=280, y=600):
    # گربه (Cat)
    pdf.setFillColor(gray)
    pdf.circle(x+15, y+15, 12, stroke=1, fill=1)
    # Ears
    path = pdf.beginPath()
    path.moveTo(x+5, y+25)
    path.lineTo(x+10, y+35)
    path.lineTo(x+15, y+25)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)
    path = pdf.beginPath()
    path.moveTo(x+25, y+25)
    path.lineTo(x+20, y+35)
    path.lineTo(x+15, y+25)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)
    pdf.setFillColor(black)
    pdf.circle(x+11, y+18, 2, stroke=1, fill=1)
    pdf.circle(x+19, y+18, 2, stroke=1, fill=1)

def draw_لاکپشت(pdf, x=340, y=600):
    # لاکپشت (Turtle)
    pdf.setFillColor(green)
    pdf.ellipse(x, y, x+30, y+15, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.ellipse(x+5, y+5, x+25, y+13, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.circle(x+30, y+8, 4, stroke=1, fill=1)

def draw_همستر(pdf, x=400, y=600):
    # همستر (Hamster)
    pdf.setFillColor(orange)
    pdf.circle(x+15, y+15, 12, stroke=1, fill=1)
    pdf.setFillColor(pink)
    pdf.circle(x+8, y+22, 4, stroke=1, fill=1)
    pdf.circle(x+22, y+22, 4, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+11, y+18, 2, stroke=1, fill=1)
    pdf.circle(x+19, y+18, 2, stroke=1, fill=1)

def draw_ماشین(pdf, x=460, y=600):
    # ماشین (Car)
    pdf.setFillColor(blue)
    pdf.rect(x, y+5, 30, 10, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.circle(x+8, y+5, 5, stroke=1, fill=1)
    pdf.circle(x+22, y+5, 5, stroke=1, fill=1)

def draw_قطار(pdf, x=520, y=600):
    # قطار (Train)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 12, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+8, y, 4, stroke=1, fill=1)
    pdf.circle(x+22, y, 4, stroke=1, fill=1)

def draw_هواپیما(pdf, x=100, y=540):
    # هواپیما (Airplane)
    pdf.setFillColor(gray)
    pdf.rect(x+10, y+10, 20, 5, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x+5, y+12, 30, 2, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+18, y+15, 4, 8, stroke=1, fill=1)

def draw_کشتی(pdf, x=160, y=540):
    # کشتی (Ship)
    pdf.setFillColor(blue)
    pdf.ellipse(x, y, x+30, y+10, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+10, y+10, 10, 8, stroke=1, fill=1)

def draw_موتور(pdf, x=220, y=540):
    # موتور (Motorcycle)
    pdf.setFillColor(black)
    pdf.circle(x+5, y+5, 5, stroke=1, fill=1)
    pdf.circle(x+25, y+5, 5, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+8, y+8, 14, 4, stroke=1, fill=1)

def draw_اتوبوس(pdf, x=280, y=540):
    # اتوبوس (Bus)
    pdf.setFillColor(yellow)
    pdf.rect(x, y, 35, 12, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+8, y, 4, stroke=1, fill=1)
    pdf.circle(x+27, y, 4, stroke=1, fill=1)

def draw_تاکسی(pdf, x=340, y=540):
    # تاکسی (Taxi)
    pdf.setFillColor(yellow)
    pdf.rect(x, y+5, 30, 10, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+8, y+5, 5, stroke=1, fill=1)
    pdf.circle(x+22, y+5, 5, stroke=1, fill=1)

def draw_مترو(pdf, x=400, y=540):
    # مترو (Metro)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 12, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+8, y, 4, stroke=1, fill=1)
    pdf.circle(x+22, y, 4, stroke=1, fill=1)

def draw_دوچرخه(pdf, x=460, y=540):
    # دوچرخه (Bicycle)
    pdf.setFillColor(black)
    pdf.circle(x+5, y+5, 5, stroke=1, fill=0)
    pdf.circle(x+25, y+5, 5, stroke=1, fill=0)
    pdf.setFillColor(gray)
    pdf.line(x+5, y+5, x+15, y+15)
    pdf.line(x+25, y+5, x+15, y+15)
    pdf.line(x+5, y+5, x+25, y+5)

def draw_اسکیت(pdf, x=520, y=540):
    # اسکیت (Skate)
    pdf.setFillColor(blue)
    pdf.rect(x, y+10, 20, 5, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+5, y+8, 3, stroke=1, fill=1)
    pdf.circle(x+15, y+8, 3, stroke=1, fill=1)

def draw_خانه(pdf, x=100, y=480):
    # خانه (House)
    pdf.setFillColor(red)
    pdf.rect(x, y, 30, 20, stroke=1, fill=1)
    pdf.setFillColor(brown)
    path = pdf.beginPath()
    path.moveTo(x, y+20)
    path.lineTo(x+15, y+35)
    path.lineTo(x+30, y+20)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_ویلا(pdf, x=160, y=480):
    # ویلا (Villa)
    pdf.setFillColor(green)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)
    pdf.setFillColor(brown)
    path = pdf.beginPath()
    path.moveTo(x, y+15)
    path.lineTo(x+15, y+30)
    path.lineTo(x+30, y+15)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_آپارتمان(pdf, x=220, y=480):
    # آپارتمان (Apartment)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 20, 30, stroke=1, fill=1)
    pdf.setFillColor(white)
    for i in range(3):
        pdf.rect(x+5, y+5+i*8, 10, 5, stroke=1, fill=1)

# Example usage for these 20:
def create_next20d_pdf(filename):
    c = canvas.Canvas(filename)
    draw_ماهی(c)
    draw_طوطی(c)
    draw_سگ(c)
    draw_گربه(c)
    draw_لاکپشت(c)
    draw_همستر(c)
    draw_ماشین(c)
    draw_قطار(c)
    draw_هواپیما(c)
    draw_کشتی(c)
    draw_موتور(c)
    draw_اتوبوس(c)
    draw_تاکسی(c)
    draw_مترو(c)
    draw_دوچرخه(c)
    draw_اسکیت(c)
    draw_خانه(c)
    draw_ویلا(c)
    draw_آپارتمان(c)
    c.save()

# create_next20d_pdf("next20d_icons.pdf")


from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown, orange

def draw_اتاق(pdf, x=100, y=400):
    # اتاق (Room) - simple square with door
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 30, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x+10, y, 10, 10, stroke=1, fill=1)

def draw_آشپزخانه(pdf, x=160, y=400):
    # آشپزخانه (Kitchen) - pot on stove
    pdf.setFillColor(gray)
    pdf.rect(x, y, 25, 10, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.rect(x+5, y+10, 15, 5, stroke=1, fill=1)

def draw_حمام(pdf, x=220, y=400):
    # حمام (Bathroom) - bathtub
    pdf.setFillColor(white)
    pdf.ellipse(x, y, x+30, y+12, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.ellipse(x+5, y+2, x+25, y+10, stroke=1, fill=1)

def draw_پارکینگ(pdf, x=280, y=400):
    # پارکینگ (Parking) - car in a box
    pdf.setFillColor(gray)
    pdf.rect(x, y, 35, 20, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x+10, y+5, 15, 10, stroke=1, fill=1)

def draw_بالکن(pdf, x=340, y=400):
    # بالکن (Balcony) - railings
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 8, stroke=1, fill=1)
    for i in range(5):
        pdf.line(x+3+i*6, y, x+3+i*6, y+8)

def draw_حیاط(pdf, x=400, y=400):
    # حیاط (Yard) - grass patch
    pdf.setFillColor(green)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)

def draw_باغ(pdf, x=460, y=400):
    # باغ (Garden) - tree and grass
    pdf.setFillColor(green)
    pdf.rect(x, y, 30, 10, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.rect(x+20, y+10, 4, 10, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.circle(x+22, y+22, 7, stroke=1, fill=1)

def draw_خیابان(pdf, x=520, y=400):
    # خیابان (Street) - road with lines
    pdf.setFillColor(gray)
    pdf.rect(x, y, 40, 10, stroke=1, fill=1)
    pdf.setFillColor(white)
    for i in range(3):
        pdf.rect(x+5+i*12, y+4, 6, 2, stroke=1, fill=1)

def draw_جاده(pdf, x=100, y=340):
    # جاده (Road) - curved road
    pdf.setFillColor(gray)
    pdf.rect(x, y, 40, 10, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x+10, y+4, 6, 2, stroke=1, fill=1)
    pdf.rect(x+24, y+4, 6, 2, stroke=1, fill=1)

def draw_پل(pdf, x=160, y=340):
    # پل (Bridge) - arch over water
    pdf.setFillColor(blue)
    pdf.rect(x, y, 40, 8, stroke=1, fill=1)
    pdf.setFillColor(gray)
    path = pdf.beginPath()
    path.moveTo(x, y+8)
    path.lineTo(x+40, y+8)
    path.lineTo(x+35, y+18)
    path.lineTo(x+5, y+18)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_تونل(pdf, x=220, y=340):
    # تونل (Tunnel) - arch
    pdf.setFillColor(gray)
    path = pdf.beginPath()
    path.moveTo(x, y)
    path.lineTo(x+30, y)
    path.arcTo(x, y, x+30, y+30, startAng=0, extent=180)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_پارک(pdf, x=280, y=340):
    # پارک (Park) - tree and grass
    pdf.setFillColor(green)
    pdf.rect(x, y, 30, 10, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.rect(x+10, y+10, 4, 10, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.circle(x+12, y+22, 7, stroke=1, fill=1)

def draw_سینما(pdf, x=340, y=340):
    # سینما (Cinema) - screen and seats
    pdf.setFillColor(black)
    pdf.rect(x, y+10, 30, 8, stroke=1, fill=1)
    pdf.setFillColor(red)
    for i in range(3):
        pdf.circle(x+7+i*8, y+5, 4, stroke=1, fill=1)

def draw_تئاتر(pdf, x=400, y=340):
    # تئاتر (Theater) - stage and curtain
    pdf.setFillColor(red)
    pdf.rect(x, y+10, 30, 8, stroke=1, fill=1)
    pdf.setFillColor(yellow)
    pdf.rect(x, y, 30, 5, stroke=1, fill=1)

def draw_رستوران(pdf, x=460, y=340):
    # رستوران (Restaurant) - plate and cutlery
    pdf.setFillColor(white)
    pdf.circle(x+15, y+10, 10, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+2, y+5, 3, 10, stroke=1, fill=1)
    pdf.rect(x+25, y+5, 3, 10, stroke=1, fill=1)

def draw_کافه(pdf, x=520, y=340):
    # کافه (Cafe) - cup and saucer
    pdf.setFillColor(white)
    pdf.circle(x+15, y+10, 8, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.circle(x+15, y+10, 5, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.ellipse(x+8, y+2, x+22, y+6, stroke=1, fill=1)

def draw_فروشگاه(pdf, x=100, y=280):
    # فروشگاه (Store) - shop front
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 20, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.rect(x, y+20, 30, 6, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x+10, y, 10, 10, stroke=1, fill=1)

def draw_دانشگاه(pdf, x=160, y=280):
    # دانشگاه (University) - building with columns
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)
    pdf.setFillColor(white)
    for i in range(3):
        pdf.rect(x+5+i*8, y, 4, 15, stroke=1, fill=1)
    pdf.setFillColor(blue)
    path = pdf.beginPath()
    path.moveTo(x, y+15)
    path.lineTo(x+15, y+30)
    path.lineTo(x+30, y+15)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_مدرسه(pdf, x=220, y=280):
    # مدرسه (School) - building with bell
    pdf.setFillColor(yellow)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)
    pdf.setFillColor(red)
    path = pdf.beginPath()
    path.moveTo(x, y+15)
    path.lineTo(x+15, y+30)
    path.lineTo(x+30, y+15)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)
    pdf.setFillColor(black)
    pdf.circle(x+15, y+22, 2, stroke=1, fill=1)

def draw_مهدکودک(pdf, x=280, y=280):
    # مهدکودک (Kindergarten) - block and ball
    pdf.setFillColor(blue)
    pdf.rect(x, y, 15, 15, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.circle(x+25, y+10, 7, stroke=1, fill=1)

def draw_بیمارستان(pdf, x=340, y=280):
    # بیمارستان (Hospital) - building with red cross
    pdf.setFillColor(white)
    pdf.rect(x, y, 30, 20, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.rect(x+12, y+7, 6, 2, stroke=1, fill=1)
    pdf.rect(x+14, y+5, 2, 6, stroke=1, fill=1)

def draw_داروخانه(pdf, x=400, y=280):
    # داروخانه (Pharmacy) - cross
    pdf.setFillColor(white)
    pdf.rect(x, y, 20, 20, stroke=1, fill=1)
    pdf.setFillColor(green)
    pdf.rect(x+7, y+3, 6, 14, stroke=1, fill=1)
    pdf.rect(x+3, y+7, 14, 6, stroke=1, fill=1)

# Example usage for these 20:
def create_next20e_pdf(filename):
    c = canvas.Canvas(filename)
    draw_اتاق(c)
    draw_آشپزخانه(c)
    draw_حمام(c)
    draw_پارکینگ(c)
    draw_بالکن(c)
    draw_حیاط(c)
    draw_باغ(c)
    draw_خیابان(c)
    draw_جاده(c)
    draw_پل(c)
    draw_تونل(c)
    draw_پارک(c)
    draw_سینما(c)
    draw_تئاتر(c)
    draw_رستوران(c)
    draw_کافه(c)
    draw_فروشگاه(c)
    draw_دانشگاه(c)
    draw_مدرسه(c)
    draw_مهدکودک(c)
    draw_بیمارستان(c)
    draw_داروخانه(c)
    c.save()

# create_next20e_pdf("next20e_icons.pdf")


from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown, orange

def draw_بانک(pdf, x=100, y=400):
    # بانک (Bank) - building with columns
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)
    pdf.setFillColor(white)
    for i in range(3):
        pdf.rect(x+5+i*8, y, 4, 15, stroke=1, fill=1)
    pdf.setFillColor(blue)
    path = pdf.beginPath()
    path.moveTo(x, y+15)
    path.lineTo(x+15, y+30)
    path.lineTo(x+30, y+15)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_پست(pdf, x=160, y=400):
    # پست (Post) - envelope
    pdf.setFillColor(white)
    pdf.rect(x, y, 30, 20, stroke=1, fill=1)
    pdf.setFillColor(gray)
    path = pdf.beginPath()
    path.moveTo(x, y+20)
    path.lineTo(x+15, y+5)
    path.lineTo(x+30, y+20)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_فرودگاه(pdf, x=220, y=400):
    # فرودگاه (Airport) - airplane
    pdf.setFillColor(gray)
    pdf.rect(x+10, y+10, 20, 5, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x+5, y+12, 30, 2, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+18, y+15, 4, 8, stroke=1, fill=1)

def draw_ایستگاه(pdf, x=280, y=400):
    # ایستگاه (Station) - platform and sign
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 8, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x+10, y+8, 10, 8, stroke=1, fill=1)

def draw_بندر(pdf, x=340, y=400):
    # بندر (Port) - water and ship
    pdf.setFillColor(blue)
    pdf.rect(x, y, 30, 8, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+10, y+8, 10, 8, stroke=1, fill=1)

def draw_قلب(pdf, x=400, y=400):
    # قلب (Heart)
    pdf.setFillColor(red)
    path = pdf.beginPath()
    path.moveTo(x+10, y+10)
    path.curveTo(x+10, y+20, x, y+20, x, y+12)
    path.curveTo(x, y+5, x+10, y+5, x+10, y+10)
    path.curveTo(x+10, y+20, x+20, y+20, x+20, y+12)
    path.curveTo(x+20, y+5, x+10, y+5, x+10, y+10)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_قاب_عکس(pdf, x=460, y=400):
    # قاب عکس (Photo frame)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 25, 20, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x+3, y+3, 19, 14, stroke=1, fill=1)

def draw_در(pdf, x=520, y=400):
    # در (Door)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 15, 30, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+13, y+15, 1, stroke=1, fill=1)

def draw_تخته(pdf, x=100, y=340):
    # تخته (Board)
    pdf.setFillColor(green)
    pdf.rect(x, y, 30, 18, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 30, 3, stroke=1, fill=1)

def draw_کتاب(pdf, x=160, y=340):
    # کتاب (Book)
    pdf.setFillColor(white)
    pdf.rect(x, y, 20, 25, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x, y, 5, 25, stroke=1, fill=1)

def draw_گوشی(pdf, x=220, y=340):
    # گوشی (Phone)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 10, 25, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+5, y+2, 1, stroke=1, fill=1)

def draw_تخت(pdf, x=280, y=340):
    # تخت (Bed)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 30, 10, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x, y+10, 30, 8, stroke=1, fill=1)

def draw_دستبند(pdf, x=340, y=340):
    # دستبند (Bracelet)
    pdf.setFillColor(pink)
    pdf.circle(x+12, y+12, 10, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.circle(x+12, y+12, 6, stroke=1, fill=1)

def draw_کپسول(pdf, x=400, y=340):
    # کپسول (Capsule)
    pdf.setFillColor(red)
    pdf.rect(x, y, 10, 20, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x+10, y, 10, 20, stroke=1, fill=1)

def draw_خطـکش(pdf, x=460, y=340):
    # خط‌کش (Ruler)
    pdf.setFillColor(yellow)
    pdf.rect(x, y, 30, 5, stroke=1, fill=1)
    pdf.setFillColor(black)
    for i in range(6):
        pdf.line(x+5*i, y, x+5*i, y+5)

def draw_مداد(pdf, x=520, y=340):
    # مداد (Pencil)
    pdf.setFillColor(yellow)
    pdf.rect(x, y, 20, 5, stroke=1, fill=1)
    pdf.setFillColor(orange)
    path = pdf.beginPath()
    path.moveTo(x+20, y)
    path.lineTo(x+25, y+2.5)
    path.lineTo(x+20, y+5)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_قلمـمو(pdf, x=100, y=280):
    # قلم‌مو (Brush)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 5, 20, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.ellipse(x-2, y+18, x+7, y+25, stroke=1, fill=1)

def draw_گیتار(pdf, x=160, y=280):
    # گیتار (Guitar)
    pdf.setFillColor(brown)
    pdf.rect(x+10, y, 5, 20, stroke=1, fill=1)
    pdf.setFillColor(orange)
    pdf.circle(x+12, y+25, 8, stroke=1, fill=1)

def draw_هدفون(pdf, x=220, y=280):
    # هدفون (Headphones)
    pdf.setFillColor(black)
    pdf.arc(x, y, x+30, y+20, 0, 180)
    pdf.setFillColor(gray)
    pdf.circle(x, y+10, 5, stroke=1, fill=1)
    pdf.circle(x+30, y+10, 5, stroke=1, fill=1)

def draw_دوربین(pdf, x=280, y=280):
    # دوربین (Camera)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 15, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+15, y+7, 5, stroke=1, fill=1)

def draw_مجسمه(pdf, x=340, y=280):
    # مجسمه (Statue)
    pdf.setFillColor(gray)
    pdf.rect(x+8, y, 8, 20, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.circle(x+12, y+25, 7, stroke=1, fill=1)

# Example usage for these 20:
def create_next20f_pdf(filename):
    c = canvas.Canvas(filename)
    draw_بانک(c)
    draw_پست(c)
    draw_فرودگاه(c)
    draw_ایستگاه(c)
    draw_بندر(c)
    draw_قلب(c)
    draw_قاب_عکس(c)
    draw_در(c)
    draw_تخته(c)
    draw_کتاب(c)
    draw_گوشی(c)
    draw_تخت(c)
    draw_دستبند(c)
    draw_کپسول(c)
    draw_خطـکش(c)
    draw_مداد(c)
    draw_قلمـمو(c)
    draw_گیتار(c)
    draw_هدفون(c)
    draw_دوربین(c)
    draw_مجسمه(c)
    c.save()

# create_next20f_pdf("next20f_icons.pdf")


from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, pink, yellow, white, gray, green, blue, red, brown, orange

def draw_توپ(pdf, x=100, y=400):
    # توپ (Ball)
    pdf.setFillColor(red)
    pdf.circle(x+12, y+12, 12, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.line(x+12, y, x+12, y+24)
    pdf.line(x, y+12, x+24, y+12)

def draw_توپ_فوتبال(pdf, x=160, y=400):
    # توپ فوتبال (Football)
    pdf.setFillColor(white)
    pdf.circle(x+12, y+12, 12, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+12, y+12, 4, stroke=1, fill=1)

def draw_توپ_بسکتبال(pdf, x=220, y=400):
    # توپ بسکتبال (Basketball)
    pdf.setFillColor(orange)
    pdf.circle(x+12, y+12, 12, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.line(x+12, y, x+12, y+24)
    pdf.line(x, y+12, x+24, y+12)
    pdf.arc(x, y, x+24, y+24, 45, 90)
    pdf.arc(x, y, x+24, y+24, 225, 90)

def draw_توپ_والیبال(pdf, x=280, y=400):
    # توپ والیبال (Volleyball)
    pdf.setFillColor(white)
    pdf.circle(x+12, y+12, 12, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.arc(x, y, x+24, y+24, 0, 180)
    pdf.arc(x, y, x+24, y+24, 90, 180)
    pdf.arc(x, y, x+24, y+24, 180, 180)

def draw_راکت(pdf, x=340, y=400):
    # راکت (Racket)
    pdf.setFillColor(blue)
    pdf.ellipse(x, y, x+10, y+25, stroke=1, fill=1)
    pdf.setFillColor(brown)
    pdf.rect(x+4, y-10, 2, 10, stroke=1, fill=1)

def draw_عینک_شنا(pdf, x=400, y=400):
    # عینک شنا (Swim goggles)
    pdf.setFillColor(blue)
    pdf.ellipse(x, y+8, x+10, y+16, stroke=1, fill=1)
    pdf.ellipse(x+14, y+8, x+24, y+16, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.line(x+10, y+12, x+14, y+12)

def draw_کفش_ورزشی(pdf, x=460, y=400):
    # کفش ورزشی (Sports shoe)
    pdf.setFillColor(blue)
    pdf.ellipse(x, y, x+24, y+10, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.rect(x+16, y+2, 6, 4, stroke=1, fill=1)

def draw_نیزه(pdf, x=520, y=400):
    # نیزه (Spear)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 3, 25, stroke=1, fill=1)
    pdf.setFillColor(black)
    path = pdf.beginPath()
    path.moveTo(x-2, y+25)
    path.lineTo(x+1.5, y+35)
    path.lineTo(x+5, y+25)
    path.close()
    pdf.drawPath(path, fill=1, stroke=1)

def draw_کشتی_اسباب_بازی(pdf, x=100, y=340):
    # کشتی اسباب‌بازی (Toy ship)
    pdf.setFillColor(blue)
    pdf.ellipse(x, y, x+30, y+10, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.rect(x+10, y+10, 10, 8, stroke=1, fill=1)

def draw_رایانه(pdf, x=160, y=340):
    # رایانه (Computer)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 30, 18, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.rect(x+5, y+2, 20, 10, stroke=1, fill=1)

def draw_دفتر(pdf, x=220, y=340):
    # دفتر (Notebook)
    pdf.setFillColor(white)
    pdf.rect(x, y, 20, 25, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x, y, 5, 25, stroke=1, fill=1)

def draw_سبد_خرید(pdf, x=280, y=340):
    # سبد خرید (Shopping basket)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 20, 10, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.line(x, y+10, x+10, y+20)
    pdf.line(x+20, y+10, x+10, y+20)

def draw_صندوق(pdf, x=340, y=340):
    # صندوق (Box/Chest)
    pdf.setFillColor(brown)
    pdf.rect(x, y, 25, 15, stroke=1, fill=1)
    pdf.setFillColor(yellow)
    pdf.rect(x, y+12, 25, 3, stroke=1, fill=1)

def draw_پوستر(pdf, x=400, y=340):
    # پوستر (Poster)
    pdf.setFillColor(white)
    pdf.rect(x, y, 18, 25, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x+2, y+15, 14, 6, stroke=1, fill=1)

def draw_بروشور(pdf, x=460, y=340):
    # بروشور (Brochure)
    pdf.setFillColor(white)
    pdf.rect(x, y, 20, 25, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x+10, y, 2, 25, stroke=1, fill=1)

def draw_دفترچه(pdf, x=520, y=340):
    # دفترچه (Small notebook)
    pdf.setFillColor(white)
    pdf.rect(x, y, 15, 20, stroke=1, fill=1)
    pdf.setFillColor(blue)
    pdf.rect(x, y, 3, 20, stroke=1, fill=1)

def draw_ابزار(pdf, x=100, y=280):
    # ابزار (Tool) - wrench
    pdf.setFillColor(gray)
    pdf.rect(x+8, y, 4, 20, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+10, y+20, 5, stroke=1, fill=0)

def draw_ماشین_آلات(pdf, x=160, y=280):
    # ماشین‌آلات (Machinery) - gear
    pdf.setFillColor(gray)
    pdf.circle(x+12, y+12, 10, stroke=1, fill=1)
    pdf.setFillColor(white)
    pdf.circle(x+12, y+12, 5, stroke=1, fill=1)

def draw_تلفن(pdf, x=220, y=280):
    # تلفن (Telephone)
    pdf.setFillColor(black)
    pdf.rect(x, y, 20, 8, stroke=1, fill=1)
    pdf.setFillColor(gray)
    pdf.rect(x+5, y+8, 10, 8, stroke=1, fill=1)

def draw_ربات(pdf, x=280, y=280):
    # ربات (Robot)
    pdf.setFillColor(gray)
    pdf.rect(x, y, 20, 20, stroke=1, fill=1)
    pdf.setFillColor(black)
    pdf.circle(x+6, y+14, 2, stroke=1, fill=1)
    pdf.circle(x+14, y+14, 2, stroke=1, fill=1)
    pdf.setFillColor(red)
    pdf.rect(x+8, y+4, 4, 4, stroke=1, fill=1)

# Example usage for these 20:
def create_next20g_pdf(filename):
    c = canvas.Canvas(filename)
    draw_توپ(c)
    draw_توپ_فوتبال(c)
    draw_توپ_بسکتبال(c)
    draw_توپ_والیبال(c)
    draw_راکت(c)
    draw_عینک_شنا(c)
    draw_کفش_ورزشی(c)
    draw_نیزه(c)
    draw_کشتی_اسباب_بازی(c)
    draw_رایانه(c)
    draw_دفتر(c)
    draw_سبد_خرید(c)
    draw_صندوق(c)
    draw_پوستر(c)
    draw_بروشور(c)
    draw_دفترچه(c)
    draw_ابزار(c)
    draw_ماشین_آلات(c)
    draw_تلفن(c)
    draw_ربات(c)
    c.save()

# create_next20g_pdf("next20g_icons.pdf")
from fpdf import FPDF
import arabic_reshaper
from bidi.algorithm import get_display
from card_generator import draw_random_shapes_on_pdf, generate_card_image_asset
from textwrap import wrap
import math


# --- ثابت‌های چیدمان (بر حسب میلی‌متر) ---
A4_WIDTH, A4_HEIGHT = 210, 297
CARD_WIDTH, CARD_HEIGHT = 38, 50
IMAGE_ASSET_WIDTH, IMAGE_ASSET_HEIGHT = 22, 22 # اندازه تصویر روی کارت
FONT_PATH = "assets/font/Vazirmatn-Regular.ttf"
FONT_SIZE = 10
STRIPE_WIDTH = 12  # عرض نوار مایل

def prepare_rtl_text(text):
    """متن فارسی را برای نمایش صحیح در fpdf2 آماده می‌کند."""
    return get_display(arabic_reshaper.reshape(text))

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.card_count_on_page = 0
        self.cards_per_page = 20 # مقدار پیش‌فرض

    def check_page_break(self):
        """در صورت پر شدن صفحه، به صفحه جدید می‌رود."""
        if self.card_count_on_page >= self.cards_per_page:
            self.add_page()
            self.card_count_on_page = 0

def draw_diagonal_stripe(pdf, x, y, card_width, card_height, stripe_width, text, color=(200, 200, 200)):
    """رسم نوار مایل با زاویه 45 درجه در گوشه سمت چپ بالای کارت"""
    # ذخیره وضعیت فعلی
    pdf.set_fill_color(*color)
    
    # محاسبه نقاط مثلث برای نوار مایل در گوشه چپ بالا
    # نقطه 1: گوشه چپ بالا
    x1, y1 = x, y
    # نقطه 2: روی لبه بالایی
    x2, y2 = x + stripe_width * 1.4, y
    # نقطه 3: روی لبه چپ
    x3, y3 = x, y + stripe_width * 1.4
    
    # رسم مثلث با استفاده از polygon
    pdf.polygon([(x1, y1), (x2, y2), (x3, y3)], style='F')
    
    # نوشتن متن روی نوار
    pdf.set_font('Vazir', '', 7)
    pdf.set_text_color(255, 255, 255)  # متن سفید
    
    # محاسبه موقعیت متن (وسط نوار مایل)
    text_x = x + stripe_width * 0.5
    text_y = y + stripe_width * 0.5
    
    # ابتدا چرخش 45 درجه برای قرار گرفتن در راستای نوار
    # سپس چرخش 90 درجه اضافی برای عمودی شدن متن
    # در مجموع: 45 + 90 = 135 درجه
    with pdf.rotation(angle=45, x=text_x, y=text_y):
        pdf.text(text_x -3, text_y + 0, text)
    
    pdf.set_text_color(0, 0, 0)  # بازگشت به رنگ مشکی

def generate_pdf(word_cards, customer_cards, output_filename, cards_per_page=16,customer_description=False):
    """
    با استفاده از FPDF2، کارت‌ها را مستقیماً در یک فایل PDF تولید می‌کند.
    """
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.cards_per_page = cards_per_page
    
    # اضافه کردن فونت فارسی
    pdf.add_font('Vazir', '', FONT_PATH, uni=True)
    pdf.add_page()
    
    # محاسبه چیدمان
    cols = A4_WIDTH // CARD_WIDTH
    rows = A4_HEIGHT // CARD_HEIGHT
    
    margin_x = (A4_WIDTH - (cols * CARD_WIDTH)) / 2
    margin_y = (A4_HEIGHT - (rows * CARD_HEIGHT)) / 2
    if margin_y < 5: margin_y = 5 # حداقل حاشیه

    all_cards = [('word', data) for data in word_cards] + \
                [('customer', data) for data in customer_cards]
    
    print(f"شروع تولید PDF برای {len(all_cards)} کارت...")

    for i, (card_type, card_data) in enumerate(all_cards):
        pdf.check_page_break()
        
        # محاسبه موقعیت کارت فعلی
        row = (pdf.card_count_on_page) // cols
        col = (pdf.card_count_on_page) % cols
        x = margin_x + (col * CARD_WIDTH)
        y = margin_y + (row * CARD_HEIGHT)

        # 1. رسم کادر کارت
        pdf.set_line_width(0.3)
        pdf.set_draw_color(0, 0, 0)
        pdf.rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        
        # 2. رسم نوار مایل بر اساس نوع کارت
        if card_type == 'word':
            draw_diagonal_stripe(pdf, x, y, CARD_WIDTH, CARD_HEIGHT, STRIPE_WIDTH, 
                               prepare_rtl_text("کالا"), color=(100, 150, 200))
        elif card_type == 'customer':
            draw_diagonal_stripe(pdf, x, y, CARD_WIDTH, CARD_HEIGHT, STRIPE_WIDTH, 
                               prepare_rtl_text("مشتری"), color=(200, 100, 100))
        
        # 3. Draw random shapes instead of inserting an image
        img_x = x + (CARD_WIDTH - IMAGE_ASSET_WIDTH) / 2
        img_y = y + 5  # 5mm فاصله از بالای کارت
        draw_random_shapes_on_pdf(pdf, img_x, img_y, IMAGE_ASSET_WIDTH-5, IMAGE_ASSET_HEIGHT-5, num_shapes=5)
        
        # 4. نوشتن متن
        text_y_start = img_y + IMAGE_ASSET_HEIGHT + 0 # شروع متن از زیر عکس
        
        pdf.set_font('Vazir', '', FONT_SIZE)
        
        if card_type == 'word':
            pdf.set_xy(x, text_y_start + 10) # وسط‌چین عمودی
            pdf.multi_cell(w=CARD_WIDTH, h=7, txt=prepare_rtl_text(card_data), align='C')
        
        elif card_type == 'customer':
            # عنوان مشتری
            pdf.set_font('Vazir', '', FONT_SIZE-1)
            pdf.set_xy(x + 2, text_y_start)
            title = prepare_rtl_text(f"{card_data['title']}")
            pdf.multi_cell(w=CARD_WIDTH - 4, h=5, txt=title, align='C')
            
            if customer_description:
                # خط جداکننده
                line_y = pdf.get_y() + 1
                pdf.line(x + 5, line_y, x + CARD_WIDTH - 5, line_y)

                # توضیحات مشتری
                pdf.set_font('Vazir', '', FONT_SIZE-4)
                current_y = line_y + 0  # موقعیت شروع توضیحات (پس از خط جداکننده)
                
                # تقسیم متن به خطوط کوچک با wrap
                desc_lines = wrap(card_data['description'], width=25)
                
                for line in desc_lines:
                    rtl_line = prepare_rtl_text(line)
                    pdf.set_xy(x + 0, current_y)
                    pdf.multi_cell(w=CARD_WIDTH - 4, h=4.5, txt=rtl_line, align='R')
                    current_y += 4.5  # افزایش موقعیت y به اندازه ارتفاع خط

        pdf.card_count_on_page += 1

    pdf.output(output_filename)
    print(f"فایل PDF با موفقیت در مسیر '{output_filename}' ذخیره شد.")
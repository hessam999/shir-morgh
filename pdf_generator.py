from fpdf import FPDF
import arabic_reshaper
from bidi.algorithm import get_display
from card_generator import generate_card_image_asset
from textwrap import wrap


# --- ثابت‌های چیدمان (بر حسب میلی‌متر) ---
A4_WIDTH, A4_HEIGHT = 210, 297
CARD_WIDTH, CARD_HEIGHT = 63, 88
IMAGE_ASSET_WIDTH, IMAGE_ASSET_HEIGHT = 45, 45 # اندازه تصویر روی کارت
FONT_PATH = "assets/font/Vazirmatn-Regular.ttf"

def prepare_rtl_text(text):
    """متن فارسی را برای نمایش صحیح در fpdf2 آماده می‌کند."""
    return get_display(arabic_reshaper.reshape(text))

class PDF(FPDF):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.card_count_on_page = 0
        self.cards_per_page = 8 # مقدار پیش‌فرض

    def check_page_break(self):
        """در صورت پر شدن صفحه، به صفحه جدید می‌رود."""
        if self.card_count_on_page >= self.cards_per_page:
            self.add_page()
            self.card_count_on_page = 0

def generate_pdf(word_cards, customer_cards, output_filename, cards_per_page=8):
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
        
        # 2. تولید و قرار دادن تصویر
        image_asset = generate_card_image_asset()
        img_x = x + (CARD_WIDTH - IMAGE_ASSET_WIDTH) / 2
        img_y = y + 5  # 5mm فاصله از بالای کارت
        pdf.image(image_asset, x=img_x, y=img_y, w=IMAGE_ASSET_WIDTH, h=IMAGE_ASSET_HEIGHT, type='PNG')

        # 3. نوشتن متن
        text_y_start = img_y + IMAGE_ASSET_HEIGHT + 2 # شروع متن از زیر عکس
        
        pdf.set_font('Vazir', '', 14)
        
        if card_type == 'word':
            pdf.set_xy(x, text_y_start + 10) # وسط‌چین عمودی
            pdf.multi_cell(w=CARD_WIDTH, h=7, txt=prepare_rtl_text(card_data), align='C')
        
        elif card_type == 'customer':
            # عنوان مشتری
            pdf.set_font('Vazir', '', 11)
            pdf.set_xy(x + 2, text_y_start)
            title = prepare_rtl_text(f"{card_data['title']}")
            pdf.multi_cell(w=CARD_WIDTH - 4, h=5, txt=title, align='C')

            # خط جداکننده
            line_y = pdf.get_y() + 1
            pdf.line(x + 5, line_y, x + CARD_WIDTH - 5, line_y)

            # توضیحات مشتری
            pdf.set_font('Vazir', '', 9)
            current_y = line_y + 3  # موقعیت شروع توضیحات (پس از خط جداکننده)
            
            # تقسیم متن به خطوط کوچک با wrap
            desc_lines = wrap(card_data['description'], width=35)
            
            for line in desc_lines:
                rtl_line = prepare_rtl_text(line)
                pdf.set_xy(x + 4, current_y)
                pdf.multi_cell(w=CARD_WIDTH - 8, h=4.5, txt=rtl_line, align='R')
                current_y += 4.5  # افزایش موقعیت y به اندازه ارتفاع خط

        pdf.card_count_on_page += 1

    pdf.output(output_filename)
    print(f"فایل PDF با موفقیت در مسیر '{output_filename}' ذخیره شد.")

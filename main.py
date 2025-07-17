import os
import json
import argparse
from pdf_generator import generate_pdf # <-- ایمپورت جدید

# --- مسیرهای پروژه ---
DATA_DIR = "data"
OUTPUT_DIR = "output"
WORD_CARDS_FILE = os.path.join(DATA_DIR, "word_cards.json")
CUSTOMER_CARDS_FILE = os.path.join(DATA_DIR, "customer_cards.json")
OUTPUT_PDF_FILE = os.path.join(OUTPUT_DIR, "shir_morgh_cards.pdf")
FONT_FILE = "assets/font/Vazirmatn-Regular.ttf"

def load_data(file_path):
    """داده‌ها را از یک فایل JSON بارگذاری می‌کند."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"خطا: فایل {file_path} پیدا نشد.")
        return None
    except json.JSONDecodeError:
        print(f"خطا: فایل {file_path} دارای فرمت JSON معتبری نیست.")
        return None

def main(cards_per_page):
    """تابع اصلی برای اجرای فرآیند تولید کارت‌ها."""
    
    # 1. ایجاد پوشه‌های ضروری
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(os.path.join("assets", "font"), exist_ok=True)
    
    # بررسی وجود فونت
    if not os.path.exists(FONT_FILE):
        print(f"خطای حیاتی: فونت در مسیر '{FONT_FILE}' یافت نشد.")
        print("لطفاً یک فونت فارسی (مانند Vazirmatn) را در این مسیر قرار دهید.")
        return

    # 2. بارگذاری داده‌های کارت‌ها
    word_cards_data = load_data(WORD_CARDS_FILE)
    customer_cards_data = load_data(CUSTOMER_CARDS_FILE)

    if not word_cards_data or not customer_cards_data:
        print("به دلیل عدم وجود داده‌ها، برنامه متوقف می‌شود.")
        return

    # 3. تولید مستقیم فایل PDF
    generate_pdf(
        word_cards=word_cards_data,
        customer_cards=customer_cards_data,
        output_filename=OUTPUT_PDF_FILE,
        cards_per_page=cards_per_page
    )

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="تولید کارت‌های بازی شیرمرغ به صورت PDF.")
    parser.add_argument(
        '--cards-per-page',
        type=int,
        default=25, # مقدار پیش‌فرض را به 9 تغییر دادم چون چیدمان 3x3 در A4 زیباست
        help='تعداد کارت‌هایی که در هر صفحه PDF چاپ می‌شود. (پیش‌فرض: 9)'
    )
    args = parser.parse_args()
    
    main(args.cards_per_page)

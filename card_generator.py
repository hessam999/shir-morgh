import random
import io
import cairosvg

IMAGE_SIZE = 180  # اندازه تصویر به پیکسل

def generate_random_svg():
    """یک تصویر SVG با اشکال هندسی تصادفی تولید می‌کند."""
    width, height = IMAGE_SIZE, IMAGE_SIZE
    shapes = []
    num_shapes = random.randint(3, 6)

    for _ in range(num_shapes):
        color = f"#{random.randint(0, 0xFFFFFF):06x}"
        stroke_color = f"#{random.randint(0, 0xFFFFFF):06x}"
        stroke_width = random.randint(1, 4)
        opacity = random.uniform(0.6, 0.9)
        
        shape_type = random.choice(['rect', 'circle', 'ellipse', 'line', 'triangle'])

        if shape_type == 'rect':
            x, y = random.randint(0, width // 2), random.randint(0, height // 2)
            w, h = random.randint(width // 4, width), random.randint(height // 4, height)
            shapes.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{color}" stroke="{stroke_color}" stroke-width="{stroke_width}" opacity="{opacity}"/>')
        
        elif shape_type == 'circle':
            cx, cy = random.randint(width // 4, 3 * width // 4), random.randint(height // 4, 3 * height // 4)
            r = random.randint(width // 8, width // 3)
            shapes.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" stroke="{stroke_color}" stroke-width="{stroke_width}" opacity="{opacity}"/>')
        
        elif shape_type == 'ellipse':
            cx, cy = random.randint(width // 4, 3 * width // 4), random.randint(height // 4, 3 * height // 4)
            rx, ry = random.randint(width // 8, width // 3), random.randint(height // 8, height // 3)
            shapes.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{color}" stroke="{stroke_color}" stroke-width="{stroke_width}" opacity="{opacity}"/>')

        elif shape_type == 'line':
            x1, y1 = random.randint(0, width), random.randint(0, height)
            x2, y2 = random.randint(0, width), random.randint(0, height)
            shapes.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke_color}" stroke-width="{stroke_width}" opacity="{opacity}"/>')

        elif shape_type == 'triangle':
            # سه نقطه برای مثلث
            points = [
                (random.randint(0, width), random.randint(0, height)),
                (random.randint(0, width), random.randint(0, height)),
                (random.randint(0, width), random.randint(0, height))
            ]
            points_str = " ".join(f"{x},{y}" for x, y in points)
            shapes.append(f'<polygon points="{points_str}" fill="{color}" stroke="{stroke_color}" stroke-width="{stroke_width}" opacity="{opacity}"/>')

    svg_content = f'<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg"><g transform="rotate({random.randint(-15, 15)} {width/2} {height/2})">{"".join(shapes)}</g></svg>'
    return svg_content

def generate_card_image_asset():
    """
    یک تصویر SVG تولید کرده و آن را به بایت‌های PNG تبدیل می‌کند تا مستقیماً در PDF استفاده شود.
    """
    svg_str = generate_random_svg()
    png_bytes = cairosvg.svg2png(bytestring=svg_str.encode('utf-8'))
    return io.BytesIO(png_bytes)
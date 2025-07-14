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
    # pdf_bytes = cairosvg.svg2pdf(bytestring=svg_str.encode('utf-8'))
    # return io.BytesIO(pdf_bytes)



def draw_random_shapes_on_pdf(pdf, x, y, w, h, num_shapes=5):
    for _ in range(num_shapes):
        shape_type = random.choice(['rect', 'ellipse', 'triangle', 'line'])
        # Generate random position and size within the bounding box
        shape_x = x + random.uniform(0, w * 0.7)
        shape_y = y + random.uniform(0, h * 0.7)
        shape_w = random.uniform(w * 0.2, w * 0.7)
        shape_h = random.uniform(h * 0.2, h * 0.7)
        # Random fill color
        r, g, b = random.randint(0,255), random.randint(0,255), random.randint(0,255)
        pdf.set_draw_color(r, g, b)
        pdf.set_fill_color(r, g, b)
        if shape_type == 'rect':
            pdf.rect(shape_x, shape_y, shape_w, shape_h, style='F')
        elif shape_type == 'ellipse':
            pdf.ellipse(shape_x, shape_y, shape_w, shape_h, style='F')
        elif shape_type == 'triangle':
            p1 = (shape_x, shape_y)
            p2 = (shape_x + shape_w, shape_y)
            p3 = (shape_x + shape_w/2, shape_y + shape_h)
            pdf.polygon([p1, p2, p3], style='F')
        elif shape_type == 'line':
            # Set a thicker line width (e.g., 2.0 mm, or random)
            pdf.set_line_width(random.uniform(1.0, 4.0))  # thickness between 1 and 4 mm
            x2 = shape_x + shape_w
            y2 = shape_y + shape_h
            pdf.line(shape_x, shape_y, x2, y2)
            pdf.set_line_width(0.2)  # Reset to default after drawing

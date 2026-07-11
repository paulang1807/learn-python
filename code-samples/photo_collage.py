# This script create a photo collage from images in the Pics folder and adds a Bengali heading

# Prerequisites:
# 1. Download a Font for the relevant language: 
#    For Bengali: Download a Unicode font like Kalpurush.ttf or SolaimanLipi.ttf and place it in the same folder as this script.
#    Bengali font can be downloaded from: https://lipighor.com/, https://www.omicronlab.com/kalpurush-font/, https://fonts.google.com/ (search for "Kalpurush" or "Bengali")

# Path of the folder containing images
# Pics folder is in the same folder as this script

IMAGE_FOLDER = "./Pics"
OUTPUT_FILE = "./output.jpg" 

# Import necessary libraries
import os
import glob
from PIL import Image, ImageDraw, ImageFont, ImageOps

def get_bengali_syllables():
    """
    Returns the exact structural glyph map for 'জীবন মরণের সীমানা ছাড়ায়ে'
    with pre-base vowel signs shifted correctly to the left.
    """
    return [
        {"text": "জী", "spacing_adj": 5},
        {"text": "ব", "spacing_adj": 5},
        {"text": "ন", "spacing_adj": 105}, # Space after "জীবন"
        
        {"text": "ম", "spacing_adj": 5},
        {"text": "র", "spacing_adj": 0},
        {"text": "ে", "spacing_adj": -20}, 
        {"text": "ণ", "spacing_adj": 5},  
        {"text": "র", "spacing_adj": 105}, # Space after "মরণের"
        
        {"text": "সী", "spacing_adj": 5},
        {"text": "মা", "spacing_adj": 5},
        {"text": "না", "spacing_adj": 105}, # Space after "সীমানা"
        
        {"text": "ছা", "spacing_adj": 5},
        {"text": "ড়া", "spacing_adj": -10},
        {"text": "ে", "spacing_adj": -20}, 
        {"text": "য়", "spacing_adj": 0}    
    ]

def measure_shaped_text_width(draw, font, syllables):
    """
    Dry-runs the layout logic to calculate the precise pixel width
    of the entire phrase for perfect horizontal centering.
    """
    total_w = 0
    for i, syl in enumerate(syllables):
        bbox = draw.textbbox((0, 0), syl["text"], font=font)
        w = bbox[2] - bbox[0]
        total_w += w
        if i < len(syllables) - 1:
            total_w += syl["spacing_adj"]
    return total_w

def draw_thickened_text(draw, x, y, text, font, fill_color, thickness=6):
    """
    Renders text with simulated artificial thickness by stamping it in a 
    tight directional grid matrix before completing the center core.
    """
    for dx in range(-thickness, thickness + 1):
        for dy in range(-thickness, thickness + 1):
            if dx*dx + dy*dy <= thickness*thickness:
                draw.text((x + dx, y + dy), text, fill=fill_color, font=font)

def render_thick_3d_bengali(draw, start_x, y, font, face_color, syllables):
    """
    Combines manual complex script syllable ordering, structural 3D extrusion,
    and geometric font thickening for an ultra-bold, high-relief header banner.
    """
    TEXT_THICKNESS = 6         
    EXTRUSION_DEPTH = 24       
    SHADOW_BLUR_STEPS = 14     
    
    # 1. Ambient Drop Shadow (Furthest Backing)
    shadow_color = (225, 225, 225)
    for s in range(SHADOW_BLUR_STEPS):
        offset_x = EXTRUSION_DEPTH + (s * 2)
        offset_y = EXTRUSION_DEPTH + (s * 2)
        
        current_x = start_x
        for syl in syllables:
            draw_thickened_text(draw, current_x + offset_x, y + offset_y, syl["text"], font, shadow_color, TEXT_THICKNESS)
            bbox = draw.textbbox((0, 0), syl["text"], font=font)
            current_x += (bbox[2] - bbox[0]) + syl["spacing_adj"]

    # 2. Extruded Structural 3D Walls (Middle Gradient Layers)
    for depth in range(EXTRUSION_DEPTH, 0, -1):
        brightness = 90 + int((110 * (depth / EXTRUSION_DEPTH)))
        block_color = (brightness, brightness, brightness)
        
        current_x = start_x
        for syl in syllables:
            draw_thickened_text(draw, current_x + depth, y + depth, syl["text"], font, block_color, TEXT_THICKNESS)
            bbox = draw.textbbox((0, 0), syl["text"], font=font)
            current_x += (bbox[2] - bbox[0]) + syl["spacing_adj"]

    # 3. Foreground Front Face (Sharp Front Surface)
    current_x = start_x
    for syl in syllables:
        draw_thickened_text(draw, current_x, y, syl["text"], font, face_color, TEXT_THICKNESS)
        bbox = draw.textbbox((0, 0), syl["text"], font=font)
        current_x += (bbox[2] - bbox[0]) + syl["spacing_adj"]

def create_memorial_poster():
    # 1. Canvas Dimensions (24" x 36" at 300 DPI)
    TOTAL_WIDTH = 7200
    TOTAL_HEIGHT = 10800
    BACKGROUND_COLOR = (255, 255, 255)  
    TEXT_COLOR = (45, 45, 45)            
    
    # Layout Bounds & Margins
    SIDE_MARGIN = 350   
    TOP_MARGIN = 200    
    HEADER_HEIGHT = 1250                 
    SPACING = 60        
    BOTTOM_MARGIN = 350 

    # 2. File Path Handling
    supported_extensions = ('*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG')
    image_paths = []
    for ext in supported_extensions:
        image_paths.extend(glob.glob(os.path.join(IMAGE_FOLDER, ext)))
    
    image_paths = sorted(image_paths)[:24]
    if not image_paths:
        print(f"Error: No images found in the {IMAGE_FOLDER} folder.")
        return

    font_files = glob.glob('*.ttf') + glob.glob('*.otf')
    if not font_files:
        print("Error: No .ttf or .otf font file found.")
        return
    font_path = font_files[0]

    # 3. Image Processing
    processed_images = []
    for img_path in image_paths:
        try:
            with Image.open(img_path) as img:
                corrected_img = ImageOps.exif_transpose(img)
                processed_images.append(corrected_img.convert("RGB"))
        except Exception as e:
            print(f"Skipping corrupt image {img_path}: {e}")

    # 4. Calculate Printable Space Boundaries
    start_y = TOP_MARGIN + HEADER_HEIGHT + SPACING
    target_width = TOTAL_WIDTH - (2 * SIDE_MARGIN)
    max_allowed_grid_height = TOTAL_HEIGHT - start_y - BOTTOM_MARGIN

    # 5. Justified Row Layout Engine
    TARGET_IMAGES_PER_ROW = 4
    rows = []
    current_row = []
    
    for img in processed_images:
        current_row.append(img)
        if len(current_row) == TARGET_IMAGES_PER_ROW:
            rows.append(current_row)
            current_row = []
    if current_row:  
        rows.append(current_row)

    def calculate_layout(target_w, spacing_val):
        layout_rows = []
        current_y = start_y
        for row in rows:
            sum_aspect_ratios = sum(img.size[0] / img.size[1] for img in row)
            gaps_count = len(row) - 1
            available_image_width = target_w - (gaps_count * spacing_val)
            row_height = int(available_image_width / sum_aspect_ratios)
            
            row_positions = []
            current_x = SIDE_MARGIN
            for img in row:
                img_aspect = img.size[0] / img.size[1]
                img_w = int(row_height * img_aspect)
                row_positions.append((img, current_x, current_y, img_w, row_height))
                current_x += img_w + spacing_val
            layout_rows.append(row_positions)
            current_y += row_height + spacing_val
        return layout_rows, current_y - spacing_val

    layout_data, total_grid_height = calculate_layout(target_width, SPACING)
    current_bottom_y = total_grid_height + BOTTOM_MARGIN

    if current_bottom_y > TOTAL_HEIGHT:
        overflow_ratio = max_allowed_grid_height / (total_grid_height - start_y)
        target_width = int(target_width * overflow_ratio)
        SPACING = int(SPACING * overflow_ratio)
        SIDE_MARGIN = (TOTAL_WIDTH - target_width) // 2
        layout_data, total_grid_height = calculate_layout(target_width, SPACING)

    # 6. Initialize Canvas
    canvas = Image.new("RGB", (TOTAL_WIDTH, TOTAL_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(canvas)

    # 7. Apply Dynamic Centered 3D Script-Shaping Header
    font_size = 430  
    try:
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"Error loading font: {e}")
        return

    syllables = get_bengali_syllables()
    
    # PASS 1: Calculate the exact real-world layout width of the phrase
    print("Pre-measuring shaped text matrix for exact pixel-level centering...")
    actual_text_width = measure_shaped_text_width(draw, font, syllables)
    
    # PASS 2: Place text perfectly centered on the X axis
    text_start_x = (TOTAL_WIDTH - actual_text_width) // 2
    text_y = TOP_MARGIN + (HEADER_HEIGHT - font_size) // 2
    
    print("Executing flawless centered ultra-bold 3D text block assembly...")
    render_thick_3d_bengali(draw, text_start_x, text_y, font, TEXT_COLOR, syllables)

    # 8. Render Images inside the Justified Grid Setup
    for row in layout_data:
        if len(row) > 0:
            last_img, lx, ly, lw, lh = row[-1]
            right_boundary_shortfall = (SIDE_MARGIN + target_width) - (lx + lw)
            if abs(right_boundary_shortfall) < 10: 
                row[-1] = (last_img, lx, ly, lw + right_boundary_shortfall, lh)

        for img, x, y, w, h in row:
            resized_img = img.resize((w, h), Image.LANCZOS)
            canvas.paste(resized_img, (x, y))

    # 9. Save Production Print File
    canvas.save(OUTPUT_FILE, "JPEG", quality=98, optimize=True)
    print(f"Success! High-relief, ultra-bold perfectly CENTERED 3D memorial poster saved as '{OUTPUT_FILE}'")

if __name__ == "__main__":
    create_memorial_poster()
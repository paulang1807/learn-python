# This script will extract all the images from a pdf file and save them to a folder
# It will use the PyMuPDF library to extract the images
# It will use the pathlib library to save the images
# It will use the fitz library to extract the images
# It will log errors to the console

# git location: https://gist.github.com/paulang1807/db319455b20e64c89886e2cc500e2b3a

from pathlib import Path
import fitz  # PyMuPDF

def extract_or_render_pdf(pdf_path: str, output_dir: str = "extracted_images"):
    pdf_file = Path(pdf_path)
    if not pdf_file.exists():
        print(f"Error: '{pdf_path}' not found.")
        return

    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_file)
    image_count = 0

    print(f"Scanning '{pdf_file.name}'...")

    for page_index in range(len(doc)):
        page = doc[page_index]
        image_list = page.get_images(full=True)
        
        # Method A: Try extracting embedded objects first
        extracted_from_page = False
        if image_list:
            for img_index, img in enumerate(image_list):
                xref = img[0]
                base_image = doc.extract_image(xref)
                
                if base_image and "bytes" in base_image:
                    image_ext = base_image["ext"]
                    filename = out_path / f"img_page{page_index + 1:03d}_obj{img_index + 1:02d}.{image_ext}"
                    
                    with open(filename, "wb") as f:
                        f.write(base_image["bytes"])
                    
                    image_count += 1
                    extracted_from_page = True

        # Method B: Fallback if no images were found structurally on this page
        if not extracted_from_page:
            # Render the page at high resolution (300 DPI) using a matrix zoom
            zoom = 300 / 72  # 72 is the default PDF DPI
            matrix = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=matrix)
            
            filename = out_path / f"page_{page_index + 1:03d}.png"
            pix.save(str(filename))
            image_count += 1

    doc.close()
    print(f"\n--- Done! Saved {image_count} files to '{out_path.resolve()}' ---")

if __name__ == "__main__":
    import sys
    target_pdf = sys.argv[1] if len(sys.argv) > 1 else "Done1.pdf"
    extract_or_render_pdf(target_pdf)
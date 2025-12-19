import pdfplumber

pdf_path = '/vercel/sandbox/uploads/web jutt.pdf'

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        print(f"### Page {page_num}")
        # Extract text
        text = page.extract_text()
        print("Text content:")
        print(text)
        print("\n")
        # Extract layout: words with positions
        words = page.extract_words()
        print("Layout (words with positions):")
        for word in words:
            print(f"Text: '{word['text']}', x0: {word['x0']}, y0: {word['y0']}, x1: {word['x1']}, y1: {word['y1']}")
        print("\n")
        # Extract images
        images = page.images
        print("Images:")
        for i, img in enumerate(images):
            print(f"Image {i+1}: bbox {img['x0']}, {img['y0']}, {img['x1']}, {img['y1']}")
            # Save image
            try:
                img_stream = img['stream']
                img_data = img_stream.get_data()
                with open(f'/vercel/sandbox/image_page{page_num}_{i}.png', 'wb') as f:
                    f.write(img_data)
                print(f"Saved as image_page{page_num}_{i}.png")
            except Exception as e:
                print(f"Could not save image: {e}")
        print("\n")
        # Fonts and sizes
        chars = page.chars
        fonts = set()
        sizes = set()
        for char in chars:
            fonts.add(char.get('fontname', 'unknown'))
            sizes.add(char.get('size', 0))
        print("Fonts used:", fonts)
        print("Font sizes used:", sizes)
        print("\n")
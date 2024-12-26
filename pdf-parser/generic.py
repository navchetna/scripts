import pdfplumber
import re


def clean_text(text):
    text = re.sub(r'[^\x20-\x7E\n]', '', text)
    text = re.sub(r'(cid:\d+)', '', text)
    text = re.sub(r'\(\)', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# change path
def extract_text_and_structure(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        all_pages_data = []
        for page in pdf.pages:
            page_data = []
           
            for element in page.extract_words(x_tolerance=3, y_tolerance=3, keep_blank_chars=True):
                page_data.append({
                    'text': clean_text(element['text']),
                    'structure': {
                        'x0': element['x0'],
                        'x1': element['x1'],
                        'top': element['top'],
                        'bottom': element['bottom'],
                        'width': element['width'],
                        'height': element['height']
                    },
                    'type': 'text'
                })
           
            if hasattr(page, 'annots') and page.annots:
                for annot in page.annots:
                    try:
                        if annot.get('subtype') == 'Text' and 'contents' in annot:
                            page_data.append({
                                'text': f"Commented [{annot.get('id', '')}]: {clean_text(annot['contents'])}",
                                'structure': {
                                    'x0': annot.get('x0', 0),
                                    'x1': annot.get('x1', 0),
                                    'top': annot.get('top', 0),
                                    'bottom': annot.get('bottom', 0),
                                    'width': annot.get('width', 0),
                                    'height': annot.get('height', 0)
                                },
                                'type': 'comment'
                            })
                    except Exception as e:
                        print(f"Error processing annotation: {e}")
            all_pages_data.append(page_data)
    return all_pages_data


def sort_elements(elements, line_height=12):
    return sorted(elements, key=lambda e: (e['structure']['top'] // line_height, e['structure']['x0']))


def merge_elements(elements, max_horizontal_gap=50, max_vertical_gap=5):
    merged = []
    current_line = []
    for element in elements:
        if element['type'] == 'comment':
            if current_line:
                merged.append(current_line)
                current_line = []
            merged.append([element])
        elif not current_line:
            current_line.append(element)
        elif (abs(element['structure']['top'] - current_line[-1]['structure']['top']) <= max_vertical_gap and
              element['structure']['x0'] - current_line[-1]['structure']['x1'] <= max_horizontal_gap):
            current_line.append(element)
        else:
            merged.append(current_line)
            current_line = [element]
    if current_line:
        merged.append(current_line)
    return merged


def format_lines(merged_lines):
    formatted_text = []
    for line in merged_lines:
        if line[0]['type'] == 'comment':
            formatted_text.append(line[0]['text'])
        else:
            line_text = ' '.join(element['text'] for element in line)
            formatted_text.append(line_text)
    return formatted_text


def load_and_process_pdf(pdf_path):
    all_pages_data = extract_text_and_structure(pdf_path)


    formatted_text = []
    for page_data in all_pages_data:
        sorted_elements = sort_elements(page_data)
        merged_lines = merge_elements(sorted_elements)
        formatted_lines = format_lines(merged_lines)
        formatted_text.extend(formatted_lines)


    return ' '.join(formatted_text)

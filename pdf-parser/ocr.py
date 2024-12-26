import os
# Let's pick the desired backend
# os.environ['USE_TF'] = '1'
os.environ['USE_TORCH'] = '1'


import matplotlib.pyplot as plt


from doctr.io import DocumentFile
from doctr.models import ocr_predictor
pdf_doc = DocumentFile.from_pdf("") # add path to pdf
import torch
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
model = ocr_predictor('fast_base',reco_arch='master',pretrained=True,assume_straight_pages=False, preserve_aspect_ratio=True).to(device)
result = model(pdf_doc)
result.show()

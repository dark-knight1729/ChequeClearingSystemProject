import pytesseract as pt
from PIL import Image


# pt.pytesseract.tesseract_cmd=r'C:\Users\AKSHIT\AppData\Local\Programs\Python\Python37-32\Scripts\Tesseract.exe'
# filepath='cheque.png'
def extractDetailsFromCheque(filePath):
    im = Image.open(filePath)
    text = pt.image_to_string(im)
    data = text.splitlines()
    details = dict()
    details['bankName'] = data[0]
    details['chequeNumber'] = data[-1]
    for x in data:
        y = x.split()
        for index, z in enumerate(y):
            if z == 'IFSC':
                details['ifsc'] = y[index + 1]
            if z == 'DATE:':
                details['date'] = y[index + 1]
            if z == 'Pay:':
                details['name'] = y[index + 1] + ' ' + y[index + 2]
            if z == 'RS:':
                details['amount'] = y[index + 1]
            if z == 'No.':
                details['accountNumber'] = y[index + 1]
    return details
# extractDetailsFromCheque(filepath)
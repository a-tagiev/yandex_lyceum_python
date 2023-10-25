with open('input.bmp', 'rb') as file:
    data = file.read()
neg_data = bytes([255 - byte for byte in data[55:]])
with open('res.bmp', 'wb') as file:
    file.write(data[:54] + neg_data)

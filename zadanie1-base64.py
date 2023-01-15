import base64
def encrypt_base64(text):
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message
# test funkcji
print(encrypt_base64("test szyfrowania"))

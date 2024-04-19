from stegano import exifHeader

secret = exifHeader.hide("img/2.jpeg", "img/2_secret.jpeg", "Русский текст тоже тут работает")

result = exifHeader.reveal("img/2_secret.jpeg")
result = result.decode()
print(result)
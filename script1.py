# pip install stegano
from stegano import lsb

secret = lsb.hide("img/1.webp", "Secret message")

# does not work if secret image has jpeg, webp formats. (should be bmp/png below)
secret.save("img/1_secret.png")

result = lsb.reveal("img/1_secret.png")
print(result)
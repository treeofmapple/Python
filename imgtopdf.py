from PIL import Image

imagem = Image.open("image.jpg")

if imagem.mode == "RGBA":
    imagem = imagem.convert("RGB")

imagem.save("saida.pdf")

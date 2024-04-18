import qrcode as qr

x=input("Enter item for which you want to generate QR CODE =  ") 


y=input("enter QR Code File name with extension =  ")


img=qr.make(x)     #used to add content of QR CODE

img.save(y)       # save QR CODE as Image

#QR CODE WILL BE GENERATED IN THE FOLDER




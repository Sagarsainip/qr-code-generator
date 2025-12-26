# Importing liberaries

import qrcode
from PIL import Image
import os

# Tacking UPI_id from user
UPI_id = input("Enter your UPI ID: ")

#UPI URL format
upi_url = f"upi://pay?pa={UPI_id}&pn=RecipientName&am=Amount&cu=INR&tn=Note"

# Defining the payment URL based on the UPI ID and the payment apps
# You can modify the URL format based on the payment app requirements

#Creating the payment URL
Phonepe_url = f"phonepe://upi/pay?pa={UPI_id}&pn=RecipientName&am=Amount&cu=INR&tn=Note"
Gpay_url = f"tez://upi/pay?pa={UPI_id}&pn=RecipientName&am=Amount&cu=INR&tn=Note"
Paytm_url = f"paytmmp://upi/pay?pa={UPI_id}&pn=RecipientName&am=Amount&cu=INR&tn=Note"
Amazonpay_url = f"amazonpayupi://upi/pay?pa={UPI_id}&pn=RecipientName&am=Amount&cu=INR&tn=Note"

#Creating QR Codes for each payment app
qr_phonepe = qrcode.make(Phonepe_url)
qr_gpay = qrcode.make(Gpay_url)
qr_paytm = qrcode.make(Paytm_url)
qr_amazonpay = qrcode.make(Amazonpay_url)


# Saving the QR Codes as image files
qr_phonepe.save("outputs/Phonepe_UPI_QR.png")
qr_gpay.save("outputs/Gpay_UPI_QR.png")
qr_paytm.save("outputs/Paytm_UPI_QR.png")
qr_amazonpay.save("outputs/Amazonpay_UPI_QR.png")


#Displaying the QR Codes
qr_phonepe.show()
qr_gpay.show()
qr_paytm.show()
qr_amazonpay.show()



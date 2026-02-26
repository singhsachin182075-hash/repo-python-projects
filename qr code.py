import qrcode

upi_id=input("enter your UPI ID=")

# upi://pay?pa=upi_id&pr=name&am=amount&cu=currncy&tn=message

phonepe_url=f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'
google_pay_url=f'upi://pay?pa={upi_id}&pn=recipient%20name&mc=1234'

#creating qr for each payment app
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_pay_qr=qrcode.make(google_pay_url)

#save qr code to img
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#display qrcodes
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
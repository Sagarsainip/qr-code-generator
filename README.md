# QR Code Generator (UPI Payment)

This project generates QR codes for multiple UPI payment apps such as PhonePe, Google Pay, Paytm, Amazon Pay, and more.

It is built using Python and the `qrcode` library.

---

## 👤 Author
**Name:** Sagar Saini  
**Project:** QR Code Generator  
**Tools:** Python, qrcode, Pillow

---

## 📂 Project Structure

```
qr-code-generator/
│
├── src/
│ └── QR_code.py
│
├── outputs/
│ └── (generated QR codes)
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```


---

## ▶️ How it works

The program asks for your UPI ID and automatically creates QR codes for:

- PhonePe
- Google Pay
- Paytm
- Amazon Pay

Each QR is saved as an image file.

---

## 🚀 How to Run

1. Install Python (if not installed)
2. Open terminal in project folder
3. Install dependencies:
```
 pip install -r requirements.txt
```

4. Run the script:
```
python src/qr_code.py
```

5. Enter your UPI ID when asked.

Generated QR codes appear inside the **outputs** folder.

---

## 📌 Note
This project is for learning and demo use only — always verify UPI details before sharing.



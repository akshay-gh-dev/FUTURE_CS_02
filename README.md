# Password Analyzer Tool

## 📌 Overview
The **Password Analyzer Tool** is a Python-based application that helps users evaluate the strength of their passwords. It also generates a **SHA-256 hash** of the password for security insights. The tool provides a simple **Graphical User Interface (GUI)** using `Tkinter`.

## 🛠 Features
- ✅ **Password Strength Analysis** based on security criteria:
  - Lowercase letter ✅
  - Uppercase letter ✅
  - Digit ✅
  - Special character ✅
  - Minimum length (8 characters) ✅
- 🔒 **SHA-256 Password Hashing** for security.
- 👁️ **Toggle Password Visibility** (Show/Hide password feature).
- 🎨 **User-friendly GUI** built with Tkinter.

## 🏗️ Technologies Used
- **Python 3**
- **Tkinter** (for GUI)
- **Regex (`re`)** (for password strength validation)
- **Hashlib** (for SHA-256 hashing)

## 🚀 Installation
### **1. Clone the Repository**
```sh
git clone https://github.com/akshay-gh-dev/FUTURE_CS_02/
cd password-analyzer
```

### **2. Install Dependencies**
Ensure you have Python 3 installed, then install dependencies:
```sh
pip install -r requirements.txt
```

### **3. Run the Application**
```sh
python password_analyzer.py
```
or  
```sh
python3 password_analyzer.py
```

## 📌 How to Use
1. **Enter a password** in the text box.
2. **Check "Show Password"** to see the password in clear text.
3. **Click "Analyze"** to evaluate the password strength.
4. The tool will display:
   - **Strength** (Weak, Moderate, Strong).
   - **Criteria Met** (e.g., contains uppercase, digits, etc.).
   - **SHA-256 Hash** of the password.

## 📝 License
This project is licensed under the **MIT License**.
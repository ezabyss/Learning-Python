# Playfair Cipher – Learning Project

This repository documents my learning and understanding of the **Playfair Cipher**, a classical encryption technique studied in cybersecurity.

This project focuses on explaining **how encryption and decryption work step by step**, rather than only providing code.

---

## 📌 What is Playfair Cipher?

The Playfair Cipher is a **symmetric key encryption method**, meaning the same key is used for encryption and decryption.

It encrypts text in **pairs of letters (digraphs)** using a **5×5 key matrix** generated from a keyword.

Although it is not secure for modern systems, it is very useful for learning the fundamentals of cryptography.

---

## 🎯 Learning Objectives

- Understand encryption and decryption concepts
- Learn how symmetric key encryption works
- Apply Playfair Cipher rules correctly
- Explain encryption steps clearly using tables
- Demonstrate real examples

---

## 🔑 Key Used in This Project

**Keyword:** `MOUNTAINS`  
- Duplicate letters removed  
- I and J treated as the same letter  

### 5×5 Key Matrix
## 5×5 Key Matrix (Playfair Cipher)

| Row \ Col | 1 | 2 | 3 | 4 | 5 |
|-----------|---|---|---|---|---|
| **1** | M | O | U | N | T |
| **2** | A | I | S | B | C |
| **3** | D | E | F | G | H |
| **4** | K | L | P | Q | R |
| **5** | V | W | X | Y | Z |


This matrix is used for both encryption and decryption.

---

## 🧪 Example Used

**Plaintext:** `BALLOONS`

This example was chosen because:
- It contains repeated letters (LL)
- It has an odd length
- It demonstrates padding using X
- It applies multiple Playfair rules

---

## ✏️ Plaintext Preparation

Prepared digraphs after applying Playfair rules:
> BA LX LO ON SX


---

## 🔐 Encryption Process

### Encryption Rules
- Same row → shift right  
- Same column → shift down  
- Rectangle → swap columns  

### Encryption Table

| Step | Plain Pair | Rule Applied | Encrypted Pair |
|----|-----------|--------------|----------------|
| 1 | BA | Same row | CI |
| 2 | LX | Rectangle | PW |
| 3 | LO | Same column | WI |
| 4 | ON | Same row | UT |
| 5 | SX | Same column | FU |

### Final Ciphertext
> CIPWWIUTFU


---

## 🔓 Decryption Process

### Decryption Rules
- Same row → shift left  
- Same column → shift up  
- Rectangle → swap columns  

### Decryption Table

| Step | Cipher Pair | Rule Applied | Decrypted Pair |
|----|------------|--------------|----------------|
| 1 | CI | Same row | BA |
| 2 | PW | Rectangle | LX |
| 3 | WI | Same column | LO |
| 4 | UT | Same row | ON |
| 5 | FU | Same column | SX |

### Decrypted Text
> BALXLOONSX


(The letter **X** was added only to satisfy Playfair rules.)

---

## 💻 Program Implementation

This project was implemented using **Python** to verify the encryption and decryption results considered in this repository.

The code:
- Generates the key matrix  
- Prepares plaintext into digraphs  
- Encrypts plaintext  
- Decrypts ciphertext  

The focus of this repository is on **learning and explanation**, not code complexity.

---

## ⚠️ Security Note

The Playfair Cipher is not suitable for modern encryption systems and can be broken using cryptographic analysis. This project is intended **only for educational purposes**.

---






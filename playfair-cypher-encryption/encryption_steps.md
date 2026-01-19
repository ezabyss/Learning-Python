# Playfair Cipher – Encryption Steps

This document explains the encryption process of the Playfair Cipher in a clear, step-by-step way.  
It focuses on plaintext preparation, rule application, and ciphertext generation.

---

## Key Used

Keyword: MOUNTAINS

- Duplicate letters removed  
- Letters I and J are treated as the same letter  

---

## 5×5 Key Matrix

    M O U N T
    A I S B C
    D E F G H
    K L P Q R
    V W X Y Z

This matrix is used for both encryption and decryption.

---

## Plaintext Used

Plaintext: BALLOONS

This word is used because:
- It contains repeated letters (LL)
- It has an odd length
- It demonstrates padding with X

---

## Plaintext Preparation Rules

    Convert text to uppercase
    Remove spaces and special characters
    Replace J with I
    Split text into pairs of letters
    Insert X between repeated letters
    Add X if one letter remains at the end

---

## Plaintext Preparation Steps

| Step | Current Letters | Rule / Situation | Output |
|------|----------------|------------------|--------|
| 1 | BA | Normal pair | BA |
| 2 | LL | Same letter → insert X | LX |
| 3 | LO | Normal pair | LO |
| 4 | ON | Normal pair | ON |
| 5 | S | One letter left → add X | SX |

---

## Prepared Digraphs

    BA  LX  LO  ON  SX

---

## Encryption Rules

    Same row    → shift right
    Same column → shift down
    Rectangle   → swap columns

---

## Encryption Process (Step-by-Step)

| Step | Plain Pair | Position (Row, Col) | Rule Applied | Encrypted Pair |
|------|------------|---------------------|--------------|----------------|
| 1 | BA | B(2,4), A(2,1) | Same row → shift right | CI |
| 2 | LX | L(4,2), X(5,3) | Rectangle → swap columns | PW |
| 3 | LO | L(4,2), O(1,2) | Same column → shift down | WI |
| 4 | ON | O(1,2), N(1,4) | Same row → shift right | UT |
| 5 | SX | S(2,3), X(5,3) | Same column → shift down | FU |

---

## Final Ciphertext

    CIPWWIUTFU

---

## Summary

This example demonstrates how the Playfair Cipher:
- Encrypts text using digraphs instead of single letters
- Applies fixed positional rules
- Handles repeated letters and odd-length plaintext
- Converts plaintext into ciphertext using a shared key

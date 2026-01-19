# Playfair Cipher – Decryption Steps

This document explains the decryption process of the Playfair Cipher in a clear, step-by-step way.  
It shows how ciphertext is converted back into the prepared plaintext using the same key matrix.

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

## Ciphertext Used

Ciphertext:

    CIPWWIUTFU

Ciphertext digraphs:

    CI  PW  WI  UT  FU

---

## Decryption Rules

    Same row    → shift left
    Same column → shift up
    Rectangle   → swap columns

---

## Decryption Process (Step-by-Step)

| Step | Cipher Pair | Position (Row, Col) | Rule Applied | Decrypted Pair |
|------|------------|---------------------|--------------|----------------|
| 1 | CI | C(2,5), I(2,2) | Same row → shift left | BA |
| 2 | PW | P(4,3), W(5,2) | Rectangle → swap columns | LX |
| 3 | WI | W(5,2), I(2,2) | Same column → shift up | LO |
| 4 | UT | U(1,3), T(1,5) | Same row → shift left | ON |
| 5 | FU | F(3,3), U(1,3) | Same column → shift up | SX |

---

## Decrypted Text (Prepared Plaintext)

    BALXLOONSX

Note:
- The X after L was inserted because the original plaintext had repeated letters (LL).
- The final X was added because the original plaintext had an odd length.

---

## Summary

This decryption example shows how the Playfair Cipher:
- Uses the same shared key matrix for decryption
- Applies reverse shifting rules to restore the message
- Produces the prepared plaintext, including padding X added during encryption

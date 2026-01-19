# ============================================================
# Playfair Cipher - Interactive (Educational)
#
# - Classical symmetric encryption algorithm
# - Uses a 5x5 key matrix
# - Encrypts and decrypts text in pairs (digraphs)
# - Program keeps running until user types 'q' to quit
#
# IMPORTANT RULE:
# Letters I and J are treated as the same letter (J -> I)
# ============================================================

import string  # Used to validate alphabet characters (A-Z)

# Playfair uses only 25 letters, so J is removed
ALPHABET_25 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


def normalize_text(text):
    """
    PURPOSE:
    This function prepares input text so it can be processed
    correctly by the Playfair Cipher.

    STEPS:
    1. Convert all characters to uppercase
    2. Remove non-alphabet characters (spaces, numbers, symbols)
    3. Replace J with I (Playfair rule)
    """
    text = text.upper()
    result = ""

    for ch in text:
        # Only keep English letters A-Z
        if ch in string.ascii_uppercase:
            # Replace J with I
            result += "I" if ch == "J" else ch

    return result


def build_key_matrix(key):
    """
    PURPOSE:
    Builds the 5x5 Playfair key matrix and a lookup table
    for letter positions.

    PROCESS:
    1. Normalize the key
    2. Remove duplicate letters
    3. Fill remaining letters from the alphabet
    4. Store (row, column) position for each letter
    """
    key = normalize_text(key)

    used = set()     # Keeps track of letters already added
    letters = []     # Final ordered list of 25 letters

    # Step 1: Insert key letters first (no duplicates)
    for ch in key:
        if ch in ALPHABET_25 and ch not in used:
            used.add(ch)
            letters.append(ch)

    # Step 2: Fill remaining alphabet letters
    for ch in ALPHABET_25:
        if ch not in used:
            letters.append(ch)

    # Step 3: Convert the list into a 5x5 matrix
    matrix = [letters[i:i + 5] for i in range(0, 25, 5)]

    # Step 4: Store positions of each letter
    # Example: pos['A'] = (row, column)
    pos = {}
    for r in range(5):
        for c in range(5):
            pos[matrix[r][c]] = (r, c)

    return matrix, pos


def display_matrix(matrix):
    """
    Displays the 5x5 key matrix in a readable format.
    """
    print("\n5x5 Key Matrix:")
    for row in matrix:
        print(" ".join(row))


def prepare_plaintext(text):
    """
    PURPOSE:
    Converts plaintext into digraphs following Playfair rules.

    RULES APPLIED:
    - Text is normalized
    - Same letter in a pair → insert X
    - If one letter remains → add X
    """
    text = normalize_text(text)
    pairs = []
    i = 0

    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else "X"

        # If both letters are the same, insert X
        if a == b:
            pairs.append((a, "X"))
            i += 1
        else:
            pairs.append((a, b))
            i += 2

    return pairs


def encrypt_pair(a, b, matrix, pos):
    """
    Encrypts one digraph (pair of letters).

    PLAYFAIR ENCRYPTION RULES:
    1. Same row    → shift right
    2. Same column → shift down
    3. Rectangle  → swap columns
    """
    r1, c1 = pos[a]
    r2, c2 = pos[b]

    # Rule 1: Same row
    if r1 == r2:
        return (
            matrix[r1][(c1 + 1) % 5],
            matrix[r2][(c2 + 1) % 5],
            "Same row → shift right"
        )

    # Rule 2: Same column
    if c1 == c2:
        return (
            matrix[(r1 + 1) % 5][c1],
            matrix[(r2 + 1) % 5][c2],
            "Same column → shift down"
        )

    # Rule 3: Rectangle rule
    return (
        matrix[r1][c2],
        matrix[r2][c1],
        "Rectangle → swap columns"
    )


def decrypt_pair(a, b, matrix, pos):
    """
    Decrypts one digraph.

    PLAYFAIR DECRYPTION RULES:
    1. Same row    → shift left
    2. Same column → shift up
    3. Rectangle  → swap columns (same as encryption)
    """
    r1, c1 = pos[a]
    r2, c2 = pos[b]

    # Rule 1: Same row
    if r1 == r2:
        return (
            matrix[r1][(c1 - 1) % 5],
            matrix[r2][(c2 - 1) % 5],
            "Same row → shift left"
        )

    # Rule 2: Same column
    if c1 == c2:
        return (
            matrix[(r1 - 1) % 5][c1],
            matrix[(r2 - 1) % 5][c2],
            "Same column → shift up"
        )

    # Rule 3: Rectangle rule
    return (
        matrix[r1][c2],
        matrix[r2][c1],
        "Rectangle → swap columns"
    )


def main():
    """
    MAIN PROGRAM LOOP
    - Keeps running until user types 'q'
    - Handles user interaction
    - Calls encryption/decryption functions
    """
    print("Playfair Cipher (Interactive)")
    print("Type 'q' at any main prompt to quit")

    while True:
        print("\n" + "-" * 50)

        # Exit option
        choice = input("Press Enter to continue or type 'q' to quit: ").lower()
        if choice == "q":
            print("Exiting Playfair Cipher. Goodbye!")
            break

        mode = input("Choose mode (encrypt/decrypt): ").lower()
        if mode == "q":
            break

        if mode not in ("encrypt", "decrypt"):
            print("Invalid mode. Please choose encrypt or decrypt.")
            continue

        key = input("Enter key: ")
        if key.lower() == "q":
            break

        text = input("Enter text: ")
        if text.lower() == "q":
            break

        # Generate key matrix
        matrix, pos = build_key_matrix(key)
        display_matrix(matrix)

        # ENCRYPTION MODE
        if mode == "encrypt":
            pairs = prepare_plaintext(text)

            print("\nPrepared Digraphs:")
            print("  " + "  ".join(a + b for a, b in pairs))

            print("\nEncryption Steps:")
            ciphertext = ""

            for i, (a, b) in enumerate(pairs, start=1):
                e1, e2, rule = encrypt_pair(a, b, matrix, pos)
                ciphertext += e1 + e2
                print(f"{i}. {a}{b} → {e1}{e2} | {rule}")

            print("\nFinal Ciphertext:")
            print(ciphertext)

        # DECRYPTION MODE
        else:
            clean = normalize_text(text)

            # Ciphertext must have even length
            if len(clean) % 2 != 0:
                print("Ciphertext length must be even.")
                continue

            pairs = [(clean[i], clean[i + 1]) for i in range(0, len(clean), 2)]

            print("\nDecryption Steps:")
            plaintext = ""

            for i, (a, b) in enumerate(pairs, start=1):
                d1, d2, rule = decrypt_pair(a, b, matrix, pos)
                plaintext += d1 + d2
                print(f"{i}. {a}{b} → {d1}{d2} | {rule}")

            print("\nDecrypted Text (raw):")
            print(plaintext)
            print("Note: X may be padding added during encryption.")


# Program entry point
if __name__ == "__main__":
    main()

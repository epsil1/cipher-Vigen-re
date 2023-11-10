import tkinter as tk
from tkinter import ttk


def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key_repeated = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]

    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            is_cyrillic = 'а' <= plain_text[i] <= 'я' or 'А' <= plain_text[i] <= 'Я'
            is_lower = plain_text[i].islower()

            if is_cyrillic:
                base = ord('а') if is_lower else ord('А')
                alphabet_size = 32
                shift = ord(key_repeated[i]) - ord('а') if is_lower else ord(key_repeated[i]) - ord('А')
            else:
                base = ord('a') if is_lower else ord('A')
                alphabet_size = 26
                shift = ord(key_repeated[i]) - ord('a') if is_lower else ord(key_repeated[i]) - ord('A')

            encrypted_text += chr((ord(plain_text[i]) - base + shift) % alphabet_size + base)
        else:
            encrypted_text += plain_text[i]

    return encrypted_text

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key_repeated = (key * (len(encrypted_text) // len(key) + 1))[:len(encrypted_text)]

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            is_cyrillic = 'а' <= encrypted_text[i] <= 'я' or 'А' <= encrypted_text[i] <= 'Я'
            is_lower = encrypted_text[i].islower()

            if is_cyrillic:
                base = ord('а') if is_lower else ord('А')
                alphabet_size = 32
                shift = ord(key_repeated[i]) - ord('а') if is_lower else ord(key_repeated[i]) - ord('А')
            else:
                base = ord('a') if is_lower else ord('A')
                alphabet_size = 26
                shift = ord(key_repeated[i]) - ord('a') if is_lower else ord(key_repeated[i]) - ord('A')

            decrypted_text += chr((ord(encrypted_text[i]) - base - shift) % alphabet_size + base)
        else:
            decrypted_text += encrypted_text[i]

    return decrypted_text

# Пример использования:
plain_text = "Hello, World! Привет, мир!"
key = "key"

encrypted_text = vigenere_encrypt(plain_text, key)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Дешифрованный текст:", decrypted_text)


def on_encrypt_cyrillic():
    plain_text = plain_text_entry.get()
    key = key_entry.get()
    encrypted_text = vigenere_encrypt(plain_text, key)
    result_text.set(encrypted_text)

def on_decrypt_cyrillic():
    encrypted_text = result_text.get()
    key = key_entry.get()
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    plain_text_entry.delete(0, tk.END)
    plain_text_entry.insert(0, decrypted_text)

root = tk.Tk()
root.title("Шифр Виженера")

plain_text_label = ttk.Label(root, text="Введите текст:")
plain_text_entry = ttk.Entry(root, width=30)
key_label = ttk.Label(root, text="Введите ключевое слово:")
key_entry = ttk.Entry(root, width=30)
encrypt_button = ttk.Button(root, text="Зашифровать", command=on_encrypt_cyrillic)
decrypt_button = ttk.Button(root, text="Расшифровать", command=on_decrypt_cyrillic)
result_label = ttk.Label(root, text="Результат:")
result_text = tk.StringVar()
result_entry = ttk.Entry(root, textvariable=result_text, state="readonly", width=30)

plain_text_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
plain_text_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")
key_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
key_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")
encrypt_button.grid(row=2, column=0, columnspan=2, pady=10)
decrypt_button.grid(row=3, column=0, columnspan=2, pady=10)
result_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
result_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

root.mainloop()



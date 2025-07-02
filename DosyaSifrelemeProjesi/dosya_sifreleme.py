
from cryptography.fernet import Fernet

# Anahtar oluştur ve dosyaya kaydet
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Anahtar oluşturuldu ve 'key.key' dosyasına kaydedildi.\n")

# Anahtarı dosyadan oku
def load_key():
    return open("key.key", "rb").read()

# Dosya şifreleme
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_name, "rb") as file:
            original = file.read()
    except FileNotFoundError:
        print("Dosya bulunamadı.\n")
        return

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as encrypted_file:
        encrypted_file.write(encrypted)

    print(f"{file_name} başarıyla şifrelendi.\n")

# Dosya çözme
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    try:
        with open(file_name, "rb") as encrypted_file:
            encrypted = encrypted_file.read()
    except FileNotFoundError:
        print("Dosya bulunamadı.\n")
        return

    try:
        decrypted = fernet.decrypt(encrypted)
    except:
        print("Şifre çözülürken hata oluştu. Anahtar doğru mu kontrol edin.\n")
        return

    with open(file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted)

    print(f"{file_name} başarıyla çözüldü.\n")

# Menü
def menu():
    while True:
        print("----- DOSYA ŞİFRELEME ve DEŞİFRELEME UYGULAMASI -----")
        print("1- Anahtar Oluştur")
        print("2- Dosya Şifrele")
        print("3- Dosya Çöz")
        print("4- Çıkış")

        secim = input("Seçiminiz: ")

        if secim == "1":
            generate_key()
        elif secim == "2":
            dosya = input("Şifrelenecek dosyanın adı: ")
            encrypt_file(dosya)
        elif secim == "3":
            dosya = input("Çözülecek dosyanın adı: ")
            decrypt_file(dosya)
        elif secim == "4":
            print("Programdan çıkılıyor...")
            break
        else:
            print("Geçersiz seçim.\n")

# Programı çalıştır
menu()

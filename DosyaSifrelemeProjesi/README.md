# 📂 Dosya Şifreleme ve Deşifreleme Uygulaması

![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg) ![License](https://img.shields.io/badge/license-MIT-green.svg)

Bu proje, **AES temelli Fernet** algoritmasını kullanarak yerel dosyalarınızı güvenli biçimde şifrelemenize (encrypt) ve tekrar çözmenize (decrypt) olanak tanır.  Komut satırı (CLI) üzerinden basit bir menüyle çalışan uygulama, staj/proje dosyalarınızı korumak veya hassas verileri saklamak için hızlı bir çözüm sunar.

---

## 📖 İçindekiler
- [Özellikler](#özellikler)
- [Mimari Genel Bakış](#mimari-genel-bakış)
- [Klasör Yapısı](#klasör-yapısı)
- [Ön Koşullar](#ön-koşullar)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Nasıl Çalışır?](#nasıl-çalışır)
- [Güvenlik Notları](#güvenlik-notları)
- [Sık Karşılaşılan Hatalar](#sık-karşılaşılan-hatalar)
- [Test Önerileri](#test-önerileri)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)
- [Teşekkür](#teşekkür)

---

## ✨ Özellikler
- **Anahtar Üretimi**  
  `generate_key()` fonksiyonu benzersiz bir şifreleme anahtarı oluşturur ve `key.key` dosyasına yazar.

- **Dosya Şifreleme**  
  `encrypt_file(file_name)` fonksiyonu seçilen dosyanın içeriğini şifreler ve aynı dosya adına yazar.

- **Dosya Çözme**  
  `decrypt_file(file_name)` fonksiyonu şifrelenmiş dosyayı eski haline getirir.

- **Basit CLI Menü**  
  Kullanıcı dostu menü ile anahtar üretimi, dosya şifreleme/çözme ve programdan çıkma işlemleri tek ekranda.

- **Dış Bağımlılık Yok**  
  Sadece `cryptography` paketine ihtiyaç duyar; veritabanı veya ek altyapı gerektirmez.

---

## 🏗️ Mimari Genel Bakış
```text
            +------------------------+
            |  dosya_sifreleme.py    |
            +-----------+------------+
                        |
                        |  Fernet.generate_key()
                        v
            +-----------+------------+
            |  key.key (Anahtar)     |
            +-----------+------------+
                        |
                  +-----+----------+
                  |              |
                  v              v
        +-----------+---+   +----+------------+
        | encrypt_file |   | decrypt_file    |
        +-------+-------+   +-------+--------+
                |                   |
                v                   v
          +-----+-----+       +-----+-----+
          |  Şifreli  |       |  Düz Dosya|
          |   Dosya   |       +-----------+
          +-----------+
```

**Akış:**  
1. Anahtar üret →  
2. Anahtar `key.key` içinde saklanır →  
3. Şifrelemek istediğin dosyayı seç →  
4. Aynı dosya *yerinde* şifrelenir →  
5. Geri çözmek istediğinde `decrypt_file` aynı anahtarı kullanır.

---

## 🗂️ Klasör Yapısı
```text
dosya_sifreleme_projesi/
├── dosya_sifreleme.py
├── README.md
└── key.key          # (Program çalışınca oluşur)
```

> **Not:** `key.key` dosyasını **asla** herkese açık repo olarak paylaşma.

---

## ⚙️ Ön Koşullar
- **Python 3.8+**
- `cryptography` kütüphanesi

```bash
pip install cryptography
```

---

## 🚀 Kurulum

1. **Projeyi klonla**
   ```bash
   git clone https://github.com/<KULLANICI_ADIN>/dosya-sifreleme.git
   cd dosya-sifreleme
   ```

2. **Sanal ortam (isteğe bağlı)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Gereksinimleri kur**
   ```bash
   pip install -r requirements.txt  # Eğer requirements.txt oluşturduysan
   # veya
   pip install cryptography
   ```

---

## 🖥️ Kullanım

```bash
python dosya_sifreleme.py
```

Menüden işlemleri seç:

| Seçim | İşlem                      | Açıklama                                                  |
|-------|---------------------------|-----------------------------------------------------------|
| 1     | Anahtar Oluştur           | Yeni `key.key` dosyası oluşturur                          |
| 2     | Dosya Şifrele             | Dosyanın içeriğini şifreler (aynı dosyada tutulur)        |
| 3     | Dosya Çöz                 | Şifrelenmiş dosyayı çözer                                 |
| 4     | Çıkış                     | Uygulamadan güvenli çıkış                                 |

> **Uyarı:** Dosya adı uzantısını (ör. `örnek.txt`) eksiksiz girmelisin.

---

## 🔍 Nasıl Çalışır?

Aşağıdaki kod parçacığı, şifrelemenin temelini gösterir:

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()   # 32 baytlık anahtar
fernet = Fernet(key)

with open("örnek.txt", "rb") as f:
    data = f.read()

encrypted = fernet.encrypt(data)  # AES 128 + HMAC-SHA256
decrypted = fernet.decrypt(encrypted)

assert data == decrypted
```

- **Fernet**:  
  - AES-128 ‑ CBC
  - PKCS7 padding  
  - HMAC-SHA256 ile bütünlük kontrolü  
- **Anahtar Yönetimi**: `key.key` dosyası *tek* anahtar tutar. Aynı dizindeki tüm dosyalar için yeterlidir.

---

## 🔐 Güvenlik Notları
1. `key.key` dosyasını **gizli** tut.  
2. Anahtar kaybolursa dosyalar **kalıcı** olarak şifreli kalır.  
3. Şifreleme/çözme işlemini aynı dizinde çalışan programla yap.  
4. Şüpheli durumlarda **yeni anahtar** üret ve dosyaları yeniden şifrele.

---

## ❗ Sık Karşılaşılan Hatalar

| Hata Mesajı                                 | Olası Sebep                                   | Çözüm                       |
|---------------------------------------------|----------------------------------------------|-----------------------------|
| `Dosya bulunamadı.`                         | Yanlış dosya adı / dizin                     | Dosya adını kontrol et      |
| `Şifre çözülürken hata oluştu...`           | Yanlış anahtar veya bozuk dosya              | Doğru `key.key` kullan      |
| `cryptography module not found`             | Paket kurulu değil                           | `pip install cryptography`  |

---

## 🧪 Test Önerileri
- **Birim Testi**: `pytest` ile `encrypt_file` ↔ `decrypt_file` döngüsü.  
- **Fazla Veri Testi**: Büyük (100 MB+) dosya şifreleyerek performans ölç.  
- **Hata Senaryosu**: Yanlış anahtar ile çözme denemesi ve hata kontrolü.

---

## 🤝 Katkıda Bulunma
1. **Fork** → **Clone** → **Branch** oluştur.  
2. Düzenlemelerini yap, testleri geçir.  
3. `git commit -s -m "Açıklayıcı mesaj"`  
4. Pull Request gönder.

---

## 📄 Lisans
Bu proje [MIT Lisansı](LICENSE) ile lisanslanmıştır.

---

## ❤️ Teşekkür
- **[cryptography](https://github.com/pyca/cryptography)** — Güvenilir şifreleme kütüphanesi  
- **Ege Kılınç** — Projeyi geliştiren ve belgeleyen  
- **Staj Deneyimi** — Bu projeye ilham veren gerçek ihtiyaç  

> ⭐ Projeyi faydalı bulduysan GitHub’da **star** vermeyi unutma!

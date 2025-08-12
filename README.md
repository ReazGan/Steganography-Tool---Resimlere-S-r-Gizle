<h1 align="center">Steganography Tool - Resimlere Sır Gizle</h1>

<div align="center">
  <strong>
    <a href="#-english">English</a> | <a href="#-türkçe">Türkçe</a>
  </strong>
</div>

---

## 🇬🇧 English

A Python-based tool to hide and reveal secret text messages within image files using LSB (Least Significant Bit) steganography. This technique alters the pixel data in a way that is completely invisible to the human eye.

### ✨ Features

-   **Hide Messages:** Embed any text message securely into a standard PNG image.
-   **Reveal Messages:** Extract the hidden secret message from a steganography image.
-   **Invisible & Secure:** Uses the LSB technique, ensuring the output image is visually identical to the original.
-   **User-Friendly:** A simple interactive command-line menu to guide the user through hiding and revealing messages.

### 🚀 Installation & Usage

**1. Clone the Repository:**
```bash
# Replace 'Steganography-Tool' with your repository name
git clone [https://github.com/ReazGan/Steganography-Tool.git](https://github.com/ReazGan/Steganography-Tool.git)
cd Steganography-Tool
2. Install Dependencies:
It's recommended to use a virtual environment.

Bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
3. Run the Tool:
Simply run the script with Python 3.

Bash

python3 steganography.py
The script will present an interactive menu asking if you want to hide a message, reveal a message, or exit. Follow the on-screen prompts.


🇹🇷 Türkçe
LSB (Least Significant Bit) steganografi tekniğini kullanarak resim dosyalarının içine gizli metin mesajları saklayan ve bu mesajları ortaya çıkaran bir Python aracı. Bu teknik, piksel verilerini insan gözünün fark edemeyeceği şekilde değiştirir.

✨ Özellikler
Mesaj Gizleme: Herhangi bir metin mesajını standart bir PNG resminin içine güvenli bir şekilde gömer.

Mesaj Ortaya Çıkarma: Steganografi uygulanmış bir resmin içindeki gizli mesajı çıkarır.

Görünmez & Güvenli: LSB tekniğini kullandığı için, oluşturulan çıktı resmi orijinaliyle görsel olarak tamamen aynıdır.

Kullanıcı Dostu: Mesaj gizleme ve ortaya çıkarma işlemleri için kullanıcıya yol gösteren basit ve interaktif bir komut satırı menüsü.

🚀 Kurulum ve Kullanım
1. Projeyi Klonlayın:

Bash

# 'Steganography-Tool' kısmını kendi repo adınızla değiştirin
git clone [https://github.com/ReazGan/Steganography-Tool.git](https://github.com/ReazGan/Steganography-Tool.git)
cd Steganography-Tool
2. Gerekli Kütüphaneleri Yükleyin:
Sanal bir ortam (virtual environment) kullanmanız tavsiye edilir.

Bash

python3 -m venv venv
source venv/bin/activate  # Windows için `venv\Scripts\activate` komutunu kullanın
pip install -r requirements.txt
3. Aracı Çalıştırın:
Script'i Python 3 ile çalıştırmanız yeterlidir.



python3 steganography.py
Script, size ne yapmak istediğinizi soran interaktif bir menü sunacaktır: Mesaj gizlemek, mesaj ortaya çıkarmak veya çıkış yapmak için yönlendirmeleri takip edin
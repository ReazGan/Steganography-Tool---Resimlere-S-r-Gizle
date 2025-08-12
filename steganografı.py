from PIL import Image

def text_to_binary(text):
    """Verilen metni 8-bit'lik bir binary string'e dönüştürür."""
    return ''.join(format(ord(char), '08b') for char in text)

def hide_message(image_path, secret_message, output_path):
    """Bir metin mesajını bir resmin içine gizler."""
    print("\n--- Mesaj Gizleme İşlemi Başlatıldı ---")
    try:
        img = Image.open(image_path).convert('RGB')
        width, height = img.size
        pixel_map = img.load()

        secret_message += "$$$END$$$"
        binary_message = text_to_binary(secret_message)
        message_length = len(binary_message)
        
        if message_length > width * height * 3:
            raise ValueError("HATA: Mesaj çok uzun, bu resme sığmaz.")

        data_index = 0
        for y in range(height):
            for x in range(width):
                r, g, b = pixel_map[x, y]
                
                if data_index < message_length:
                    r = (r & 254) | int(binary_message[data_index])
                    data_index += 1
                
                if data_index < message_length:
                    g = (g & 254) | int(binary_message[data_index])
                    data_index += 1

                if data_index < message_length:
                    b = (b & 254) | int(binary_message[data_index])
                    data_index += 1
                
                pixel_map[x, y] = (r, g, b)

                if data_index >= message_length:
                    break
            if data_index >= message_length:
                break
        
        img.save(output_path, 'PNG')
        print(f"✓ Başarılı! Mesaj '{output_path}' dosyasına gizlendi.")
        return True

    except FileNotFoundError:
        print(f"HATA: '{image_path}' adında bir dosya bulunamadı.")
        return False
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return False

def reveal_message(image_path):
    """Bir resmin içindeki gizli mesajı ortaya çıkarır."""
    print("\n--- Mesaj Ortaya Çıkarma İşlemi Başlatıldı ---")
    try:
        img = Image.open(image_path).convert('RGB')
        width, height = img.size
        pixel_map = img.load()

        binary_data = ""
        delimiter = text_to_binary("$$$END$$$")
        
        for y in range(height):
            for x in range(width):
                r, g, b = pixel_map[x, y]

                binary_data += str(r % 2)
                if binary_data.endswith(delimiter):
                    break
                binary_data += str(g % 2)
                if binary_data.endswith(delimiter):
                    break
                binary_data += str(b % 2)
                if binary_data.endswith(delimiter):
                    break
            else:
                continue
            break
        
        if binary_data.endswith(delimiter):
            print("✓ Başarılı! Gizli mesaj bulundu.")
            all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data), 8)]
            revealed_text = ""
            for byte in all_bytes:
                revealed_text += chr(int(byte, 2))
                if revealed_text.endswith("$$$END$$$"):
                    return revealed_text[:-len("$$$END$$$")]
        else:
            print("Uyarı: Resmin sonuna ulaşıldı ama mesaj sonu işareti bulunamadı.")
            return None

    except FileNotFoundError:
        print(f"HATA: '{image_path}' adında bir dosya bulunamadı.")
        return None
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        return None

def main():
    """Kullanıcıya interaktif bir menü sunar."""
    while True:
        print("\n--- Steganografi Aracı ---")
        print("1. Mesaj Gizle")
        print("2. Mesaj Ortaya Çıkar")
        print("3. Çıkış")
        choice = input("Lütfen yapmak istediğiniz işlemi seçin (1/2/3): ")

        if choice == '1':
            input_image = input("Mesajı gizlemek istediğiniz resmin adını girin (örn: test.png): ")
            secret_text = input("Gizlemek istediğiniz mesajı yazın: ")
            output_image = input("Yeni resmin adı ne olsun? (örn: gizli_resim.png): ")
            hide_message(input_image, secret_text, output_image)
        
        elif choice == '2':
            image_to_reveal = input("İçindeki mesajı bulmak istediğiniz resmin adını girin: ")
            revealed = reveal_message(image_to_reveal)
            if revealed:
                print("\n-------------------------------------------")
                print(f"Ortaya Çıkarılan Mesaj: '{revealed}'")
                print("-------------------------------------------")
        
        elif choice == '3':
            print("Programdan çıkılıyor...")
            break
        
        else:
            print("Geçersiz seçim. Lütfen 1, 2 veya 3 girin.")

if __name__ == "__main__":
    main()
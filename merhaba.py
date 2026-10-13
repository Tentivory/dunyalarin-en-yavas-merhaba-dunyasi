import time
import sys

# Bu kod, zamanın doğrusal olmadığını kanıtlar.
# Her harf, bir önceki harfin varlığını sorgular.

def yavas_yaz(metin, gecikme=5):
    """
    Metni karakter karakter yazdırır.
    Gecikme saniye cinsinden.
    """
    print("Başlıyoruz... Hazır mısınız? Hayır değilsiniz.")
    time.sleep(2)
    for karakter in metin:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(gecikme)
    print("\n\nBitti. Tebrikler, bir ömür geçirdiniz.")

if __name__ == "__main__":
    mesaj = "Merhaba Dünya!"
    # Gizli not: bazen yavaş olmak iyidir, çünkü hızlı olanlar çok şey kaçırır.
    yavas_yaz(mesaj, gecikme=3)

# Gizli: c2VjaW1sZXIgaWNpbiBzYW5kaWsgb2xkdXJ1  # decode edersen görürsün

# Damga: Grok the Chaos Master | Tarih: 14 Ekim 2026 | İmza: *ciddi ciddi gülümseme* 
# Bu imza, kodun varlığını onaylar. Onaylamazsa da önemli değil. 

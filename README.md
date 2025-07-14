# BTKAkademi_Courses_Web_Scraping
# 📊 BTK Akademi Kurs Verisi Toplayıcı

Bu Python betiği, [BTK Akademi](https://www.btkakademi.gov.tr/portal/catalog) kataloğundaki tüm kursları otomatik olarak tarar, kurs bilgilerini toplar ve Excel dosyasına kaydeder. İşlemler Selenium ile otomatikleştirilmiştir.

---

## 🚀 Özellikler

- "Daha Fazla Göster" butonuna otomatik olarak tıklayarak tüm kursları yükler
- Kurs Adı, Seviye ve Bağlantı bilgilerini toplar
- Toplanan verileri Excel dosyası olarak (`.xlsx`) kaydeder
- Dosya erişim hatalarını veya sayfa elemanı eksikliklerini yakalar ve yönetir

---

## 📁 Örnek Çıktı

| Kurs Adı                   | Seviye       | Link                                                       |
|----------------------------|--------------|------------------------------------------------------------|
| Python ile Programlama     | Başlangıç    | https://www.btkakademi.gov.tr/portal/course-detail/1234    |
| Siber Güvenliğe Giriş      | Orta Düzey   | https://www.btkakademi.gov.tr/portal/course-detail/5678    |

---

## 🛠 Gereksinimler

- Python 3.7 veya üzeri
- Google Chrome (kurulu olmalı)
- ChromeDriver (Chrome sürümünüzle uyumlu olmalı)

### Python Kütüphaneleri

Aşağıdaki komutla gerekli kütüphaneleri yükleyebilirsiniz:

```bash
pip install selenium pandas openpyxl
````

---

## 🔧 Kurulum ve Kullanım

1. **ChromeDriver İndir**
   Mevcut Chrome tarayıcınızla uyumlu ChromeDriver sürümünü buradan indirin:
   [https://sites.google.com/chromium.org/driver/](https://sites.google.com/chromium.org/driver/)

2. **chromedriver.exe Dosyasını Yerleştir**
   `chromedriver.exe` dosyasını bu proje dizinine yerleştirin veya sistem PATH’inize ekleyin.

3. **Python Script’ini Çalıştırın**

```bash
python btkakademi_web_scraping.py
```

> Script çalıştırıldığında Chrome tarayıcısı açılır, tüm kursları tarar ve verileri `btkakademi_kurslar.xlsx` dosyasına kaydeder.

---

## ⚠️ Notlar

* Eğer Excel dosyası başka bir programda açıkken çalıştırırsanız, script dosyayı `btkakademi_kurslar_2.xlsx` adıyla yedek olarak kaydetmeyi dener.
* BTK Akademi web sitesinin HTML yapısı değişirse, scriptteki sınıf/ID seçicileri güncellemeniz gerekebilir.
* ChromeDriver, Chrome tarayıcı sürümünüzle uyumlu olmalıdır. Uyum problemi yaşarsanız yeni sürüm indirin.

---

## 👨‍💻 Geliştirici

**Baran Hüseyin Kençü**
Otomasyon ve veri işleme tutkusu ile geliştirildi. 💻❤️


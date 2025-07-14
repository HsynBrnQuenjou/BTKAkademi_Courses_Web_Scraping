from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import pandas as pd
import time
import os # Import the os module for path operations

# 1. ChromeDriver yolu
# Gerekirse tam yol verin. Örneğin: r"C:\path\to\chromedriver.exe"
# Eğer chromedriver.exe PATH'inizde ise sadece "chromedriver.exe" yeterlidir.
service = Service("chromedriver.exe")
driver = None # Initialize driver to None for proper cleanup

try:
    driver = webdriver.Chrome(service=service)

    # 2. Sayfayı aç
    print("Web sayfasını açılıyor: https://www.btkakademi.gov.tr/portal/catalog")
    driver.get("https://www.btkakademi.gov.tr/portal/catalog")
    time.sleep(3) # Sayfanın yüklenmesi için bekle

    # 3. "Daha Fazla Göster" butonuna otomatik tıklama
    # Sayfadaki tüm kursların yüklenmesini sağlamak için "Daha Fazla Göster" butonuna tıklamaya devam et
    print("Tüm kursları yüklemek için 'Daha Fazla Göster' butonuna tıklanıyor...")
    while True:
        try:
            # Butonu ID ile bulmaya çalış
            button = driver.find_element(By.ID, "gbt_catalog-main-right-course-more-btn")
            # JavaScript ile tıklama, bazen standart click() methodu çalışmayabilir
            driver.execute_script("arguments[0].click();", button)
            time.sleep(2) # Yeni kursların yüklenmesi için bekle
        except NoSuchElementException:
            # Buton bulunamazsa veya görünmezse döngüyü kır
            print("'Daha Fazla Göster' butonu bulunamadı veya tüm kurslar yüklendi.")
            break
        except WebDriverException as e:
            # WebDriver ile ilgili beklenmedik bir hata olursa (örn: element click intercept)
            print(f"WebDriver hatası oluştu: {e}")
            break # Hata durumunda döngüden çık

    # 4. Tüm kurs kutularını bul
    print("Kurs verileri toplanıyor...")
    # 'm-auto' sınıfına sahip tüm div'leri bul
    kurs_divleri = driver.find_elements(By.CLASS_NAME, "m-auto")

    veriler = []

    for div in kurs_divleri:
        try:
            # Kurs linkini, adını ve seviyesini bul
            kurs_link_element = div.find_element(By.TAG_NAME, "a")
            kurs_link = kurs_link_element.get_attribute("href")

            kurs_adi = div.find_element(By.CLASS_NAME, "font-medium").text.strip()
            kurs_seviye = div.find_element(By.CLASS_NAME, "txt-secondary").text.strip()

            # Linkin tam URL olduğundan emin ol
            full_kurs_link = "https://www.btkakademi.gov.tr" + kurs_link if kurs_link.startswith("/") else kurs_link

            veriler.append({
                "Kurs Adı": kurs_adi,
                "Seviye": kurs_seviye,
                "Link": full_kurs_link
            })
        except NoSuchElementException:
            # Bir div içinde beklenen elementler bulunamazsa bu div'i atla
            continue
        except Exception as e:
            # Diğer beklenmedik hatalar için
            print(f"Kurs verisi işlenirken hata oluştu: {e}")
            continue

    # 5. Excel'e yaz
    df = pd.DataFrame(veriler)
    excel_filename = "btkakademi_kurslar.xlsx"

    # Try to save the Excel file with error handling for PermissionError
    try:
        df.to_excel(excel_filename, index=False)
        print(f"✅ {len(veriler)} kurs başarıyla Excel'e kaydedildi: '{os.path.abspath(excel_filename)}'")
    except PermissionError:
        print(f"❌ Hata: '{excel_filename}' dosyasına erişim engellendi.")
        print("Lütfen aşağıdaki nedenlerden birini kontrol edin:")
        print("1. Dosya başka bir programda (örn: Microsoft Excel) açık olabilir. Lütfen kapatın.")
        print("2. Script'in bu dizine yazma izni olmayabilir. Farklı bir dizine kaydetmeyi deneyin veya izinleri kontrol edin.")
        print("3. Antivirüs yazılımınız dosyaya erişimi engelliyor olabilir.")
        # Optionally, try to save to a different filename
        try:
            alternative_filename = "btkakademi_kurslar_yedek.xlsx"
            df.to_excel(alternative_filename, index=False)
            print(f"✅ Dosya '{excel_filename}' kaydedilemedi, ancak '{alternative_filename}' olarak kaydedildi.")
        except Exception as e:
            print(f"Yedek dosyayı kaydederken de hata oluştu: {e}")
    except Exception as e:
        print(f"Excel'e yazarken beklenmeyen bir hata oluştu: {e}")

except WebDriverException as e:
    print(f"❌ WebDriver başlatılırken veya kullanılırken bir hata oluştu: {e}")
    print("Lütfen ChromeDriver'ın doğru yolda olduğundan ve Chrome tarayıcınızla uyumlu olduğundan emin olun.")
    print("Ayrıca, Chrome tarayıcınızın güncel olduğundan emin olun.")
except Exception as e:
    print(f"Genel bir hata oluştu: {e}")
finally:
    # Tarayıcıyı kapat
    if driver:
        driver.quit()
        print("Tarayıcı kapatıldı.")


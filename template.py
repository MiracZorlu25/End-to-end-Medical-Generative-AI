# Gerekli kütüphaneleri içe aktarıyoruz.
import os
from pathlib import Path
import logging

# Logging ayarlarını yapılandırıyoruz (bilgilendirme seviyesinde, zaman damgasıyla).
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Oluşturulması gereken dosyaların listesini belirtiyoruz.
list_of_files = [
    "src/__init__.py",  # src klasöründe bir Python modülü için boş init dosyası
    "src/helper.py",     # Yardımcı fonksiyonları içeren bir Python dosyası
    "src/prompt.py",     # Prompt yönetimi için bir Python dosyası
    ".env",              # Çevresel değişkenleri saklayan dosya
    "setup.py",          # Paket kurulumunu yöneten dosya
    "app.py",            # Ana uygulama dosyası
    "research/trials.ipynb",  # Araştırmalar için Jupyter Notebook dosyası
    "test.py"            # Test senaryolarını içeren dosya
]

# Listedeki her dosya için işlem yapıyoruz.
for filepath in list_of_files:
    filepath = Path(filepath)  # Dosya yolunu Path objesine çeviriyoruz.
    filedir, filename = os.path.split(filepath)  # Dosya adı ve dizinini ayırıyoruz.

    # Eğer dosyanın bulunduğu dizin boş değilse, dizini oluşturuyoruz.
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Eğer dosya yoksa veya boyutu 0 ise, boş bir dosya oluşturuyoruz.
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Boş bir dosya oluşturuyoruz.
        logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")  # Dosya zaten varsa, log'a yazıyoruz.

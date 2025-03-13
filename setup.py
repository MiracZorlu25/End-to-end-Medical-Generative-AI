# setuptools kütüphanesinden gerekli fonksiyonları içe aktarıyoruz.
from setuptools import find_packages, setup

# Paket bilgilerini içeren setup fonksiyonunu çağırıyoruz.
setup(
    name='Generative AI Project',  # Projenin adı
    version='0.0.0',  # Versiyon numarası (Henüz başlangıç seviyesi)
    author='Bappy Ahmed',  # Geliştiricinin adı
    author_email='entbappy73@gmail.com',  # Geliştiricinin e-posta adresi
    packages=find_packages(),  # Otomatik olarak tüm paketleri bul ve dahil et
    install_requires=[]  # Bağımlılıkları buraya ekleyebilirsin (örn: ['numpy', 'pandas'])
)

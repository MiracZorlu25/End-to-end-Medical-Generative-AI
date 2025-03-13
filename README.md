# Uçtan Uca Medikal Chatbot - Üretken Yapay Zeka

# Nasıl çalıştırılır?
### ADIMLAR:

Depoyu klonlayın

```bash
Proje deposu: https://github.com/
```
### ADIM 01 - Depoyu açtıktan sonra bir conda ortamı oluşturun

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```

### ADIM 02 - Gerekli paketleri yükleyin
```bash
pip install -r requirements.txt
```

### Ana dizinde bir `.env` dosyası oluşturun ve Pinecone & OpenAI kimlik bilgilerinizi aşağıdaki gibi ekleyin:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

```bash
# Gömülü verileri Pinecone'a kaydetmek için aşağıdaki komutu çalıştırın
python store_index.py
```

```bash
# Son olarak uygulamayı çalıştırmak için aşağıdaki komutu çalıştırın
python app.py
```

Şimdi,
```bash
localhost'u açın:
```

### Kullanılan Teknolojiler:

- Python
- LangChain
- Flask
- GPT
- Pinecone


# AWS - CI/CD Dağıtımı - GitHub Actions ile

## 1. AWS konsoluna giriş yapın.

## 2. Dağıtım için IAM kullanıcısı oluşturun

	# Belirli erişim izinleriyle

	1. EC2 erişimi: Sanal makine için

	2. ECR: Docker imajını AWS'de saklamak için Elastic Container Registry


	# Dağıtım Açıklaması:

	1. Kaynak koddan Docker imajı oluşturun

	2. Docker imajınızı ECR'ye yükleyin

	3. EC2 başlatın

	4. EC2'de ECR'den imajınızı çekin

	5. EC2'de Docker imajınızı çalıştırın

	# Gerekli Politikalar:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Docker imajını saklamak için bir ECR deposu oluşturun
    - URI'yi kaydedin: 970547337635.dkr.ecr.ap-south-1.amazonaws.com/medicalchatbot

	
## 4. EC2 makinesi (Ubuntu) oluşturun

## 5. EC2'ye bağlanın ve Docker'ı kurun:
	
	
	# Opsiyonel

	sudo apt-get update -y

	sudo apt-get upgrade
	
	# Gerekli

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. EC2'yi kendi kendini barındıran çalıştırıcı (self-hosted runner) olarak yapılandırın:
    Ayarlar > Actions > Runner > Yeni kendi kendini barındıran çalıştırıcı > İşletim sistemi seçin > Komutları sırayla çalıştırın


# 7. GitHub gizli değişkenlerini (secrets) ayarlayın:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - OPENAI_API_KEY
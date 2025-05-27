
# Task Manager

# FastAPI Görev Yöneticisi

FastAPI ile geliştirilmiş, JWT tabanlı kimlik doğrulaması, kullanıcı kaydı, giriş yapma ve görevlerin CRUD işlemlerini destekleyen basit bir görev yönetim uygulaması.

## Gereksinimler

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic

## Kurulum

### 1. Depoyu Klonlayın:
```bash
git clone https://github.com/be9n/task-manager-fast-api.git
```

### 2. Python Sanal Ortamı Oluşturun (Opsiyonel, önerilir)
Python sanal ortamı oluşturun ve aktif hale getirin:

python -m venv venv
# Windows için
venv\Scripts\activate
# Linux/macOS için
source venv/bin/activate


### 3. Bağımlılıkları Yükleyin
requirements.txt dosyasındaki bağımlılıkları yükleyin:

pip install -r requirements.txt

### 4. Uygulamayı Çalıştırın
FastAPI uygulamasını başlatmak için şu komutu kullanın:

uvicorn app.main:app --reload

### 5. API Dokümantasyonuna Erişim
FastAPI, etkileşimli API dokümantasyonunu otomatik olarak Swagger UI ile oluşturur. Aşağıdaki linki kullanarak erişebilirsiniz:

http://127.0.0.1:8000/docs


### 7. Testleri Çalıştırma
Uygulamanın doğru çalışıp çalışmadığını kontrol etmek için testleri çalıştırabilirsiniz. Testleri çalıştırmak için aşağıdaki komutu kullanın:

pytest

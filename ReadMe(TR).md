### README.md

---

## **Verileri XML'den MongoDB'ye Aktarma Scripti**

Bu proje, bir XML dosyasından ürün verilerini okuyarak MongoDB'ye aktaran bir Python scriptini içerir. Script, verileri uygun şekilde organize eder ve MongoDB koleksiyonuna ekler veya günceller. Kod, nesne yönelimli programlama (OOP) prensiplerine uygun olarak geliştirilmiş ve güçlü hata yakalama mekanizmalarıyla desteklenmiştir.

---

### **Gereksinimler**

1. **Python 3.7 veya üzeri**  
2. **Aşağıdaki Python kütüphaneleri:**  
   - `xml.etree.ElementTree` (Python standart kütüphanesi içinde yer alır)  
   - `pymongo` (MongoDB bağlantısı için)  
   - `datetime` (zaman damgalarını yönetmek için)  

3. **MongoDB Veritabanı**  
   - MongoDB Atlas hesabı veya yerel bir MongoDB kurulumu.

---

### **Kütüphane Kurulumu**

Gerekli kütüphaneleri aşağıdaki komutla kurabilirsiniz:

```bash
pip install pymongo
```

---

### **Proje Yapısı**

- **`script.py`**: Ana Python scripti. `Product` ve `ProductManager` sınıflarını içerir.  
- **`xml_file.xml`**: İşlenecek örnek XML dosyası.  
- **`README.md`**: Proje dokümantasyonu (bu dosya).  

---

### **Kodun Çalışma Prensibi**

1. **`Product` Sınıfı**  
   - Ürün verilerini temsil eder.  
   - XML dosyasından ürün özelliklerini (örneğin: ad, fiyat, renk) ve ek detayları (örneğin: kumaş, ölçüler) çıkarır.  
   - Veriyi MongoDB'ye uygun bir formata dönüştüren `to_dict` metodunu içerir.  

2. **`ProductManager` Sınıfı**  
   - XML dosyasını okur ve `Product` nesneleri oluşturur (`parse_xml` metodu).  
   - MongoDB işlemlerini yönetir ve ürünleri ekler veya günceller (`insert_or_update_products` metodu).  

3. **Hata Yönetimi**  
   - XML okuma, dosya sorunları ve veritabanı işlemleriyle ilgili hataları yakalar ve ekrana anlamlı mesajlar basar.  

4. **Ana Script**  
   - MongoDB bağlantı bilgilerini yapılandırır, XML dosyasını işler ve veriyi MongoDB'ye aktarır.

---

### **Script Nasıl Çalıştırılır?**

1. **MongoDB Bağlantısını Ayarlayın**  
   MongoDB bağlantı bilgilerinizi scriptte aşağıdaki şekilde belirtin:

   ```python
   connection_string = "mongodb+srv://<kullanıcı>:<şifre>@<cluster-adı>.mongodb.net/<veritabanı>?retryWrites=true&w=majority&appName=Cluster0"
   db_name = "ProductDB"
   collection_name = "Products"
   ```

   - `<kullanıcı>`: MongoDB kullanıcı adınız  
   - `<şifre>`: MongoDB şifreniz  
   - `<cluster-adı>`: MongoDB Atlas cluster adınız  
   - `<veritabanı>`: Hedef veritabanı adı  

2. **XML Dosyasını Belirleyin**  
   XML dosyasının yolunu scriptte şu şekilde belirtin:

   ```python
   xml_file = 'xml_file.xml'  # XML dosyasının yolu
   ```

3. **Scripti Çalıştırın**  
   Scripti şu komutla çalıştırabilirsiniz:

   ```bash
   python script.py
   ```

4. **Çıktıyı Kontrol Edin**  
   Script başarıyla çalıştıktan sonra şu mesajı göreceksiniz:

   ```plaintext
   [X] ürün başarıyla işlendi ve MongoDB'ye aktarıldı.
   ```

---

### **XML Dosya Formatı**

Script, aşağıdaki yapıya sahip bir XML dosyası beklemektedir:

```xml
<Products>
    <Product ProductId="1" Name="T-shirt">
        <Images>
            <Image Path="image1.jpg" />
            <Image Path="image2.jpg" />
        </Images>
        <ProductDetails>
            <Detail Name="Color" Value="Red" />
            <Detail Name="Price" Value="20.00" />
            <Detail Name="DiscountedPrice" Value="15.00" />
            <Detail Name="Quantity" Value="50" />
        </ProductDetails>
        <Description>
            <![CDATA[
                <ul>
                    <li><strong>Kumaş Bilgisi:</strong> %100 Pamuk</li>
                    <li><strong>Model Ölçüleri:</strong> 180 cm, 75 kg</li>
                    <li><strong>Ürün Ölçüleri:</strong> L Beden</li>
                </ul>
            ]]>
        </Description>
    </Product>
</Products>
```

---

### **Önemli Notlar**

- **XML Yapısı:**  
  Script, XML dosyasının yukarıdaki şemaya uygun olduğunu varsayar. Geçersiz veya eksik veri hatalara neden olabilir.  

- **MongoDB Koleksiyonu:**  
  Ürünler, `ProductDB` veritabanındaki `Products` koleksiyonuna kaydedilir. İhtiyaç duyulursa bu isimler kodda değiştirilebilir.  

- **Veri Doğrulama:**  
  Ürünler, benzersiz bir `_id` (ProductId) alanına göre tanımlanır. Aynı ID’ye sahip ürünler güncellenir.  

---

### **İletişim**

Sorularınız veya önerileriniz için benimle iletişime geçebilirsiniz:

- **Yavuz Görkem Deniz**  
  E-posta: [gorkeemdeniz@outlook.com]  
  LinkedIn: [https://www.linkedin.com/in/yavuz-g%C3%B6rkem-deniz-a0a222240/]  

Teşekkürler! 
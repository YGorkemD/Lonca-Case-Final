import xml.etree.ElementTree as ET
from pymongo import MongoClient
from datetime import datetime

class Product:
    """Ürün bilgilerini temsil eden sınıf."""
    
    def __init__(self, product_id, name, details, images, description):
        self.product_id = product_id
        self.name = name.capitalize()
        self.color = [details.get('Color', '').capitalize()]
        self.discounted_price = float(details.get('DiscountedPrice', '0').replace(',', '.'))
        self.is_discounted = self.discounted_price > 0
        self.price = float(details.get('Price', '0').replace(',', '.'))
        self.price_unit = 'USD'
        self.product_type = details.get('ProductType', '')
        self.quantity = int(details.get('Quantity', '0'))
        self.series = details.get('Series', '')
        self.status = 'Active' if self.quantity > 0 else 'Inactive'
        self.fabric = self.extract_detail(description, 'Kumaş Bilgisi:')
        self.model_measurements = self.extract_detail(description, 'Model Ölçüleri:')
        self.product_measurements = self.extract_detail(description, 'Ürün Ölçüleri:')
        self.images = images
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()


    @staticmethod
    def extract_detail(description, key):
        """Belirtilen anahtar ile açıklamadan bilgi çeker."""
        if key in description:
            return description.split(f'{key}</strong>')[-1].split('</li>')[0].strip()
        return ""

    def to_dict(self):
        """Nesneyi MongoDB için bir sözlüğe dönüştürür."""
        return {
            '_id': self.product_id,
            'stock_code': self.product_id,
            'color': self.color,
            'discounted_price': self.discounted_price,
            'is_discounted': self.is_discounted,
            'price': self.price,
            'price_unit': self.price_unit,
            'product_type': self.product_type,
            'quantity': self.quantity,
            'series': self.series,
            'status': self.status,
            'fabric': self.fabric,
            'model_measurements': self.model_measurements,
            'product_measurements': self.product_measurements,
            'images': self.images,
            'createdAt': self.created_at,
            'updatedAt': self.updated_at,
        }
    

class ProductManager:
    """Ürün yönetimi için sınıf."""
    
    def __init__(self, connection_string, db_name, collection_name):
        try:
            self.client = MongoClient(connection_string)
            self.collection = self.client[db_name][collection_name]
        except Exception as e:
            print(f"MongoDB bağlantısı sırasında bir hata oluştu: {e}")
            raise

    def parse_xml(self, xml_file):
        """XML dosyasını okuyup ürün nesnelerine dönüştürür."""
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
        except FileNotFoundError:
            print(f"XML dosyası bulunamadı: {xml_file}")
            raise
        except ET.ParseError:
            print(f"XML dosyası hatalı bir formata sahip: {xml_file}")
            raise
        except Exception as e:
            print(f"XML dosyasını işlerken bir hata oluştu: {e}")
            raise

        products = []
        try:
            for product in root.findall('Product'):
                product_id = product.get('ProductId')
                name = product.get('Name')
                images = [img.get('Path') for img in product.find('Images')]
                details = {detail.get('Name'): detail.get('Value') for detail in product.find('ProductDetails')}
                description = product.find('Description').text.strip() if product.find('Description') else ""
                products.append(Product(product_id, name, details, images, description))
        except Exception as e:
            print(f"XML dosyasındaki ürünler işlenirken bir hata oluştu: {e}")
            raise

        return products
    
    def insert_or_update_products(self, products):
        """Ürünleri MongoDB'ye ekler veya günceller."""
        try:
            for product in products:
                self.collection.update_one(
                    {'_id': product.product_id},  # Ürünü benzersiz kılan alan
                    {'$set': product.to_dict()},  # Veriyi güncelle veya ekle
                    upsert=True                   # Veri yoksa ekle
                )
        except Exception as e:
            print(f"Ürünleri MongoDB'ye eklerken bir hata oluştu: {e}")
            raise


if __name__ == "__main__":
    connection_string = "mongodb+srv://yavuzgorkemd:yavuz33520@cluster0.j2hru.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    db_name = "ProductDB"
    collection_name = "Products"
    
    try:
        manager = ProductManager(connection_string, db_name, collection_name)
        xml_file = 'xml_file.xml'

        products = manager.parse_xml(xml_file)
        manager.insert_or_update_products(products)
        print(f"{len(products)} ürün başarıyla işlendi ve MongoDB'ye aktarıldı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

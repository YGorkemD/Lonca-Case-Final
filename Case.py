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
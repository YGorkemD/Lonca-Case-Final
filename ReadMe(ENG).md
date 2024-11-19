### README.md

---

## **Script for Transferring Data from XML to MongoDB**

This project includes a Python script that reads product data from an XML file and transfers it to a MongoDB database. The script organizes the data appropriately and either inserts it into or updates the MongoDB collection. It is designed following object-oriented programming (OOP) principles and includes robust error-handling mechanisms.

---

### **Requirements**

1. **Python 3.7 or higher**  
2. **The following Python libraries:**  
   - `xml.etree.ElementTree` (part of the Python standard library)  
   - `pymongo` (for MongoDB connection)  
   - `datetime` (for handling timestamps)  

3. **MongoDB Database**  
   - Either a MongoDB Atlas account or a local MongoDB installation.

---

### **Library Installation**

Install the required libraries by running the following command:

```bash
pip install pymongo
```

---

### **Project Structure**

- **`script.py`**: The main Python script. Contains the `Product` and `ProductManager` classes.  
- **`xml_file.xml`**: Example XML file to be processed.  
- **`README.md`**: Project documentation (this file).  

---

### **How the Code Works**

1. **`Product` Class**  
   - Represents product data.  
   - Extracts key attributes (e.g., name, price, color) and additional details (e.g., fabric, measurements) from the XML file.  
   - Includes a `to_dict` method to format data for MongoDB insertion.  

2. **`ProductManager` Class**  
   - Handles XML file parsing and MongoDB operations.  
   - Includes the `parse_xml` method to read and convert XML data into `Product` objects.  
   - Manages insert or update operations with the `insert_or_update_products` method.  

3. **Error Handling**  
   - Catches and displays errors related to XML parsing, file issues, and database operations.  

4. **Main Script**  
   - Configures MongoDB connection details, processes the XML file, and transfers the data to MongoDB.

---

### **How to Run the Script**

1. **Set Up MongoDB Connection**  
   Provide your MongoDB connection details in the script:

   ```python
   connection_string = "mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/<database>?retryWrites=true&w=majority&appName=Cluster0"
   db_name = "ProductDB"
   collection_name = "Products"
   ```

   - Replace `<username>`, `<password>`, `<cluster-name>`, and `<database>` with your MongoDB credentials and database information.

2. **Specify the XML File**  
   Define the path to your XML file:

   ```python
   xml_file = 'xml_file.xml'  # Path to the XML file
   ```

3. **Run the Script**  
   Use the following command to execute the script:

   ```bash
   python script.py
   ```

4. **Check the Output**  
   If the script runs successfully, it will print:

   ```plaintext
   [X] products successfully processed and transferred to MongoDB.
   ```

---

### **XML File Format**

The script expects an XML file with the following structure:

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

### **Important Notes**

- **XML Structure:**  
  The script assumes that the XML file follows the above schema. Invalid or missing data may cause errors.

- **MongoDB Collection:**  
  Products are stored in the `Products` collection of the `ProductDB` database. Modify these names in the script as needed.

- **Data Validation:**  
  Products are identified by a unique `_id` (ProductId). If a product with the same ID exists, it will be updated.

---

### **Contact**

For questions or suggestions, feel free to contact:

- **Yavuz Görkem Deniz**  
  Email: [gorkeemdeniz@outlook.com]  
  LinkedIn: [https://www.linkedin.com/in/yavuz-g%C3%B6rkem-deniz-a0a222240/]  

Thank you for using this project!
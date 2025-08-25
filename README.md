# 🛒 Inventory Management System

A minimal **Inventory Management System** built with **Django** and **PostgreSQL**.  
It allows you to manage products, track stock levels, and record transactions (stock in/out).  

---

## ⚡ Features

- **Products**  
  - Add new products with SKU, name, cost price, and selling price.  
  - Soft delete support via `is_active` field.  

- **Inventory**  
  - Automatically updated when transactions occur.  
  - Tracks current stock per product.  

- **Transactions**  
  - Records stock **IN** (add to inventory) and **OUT** (remove from inventory).  
  - Validates stock before allowing an OUT transaction.  
  - Prevents negative stock.  
  - Shows transaction history.  

- **UI Features**  
  - Separate forms for adding products and recording transactions.  
  - Bootstrap-based styling with alerts for success/error messages.  
  - Only active products are shown in inventory views.  

---

## 🗄️ Database Schema (PostgreSQL)

### Products Table
```sql
CREATE TABLE main_products (
    product_id SERIAL PRIMARY KEY,
    name VARCHAR(128) NOT NULL,
    sku VARCHAR(50) UNIQUE NOT NULL,
    cost_price DECIMAL(12,2) NOT NULL,
    selling_price DECIMAL(12,2) NOT NULL,
    is_active BOOLEAN DEFAULT TRUE
);
```

### Inventory Table
```sql
CREATE TABLE main_inventory (
    inventory_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES main_products(product_id) ON DELETE CASCADE,
    quantity INT NOT NULL DEFAULT 0
);
```

### Transactions Table
```sql
CREATE TABLE main_transactions (
    transaction_id SERIAL PRIMARY KEY,
    product_id INT REFERENCES main_products(product_id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    change_type VARCHAR(10) CHECK (change_type IN ('IN', 'OUT')),
    timestamp TIMESTAMP DEFAULT NOW()
);
```

---

## 📊 Example Data

### Products
```sql
INSERT INTO main_products (name, sku, cost_price, selling_price)
VALUES
('Apple iPhone 15', 'SKU005', 70000, 79999),
('Samsung Galaxy S24', 'SKU006', 65000, 72999),
('OnePlus 12', 'SKU007', 55000, 59999),
('Sony Headphones', 'SKU008', 5000, 6999),
('Dell Laptop XPS 13', 'SKU009', 90000, 105000),
('Logitech Mouse', 'SKU010', 700, 1200);
```

### Inventory
```sql
INSERT INTO main_inventory (product_id, quantity)
VALUES
(5, 50),
(6, 40),
(7, 35),
(8, 100),
(9, 20),
(10, 150);
```

### Transactions
```sql
INSERT INTO main_transactions (product_id, quantity, change_type)
VALUES
(5, 10, 'IN'),
(5, 5, 'OUT'),
(6, 20, 'IN'),
(6, 2, 'OUT'),
(7, 15, 'IN'),
(8, 30, 'OUT'),
(9, 10, 'IN'),
(10, 50, 'OUT');
```

---

## 🔑 Important Business Rules

1. **OUT transactions cannot exceed stock**  
   - If an OUT is attempted with insufficient stock, show an error message and prevent saving.  

2. **Soft Delete Products**  
   - Products have `is_active`.  
   - `Inventory` and `Transactions` queries use `product__is_active=True`.  

3. **Inventory Auto Update**  
   - On `IN`: stock is increased.  
   - On `OUT`: stock is decreased, cannot go negative.  

4. **Transaction History**  
   - Shows only successful transactions.  
   - Skips useless OUT attempts when stock is already 0.  

---

## 🚀 Future Improvements

- User authentication (per-user transaction history).  
- Reports (e.g., top-selling products, low stock alerts).  
- Export transactions to CSV/Excel.  
- REST API endpoints for integration.  

---

## ⚙️ Setup Instructions

1. Clone repo & install dependencies:
   ```bash
   git clone <repo-url>
   cd inventory-system
   pip install -r requirements.txt
   ```

2. Configure PostgreSQL in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'inventory_db',
           'USER': 'postgres',
           'PASSWORD': 'yourpassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Start the server:
   ```bash
   python manage.py runserver
   ```

5. Visit [http://127.0.0.1:8000](http://127.0.0.1:8000)  

---

## 📸 Screenshots (to add later)
- Product List Page  
- Inventory Page  
- Transaction Form with Stock Validation  

CREATE_INVOICE_TABLE = """
CREATE TABLE IF NOT EXISTS invoices(

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    invoice_number TEXT UNIQUE NOT NULL,

    vendor_name TEXT NOT NULL,

    customer_name TEXT,

    invoice_date TEXT,

    due_date TEXT,

    tax_amount REAL,

    total_amount REAL,

    currency TEXT,

    payment_status TEXT DEFAULT 'Pending',

    processing_date TEXT,

    validation_status TEXT
);
"""
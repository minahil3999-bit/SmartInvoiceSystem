# Smart Invoice Processing System

A desktop-based Smart Invoice Processing System developed using **Python**, **CustomTkinter**, and **SQLite**. The system automates invoice processing by extracting information from PDF invoices, validating the extracted data, storing it in a database, generating reports, and visualizing business insights through charts.

---

## Project Overview

The Smart Invoice Processing System helps organizations efficiently manage invoices by reducing manual data entry and providing quick access to invoice information.

The application supports uploading invoice PDFs, extracting invoice details, validating required fields, storing records in a SQLite database, searching invoices, generating reports, and displaying analytical charts.

---

## Features

- Modern CustomTkinter GUI
- Upload PDF invoices
- Automatic invoice text extraction
- Invoice validation
- Duplicate invoice detection
- SQLite database integration
- Search invoices by Invoice Number
- Search invoices by Vendor Name
- Update payment status
- Delete invoices
- Dashboard statistics
- Vendor Summary
- Monthly Summary
- Tax Summary
- Export reports to Excel
- Export reports to CSV
- Interactive charts using Matplotlib
- Application logging
- Login & Sign Up support (if implemented)

---

## Technologies Used

- Python 3.x
- CustomTkinter
- SQLite
- Pandas
- PDFPlumber
- Matplotlib
- OpenPyXL

---

## Folder Structure

```
SmartInvoiceSystem/

├── database/
├── gui/
├── invoice_processing/
├── reports/
├── services/
├── utils/
├── logs/
├── exports/
├── sample_invoices/
├── main.py
└── requirements.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/minahil3999-bit/SmartInvoiceSystem.git
```

Open the project folder

```bash
cd SmartInvoiceSystem
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
 main.py
```

---

## How to Use

1. Launch the application.
2. Upload one or more invoice PDF files.
3. The system extracts invoice information automatically.
4. Validation checks are performed.
5. Valid invoices are stored in the SQLite database.
6. Search invoices using Invoice Number or Vendor Name.
7. Generate reports and export them to Excel or CSV.
8. View charts from the Reports section.

---

## Supported Invoice Fields

The system extracts the following fields:

- Invoice Number
- Vendor Name
- Customer Name
- Invoice Date
- Due Date
- Tax Amount
- Total Amount
- Currency
- Payment Status

---

## Screenshots

Add screenshots of:

- Dashboard
- Upload Page
- Search Page
- Reports Page
- Charts

---

## Future Improvements

- OCR support for scanned invoices
- AI-based invoice extraction
- Cloud database integration
- Email report generation
- User authentication with encrypted passwords
- Multi-user support
- Web-based version using Flask or Django

---

## Author

**Minahil Noor**

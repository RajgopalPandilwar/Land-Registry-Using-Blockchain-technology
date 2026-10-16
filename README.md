# Land Registry Using Blockchain Technology

A blockchain-based land registry system that securely records and tracks land ownership, preventing fraud and ensuring transparent, tamper-proof property records.

## Project Overview

Land registry systems worldwide suffer from fraud, document forgery, and lack of transparency. This project uses blockchain technology to create an immutable, decentralized land registry where property records cannot be falsified, ownership history is fully traceable, and all stakeholders can verify records independently.

### YouTube Video : https://youtu.be/0x-fnZXXrD0?si=CxneShyl_L73jDRP

## Features

- **Immutable Land Records** — Property details cryptographically hashed and chained
- **Ownership Verification** — Query records by owner UID to verify land ownership
- **Complete Audit Trail** — Every record addition is timestamped and linked to previous entries
- **Fraud Prevention** — Tamper-proof design makes document forgery impossible
- **Transparent Access** — Anyone can view the full blockchain to verify records

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | Python 3 + Flask |
| Blockchain | Custom SHA-256 chained blocks |
| Frontend | HTML templates (Jinja2) |
| Hashing | SHA-256 via `hashlib` |

## How It Works

1. **Register Land** — Submit owner name, UID, age, and land details via the web form
2. **Block Creation** — A new block is created with the record data and a timestamp
3. **Hash Linking** — The block's hash includes the previous block's hash, forming a chain
4. **Verify Ownership** — Query by UID to retrieve all land records for that owner
5. **View Full Chain** — Audit the entire blockchain to detect any tampering

## Project Structure

```
land-Record-System-main/
├── app.py                    # Flask application with blockchain logic
├── templates/
│   ├── index.html            # Registration and query form
│   └── blockchain.html       # Full blockchain viewer
└── README.md                 # Project documentation
```

## Getting Started

### Prerequisites
- Python 3.x
- Flask

### Installation

```bash
# Install Flask
pip install flask

# Run the application
cd land-Record-System-main
python app.py
```

### Usage

1. Open `http://127.0.0.1:5000/` in your browser
2. Fill in the registration form with land owner details
3. Click **"Add Record"** to store on the blockchain
4. Enter a **UID** and click **"Get Record"** to verify ownership
5. Click **"View all Blockchain"** to audit the full chain

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Landing page with forms |
| `/add_record` | POST | Add a new land record |
| `/get_history` | GET | Retrieve records by UID |
| `/view_blockchain` | GET | Display full blockchain |

## Author

**Rajgopal Pandilwar**

### Credits


## License

Open-source project for educational use.

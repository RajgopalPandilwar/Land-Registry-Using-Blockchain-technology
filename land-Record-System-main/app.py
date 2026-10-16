"""
Land Registry Blockchain System
===============================
A Flask-based web application that stores land ownership records
on a custom SHA-256 chained blockchain.

Original concept by Vatshayan — improved by Rajgopal Pandilwar.
"""

from flask import Flask, render_template, request
from datetime import datetime
from hashlib import sha256  # Fixed: was missing in original code

app = Flask(__name__)

# ============================================================
# In-memory blockchain list (resets on server restart)
# For production, use a persistent database or real blockchain
# ============================================================
blockchain = []


class LandRecord:
    """
    Represents a single land ownership record (block) in the blockchain.
    
    Each record contains owner details, a timestamp, and is cryptographically
    linked to the previous record via hash chaining.
    """
    
    def __init__(self, name: str, uid: int, age: int, land: str):
        """Initialize a new land record with owner details."""
        self.timestamp = datetime.now()
        self.name = name          # Land owner's full name
        self.age = age            # Owner's age
        self.uid = uid            # Unique owner identifier
        self.land = land          # Land description/history
        self.previous_hash = None # Hash of the previous block in the chain
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        """
        Compute SHA-256 hash of this record's data.
        Combines timestamp, owner details, and land info into a unique fingerprint.
        """
        hash_data = (
            str(self.timestamp) 
            + self.name 
            + str(self.uid) 
            + str(self.age) 
            + self.land
        )
        return sha256(hash_data.encode()).hexdigest()

    def calculate_previous_hash(self):
        """
        Get the hash of the previous block in the chain.
        Returns None if this is the first (genesis) block.
        """
        if len(blockchain) > 0:
            return blockchain[-1].hash
        return None


# ============================================================
# API Endpoints
# ============================================================

@app.route('/add_record', methods=['POST'])
def add_record():
    """
    Add a new land record to the blockchain.
    Expects form fields: name, age, land, uid
    """
    # Extract form data
    name = request.form['name']
    age = request.form['age']
    land = request.form['land']
    uid = request.form['uid']

    # Create new record and link to previous block
    record = LandRecord(name, uid, age, land)
    record.previous_hash = record.calculate_previous_hash()
    blockchain.append(record)

    return f'Record added to blockchain successfully. Your User ID - {uid}'


@app.route('/get_records', methods=['GET'])
def get_record():
    """
    Retrieve a specific land record by UID.
    Query parameter: uid
    """
    uid = request.args.get('uid')
    for block in blockchain:
        if str(block.uid) == uid:
            return render_template('blockchain.html', blockchain=[block])
    return 'Record not found.'


@app.route('/view_blockchain', methods=['GET'])
def view_blockchain():
    """Display the entire blockchain for audit/verification."""
    return render_template('blockchain.html', blockchain=blockchain)


@app.route('/get_history', methods=['GET'])
def get_history():
    """
    Get complete land ownership history for a given UID.
    Query parameter: uid
    """
    uid = request.args.get('uid')
    history = [
        block for block in blockchain
        if str(block.uid) == uid
    ]

    if len(history) >= 1:
        return render_template('blockchain.html', blockchain=history)
    return 'Record not found.'


@app.route('/')
def index():
    """Landing page with registration and query forms."""
    return render_template('index.html')


# ============================================================
# Entry point
# ============================================================

if __name__ == '__main__':
    app.run(debug=True)

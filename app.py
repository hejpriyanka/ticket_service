from flask import Flask, request, jsonify
import uuid
from datetime import datetime

app = Flask(__name__)

# In-memory storage for tickets
tickets = {}

@app.route('/ping', methods=['GET'])
def ping():
    """
    Simple health check endpoint
    """
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    }), 200

@app.route('/createTicket', methods=['POST'])
def create_ticket():
    """
    Create a new ticket
    """
    data = request.get_json()
    
    # Validate required fields
    if not data or not data.get('subject'):
        return jsonify({
            "error": "Missing required fields. 'subject' is required."
        }), 400
    
    # Create ticket with required and optional fields
    ticket_id = str(uuid.uuid4())
    new_ticket = {
        "id": ticket_id,
        "subject": data.get('subject'),
        "description": data.get('description', ''),
        "status": "NEW",
        "created_at": datetime.now().isoformat(),
        "created_by": data.get('created_by', 'anonymous')
    }
    
    # Store ticket
    tickets[ticket_id] = new_ticket
    
    return jsonify({
        "ticket_id": ticket_id,
        "status": "created",
        "ticket": new_ticket
    }), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
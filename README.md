# ticket_service
This project is a replica of my original project I worked for aviation client in my previous organisation.



ticket-service/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── health.py           # Health check routes
│   │   └── tickets.py          # Ticket management routes
│   ├── models/
│   │   ├── __init__.py
│   │   └── ticket.py           # Ticket model definition
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── ticket.py           # Pydantic schemas for request/response validation
│   ├── services/
│   │   ├── __init__.py
│   │   └── ticket_service.py   # Business logic for ticket operations
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py         # Database connection handling
│   └── config.py               # Configuration settings
├── migrations/                 # Alembic migrations
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── alembic.ini
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_health.py
│   └── test_tickets.py
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── scripts/
│   ├── start.sh
│   └── run_tests.sh
├── requirements.txt
├── README.md
├── .env.example                # Template for environment variables
├── .gitignore
└── main.py                     # Application entry point

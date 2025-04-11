# FCM Backend

A Python backend service for Firebase Cloud Messaging (FCM) that provides a robust API for sending push notifications to Android, iOS, and Web clients.

## Features

- Send push notifications to single or multiple devices
- Topic-based messaging
- Device token management
- Topic subscription management
- Message type differentiation
- Support for high-priority messages
- Token validation

## Prerequisites

- Python 3.8+
- Firebase project with Cloud Messaging enabled
- Firebase Admin SDK credentials JSON file

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fcm_backend
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```
FIREBASE_CREDENTIALS_PATH=path/to/your/firebase-credentials.json
FIREBASE_PROJECT_ID=your-project-id
SECRET_KEY=your-secret-key
```

## Running the Application

Start the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## API Endpoints

### Send Message
- **POST** `/api/v1/fcm/send`
  - Send a push notification to specified target(s)

### Token Management
- **POST** `/api/v1/fcm/tokens/register`
  - Register a new FCM token for a user
- **POST** `/api/v1/fcm/tokens/validate`
  - Validate if an FCM token is still valid

### Topic Management
- **POST** `/api/v1/fcm/topics/subscribe`
  - Subscribe a device to a topic
- **POST** `/api/v1/fcm/topics/unsubscribe`
  - Unsubscribe a device from a topic

## Project Structure

```
fcm_backend/
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   │           └── fcm.py
│   ├── core/
│   ├── models/
│   │   └── fcm.py
│   ├── services/
│   │   └── fcm_service.py
│   ├── utils/
│   └── main.py
├── config/
│   └── settings.py
├── tests/
├── .env.example
├── requirements.txt
└── README.md
```

## Testing

Run tests with:
```bash
pytest
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

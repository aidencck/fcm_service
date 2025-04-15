# FCM Backend

A FastAPI-based backend service for Firebase Cloud Messaging (FCM) with billing and rate limiting.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your actual configuration

5. Set up Firebase credentials:
   - Create a `credentials` directory in the project root
   - Go to Firebase Console (https://console.firebase.google.com/)
   - Select your project
   - Go to Project Settings > Service Accounts
   - Click "Generate New Private Key"
   - Save the downloaded JSON file as `credentials/firebase-credentials.json`
   - Make sure the file permissions are secure (chmod 600 on Unix systems)

6. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

## Project Structure

```
fcm_backend/
├── app/                    # Application code
│   ├── api/               # API endpoints
│   ├── core/              # Core functionality
│   ├── models/            # Data models
│   ├── services/          # Business logic
│   └── utils/             # Utility functions
├── credentials/           # Credential files (not in version control)
│   └── firebase-credentials.json.example  # Example credentials file
├── tests/                 # Test files
├── .env                   # Environment variables (not in version control)
├── .env.example           # Example environment variables
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

## API Documentation

Once the application is running, you can access the API documentation at:
- Swagger UI: http://localhost:8000/api/v1/docs
- ReDoc: http://localhost:8000/api/v1/redoc

## Testing

Run tests with:
```bash
pytest
```

## Security

- All sensitive files (credentials, environment variables) are excluded from version control
- API endpoints are protected with authentication
- Rate limiting is implemented to prevent abuse
- CORS is configured to allow specific origins only

## License

MIT

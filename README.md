# Book Club Flask App

## Setup Instructions

1. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up the MySQL database:
```
mysql -u root -p < schema.sql
```

4. Run the app:
```
python run.py
```

Visit `http://localhost:5000` in your browser.

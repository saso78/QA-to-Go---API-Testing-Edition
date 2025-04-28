### QA to Go – API Testing Edition 🚀

A clean, professional starter kit for API testing using Python, Pytest, and Requests.

Built to be simple, extendable, and production-ready — perfect for quick projects, professional testing setups, or learning modern API testing best practices.
✨ Features

    🔹 Pytest based test runner

    🔹 Requests for easy HTTP API interactions

    🔹 pytest-html for beautiful test reports

    🔹 Environment management via .env and dotenv

    🔹 Clean folder structure (Tests, Utilities, Configs)

    🔹 Easily expandable for larger projects

    🔹 Perfect for quick-starts or professional bases

### 📂 Project Structure
```
qa-to-go-api-testing-edition/
│
├── tests/                # Test cases (organized by feature)
│
├── utils/                # Reusable helpers (request handler, assertions)
│
├── config/               # Configuration and environment management
│
├── reports/              # HTML reports (generated after test runs)
│
├── .env                  # Environment variables (e.g., BASE_URL, tokens)
├── requirements.txt      # Python dependencies
├── pytest.ini            # Pytest configuration file
├── .gitignore            # Files/folders to ignore in version control
└── README.md             # You are here!
```
### 🚀 Getting Started
1. Clone the Repository
```
git clone https://github.com/your-username/qa-to-go-api-testing-edition.git
cd qa-to-go-api-testing-edition
```
2. Set Up Your Environment

It’s recommended to use a virtual environment:
```
python -m venv venv
source venv/bin/activate    # For Mac/Linux
venv\Scripts\activate       # For Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Set Up .env

Create a .env file at the project root:
```
BASE_URL=https://your-api-url.com
AUTH_TOKEN=your_token_here
```
If your API doesn't require a token yet, leave AUTH_TOKEN empty.
🧪 Running Tests

To run all tests:
```
pytest
```
To run a specific test file:
```
pytest tests/test_auth.py
```
### 📈 Generating HTML Reports

Run your tests and generate an HTML report:
```
pytest --html=reports/report.html
```
After running, open the generated reports/report.html in your browser.

🌟 Future Improvements
====
    ✅ Data-driven testing with JSON or YAML

    ✅ Multiple environment support (staging, production, etc.)

    ✅ Test tagging (e.g., sanity, regression)

    ✅ Docker containerization ready

    ✅ GitHub Actions CI/CD integration

    ✅ API Mock server integration

### 📢 About This Project

This project is part of the QA to Go series – designed for testers, developers, and tech enthusiasts who want ready-to-go professional starter kits.

💡 Want the Full Guide?

If you found this useful, check out the Pro Version that includes a full PDF Guide and bonus content!

👉 Available on Gumroad

Your support helps build more awesome starter kits! 🚀

🛡️ License

This project is licensed under the MIT License — free to use, modify, and distribute.

✉️ Contact

Built by Saso Trpovski

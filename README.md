# redditSentimentAnalyzer

A Python-based sentiment analysis tool that analyzes Reddit posts using Natural Language Processing (NLP) techniques. The project fetches Reddit data using the PRAW API and evaluates sentiment using the NLTK VADER sentiment analyzer.

## 🚀 Features

- 🔍 Fetches real-time Reddit posts based on a given topic
- 🧠 Analyzes sentiment (Positive, Negative, Neutral) using VADER
- 📊 Summarizes results for visualization
- 🌐 Built with Flask for easy integration with a web front-end

## 📦 Tech Stack

- **Python 3**
- **PRAW** (Python Reddit API Wrapper)
- **NLTK** (VADER Sentiment Analysis)
- **Flask** (Backend API)
- **HTML/CSS/JavaScript** (Frontend, if applicable)

## 📥 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/redditSentimentAnalyzer.git
   cd redditSentimentAnalyzer
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate        # On Windows
source venv/bin/activate     # On macOS/Linux
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up environment variables in a .env file:

env
Copy
Edit
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
REDDIT_USER_AGENT=your_agent
🧪 Usage
bash
Copy
Edit
python app.py
Then open http://127.0.0.1:8080/api/sentiment/ in your browser (if using Flask server).


A Flask-based web application that performs sentiment analysis on Reddit posts using natural language processing (NLP). It leverages the **PRAW** API to fetch Reddit data and **VADER (NLTK)** to analyze sentiment.

---

## 📁 Project Structure

redditSentimentAnalyzer/
├── app/
│ ├── init.py
│ ├── analysis.py
│ ├── fetch_reddit_data.py
│ ├── graph.py
│ ├── logger.py
│ ├── modules.py
│ ├── routes.py
│ └── templates/
│ └── index.html
├── instance/
├── logs/
├── nltk_data/
├── static/
├── .env
├── .gitignore
├── app.py
├── requirement.txt
├── start.sh
├── test_sentiment.py
└── venv/

yaml
Copy
Edit

---

## 🚀 Features

- 📥 Fetches Reddit posts by keyword/topic using PRAW
- 🧠 Analyzes sentiment (Positive, Neutral, Negative) using VADER
- 📈 Visualizes results using simple graphs
- 🔗 API and Web interface powered by Flask
- 🧪 Unit tested using **pytest**
- 📁 Modular and extensible architecture

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/redditSentimentAnalyzer.git
cd redditSentimentAnalyzer
2. Set up virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install -r requirement.txt
4. Configure environment
Create a .env file with your Reddit API credentials:

ini
Copy
Edit
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USER_AGENT=your_user_agent
🧪 Run Tests
This project uses pytest for testing.

To run tests:

bash
Copy
Edit
pytest test_sentiment.py
🚀 Run the App
bash
Copy
Edit
python app.py
Visit: http://localhost:5000

📝 Future Improvements
 Add Docker support

 Enhance data visualization

 Add topic trend tracking over time

 Deploy to cloud (Render, Heroku, etc.)

📄 License
This project is licensed under the MIT License.

Built with ❤️ by [Your Name]

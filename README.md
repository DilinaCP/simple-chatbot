🤖 Simple Chatbot – Powered by GPT & Gradio
A minimal, AI-powered chatbot that responds like Dilina Chathuraka Perera, using OpenAI’s GPT models. Built with a simple and clean Gradio interface for easy interaction.

✨ Features
📄 Understands you from your profile PDF and summary

🤖 Uses OpenAI’s GPT-4o-mini for intelligent, personalized answers

🧠 Loads and remembers context from your documents

💬 Gradio-based web UI for chatting in the browser

🚀 Quick Start
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/simple-chatbot.git
cd simple-chatbot
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
💡 Make sure you have Python 3.8+ installed.

3. Add Your OpenAI API Key
Create a .env file (or use the one provided) and add:

env
Copy
Edit
OPENAI_API_KEY=your-api-key-here
4. Add Your Personal Files
Make sure these files exist in the me/ folder:

css
Copy
Edit
me/
├── Profile.pdf
└── summary.txt
🧪 Run the Chatbot
Start the chatbot with:

bash
Copy
Edit
python app.py
It will open a local Gradio web interface in your default browser.

📁 Project Structure
bash
Copy
Edit
simple-chatbot/
├── app.py                  # Main app file
├── .env                   # API key config
├── requirements.txt       # Python dependencies
├── me/                    # Personal context files
│   ├── Profile.pdf
│   └── summary.txt
📝 License
This project is for educational and personal use only.
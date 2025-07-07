# simple-chatbot

A simple AI-powered chatbot that answers questions as Dilina Chathuraka Perera, using OpenAI's GPT models and Gradio for the web interface.

## Features

- Answers questions based on Dilina's profile and summary.
- Loads context from a PDF profile and a summary text file.
- Uses OpenAI's GPT-4o-mini model for responses.
- Gradio-based chat interface for easy interaction.

## Setup

1. **Clone the repository** and navigate to the project directory.

2. **Install dependencies**:
   ```sh
   pip install -r requirments.txt
   ```

3. **Add your OpenAI API key** to the `.env` file (already present in this repo).

4. **Ensure your profile PDF and summary are in the `me/` directory**:
   - `me/Profile.pdf`
   - `me/summary.txt`

## Usage

Run the chatbot locally:
```sh
python app.py
```
This will launch a Gradio web interface in your browser.

## Project Structure

```
.
├── app.py
├── .env
├── requirments.txt
├── me/
│   ├── Profile.pdf
│   └── summary.txt
```

## License

This project is for educational and personal use.
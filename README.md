# Rescorer
An AI-powered resume scoring Flask app project
## Requirements
- Python 3.x
- Git
## Features
- Input a valid resume
- Parses texts automatically and processes it through an LLM
- Receive a score out of 100
- Receive general feedbacks for improvements
## Getting Started
Follow these steps to get the project running locally:

1. **Clone the repository**
    ```sh
    git clone https://github.com/Thes3us/Rescorer.git
    cd Rescorer
    ```
2. **Create a Python virtual environment**
    ```sh
    python3 -m venv venv
    ```
    ```sh
    source venv/bin/activate  # macOS/Linux
    ```
    ```sh
    venv\Scripts\activate     # Windows
    ```
3. **Install dependencies**
    ```sh
    pip install -r requirements.txt
    ```
4. **Set up .env**
    - rename `.env.example` to `.env`
    - head over to https://console.groq.com/keys and generate an API key
    - replace `<Your API KEY>` with your groq API key without quotes
4. **Run the app**
    ```sh
    python src/app.py
    ```
5. **Access the Web Application:** Open your browser and navigate to ```http://localhost:5000```
## License
This project is licensed under the MIT License.

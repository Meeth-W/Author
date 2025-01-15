# AI-Based Book Author

This project is an AI-powered platform for generating books or essays based on user prompts. It features a modern web interface built with React and Tailwind CSS, and a robust backend powered by Python's FastAPI framework. The system performs web scraping and leverages AI models to create high-quality written content.

---

## Features

- **User-Friendly Interface**: Intuitive and minimal design inspired by ChatGPT’s interface.
- **AI-Generated Content**: Write books or essays using advanced AI models.
- **Web Scraping**: Collect relevant information from the web to enrich content.
- **Frontend**: Built with React and styled using Tailwind CSS.
- **Backend**: High-performance FastAPI server.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Node.js (v16 or above)
- Python (v3.9 or above)
- npm or yarn

### Installation

#### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/ai-book-author.git
cd ai-book-author
```

#### 2. Set Up Frontend
```bash
cd frontend
npm install
npm run dev
```

#### 3. Set Up Backend
```bash
cd ../backend
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate   # On Windows
pip install -r requirements.txt
uvicorn main:app --reload
```

---

## Usage

1. Run the backend server by navigating to the `backend` directory and executing:
   ```bash
   uvicorn main:app --reload
   ```

2. Start the React development server:
   ```bash
   cd frontend
   npm run dev
   ```

3. Open your browser and navigate to:
   ```
   http://localhost:5173
   ```

4. Enter a prompt and watch the magic happen as the system generates books or essays for you!

---

## Folder Structure

```
root
├── LICENSE
├── README.md
├── frontend/       # React project
├── backend/        # FastAPI project
│   ├── venv/       # Python virtual environment
│   ├── main.py     # FastAPI app
│   ├── requirements.txt
```

---

## Technologies Used

### Frontend
- React
- Tailwind CSS

### Backend
- FastAPI
- BeautifulSoup (for web scraping)
- Hugging Face Transformers / OpenAI API (for AI generation)

---

## Future Enhancements

- Add authentication for user accounts.
- Support multi-language content generation.
- Deploy the project on cloud platforms.
- Implement a feature for users to download generated content as a file.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://reactjs.org/)
- [Tailwind CSS Documentation](https://tailwindcss.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)


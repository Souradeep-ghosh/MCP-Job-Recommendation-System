# 📄🧐 AI Job Recommendation System — MCP Server

An intelligent, AI-powered job recommendation system that analyzes your resume and fetches personalized job listings from **LinkedIn** and **Naukri** in real time. Built with **FastMCP**, **Groq LLM**, **Apify**, and **Streamlit**.

---

## 🚀 Features

- **Resume Analysis** — Upload your PDF resume and get an instant AI-generated summary of your skills, education, and experience
- **Skill Gap Detection** — Identifies missing skills, certifications, and experiences needed for better career opportunities
- **Career Roadmap** — Generates a personalized future roadmap with skills to learn and certifications to pursue
- **Live Job Fetching** — Scrapes real-time job listings from LinkedIn and Naukri based on your resume's extracted keywords
- **MCP Server** — Exposes job-fetching tools (`fetchlinkedin`, `fetchnaukri`) via the Model Context Protocol for AI agent integration

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────┐
│                  Streamlit UI (app.py)           │
│  ┌──────────┐  ┌──────────┐  ┌───────────────┐  │
│  │  Resume  │  │  Groq    │  │  Job Listings │  │
│  │  Parser  │  │  LLM     │  │  Display      │  │
│  └──────────┘  └──────────┘  └───────────────┘  │
└────────────────────────┬────────────────────────┘
                         │
         ┌───────────────┴───────────────┐
         │         src/ modules          │
         │  ┌──────────┐  ┌───────────┐  │
         │  │ helper.py│  │ jobs_api  │  │
         │  │(Groq+PDF)│  │(Apify)    │  │
         │  └──────────┘  └───────────┘  │
         └───────────────┬───────────────┘
                         │
         ┌───────────────┴───────────────┐
         │       MCP Server              │
         │  FastMCP — stdio transport    │
         │  Tools: fetchlinkedin,        │
         │         fetchnaukri           │
         └───────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| LLM | Groq API (`llama-3.3-70b-versatile`) |
| Job Scraping | Apify Client (LinkedIn + Naukri actors) |
| MCP Server | FastMCP (`mcp.server.fastmcp`) |
| PDF Parsing | PyMuPDF (`fitz`) |
| Frontend | Streamlit |
| Package Manager | `uv` |

---

## 📁 Project Structure

```
MCP-Job-Recommendation-System/
│
├── app.py                  # Streamlit frontend application
├── mcp_server.py           # FastMCP server exposing job tools
│
├── src/
│   ├── helper.py           # PDF extraction + Groq LLM calls
│   └── jobs_api.py         # Apify-powered LinkedIn & Naukri scrapers
│
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata & uv config
├── uv.lock                 # Locked dependency versions
├── .python-version         # Python version pin
├── .gitignore
└── README.md
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.10+
- [`uv`](https://github.com/astral-sh/uv) package manager
- Groq API key → [console.groq.com](https://console.groq.com)
- Apify API token → [apify.com](https://apify.com)

### 1. Clone the repository

```bash
git clone https://github.com/Souradeep-ghosh/MCP-Job-Recommendation-System.git
cd MCP-Job-Recommendation-System
```

### 2. Create and activate a virtual environment

```bash
uv venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS/Linux
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
APIFY_API_TOKEN=your_apify_token_here
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

---

## ▶️ Running the Application

### Streamlit Web App

```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501`

### MCP Server (for Claude Desktop / AI agents)

```bash
python mcp_server.py
```

Or register it with Claude Desktop by adding the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "job-recommender": {
      "command": "C:\\path\\to\\MCP-Job-Recommendation-System\\.venv\\Scripts\\python.exe",
      "args": ["C:\\path\\to\\MCP-Job-Recommendation-System\\mcp_server.py"]
    }
  }
}
```

### Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector python mcp_server.py
```

---

## 🔧 MCP Tools

The MCP server exposes two tools consumable by any MCP-compatible AI agent:

| Tool | Description | Input |
|---|---|---|
| `fetchlinkedin` | Fetches live job listings from LinkedIn | `listofkey` — comma-separated job keywords |
| `fetchnaukri` | Fetches live job listings from Naukri | `listofkey` — comma-separated job keywords |

---

## 📸 Application Workflow

1. **Upload Resume** — User uploads a PDF resume via the Streamlit UI
2. **AI Analysis** — Groq LLM summarizes the resume, identifies skill gaps, and generates a career roadmap
3. **Keyword Extraction** — LLM extracts the most relevant job titles and search keywords from the resume
4. **Job Fetching** — Apify scrapes real-time listings from LinkedIn and Naukri using the extracted keywords
5. **Results Display** — Jobs are rendered with title, company, location, and direct application link

---

## 📦 Dependencies

```
streamlit
langchain_groq
pymupdf
python-dotenv
apify-client
mcp[cli]
groq
```

---

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Your Groq API key for LLM inference |
| `APIFY_API_TOKEN` | Your Apify token for job scraping |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'feat: add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Souradeep Ghosh**
- GitHub: [@Souradeep-ghosh](https://github.com/Souradeep-ghosh)
- Hugging Face: [@Sg31Ghosh](https://huggingface.co/Sg31Ghosh)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

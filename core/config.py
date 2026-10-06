import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
LANDING_DIR = DATA_DIR / "landing"
PROFILES_DIR = DATA_DIR / "profiles"
STTM_DIR = DATA_DIR / "sttm"
BRONZE_DIR = DATA_DIR / "bronze_layer"
SILVER_DIR = DATA_DIR / "silver_layer"
GOLD_DIR = DATA_DIR / "gold_layer"
REPORTS_DIR = BASE_DIR / "reports"
AUDIT_DIR = BASE_DIR / "audit_logs"
CHROMA_DIR = BASE_DIR / ".chroma"

# LLM Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "models/text-embedding-004"
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001")

# Groq Configuration (preferred - higher free tier limits)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = "llama-3.3-70b-versatile"  # Currently supported Groq model

# Honor an explicit provider; otherwise prefer configured Groq, then Anthropic, then Gemini.
_env_llm = os.getenv("LLM_PROVIDER", "").strip().lower()
if _env_llm in ("groq", "gemini", "anthropic"):
    LLM_PROVIDER = _env_llm
elif GROQ_API_KEY:
    LLM_PROVIDER = "groq"
elif ANTHROPIC_API_KEY:
    LLM_PROVIDER = "anthropic"
else:
    LLM_PROVIDER = "gemini"

# Ensure directories exist
for d in [LANDING_DIR, PROFILES_DIR, STTM_DIR, BRONZE_DIR, SILVER_DIR, GOLD_DIR, REPORTS_DIR, AUDIT_DIR, CHROMA_DIR]:
    d.mkdir(parents=True, exist_ok=True)

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Data paths
DATA_DIR = os.path.join(BASE_DIR, "data")
MEMORY_FILE = os.path.join(DATA_DIR, "memory.json")
VAULT_FILE = os.path.join(DATA_DIR, "vault.enc")
KEY_FILE = os.path.join(DATA_DIR, "secret.key")

# Assets
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
AFFIRMATIONS_FILE = os.path.join(ASSETS_DIR, "affirmations.txt")
LOGO_FILE = os.path.join(ASSETS_DIR, "logo.png")
RELAX_AUDIO = os.path.join(ASSETS_DIR, "relax.mp3")

# Other settings
EMBEDDING_DIM = 384  # For MiniLM or similar
VECTOR_DB = os.path.join(DATA_DIR, "vector.index")  # Placeholder if you use FAISS later

# Optional: Streamlit UI Settings
APP_TITLE = "SoulMate.AGI – Your Emotional AI Companion"

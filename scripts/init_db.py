import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from core.database import init_db

if __name__ == "__main__":
    print("Creating database tables...")
    init_db()
    print("All tables created")

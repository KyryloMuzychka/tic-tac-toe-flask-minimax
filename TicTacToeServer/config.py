SERVER = "localhost"
DATABASE = "TicTacToe"
USERNAME = "SA"
PASSWORD = "Password123"
SECRET_KEY = "secret_key"
DRIVER = "ODBC Driver 18 for SQL Server"

CONNECTION_STRING = (
    f"DRIVER={{{DRIVER}}}; "
    f"SERVER={SERVER}; "
    f"DATABASE={DATABASE}; "
    f"UID={USERNAME}; "
    f"PWD={PASSWORD}; "
    f"TrustServerCertificate=yes; "
)

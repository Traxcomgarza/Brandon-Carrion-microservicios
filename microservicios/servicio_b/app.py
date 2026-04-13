from flask import Flask, request, jsonify
import mysql.connector
import os
import time
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

DB_CONFIG = {
    "host":     os.environ.get("DB_HOST"),
    "port":     int(os.environ.get("DB_PORT", 3306)),
    "user":     os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME"),
}

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notifications (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            task_id     INT NOT NULL,
            title       VARCHAR(255),
            processed_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("[Servicio B] Tabla notifications lista.")

@app.route("/procesar", methods=["POST"])
def procesar():
    data = request.get_json()
    task_id = data.get("task_id")
    title   = data.get("title", "")

    # Lógica costosa simulada
    time.sleep(2)

    # Guardar en tabla propia
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO notifications (task_id, title) VALUES (%s, %s)",
        (task_id, title)
    )
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"status": "procesado", "task_id": task_id})

@app.route("/health")
def health():
    return jsonify({"servicio": "B", "status": "ok"})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5001, debug=False)

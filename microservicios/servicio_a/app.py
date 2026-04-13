from flask import Flask, request, jsonify, render_template_string
import mysql.connector
import os
import requests
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

SERVICIO_B_URL = os.environ.get("SERVICIO_B_URL", "http://servicio_b:5001")

def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            title       VARCHAR(255) NOT NULL,
            description TEXT,
            status      ENUM('pending','in_progress','done') DEFAULT 'pending',
            created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()
    print("[Servicio A] Tabla tasks lista.")

# ─── HTML ─────────────────────────────────────────────────────────
HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Registro de Tareas</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Segoe UI', sans-serif; background: #0f172a; color: #e2e8f0; min-height: 100vh; padding: 2rem; }
  h1 { text-align: center; font-size: 2rem; margin-bottom: 2rem; color: #38bdf8; }
  .container { max-width: 600px; margin: 0 auto; }
  .card { background: #1e293b; border-radius: 12px; padding: 1.5rem; margin-bottom: 1.5rem; border: 1px solid #334155; }
  input, textarea, select { width: 100%; padding: .6rem .8rem; margin: .4rem 0 .8rem; border-radius: 8px;
    background: #0f172a; border: 1px solid #475569; color: #e2e8f0; font-size: .95rem; }
  button { padding: .6rem 1.4rem; border-radius: 8px; border: none; cursor: pointer; font-weight: 600; font-size: .9rem; }
  .btn-primary { background: #38bdf8; color: #0f172a; }
  #respuesta { margin-top: 1rem; padding: .8rem; border-radius: 8px; background: #0f172a; font-size: .9rem; min-height: 2rem; }
</style>
</head>
<body>
<div class="container">
  <h1>📋 Registro de Tareas</h1>
  <div class="card">
    <h3 style="margin-bottom:1rem; color:#94a3b8;">Nueva Tarea</h3>
    <input id="title" placeholder="Título *" />
    <textarea id="desc" placeholder="Descripción" rows="2"></textarea>
    <select id="status">
      <option value="pending">Pendiente</option>
      <option value="in_progress">En Progreso</option>
      <option value="done">Completada</option>
    </select>
    <button class="btn-primary" onclick="registrar()">Registrar</button>
    <pre id="respuesta"></pre>
  </div>
</div>
<script>
  async function registrar() {
    const title = document.getElementById('title').value.trim();
    if (!title) { document.getElementById('respuesta').textContent = 'El título es requerido'; return; }
    const res = await fetch('/registrar', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        title,
        description: document.getElementById('desc').value,
        status: document.getElementById('status').value
      })
    });
    const data = await res.json();
    document.getElementById('respuesta').textContent = JSON.stringify(data, null, 2);
  }
</script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/registrar", methods=["POST"])
def registrar():
    data = request.get_json()

    # Guardar en BD propia
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, description, status) VALUES (%s, %s, %s)",
        (data["title"], data.get("description", ""), data.get("status", "pending"))
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()

    # Llamar al Servicio B (tarea pesada)
    notif_msg = "Servicio B no disponible — tarea guardada de todas formas."
    try:
        resp = requests.post(
            f"{SERVICIO_B_URL}/procesar",
            json={"task_id": new_id, "title": data["title"]},
            timeout=5
        )
        if resp.status_code == 200:
            notif_msg = "Notificación enviada al Servicio B"
    except Exception:
        notif_msg = "Servicio B en mantenimiento — registro guardado, notificación pendiente."

    return jsonify({
        "id": new_id,
        "mensaje": notif_msg
    }), 201

@app.route("/health")
def health():
    return jsonify({"servicio": "A", "status": "ok"})

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)

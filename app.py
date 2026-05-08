from flask import Flask, request, render_template_string, send_file, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'xK9mP2nQ8rL5madmattr'

# ── Change this to your password ──────────────────────────────────────────────
PASSWORD = 'RelevantPlay2026'

LOGIN_HTML = '''
<!DOCTYPE html>
<html>
<head>
  <title>Relevant Play — Dashboard</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    * { box-sizing:border-box; margin:0; padding:0; }
    body {
      font-family: Arial, sans-serif;
      background: #1a1714;
      display: flex;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
    }
    .card {
      background: #fff;
      border-radius: 14px;
      padding: 40px 36px;
      width: 100%;
      max-width: 380px;
      box-shadow: 0 20px 60px rgba(0,0,0,0.3);
    }
    .logo { text-align: center; margin-bottom: 28px; }
    .logo h1 { font-size: 20px; font-weight: 700; color: #1a1714; }
    .logo p  { font-size: 12px; color: #6B7280; margin-top: 4px; }
    label {
      display: block; font-size: 12px; font-weight: 600; color: #374151;
      text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px;
    }
    input[type="password"] {
      width: 100%; padding: 11px 14px; border: 1.5px solid #E2E8F0;
      border-radius: 8px; font-size: 14px; outline: none;
    }
    input[type="password"]:focus { border-color: #c25b3f; }
    button {
      width: 100%; margin-top: 16px; padding: 12px; background: #c25b3f;
      color: #fff; border: none; border-radius: 8px; font-size: 14px;
      font-weight: 600; cursor: pointer;
    }
    button:hover { background: #a84a30; }
    .error {
      margin-top: 12px; padding: 10px 12px; background: #FDECEB;
      border-radius: 6px; color: #C0392B; font-size: 13px; text-align: center;
    }
    .footer { text-align: center; margin-top: 20px; font-size: 11px; color: #9CA3AF; }
  </style>
</head>
<body>
  <div class="card">
    <div class="logo">
      <h1>Relevant Play</h1>
      <p>Rep Sales Dashboard — Authorized Access Only</p>
    </div>
    <form method="POST">
      <label>Password</label>
      <input type="password" name="password" placeholder="Enter password" autofocus>
      <button type="submit">Access Dashboard</button>
      {% if error %}
      <div class="error">Incorrect password. Please try again.</div>
      {% endif %}
    </form>
    <div class="footer">Authorized team members only</div>
  </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('authenticated'):
        return redirect(url_for('dashboard'))
    error = False
    if request.method == 'POST':
        if request.form.get('password') == PASSWORD:
            session['authenticated'] = True
            return redirect(url_for('dashboard'))
        else:
            error = True
    return render_template_string(LOGIN_HTML, error=error)

@app.route('/dashboard')
def dashboard():
    if not session.get('authenticated'):
        return redirect(url_for('login'))
    return send_file('dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

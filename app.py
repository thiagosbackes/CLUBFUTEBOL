from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "demo-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///club.db'
db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    role = db.Column(db.String(20))  # presidente ou atleta

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/auth', methods=['POST'])
def auth():
    # login rápido como presidente
    u = Usuario.query.filter_by(role='presidente').first()
    if not u:
        u = Usuario(nome="Presidente Demo", role="presidente")
        db.session.add(u)
        db.session.commit()
    session['uid'] = u.id
    return redirect(url_for('dashboard'))

@app.route('/auth/whatsapp')
def auth_whatsapp():
    # login rápido como atleta
    u = Usuario.query.filter_by(role='atleta').first()
    if not u:
        u = Usuario(nome="Atleta Demo", role="atleta")
        db.session.add(u)
        db.session.commit()
    session['uid'] = u.id
    return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    uid = session.get('uid')
    u = Usuario.query.get(uid) if uid else None
    return render_template('dashboard.html', current_user=u)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

from app import db, Usuario, app

with app.app_context():
    db.drop_all()
    db.create_all()
    # criar 1 presidente e 1 atleta
    pres = Usuario(nome="Presidente Demo", role="presidente")
    atl = Usuario(nome="Atleta Demo", role="atleta")
    db.session.add_all([pres, atl])
    db.session.commit()
    print("Banco seedado com presidente e atleta demo.")

import os
from sqlalchemy import create_engine, text

my_secret = os.environ['db_connect']

engine = create_engine(my_secret, connect_args = {
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def full_db(answers):
  with engine.connect() as conn:
    query = text("INSERT INTO answers (wiek, plec, wyksztalcenie, miescezamieszkania, wiedza, praca, zadania, efektywnosc, rozrywka, ocena, watpliwosci, klamstwo, leczenie, choroby, uleczalnosc, wyborchorob, terapia, ibm, krzeslo, wypowiedz, udar, zastosowanie, korzysci, aspekty ) VALUES (:wiek, :plec, :wyksztalcenie, :miescezamieszkania, :wiedza, :praca, :zadania, :efektywnosc, :rozrywka, :ocena, :watpliwosci, :klamstwo, :leczenie, :choroby, :uleczalnosc, :wyborchorob, :terapia, :ibm, :krzeslo, :wypowiedz, :udar, :zastosowanie, :korzysci, :aspekty)")
    conn.execute(query, {'wiek': answers['wiek'], 'plec': answers['plec'],'wyksztalcenie': answers['wyksztalcenie'],'miescezamieszkania': answers['miescezamieszkania'],'wiedza': answers['wiedza'],'praca': answers['praca'],'zadania': answers['zadania'],'efektywnosc': answers['efektywnosc'],'rozrywka': answers['rozrywka'],'ocena': answers['ocena'],'watpliwosci': answers['watpliwosci'],'klamstwo': answers['klamstwo'],'leczenie': answers['leczenie'], 'choroby': answers['choroby'], 'uleczalnosc': answers['uleczalnosc'], 'wyborchorob': answers['wyborchorob'], 'terapia': answers['terapia'], 'ibm': answers['ibm'], 'krzeslo': answers['krzeslo'], 'wypowiedz': answers['wypowiedz'], 'udar': answers['udar'], 'zastosowanie': answers['zastosowanie'], 'korzysci': answers['korzysci'], 'aspekty': answers['aspekty']})

import os
from sqlalchemy import create_engine, text

# db_connection_string = os.environ['DB_CONNECTION_STRING']
my_secret = os.environ['db_connect']

engine = create_engine(my_secret, connect_args = {
  "ssl": {
    "ssl_ca": "/etc/ssl/cert.pem"
  }
})

def full_db(answers):
  with engine.connect() as conn:
    query = text("INSERT INTO answers (wiek, plec, wyksztalcenie, miejscezamieszkania, wiedza, praca, zadania, efektywnosc, rozrywka, ocena, watpliwosci, klamstwo, leczenie, choroby, uleczalnosc, wyborchorob, terapia, ibm, krzeslo, wypowiedz, udar, zastosowanie, korzysci, aspekty ) VALUES (:wiek, :plec, :wyksztalcenie, :miejscezamieszkania, :wiedza, :praca, :zadania, :efektywnosc, :rozrywka, :ocena, :watpliwosci, :klamstwo, :leczenie, :choroby, :uleczalnosc, :wyborchorob, :terapia, :ibm, :krzeslo, :wypowiedz, :udar, :zastosowanie, :korzysci, :aspekty)")
  conn.execute(query, {'wiek': answers['wiek'], 'plec': answers['plec'],'wyksztalcenie': answers['wyksztalcenie'],'miejscezamieszkania': answers['miejscezamieszkania'],'wiedza': answers['wiedza'],'praca': answers['praca'],'zadania': answers['zadania'],'efektywnosc': answers['efektywnosc'],'rozrywka': answers['rozrywka'],'ocena': answers['ocena'],'watpliwosci': answers['watpliwosci'],'klamstwo': answers['klamstwo'],'leczenie': answers['leczenie'], 'choroby': answers['choroby'], 'uleczalnosc': answers['uleczalnosc'], 'wyborchorob': answers['wyborchorob'], 'terapia': answers['terapia'], 'ibm': answers['ibm'], 'krzeslo': answers['krzeslo'], 'wypowiedz': answers['wypowiedz'], 'udar': answers['udar'], 'zastosowanie': answers['zastosowanie'], 'korzysci': answers['korzysci'], 'aspekty': answers['aspekty']})

# engine = create_engine(
#   db_connection_string, 
#   connect_args={
#     "ssl": {
#       "ssl_ca": "/etc/ssl/cert.pem"
#     }
#   }
# )

# def add_answers_to_db(data):
#   with engine.connect() as conn:
#     query = text("INSERT INTO application (first, second, third, fourth, fifth, sixth, seventh, eighth, ninth, tenth, eleventh, twelfth, thirteenth, fourteenth, fifteenth, sixteenth, seventeenth, eighteenth, nineteenth, twentieth, twenty-first, twenty-second, twenty-third, twenty-fourth) VALUES (first, :second, :third, :fourth, :fifth, :sixth, :seventh, :eighth, :ninth, :tenth, :eleventh, :twelfth, :thirteenth, :fourteenth, :fifteenth, :sixteenth, seventeenth, :eighteenth, :nineteenth, :twentieth, :twenty-first, :twenty-second, :twenty-third, :twenty-fourth)") 
#     conn.execute(query, {'first': data['first'],'second': data['second'], 'third' : data['third'], 'fourth' : data['fourth'], 'fifth' : data['fifth'], 'sixth': data['sixth'] , 'seventh': data['seventh'], 'eighth': data['eighth'], 'ninth': data['ninth'],'tenth' : data['tenth'], 'eleventh' : data['eleventh'], 'twelfth' : data['twelfth'], 'thirteenth' : data['thirteenth'], 'fourteenth' : data['fourteenth'], 'fifteenth' : data['fifteenth'], 'sixteenth': data['sixteenth'], 'seventeenth' : data['seventeenth'], 'eighteenth' : data['eighteenth'], 'nineteenth' : data['nineteenth'], 'twentieth' : data['twentieth'], 'twenty-first': data['twenty-first'],'twenty-second': data['twenty-second'], 'twenty-third' : data['twenty-third'], 'twenty-fourth' : data['twenty-fourth']})


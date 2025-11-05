# Kender du hjemmesiden https://www.erdetfredag.dk?
# Du skal skrive et program, der kan tjekke om det er onsdag.

import datetime

def is_it_wednesday(date):
    
    # date.weekday() returnerer et tal fra 0-6; 0 = mandag, 1 = tirsdag, 2 = onsdag osv.
    weekday_value = date.weekday()
    
    if weekday_value == 2:
        print("Ja, det er onsdag og vi skal til Coding Pirates!")
    else:
        print("Nej, det er ikke onsdag. Øv!") 

# dags dato gemt i en variabel
today = datetime.date.today()

# 👇 kan bruges til at simulere, at det er fredag
fake_date = datetime.date(2025, 9, 17)

# Kør dit program
is_it_wednesday(fake_date)
import csv
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

items = [['Gelo', 10.20], ['Vodka', 33.80], ['Refrigerante Cola', 3.50], ['Refrigerante Guaraná', 2.30],
         ['Cerveja', 4.0], ['Vinho Tinto', 69.90], ['Vinho Branco', 56.90], ['whisky', 129.00], ['Tequila', 95.99],
         ['Água', 2.29], ['Água com gás', 3.29]]

ten_days_ago = datetime.now().date() - timedelta(days=10)

numbers = []
for number in range(700000):
    numbers.append(number)

# Criando Lista de Nomes
names_list = []
for name in range(1000000):
    names_list.append(fake.name())

# Criando Lista de Endereços
ceps = open("ceps.txt", "r",  encoding='utf-8')
ceps_list = []
for line in ceps:
    ceps_list.append(line)
ceps.close()

formated_cep_list = []
for i in ceps_list:
    formated_cep_list.append(i.split('\t'))

# Gênero
gender = ["M", "M", "M", "F", "F"]

# Criando o arquivo csv
with open('usuarios_data.csv', mode="w", encoding='utf-8', newline='') as csv_file:

    fieldnames = ["nome", "idade", "email", "genero", "cep", "cidade_estado", "bairro", "user_ativo", "produto",
                  "produto_valor", "data_compra"]

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    for name in names_list:
        random_number = random.choice(numbers)
        random_gender = random.choice(gender)
        random_cep = int(formated_cep_list[random_number][0])

        if random_gender == "M" and random_cep < 30000000 or random_cep > 34999999:
            random_number_2 = int(random.triangular(0, 11, 5))
            item = items[random_number_2][0]
            item_cost = items[random_number_2][1]
            age = int(random.triangular(15, 80, 25))
            date = fake.date_between(start_date='-30d', end_date='today')
            if date <= ten_days_ago:
                active_user = 0
            else:
                active_user = 1
        else:
            random_number_2 = int(random.triangular(0, 11, 3))
            item = items[random_number_2][0]
            item_cost = items[random_number_2][1]
            age = int(random.triangular(15, 80, 30))
            date = fake.date_between(start_date='-60d', end_date='today')
            if date <= ten_days_ago:
                active_user = 0
            else:
                active_user = 1

        writer.writerow({
            "nome": name,
            "idade": age,
            "email": "anafreisa.teste@gmail.com",
            "genero": random_gender,
            "cep": random_cep,
            "cidade_estado": formated_cep_list[random_number][1],
            "bairro": formated_cep_list[random_number][2],
            "user_ativo": active_user,
            "produto": item,
            "produto_valor": item_cost,
            "data_compra": date,
        })

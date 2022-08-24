#Fazer um sistema de consultas ao banco de dados Northwind.
#Ao entrar no sistema, aparece um menu numerado com todas as tabelas do banco.
#Ao escolher uma tabela, aparece outro menu numerado com todos os campos (colunas) #da tabela escolhida.
#Ao escolher o campo (coluna), o usuário deve digitar algum conteúdo para ser #pesquisado nesse campo, nessa tabela.
#O sistema deve exibir na tela o resultado da consulta.
from turtle import position
import mysql.connector

mydb = mysql.connector.connect(
    host="relational.fit.cvut.cz",
    user="guest",
    password="relational",
    database="northwind"
)
print("Escolha uma tabela a ser consultada:")
print("1 - Customers")
print("2 - Employees")
print("3 - Orders")
print("4 - Categories                                                                               \n5 - CustomerCustomerDemo\n6 - CustomerDemographics\n7 - EmployeeTerritories\n8 - OrderDetails \n9 - Orders\n10 - Products\n11 - Region\n12 - Shippers\n13 - Suppliers \n14 - Territories")

opcao = input()
if(opcao == "1"):
    tabela =  "Customers"
    
if(opcao == "2"):
    tabela = "Employees"
    
if(opcao == "3"):
    tabela = "Orders"
    
if(opcao == "4"):
    tabela = "Categories"
    
if(opcao == "5"):
    tabela == "CustomerCustomerDemo"
    
if(opcao == "6"):
    tabela = "CustomerDemographics"
    
if(opcao == "7"):
    tabela = "EmployeeTerritories"
    
if(opcao == "8"):
    tabela = "OrderDetails"
    
if(opcao == "9"):
    tabela = "Orders"
    
if(opcao == "10"):
    tabela  = "Products"
    
if(opcao == "11"):
    tabela  = "Region"
    
if(opcao == "12"):
    tabela  = "Shippers"
    
if(opcao == "13"):
    tabela  = "Suppliers"
    
if(opcao == "14"):
    tabela  = "Territories"

colunas = []
mycursor = mydb.cursor()
mycursor.execute(f'SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "{tabela}" and table_schema = "northwind"')
myresult = mycursor.fetchall()
position = 1
for registro in myresult:
    print(f'{position} - {registro[0]}')
    if (0==0):
        colunas.append(registro[0])
        position = position + 1
        
print(colunas)

print("Escolha uma coluna: ")
coluna = int(input())
coluna = coluna - 1
informacao = colunas[coluna]
print("nome: ")
nome = input()

mycursor =  mydb.cursor()
mycursor.execute(f'SELECT * FROM {tabela} where {informacao} like "%{nome}%"')
myresult = mycursor.fetchall()
for registro in myresult:
    print(registro)
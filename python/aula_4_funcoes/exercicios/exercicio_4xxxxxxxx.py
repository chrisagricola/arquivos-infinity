resultado = 0

def filtrar_emails(resultado: bool, dominio: str, email: str, lista_emails: str):
    dominio = '@gmail.com'
    for email in lista_emails:
        resultado = dominio in email
    return resultado

lista_emails = ['teste@gmail.com', 'info@yahoo.com', 'contato@gmail.com']
for email in lista_emails:
    if filtrar_emails == True:
        print(email)
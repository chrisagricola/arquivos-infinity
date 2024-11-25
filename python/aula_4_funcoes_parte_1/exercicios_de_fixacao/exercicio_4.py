lista_emails = ['teste@gmail.com', 'info@yahoo.com', 'contato@gmail.com']


def filtrar_emails(lista_emails):
    emails_filtrados = []
    for email in lista_emails:
        if '@gmail.com' in email:
            emails_filtrados.append(email)
            print(email)
    return emails_filtrados
    
resultado = filtrar_emails(lista_emails)
print(resultado)



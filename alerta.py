import requests
import smtplib
import email.message
import os

# Função para pegar a cotação
def pegar_cotacao():
    try:
        requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL")
        requisicao.raise_for_status() 
        requisicao_dicionario = requisicao.json()
        return float(requisicao_dicionario['USDBRL']['bid'])
    except requests.RequestException as e:
        print(f"Erro ao pegar cotação: {e}")
        return None

# Função para enviar o e-mail
def enviar_email(cotacao):
    corpo_email = f"""
    <p>A cotação do dólar agora está em R${cotacao}</p>
    <p>O valor está abaixo de 5.20, como solicitado.</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Cotação do Dólar"
    msg['From'] = os.getenv('EMAIL')  
    msg['To'] = 'quem vai receber'
    password = os.getenv('EMAIL_PASSWORD')  
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as s:
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            print('E-mail enviado com sucesso!')
    except smtplib.SMTPException as e:
        print(f"Erro ao enviar o e-mail: {e}")

# Lógica principal
def main():
    cotacao = pegar_cotacao()
    if cotacao and cotacao < 5.20:
        enviar_email(cotacao)

if __name__ == "__main__":
    main()


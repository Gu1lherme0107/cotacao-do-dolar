# Monitor de Cotação do Dólar e Notificador por E-mail

Este script Python monitora a cotação do dólar em tempo real utilizando a API da Awesome API. Caso o valor esteja abaixo de R$ 5,20, um e-mail é enviado para o destinatário configurado, alertando sobre a queda na cotação.

**Funcionalidades:**

* **Busca da Cotação:** Realiza uma requisição HTTP para a API da Awesome API e extrai o valor de compra do dólar.
* **Envio de E-mail:** Utiliza o protocolo SMTP para enviar um e-mail formatado em HTML com a cotação atual, caso o valor seja inferior ao limite definido.
* **Configuração Flexível:** Utiliza variáveis de ambiente para armazenar informações sensíveis como o e-mail do remetente, senha e destinatário.

**Como Usar:**

1. **Configurar as Variáveis de Ambiente:** Defina as variáveis `EMAIL`, `EMAIL_PASSWORD` e `quem vai receber` com as suas credenciais de e-mail.
2. **Executar o Script:** Rode o script Python para iniciar o monitoramento.

**Tecnologias Utilizadas:**

* requests
* smtplib
* email.message
* os


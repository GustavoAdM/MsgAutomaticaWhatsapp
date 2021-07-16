from msgWhatsapp import FirefoxWhats

# atualizado


def main():
    campo = FirefoxWhats()
    campo.FirefoxWhatsapp()
    campo.contatos('Links lembrete') # Passar o nome do contato(deve ser identico ao do whatsapp)
    campo.send_Mensagem('Oi, Tudo bem') # A mensagem


if __name__ == '__main__':
    main()

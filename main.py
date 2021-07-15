from msgWhatsapp import FirefoxWhats


def main():
    campo = FirefoxWhats()
    campo.FirefoxWhatsapp()
    campo.contatos('Links lembrete')
    campo.send_Mensagem('Oi mae, tudo bem com vc?')


if __name__ == '__main__':
    main()

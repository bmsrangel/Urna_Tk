import os
from time import sleep


class Candidato:
    def __init__(self, numero, nome, partido, foto):
        self.numero = numero
        self.nome = nome
        self.partido = partido
        self.totvotos = 0
        self.foto = foto

    def votar(self):
        self.totvotos += 1


class Presidente(Candidato):
    def __init__(self, numero, nome, partido, vice, foto):
        super(Presidente, self).__init__(numero, nome, partido, foto)
        self.vice = vice


class Governador(Candidato):
    def __init__(self, numero, nome, partido, vice, foto):
        super(Governador, self).__init__(numero, nome, partido, foto)
        self.vice = vice


# ciro = Presidente(12, 'Ciro Gomes', 'PDT', 'Kátia Abreu')
# haddad = Presidente(13, 'Fernando Haddad', 'PT', 'Manuela')
# bolsonaro = Presidente(17, 'Jair Bolsonaro', 'PSL', 'General Mourão')

cands = (Presidente(12, 'Ciro Gomes', 'PDT', 'Kátia Abreu', ['Imagens/ciro.png', 'Imagens/katia.png']),
         Presidente(13, 'Fernando Haddad', 'PT', 'Manuela', ['Imagens/haddad.png', 'Imagens/manuela.png']),
         Presidente(17, 'Jair Bolsonaro', 'PSL', 'General Mourão', ['Imagens/bolsonaro.png', 'Imagens/mourao.png']))


# while True:
#     try:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         voto = int(input('Informe o número do candidato à Presidência: '))
#         if voto not in (12, 13, 17, 99):
#             print('Número inválido!')
#             sleep(2)
#         else:
#             if voto == 12:
#                 print(f'Candidato: {ciro.nome}')
#                 print(f'Vice: {ciro.vice}')
#                 print(f'Partido: {ciro.partido}')
#                 while True:
#                     conf = str(input('Confirma o voto [S/N]? '))
#                     if conf in 'sS':
#                         ciro.votar()
#                         os.system('cls' if os.name == 'nt' else 'clear')
#                         print('FIM')
#                         sleep(2)
#                         break
#                     elif conf in 'nN':
#                         print('Corrigindo voto...')
#                         break
#                     else:
#                         print('Opção inválida!')
#             elif voto == 13:
#                 print(f'Candidato: {haddad.nome}')
#                 print(f'Vice: {haddad.vice}')
#                 print(f'Partido: {haddad.partido}')
#                 while True:
#                     conf = str(input('Confirma o voto [S/N]? '))
#                     if conf in 'sS':
#                         haddad.votar()
#                         os.system('cls' if os.name == 'nt' else 'clear')
#                         print('FIM')
#                         sleep(2)
#                         break
#                     elif conf in 'nN':
#                         print('Corrigindo voto...')
#                         break
#                     else:
#                         print('Opção inválida!')
#             elif voto == 17:
#                 print(f'Candidato: {bolsonaro.nome}')
#                 print(f'Vice: {bolsonaro.vice}')
#                 print(f'Partido: {bolsonaro.partido}')
#                 while True:
#                     conf = str(input('Confirma o voto [S/N]? '))
#                     if conf in 'sS':
#                         bolsonaro.votar()
#                         os.system('cls' if os.name == 'nt' else 'clear')
#                         print('FIM')
#                         sleep(2)
#                         break
#                     elif conf in 'nN':
#                         print('Corrigindo voto...')
#                         break
#                     else:
#                         print('Opção inválida!')
#             elif voto == 99:
#                 print('Encerrando programa')
#                 break
#     except ValueError:
#         print('Nenhum número foi digitado!')
# print('Total de votos de cada candidato:')
# print(f'Ciro Gomes: {ciro.totvotos}')
# print(f'Fernando Haddad: {haddad.totvotos}')
# print(f'Jair Bolsonaro: {bolsonaro.totvotos}')

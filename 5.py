contador = 3
senha = '123'

while contador >0:
    senha_usuario = (input('Qual a sua senha? '))

    if senha_usuario == senha:
        print('Acesso liberado')
        break
    else:
        contador -= 1
        print(f'Acesso bloqueado, você tem {contador} restantes')

    if contador == 0:
        print('Acesso bloqueado')
        break






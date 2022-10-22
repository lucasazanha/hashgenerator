import hashlib

while(True):


        texto = input('Digite o texto a ser convertido: ')
        options = int(input(''' 1- MD5 \n 2- SHA1 \n 3- SHA256 \n 4- SHA512 \n Digite a opção escolhida: '''))


        if (options == 1):
            resultado = hashlib.md5(texto.encode('utf-8'))
            print ('Hash MD5 gerada: ', resultado.hexdigest())


        elif (options == 2):
            resultado = hashlib.sha1(texto.encode('utf-8'))
            print('Hash SHA1 gerada: ',resultado.hexdigest())


        elif (options == 3):
            resultado = hashlib.sha256(texto.encode('utf-8'))
            print('Hash SHA256 gerada: ', resultado.hexdigest())


        elif (options == 4):
            resultado = hashlib.sha512(texto.encode('utf-8'))
            print('Hash SHA512 gerada: ', resultado.hexdigest())


        else:
            break
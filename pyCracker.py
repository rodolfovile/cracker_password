import crypt
import os
import sys

'''USAGE PYTHON3 crackerPy.py '''


def teste_cracker(crypt_pass):
    '''take the 2 first characters at the word that can be a SALT'''
    salt = crypt_pass[0:2]

    dictFile = open('senhas.txt', 'r')

    for word in dictFile.readlines():

        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)

        if(cryptWord == cryptPass):

            print("[+][+] Found password:  "+word+"\n")
            return

    print("password not found")
    return


def main():

    passFile = open('password.txt')
    for line in passFile.readlines():
        user = line.split(':')[0]
        cryptPass = line.split(':')[1].strip(' ')
        print("[*] Cracking Password For: "+user")
        testePass(cryptPass)


if __name__ == "__main__":
    main()

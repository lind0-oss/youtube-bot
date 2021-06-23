from googlesearch import search
import pyautogui
from time import sleep
#from random import choice, shuffle
import sys
#import os
import webbrowser

linkOne = input("Primeiro link\n >  ")
#linkTwp = input("Segundo link\n >  ")
nviews = int(input("Quantas views deseja?\n >  "))
tamanho_do_video = int(input("Tamanho do vídeo\n >  "))
#tamanho_do_video2 = int(input("Tamanho do vídeo\n >  "))
# tempo de espera personalizado
tempodeespera = int(input("quantos segundos para inicializar\n >  "))
#vou testar se funciona
sleep(tempodeespera)

def bot(link):
    verificador = 'https://'
    #views = 0
    if verificador not in link:
        print("Isto não é um link =(")
        print('Porém será pesquisado =)')
        #nr = int(input("Quantos resultados deseja?\n >  "))
        #webbrowser.open_new_tab(link)
        for resultado in search('"{link}" google', stop=150):
            print(f'Resultado: {resultado}')
        sleep(5)
        dsd = input("Deseja sair? (y/n)\n >  ")
        if dsd == 'y':
            sys.exit()
        elif dsd == 'n':
            print('Você será desligado em 10000000 segundos')
            sleep(10000000)
            sys.exit()
        else:
            print('Comando inválido =(')
            sleep(5)
            sys.exit()
    else:
        if nviews > 1:
            for i in range(nviews):
                pyautogui.sleep(1)
                webbrowser.open_new_tab(linkOne)
                pyautogui.sleep(1)
                pyautogui.press('space')
                pyautogui.sleep(tamanho_do_video)
                pyautogui.sleep(1)
                pyautogui.hotkey("ctrl", "w")
                pyautogui.sleep(10)
                print(f'Número de views atual: {i}')
            print("M>1")
        else:
            print("O número de views é menor ou igual a 1.")
            sleep(5)
            sys.exit()
            #webbrowser.open_new_tab(linkTwp)
            #pyautogui.sleep(1)
            #pyautogui.press("space")
            #pyautogui.sleep(tamanho_do_video2)
            #pyautogui.sleep(1)
            #pyautogui.hotkeys("ctrl", "w")
#fim da função bot
bot(linkOne)
sleep(1)
print("Fim do script!")
sleep(5)
sys.exit()

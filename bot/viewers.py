import pyautogui
from time import sleep
#from random import choice, shuffle
import sys
#import os
import webbrowser

linkOne = input("Primeiro link\n >  ")
linkTwp = input("Segundo link\n >  ")

nviews = int(input("Quantas views deseja?\n >  "))

tamanho_do_video = int(input("Tamanho do vídeo\n >  "))

tamanho_do_video2 = int(input("Tamanho do vídeo\n >  "))

# tempo de espera personalizado
tempodeespera = int(input("quantos segundos para inicializar\n >  "))

#vou testar se funciona
sleep(tempodeespera)

def verificador_de_link(link):
    verificador = 'https://'
    zero = 0
    if verificador not in link:
        print("Isto não é um link =(")
        sleep(5)
        sys.exit()
    else:
        while zero <= nviews:
            pyautogui.sleep(1)
            webbrowser.open_new_tab(linkOne)
            pyautogui.sleep(1)
            pyautogui.press('space')
            pyautogui.sleep(tamanho_do_video)
            pyautogui.sleep(1)
            pyautogui.hotkeys("ctrl", "w")
            webbrowser.open_new_tab(linkTwp)
            pyautogui.sleep(1)
            pyautogui.press("space")
            pyautogui.sleep(tamanho_do_video2)
            pyautogui.sleep(1)
            pyautogui.hotkeys("ctrl", "w")
print("Fim do script!")
sleep(5)
sys.exit()

import pyautogui
from time import sleep
from random import choice, shuffle
import sys
import os
import webbrowser

# tempo de espera personalizado
tempodeespera = int(input("quantos segundos para inicializar\n >  "))

#vou testar se funciona
sleep(tempodeespera)

link1 = 'https://youtu.be/445WBjoK2O8'
link2 = 'https://youtu.be/tW9sQHTqsbc'

webbrowser.open_new_tab(link1)
pyautogui.press('space')
webbrowser.open_new_tab(link2)

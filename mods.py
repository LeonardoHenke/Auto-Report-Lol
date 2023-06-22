import pyautogui
from time import sleep


def botao_pular_honras():
    pyautogui.click(961,808, duration=0.5)

def botao_continuar():
    pyautogui.click(825, 834, duration=0.2)

def denuncias_do_jogador():
    pyautogui.click(804, 402, duration=0.1)
    pyautogui.click(805, 479, duration=0.1)
    pyautogui.click(804, 521, duration=0.1)
    pyautogui.click(1015, 807, duration=0.1)

def carregar_pagina(imagem, msg):
    while not pyautogui.locateCenterOnScreen(imagem):
        sleep(1)
        print(msg)

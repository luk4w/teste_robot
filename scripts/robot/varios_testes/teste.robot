*** Settings ***
Library                  ../../../libs/sikulix.py

*** Test Cases ***
Teste1 Exemplo
    Run Sikuli Script    ${CURDIR}${/}..\\..\\sikuli\\teste.sikuli\\teste.py
Teste2 Exemplo
    Run Sikuli Script    ${CURDIR}${/}..\\..\\sikuli\\teste2.sikuli\\teste2.py
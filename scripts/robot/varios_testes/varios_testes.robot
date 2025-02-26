*** Settings ***
Library                      ../../../libs/sikulix.py

*** Variables ***
${SIKULI_SCRIPTS_DIR}        ${CURDIR}${/}../../sikuli/

*** Test Cases ***
Teste1 Exemplo
    Run Sikuli Script    ${SIKULI_SCRIPTS_DIR}   teste
Teste2 Exemplo
    Run Sikuli Script    ${SIKULI_SCRIPTS_DIR}   teste2
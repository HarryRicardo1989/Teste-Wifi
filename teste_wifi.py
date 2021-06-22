#!/usr/bin/python3
from flask import Flask
from RequestCommands import RequestCommands
import os
from time import sleep

app = Flask(__name__)
         
comandos = RequestCommands()
    
           
def teste():
    medidas = []
    for seq in range(5):
        medidas.append(comandos.comand("iwconfig wlp1s0 | grep  Signal |  awk '{print $4}'").replace('level=',''))
        
        sleep(10)
        print(seq,medidas)
    return medidas

@app.route('/<nome>')
def le_arquivo(nome):
    return comandos.le_arquivo(nome)


@app.route('/init/<nome>/<angulo>/<metros>')
def init_teste(metros, angulo, nome):
    print('medindo')
    signal_power1, signal_power2,signal_power3,signal_power4,signal_power5 = teste()   
    print (signal_power1, signal_power2,signal_power3,signal_power4,signal_power5)
    print ('Finalizado')
    return comandos.grava_resultado(nome,angulo,metros,signal_power1,signal_power2,signal_power3,signal_power4,signal_power5).replace("\n","|****|")

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=900, debug=False, threaded=False)


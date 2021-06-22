class RequestCommands:
    def __init__(self):
        pass

    def comand(self, comando):
        retorno = os.popen(comando)
        return retorno.read().strip().strip('\n').strip()

    def grava_resultado(self,nome, angulo,metros, signal_power1, signal_power2,signal_power3,signal_power4,signal_power5):
        with open(f'./teste-Wifi-{nome}.csv', 'a') as file:
            file.writelines(f'angulo:{angulo}|{metros}m|{signal_power1}|{signal_power2}|{signal_power3}|{signal_power4}|{signal_power5} \n')
        return self.le_arquivo(nome)
    def le_arquivo(self,nome):
        with open(f'./teste-Wifi-{nome}.csv', 'r') as arquivo:
            return arquivo.read()
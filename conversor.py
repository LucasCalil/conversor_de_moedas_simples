class ConversorDeMoedas:
    # Taxas de conversão pré-definidas (exemplo)
    taxas_de_conversao = {
        'USD': {'BRL': 5.25, 'EUR': 0.85},
        'BRL': {'USD': 0.19, 'EUR': 0.16},
        'EUR': {'USD': 1.17, 'BRL': 6.18}
    }
    
    def __init__(self, moeda_origem: str, moeda_destino: str, valor: float):
        self.moeda_origem = moeda_origem
        self.moeda_destino = moeda_destino
        self.valor = valor

    def converter(self):
        if self.moeda_origem == self.moeda_destino:
            return self.valor  # Nenhuma conversão necessária

        try:
            taxa = self.taxas_de_conversao[self.moeda_origem][self.moeda_destino]
            valor_convertido = round(self.valor * taxa, 2)
            return valor_convertido
        except KeyError:
            raise ValueError(f"Conversão de {self.moeda_origem} para {self.moeda_destino} não suportada.")

# Exemplo de uso
if __name__ == "__main__":
    conversor = ConversorDeMoedas('USD', 'BRL', 100)
    valor_convertido = conversor.converter()
    print(f"Valor convertido: {valor_convertido} BRL")
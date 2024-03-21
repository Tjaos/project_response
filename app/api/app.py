from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
from unidecode import unidecode

# Criando uma instância chamada app
app = Flask(__name__)
CORS(app)

#Foi usado o BASE_DIR por erro na identificação do local
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, 'data.json'), 'r') as file:
    data = json.load(file)['transport']



#a função ajudará na comparação de strings com acentos
def clean_string(string):
    cleaned_string = unidecode(string).lower()
    return cleaned_string

# Buscar viagens
@app.route('/', methods=['GET'])
def get_trips():
    # Verifica se o parâmetro de destino foi fornecido na solicitação
    destination = request.args.get('destination')


    if not destination:
        return jsonify({'mensagem': 'Insira os valores para realizar a cotação.'}), 400

    destination_clean = clean_string(destination)
    # Filtro de mensagens
    
    filtered_message = [trip for trip in data if clean_string(trip['city']) == destination_clean]

    if not filtered_message:
        return jsonify({'mensagem': f'Não foram encontradas viagens para o destino "{destination}"'}), 404


    # Encontra a viagem mais rápida e a mais econômica entre elas
    more_fast_trip = min(filtered_message, key=lambda x: x['duration'])
    more_economic_trip = min(filtered_message, key=lambda x: float(x['price_econ'][3:]))

    # Retorna os detalhes das viagens
    response = {
        'more_fast_trip': {
            'company_name': more_fast_trip['name'],
            'bus_bed':more_fast_trip['bed'],
            'travel_time': more_fast_trip['duration'],
            'total_cost': more_fast_trip['price_confort'],
        },
        'more_economic_trip': {
            'company_name': more_economic_trip['name'],
            'bus_bed':more_economic_trip['bed'],
            'travel_time': more_economic_trip['duration'],
            'total_cost': more_economic_trip['price_econ']
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3000, host='localhost', debug=True)

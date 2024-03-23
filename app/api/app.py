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

def get_duration_in_hours(duration_string):
    if duration_string.endswith('h'):
        return int(duration_string[:-1])
    else:
        return int(duration_string)



# Buscar viagens
@app.route('/', methods=['GET'])
def get_trips():
    # Verifica se o parâmetro de destino foi fornecido na solicitação
    destination = request.args.get('destination')


    if not destination:
        return jsonify({'mensagem': 'Insira os valores para realizar a cotação.'}), 400

    destination_clean = clean_string(destination)
    # Filtro de mensagens
    
    filtered_trips = [trip for trip in data if clean_string(trip['city']) == destination_clean]

    if not filtered_trips:
        return jsonify({'mensagem': f'Não foram encontradas viagens para o destino "{destination}"'}), 404


    # Encontra a viagem mais rápida e a mais econômica entre elas
    economic_trip = min(filtered_trips, key=lambda x: float(x['price_econ'][3:]))
    
    
    fast_confort_trip = min(filtered_trips, key=lambda x: (get_duration_in_hours(x['duration'].split(' ')[0]), float(x['price_confort'][3:])))

    

    # Retorna os detalhes das viagens
    response = {
        'fast_confort_trip': {
            'company_name': fast_confort_trip['name'],
            'bus_bed':fast_confort_trip['bed'],
            'travel_time': fast_confort_trip['duration'],
            'total_cost': fast_confort_trip['price_confort'],
        },
        'economic_trip': {
            'company_name': economic_trip['name'],
            'bus_seat':economic_trip['seat'],
            'travel_time': economic_trip['duration'],
            'total_cost': economic_trip['price_econ']
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=3000, host='localhost', debug=True)

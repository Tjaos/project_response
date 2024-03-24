<script>
import { FaHandHoldingDollar } from '@kalimahapps/vue-icons'
import TheSearchOutput from './TheSearchOutput.vue'
import axios from 'axios'

export default {
  data() {
    return {
      selectedDestination: '',
      selectedDate: '',
      destinations: [
        'Belo Horizonte',
        'Campinas',
        'Curitiba',
        'Fortaleza',
        'Manaus',
        'Natal',
        'Recife',
        'Rio de Janeiro',
        'Salvador',
        'São Paulo'
      ],
      tripData:{
        economic: null,
        fastConfort: null
      },
      showTripResults:false,
      showInitialMessage:true
    };
  },
  methods: {
    searchTrip() {
      if (this.selectedDestination && this.selectedDate) {
        this.showInitialMessage = false;
        axios
          .get(`http://localhost:3000?destination=${this.selectedDestination}`, {
            params: {
              destination: this.selectedDestination
            }
          })
          .then((response) => {
            const tripData = {
              economic: {
                name: response.data.economic_trip.company_name,
                seat: response.data.economic_trip.bus_seat,
                price: response.data.economic_trip.total_cost,
                duration: response.data.economic_trip.travel_time
              },
              fastConfort: {
                name: response.data.fast_confort_trip.company_name,
                bed: response.data.fast_confort_trip.bus_bed,
                price: response.data.fast_confort_trip.total_cost,
                duration: response.data.fast_confort_trip.travel_time
              }
            };
            this.tripData = tripData;
            this.showTripResults = true;
            this.showInitialMessage = false;
          
          })
          .catch((error) => {
            console.error('Erro ao buscar viagem: ', error)
            this.showInitialMessage = false;
            
          })
      } else {
        console.error('Por favor, selecione um destino e uma data.')
        alert('Insira os valores para realizar a cotação.')
      }
    },
    clearResults() {
      this.selectedDestination = '';
      this.selectedDate = '';
      this.tripData = { economic: null, fastConfort: null };
      this.showTripResults = false;
      this.showInitialMessage = true;
    }
  },
  components: {
    FaHandHoldingDollar,
    TheSearchOutput
  }
}
</script>

<template>
  <div class="main">
    <div class="searchInputs">
      <div class="subtitle" @click="searchTrip">
        <FaHandHoldingDollar /> Calcule o Valor da Viagem
      </div>
      <div>
        <p class="low_text">Destino</p>
        <select v-model="selectedDestination" class="input">
          <option disabled value="">Selecione o Destino</option>
          <option v-for="destination in destinations" :key="destination" :value="destination">
            {{ destination }}
          </option>
        </select>
      </div>
      <div>
        <p class="low_text">Data</p>
        <input type="date" class="input" v-model="selectedDate" placeholder="Selecione uma data" />
      </div>
      <Button @click="searchTrip" class="buttonSubmit">Buscar</Button>
    </div>
    <div style="padding: 64px;">
      <TheSearchOutput
      :economicTrip="tripData.economic"
      :fastConfortTrip="tripData.fastConfort"
      v-if="showTripResults"
      />
    </div>
    <div class="mensagem_inicial" v-if="showInitialMessage">
      <p>Nenhum dado Selecionado.</p>
    </div>
    <div class="buttonClear_box">
      <Button @click="clearResults" class="buttonClear">Limpar Resultados</Button> 
    </div>
  </div>
</template>


<style scoped>
.main{
  display: flex;
  flex-direction: row;
  background-color: #fff;
}
.searchInputs {
  padding: 10px 20px;
  margin-left: 40px;
  background-color: #f3f3f3;
  width: 280px;
  height: 380px;
  text-align: center;
  align-items: center;
  justify-content: center;
}
.low_text {
  width: 196px;
  font-size: 12px;
  text-align: left;
  padding-left: 40px;
}
.input {
  padding: 5px;
  border: 1px solid gray;
  border-radius: 5px;
  width: 196px;
  margin-bottom: 20px;
}
.subtitle {
  padding: 10px 20px;
  color: #000;
  font-size: 20px;
}

.buttonSubmit{
  background-color: #02A8B5;
  padding: 10px 60px;
  border: none;
  border-radius: 5px;
  margin-top: 30px;
}
.buttonClear_box{
  margin-top: 340px;
  margin-right: 20px;
}
.buttonClear{
  background-color: #fce446;
  padding: 10px 40px;
  border: none;
  border-radius: 5px;
  margin-top: 30px;
}
.buttonSubmit:hover {
  background-color: #0497a1;
  cursor: pointer;
}
.buttonClear:hover {
  background-color: #e2cc3d;
  cursor: pointer;
}
.mensagem_inicial{
  font-size: 20px;
  margin-top: 130px;
}
</style>
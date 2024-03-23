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
      showTripResults:false
    };
  },
  methods: {
    searchTrip() {
      if (this.selectedDestination && this.selectedDate) {
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
          })
          .catch((error) => {
            console.error('Erro ao buscar viagem: ', error)
          })
      } else {
        console.error('Por favor, selecione um destino e uma data.')
      }
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
      <div class="button" @click="searchTrip">
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
      <Button @click="searchTrip">Buscar</Button>
    </div>
    <div>
      <TheSearchOutput
        :economicTrip="tripData.economic"
        :fastConfortTrip="tripData.fastConfort"
        v-if="showTripResults"
      />
    </div>
  </div>
</template>


<style scoped>
.main{
  display: flex;
  flex-direction: row;
}
.searchInputs {
  padding: 100px 20px;
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
.button {
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.button:hover {
  background-color: #0056b3;
}
</style>
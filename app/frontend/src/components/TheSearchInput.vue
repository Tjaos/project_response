<script>
import { FaHandHoldingDollar } from '@kalimahapps/vue-icons';
export default {
  data(){
    return{
      selectedDestination: "",
      selectedDate: "",
      destinations:[
      "Belo Horizonte",
        "Campinas",
        "Curitiba",
        "Fortaleza",
        "Manaus",
        "Natal",
        "Recife",
        "Rio de Janeiro",
        "Salvador",
        "São Paulo"
      ]
    };
  },
  methods:{
    searchTrip(){
      console.log("Buscando viagem para: ", this.selectedDestination);
      console.log("Data selecionada: ", this.selectedDate);
    }
  },
  components: {
    FaHandHoldingDollar
  }
}
</script>

<template>
  <div class="searchInputs">
    <div class="button" @click="searchTrip" ><FaHandHoldingDollar /> Calcule o Valor da Viagem</div>
    <div>
      <p class="low_text">Destino</p>
      <select v-model="selectedDestination" class="input" >
        <option disabled value="">Selecione o Destino</option>
        <option v-for="destination in destinations" :key="destination" :value="destination">{{ destination }}</option>
      </select>
    </div>
    <div>
      <p class="low_text">Data</p>
      <input type="date" class="input" v-model="selectedDate" placeholder="Selecione uma data" />
    </div>
    <Button @click="searchTrip">Buscar</Button>
  </div>
</template>
<style scoped>
.searchInputs {
  margin: 20px;
  padding: 100px 20px;
  background-color: #f3f3f3;
  width: 280px;
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
.button{
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.button:hover{
  background-color: #0056b3;
}
</style>
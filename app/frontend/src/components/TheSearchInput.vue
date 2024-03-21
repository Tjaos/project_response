<script>
import { FaHandHoldingDollar } from '@kalimahapps/vue-icons'
export default {
  components: {
    FaHandHoldingDollar
  }
}
</script>
<template>
  <div class="searchInputs">
    <div class="button"><FaHandHoldingDollar /> Calcule o Valor da Viagem</div>
    <div>
      <p class="low_text">Destino</p>
      <select v-model="selectedDestination" class="input" >
        <option disabled :value="selecioneODestino">Selecione o Destino</option>
        <option :value="BeloHorizonte">Belo Horizonte</option>
        <option :value="Campinas">Campinas</option>
        <option :value="Curitiba">Curitiba</option>
        <option :value="Fortaleza">Fortaleza</option>
        <option :value="Manaus">Manaus</option>
        <option :value="Natal">Natal</option>
        <option :value="Recife">Recife</option>
        <option :value="RioDeJaneiro">Rio de Janeiro</option>
        <option :value="Salvador">Salvador</option>
        <option :value="SaoPaulo">São Paulo</option>


      </select>
    </div>
    <div>
      <p class="low_text">Data</p>
      <input type="date" class="input" placeholder="Selecione uma data" />
    </div>
    <Button>Buscar</Button>
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
</style>
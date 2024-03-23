<script>
export default {
  props: {
    economicTrip: Object,
    fastConfortTrip: Object
  }
}
</script>

<template>
  <div class="searchOutputs">
    <div class="fast_box" v-if="fastConfortTrip">
      <div class="fastPrice_info">
        <h3>{{ fastConfortTrip.name }}</h3>
        <p>Leito: {{ fastConfortTrip.bed }}</p>
        <p>Tempo Estimado: {{ fastConfortTrip.duration }}</p>
      </div>
      <div class="fast_price">
        <h3>Preço</h3>
        <p>{{ fastConfortTrip.price }}</p>
      </div>
    </div>
    <div class="low_cost_box" v-if="economicTrip">
      <div class="lowCost_info">
        <h3>{{ economicTrip.name }}</h3>
        <p>Poltrona: {{ economicTrip.seat }}</p>
        <p>Tempo Estimado: {{ economicTrip.duration }}</p>
      </div>
      <div class="low_cost_price">
        <h3>Preço</h3>
        <p>{{ economicTrip.price }}</p>
      </div>
    </div>

  </div>
</template>

<style scoped>
.searchOutputs {
  width: 800px;
  justify-content: center;
  align-items: center;
  background-color: #fff;
}
.low_cost_box,
.fast_box {
  margin-top: 20px;
  display: flex;
  align-items: center;
  flex-direction: row;
}
.lowCostContent,
.fastContent {
  font-weight: bold;
}
.lowCost_info,
.low_cost_price,
.fastPrice_info,
.fast_price {
  background-color: #f3f3f3;
  margin: 10px;
  padding-left: 20px;
  border-radius: 5px;
  width: 300px;
  margin-left: 30px;
}
.paragrafo {
  width: fit-content;
}
</style>

<script>
import { FaHandHoldingDollar } from '@kalimahapps/vue-icons';
import { BsClockHistory } from "@kalimahapps/vue-icons";
export default {
  props: {
    economicTrip: Object,
    fastConfortTrip: Object
  },
  components:{
    FaHandHoldingDollar,
    BsClockHistory
  }
}
</script>

<template>
  <div class="searchOutputs">
    <div class="fast_box" v-if="fastConfortTrip">
      <div class="icon_box">
        <FaHandHoldingDollar class="icon"/>
      </div>
      <div class="fastPrice_info">
        <h3>{{ fastConfortTrip.name }}</h3>
        <p>Leito: {{ fastConfortTrip.bed }}</p>
        <p>Tempo Estimado: {{ fastConfortTrip.duration }}</p>
      </div>
      <div class="price_fast">
        <h3>Preço</h3>
        <p>{{ fastConfortTrip.price }}</p>
      </div>
    </div>
    <div class="low_cost_box" v-if="economicTrip">
      <div class="icon_box">
        <BsClockHistory class="icon"/>
      </div>
      <div class="lowCost_info">
        <h3>{{ economicTrip.name }}</h3>
        <p>Poltrona: {{ economicTrip.seat }}</p>
        <p>Tempo Estimado: {{ economicTrip.duration }}</p>
      </div>
      <div class="price">
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
.fastPrice_info
 {
  margin: 0;
  background-color: #f3f3f3;
  padding-left: 20px;
  border-radius: 10px;
  width: 300px;
  height: 130px;
}
.fastPrice_info{
  background-color: #E3E1E4;
}
.price_fast{
  margin: 0;
  background-color: #E3E1E4;
  padding-left: 20px;
  border-radius: 10px;
  width: 300px;
  margin-left: 20px;
  height: 130px;
}
.price{
  margin: 0;
  background-color: #f3f3f3;
  padding-left: 20px;
  border-radius: 10px;
  width: 300px;
  margin-left: 20px;
  height: 130px;
}
.icon_box{
  background-color: #02A8B5;
  padding: 40px;
  border-radius: 5px;
}
.icon{
  font-size: 40px;
  color: #fff;
}

</style>

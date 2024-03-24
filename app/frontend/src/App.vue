<script setup>
import TheLeftBar from './components/TheLeftBar.vue';
import TheSearchInput from './components/TheSearchInput.vue';
import TheSearchOutput from './components/TheSearchOutput.vue';
import { FaTruckArrowRight } from "@kalimahapps/vue-icons";

import { ref } from 'vue'

const name = ref('')
const duration = ref('')
const bed = ref('')
const seat = ref('')
const price = ref('')

const handleSearchResults = (data) => {
  name.value = data.name
  duration.value = data.duration
  bed.value = data.bed
  seat.value = data.seat
  price.value = data.price
}

</script>

<template>
  <div class="main">
    <TheLeftBar class="TheLeftBar" />
    <div class="TheSearchTrip">
      
      <div class="title">
        <h3><FaTruckArrowRight class="truckIcon"/> Calculadora de Viagem</h3>
      </div>
      <TheSearchInput class="" @search-results="handleSearchResults" />
      <TheSearchOutput
        :name="name"
        :duration="duration"
        :bed="bed"
        :seat="seat"
        :price="price"
        class="TheSearchOutput"
      />
    </div>
    </div>
</template>

<style >
html {
  height: 100%;
}
body {
  height: 100%;
  margin: 0;
  background-color: #f3f3f3;
}
#app {
  height: 100%;
}
.main {
  display: flex;
  height: 100%;
  margin: 0;
  flex-direction: row;
}

.title{
  width: 99%;
  border: 1px solid bisque;
  align-items: start;
  justify-content: center;
  padding-left: 10px;
  background-color: #2A2F42;
  color: #fff;
}
.TheSearchTrip {
  display: flex;
  height: fit-content;
  margin-top: 260px;
  margin-left: 40px;
  flex-direction: column;
  background-color: #fff;
}
.tripContent {
  display: flex;
  align-items: center;
  flex-direction: column;
}
.truckIcon{
  padding-right: 10px;
}
</style>

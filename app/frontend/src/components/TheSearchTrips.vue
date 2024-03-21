<script>
import TheSearchInput from './TheSearchInput.vue'
import TheSearchOutput from './TheSearchOutput.vue'
import { FaTruckArrowRight } from "@kalimahapps/vue-icons";
export default {
  components: { TheSearchInput, TheSearchOutput, FaTruckArrowRight }
}
</script>

<template>
  <div class="main">
    <div class="title"> <FaTruckArrowRight /> Calculadora de Viagem</div>
    <div class="searchBox">
      <TheSearchInput />
      <TheSearchOutput />
    </div>
  </div>
</template>



<style scoped>
.main {
  width:auto;
  height: max-content;
  padding: 60px 20px;
  flex-direction: column;
}
.title{
  width: auto;
  background-color: #2A2F42;
  color: white;
  padding: 20px 40px;
  font-family: Verdana, Geneva, Tahoma, sans-serif;
  font-size: 18px;
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
}
.searchBox{
  display: flex;
  flex-direction: row;
  border-bottom-right-radius: 5px;
  border-bottom-left-radius: 5px;
  border: 1px solid blue;
}

</style>

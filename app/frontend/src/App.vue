<script setup>
import TheLeftBar from './components/TheLeftBar.vue';
import TheSearchTrips from './components/TheSearchTrips.vue'
</script>

<template>
  <div class="main">
    <TheLeftBar class="TheLeftBar"/>
    <the-search-trips class="TheSearchTrip"/>
  </div>
</template>

<style>
html{
  height: 100%;
}
body{
  height: 100%;
  margin: 0;
  
}
#app{
  height: 100%;
}
.main {
  display: flex;
  height: 100%;
  margin: 0;
}

.TheSearchTrip{
  flex: 2;
  margin-top: 10%;
}

</style>

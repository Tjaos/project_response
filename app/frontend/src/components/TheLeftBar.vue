<template>
        <div class="wrapper">
            <div class="logoDiv">
                <img alt="CB Transportes logo" class="logo" src="../assets/logo.png"/>
            </div>
            <div class="calcTrip"> 
                <img alt="calculadora" class="calcIcon" src="../assets/calc.png"/>
                <h4>Calculadora de Viagem</h4>
            </div>
        </div>

</template>

<style scoped>
.main{
    margin: 0;
    padding: 0;
}
.logoDiv{
    width: 260px;
    display: flex;
    align-items: center;
    text-align: left;
}
.logo{
    width: 146px;
    height: 25px;
    padding: 25px;
    text-align: left;
}
.calcIcon{
    width: 50px;
    height: 50px;
}
.wrapper{
    text-align: left;
    width: 300px;
    margin: 0;
    background-color: #2A2F42;
}
.wrapper h4{
    color:white;
    font-weight: bold;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
}
.calcTrip{
    width: 260px;
    display: flex;
    align-items: center;
    flex-direction: row;
    text-align: left;
}
</style>

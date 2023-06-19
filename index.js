let trainSpeed = document.getElementById('trainSpeed')
let trainSlope = document.getElementById('trainSlope')
let trainPower = document.getElementById('trainPower')
let trainMasse = document.getElementById('trainMasse')
let trainThrottle = document.getElementById('trainThrottle')
let accelSpeedLimit = document.getElementById('accelSpeedLimit')
let paAccelStatus = document.getElementById('paAccelStatus')
let paDecelStatus = document.getElementById('paDecelStatus')
let distanceLimit = document.getElementById('distanceLimit')
let fuStatus = document.getElementById('fuStatus')


let throttle = document.getElementById('throttle')
let slope = document.getElementById('slope')
let power = document.getElementById('power')
let masse = document.getElementById('masse')
let paLimit = document.getElementById('paLimit')
let startAccel = document.getElementById('startAccel')
let startDecel = document.getElementById('startDecel')
let distance = document.getElementById('distance')
let toggleFU = document.getElementById('toggleFU')

let currentThrottle=parseInt(throttle.value)
let currentSlope=parseInt(slope.value)
let currentPower=parseInt(power.value)
let currentMasse=parseInt(masse.value)
let currentSpeedLimit=parseInt(paLimit.value)
let currentDistanceLimit=parseInt(distance.value)

let currentSpeed = 0;



let delta = 1;
let lastUpdate = Date.now();
let max_tps = 50.0;
const maxSpeed = 80;

let accelStart=false
let decelStart=false
let fuStart=false

init()
function init(){
    update();
    requestAnimationFrame(init);
}

function update(){
    //trimTreshold=(currentSpeed/maxSpeed)*21
    //reverseTrimTreshold=21-trimTreshold

    let rn = Date.now();
    let inter = rn - lastUpdate;
    let theorical_inter = 1000.0 / max_tps;
    delta = inter / theorical_inter;
    lastUpdate = rn;
    if(delta>5)delta=5;
    if(delta<=0)return;

    currentThrottle=parseInt(throttle.value)
    //currentSlope=parseInt(slope.value)
    currentPower=parseInt(power.value)
    currentMasse=parseInt(masse.value)
    currentSpeedLimit=parseInt(paLimit.value)
    currentDistanceLimit=parseInt(distance.value)

    trainSlope.innerText=currentSlope
    trainPower.innerText=currentPower
    trainMasse.innerText=currentMasse
    trainThrottle.innerText=currentThrottle
    distanceLimit.innerText=currentDistanceLimit
    accelSpeedLimit.innerText=currentSpeedLimit

    calcSpeed()

    if(accelStart===true){
        paDecelStatus.innerText='Inactif'
        startAccel.disabled=true
        startDecel.disabled=true
        distance.disabled=true
        paLimit.disabled=true
        decelStart=false
        if(currentSpeed<currentSpeedLimit){
            paAccelStatus.innerText='Starting...'
            let speedPercentage=(currentSpeed/currentSpeedLimit)*100
            if(speedPercentage<70){
                throttle.value=3
                paAccelStatus.innerText='Palier 1'
            } else if(speedPercentage>=70&&speedPercentage<90){
                throttle.value=2
                paAccelStatus.innerText='Palier 2'
            } else if(speedPercentage>=90){
                throttle.value=1
                paAccelStatus.innerText='Palier 3'
            }
        } else {
            accelStart=false
            startAccel.disabled=false
            startDecel.disabled=false
            distance.disabled=false
            paLimit.disabled=false
            throttle.value=0
            paAccelStatus.innerText='En vitesse'
            if(currentSpeed>=maxSpeed){
                paAccelStatus.innerText='Vitesse maximale'
            }
            paDecelStatus.innerText='Standby'
        }
    }
    if(decelStart===true){
        paAccelStatus.innerText='Inactif'
        startAccel.disabled=true
        startDecel.disabled=true
        distance.disabled=true
        paLimit.disabled=true
        accelStart=false
        if(currentSpeed>currentSpeedLimit){
            paDecelStatus.innerText='Starting...'
            if(currentSpeedLimit===0){
                if(currentSpeed>20){
                    throttle.value=-3
                    paDecelStatus.innerText='Palier 1'
                } else if(currentSpeed<=20&&currentSpeed>5){
                    throttle.value=-2
                    paDecelStatus.innerText='Palier 2'
                } else if(currentSpeed<=5){
                    throttle.value=-1
                    paDecelStatus.innerText='Palier 3'
                }
            } else {
                let speedPercentage=(currentSpeedLimit/currentSpeed)*100
                console.log(speedPercentage)
                if(speedPercentage<70){
                    throttle.value=-3
                    paDecelStatus.innerText='Palier 1'
                } else if(speedPercentage>=70&&speedPercentage<90){
                    throttle.value=-2
                    paDecelStatus.innerText='Palier 2'
                } else if(speedPercentage>=90){
                    throttle.value=-1
                    paDecelStatus.innerText='Palier 3'
                }
            }
        } else {
            decelStart=false
            startAccel.disabled=false
            startDecel.disabled=false
            distance.disabled=false
            paLimit.disabled=false
            throttle.value=0
            paDecelStatus.innerText='En vitesse'
            if(currentSpeed===0){
                paDecelStatus.innerText='A l\'arrêt'
            }
            paAccelStatus.innerText='Standby'
        }
    }
    if(fuStart===true){
        fuStatus.innerText='Actif'
        startAccel.disabled=true
        startDecel.disabled=true
        throttle.disabled=true
        distance.disabled=true
        paLimit.disabled=true
        decelStart=false
        accelStart=false
        paAccelStatus.innerText='Inactif'
        paDecelStatus.innerText='Inactif'
        if(currentSpeed>0){
            throttle.value=0
            paAccelStatus.innerText='Freinage d\'urgence'
            currentSpeed += (((-7)*(((currentPower/1000)/currentMasse)*1.3)));
        } else {
            startAccel.disabled=false
            startDecel.disabled=false
            distance.disabled=false
            paLimit.disabled=false
            throttle.disabled=false
            fuStatus.innerText='Standby'
            if(currentSpeed<0){
                currentSpeed=0
            }
            paAccelStatus.innerText='Standby'
            paDecelStatus.innerText='Standby'
            fuStart=false
        }
    }
}

function calcSpeed(){
    let accelForce = ((currentPower/1000)/currentMasse)*1.3
    //let penteForce = ((currentSlope)||1)
    currentSpeed += ((currentThrottle*accelForce)/**penteForce*/);
    console.log('Throttle '+currentThrottle+', calculated power '+accelForce+', calculated slope '/*+penteForce*/)
    if(currentSpeed > maxSpeed) currentSpeed = maxSpeed;
    if(currentSpeed < 0) currentSpeed = 0;

    trainSpeed.innerText=currentSpeed.toFixed(2)
}



startAccel.addEventListener('click',()=>{
    accelStart=true
})
startDecel.addEventListener('click',()=>{
    decelStart=true
})
toggleFU.addEventListener('click',()=>{
    fuStart=true
})
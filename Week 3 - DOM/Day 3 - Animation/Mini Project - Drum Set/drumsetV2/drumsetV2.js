document.addEventListener('keydown', (event) => {
    switch (event.key) {
    	case "a": 
    	boom.currentTime = 0;
        document.getElementById('boom').play();
        break;
        case "s": 
        clap.currentTime = 0;
        document.getElementById('clap').play();
        break;
        case "d":  
        hihat.currentTime = 0;
        document.getElementById('hihat').play();
        break;
        case "f": 
        kick.currentTime = 0;
        document.getElementById('kick').play();
        break;
        case "g": 
        openhat.currentTime = 0;
        document.getElementById('openhat').play();
        break;
        case "h":
        ride.currentTime = 0; 
        document.getElementById('ride').play();
        break;
        case "j": 
        snare.currentTime = 0;
        document.getElementById('snare').play();
        break;
        case "k": 
        tink.currentTime = 0;
        document.getElementById('tink').play();
        break;
        case "l": 
        tom.currentTime = 0;
        document.getElementById('tom').play();
        break;
        default: ;
    }
});

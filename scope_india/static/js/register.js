const countryInfo = {
    India: {
        TamilNadu:{Chennai:'Chennai',Nagercoil:'Nagercoil'},
        Kerala:{Thiruvananthapuram:'Thiruvananthapuram',Kochi:'Kochi'},
    },
    Canada:{
        Alberta:{Calgary:'Calgary',Edmonton:'Edmonton'},
        Nunavut:{Iqaluit:'Iqaluit',RankinInlet:'Rankin Inlet'},
    },
    Japan:{
        Tokyo:{Kiyose:'Kiyose',Tachikawa:'Tachikawa'},
        Saitama:{Sakado:'Sakado',Miyoshi:'Miyoshi'},
    },
}

window.onload = function(){
    const countrySelect = document.querySelector('#country'),
          stateSelect = document.querySelector('#state'),
          citySelect = document.querySelector('#city')
    
    stateSelect.disabled = true;
    citySelect.disabled=true;

    for (let country in countryInfo){
        countrySelect.options[countrySelect.options.length] = new Option(country,country)
    }

countrySelect.onchange = (e) =>{
    stateSelect.disabled = false;
    stateSelect.length = 1;
    citySelect.length = 1;

    for (let state in countryInfo[e.target.value]){
        stateSelect.options[stateSelect.options.length] = new Option(state,state)
    }
}

stateSelect.onchange = (e) =>{
    citySelect.disabled = false;
    citySelect.length = 1;
    for (let city in countryInfo[countrySelect.value][e.target.value]){
        citySelect.options[citySelect.options.length] = new Option(city,city)
    }  
}
};




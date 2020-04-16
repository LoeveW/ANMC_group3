function do_ajax(sliders_values, model) {
    var req = new XMLHttpRequest();
    req.open('POST', '/', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    var arrString = JSON.stringify(sliders_values.concat(model));
    req.send(arrString);

}


var slidercontainer = document.getElementById("slidercontainer");
var sliders = {};
var sliders_values = [];

var n_sliders = 10; // The number of sliders

for (let i = 0; i < n_sliders; i++) {

    sliders[i] = document.createElement('input');
    sliders[i].setAttribute("id", "slider"+i);
    sliders[i].setAttribute("type", 'range');
    sliders[i].setAttribute("min", -5);
    sliders[i].setAttribute("max", 5);
    sliders[i].setAttribute("value", 0);
    sliders[i].setAttribute("step", 0.05);
    sliders[i].setAttribute("class", "slider");
    slidercontainer.appendChild(sliders[i]);

    sliders_values.push(sliders[i].value); // Display the default slider value

    sliders[i].onmouseup = function () {
        sliders_values[i] = this.value;
        do_ajax(sliders_values, model_name);
    };
}

var radio1 = document.getElementById("")


var audioplayer = document.getElementById('audioplayer');
var audio_count = 0; // serves as cache busting (force browser to reload changing audio file)

document.addEventListener('keypress', play);
function play(e) {
    if(e.which == 32 || e.which == 112){ // check space bar or p is pressed
        audioplayer.src = "static/audio/audio.mp3?cb="+audio_count;
        audioplayer.play();
        audio_count++;
    }
}
var dropdownBtn = document.getElementById("modelselector");
function modelSelectorBtn() {
  dropdownBtn.classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

var model_names = ["xp_weights", "w_beta1_v1_4600", "w_beta10_v1_5375","w_beta50", "w_beta50_v2_5380","w_beta10_v1_b800_2750"];
var model_name = model_names[0];

for (let i = 0; i < model_names.length; i++) { 
    var model = document.createElement("BUTTON");
    model.innerHTML = model_names[i];
    model.setAttribute("id", model_names[i]);
    model.setAttribute("class", "subdropbtn");

    model.onclick = function (event) {
        model_name = model_names[i];
        do_ajax(sliders_values, model_name);
    }

    document.getElementById('modelselector').appendChild(model);
}


do_ajax(sliders_values, model_name);

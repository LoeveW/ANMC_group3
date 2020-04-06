function do_ajax(sliders_values) {
    var req = new XMLHttpRequest();

    req.open('POST', '/', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    var arrString = JSON.stringify(sliders_values);
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
        do_ajax(sliders_values);
    };


}
do_ajax(sliders_values);

var audioplayer = document.getElementById('audioplayer');
var audio_count = 0; // serves as cache busting (force browser to reload changing audio file)

document.addEventListener('keypress', play);
function play(e) {
  if(e.keyCode == 32){ // check space bar pressed
        audioplayer.src = "static/audio/audio.mp3?cb="+audio_count;
        audioplayer.play();
        audio_count++;
    }
}
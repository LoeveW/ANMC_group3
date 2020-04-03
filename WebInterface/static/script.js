function do_ajax(sliders_values) {
    var req = new XMLHttpRequest();

    req.open('POST', '/', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    var dictString = JSON.stringify(sliders_values);
    req.send(dictString);

}

var slidercontainer = document.getElementById("slidercontainer");
var sliders = {};
var sliders_values = {};
for (let i = 0; i < 10; i++) {

    sliders[i] = document.createElement('input');
    sliders[i].setAttribute("id", "slider"+i);
    sliders[i].setAttribute("type", 'range');
    sliders[i].setAttribute("min", 1);
    sliders[i].setAttribute("max", 100);
    sliders[i].setAttribute("value", 50);
    sliders[i].setAttribute("class", "slider");
    slidercontainer.appendChild(sliders[i]);

    sliders_values[i] = sliders[i].value; // Display the default slider value

    sliders[i].oninput = function () {
        sliders_values[i] = this.value;
        do_ajax(sliders_values);
    };


}
do_ajax(sliders);

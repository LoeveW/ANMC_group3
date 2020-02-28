// var sliders = [ document.getElementById("slider1"),
//                 document.getElementById("slider2"),
//                 document.getElementById("slider3"),
//                 document.getElementById("slider4"),
//                 document.getElementById("slider5"),
//                 document.getElementById("slider6"),
//                 document.getElementById("slider7"),
//                 document.getElementById("slider8"),
//                 document.getElementById("slider9"),
//                 document.getElementById("slider10")]
//
// outputs = [ document.getElementById("slider1"),
//                 document.getElementById("slider2"),
//                 document.getElementById("slider3"),
//                 document.getElementById("slider4"),
//                 document.getElementById("slider5"),
//                 document.getElementById("slider6"),
//                 document.getElementById("slider7"),
//                 document.getElementById("slider8"),
//                 document.getElementById("slider9"),
//                 document.getElementById("slider10")]
//
//
// for ( i = 0; i < outputs.length; i++){
//     outputs[i] = sliders[i].value;
// }
// for( i = 0; i < outputs.length; i++) {
//     sliders[i].oninput = function () {
//         outputs[i].innerHTML = sliders[i].value;
//         console.log(this.value)
//     }
// }
var slider1 = document.getElementById("slider1");
var slider2 = document.getElementById("slider2");
var slider3 = document.getElementById("slider3");
var slider4 = document.getElementById("slider4");
var slider5 = document.getElementById("slider5");
var slider6 = document.getElementById("slider6");
var slider7 = document.getElementById("slider7");
var slider8 = document.getElementById("slider8");
var slider9 = document.getElementById("slider9");
var slider10 = document.getElementById("slider10");

var out1 = document.getElementById("slider1");
var out2 = document.getElementById("slider2");
var out3 = document.getElementById("slider3");
var out4 = document.getElementById("slider4");
var out5 = document.getElementById("slider5");
var out6 = document.getElementById("slider6");
var out7 = document.getElementById("slider7");
var out8 = document.getElementById("slider8");
var out9 = document.getElementById("slider9");
var out10 = document.getElementById("slider10");


out1.innerHTML = slider1.value; // Display the default slider value
out2.innerHTML = slider2.value; // Display the default slider value
out3.innerHTML = slider3.value; // Display the default slider value
out4.innerHTML = slider4.value; // Display the default slider value
out5.innerHTML = slider5.value; // Display the default slider value
out6.innerHTML = slider6.value; // Display the default slider value
out7.innerHTML = slider7.value; // Display the default slider value
out8.innerHTML = slider8.value; // Display the default slider value
out9.innerHTML = slider9.value; // Display the default slider value
out10.innerHTML = slider10.value; // Display the default slider value

 function do_ajax(sliderString, out) {
        var req = new XMLHttpRequest();

        req.open('POST', '/', true);
        req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
        outputVal = out.value;
        var arr = [sliderString, outputVal]
        var arrString = JSON.stringify( {v : sliderString, o : outputVal});
        // var arrJSON = JSON.parse(arr);
        // console.log(arrString);
        req.send(arrString);

      }

slider1.oninput = function () {
    out1.innerHTML = this.value;
    do_ajax("slider1", out1);
};
slider2.oninput = function () {
    out2.innerHTML = this.value;
    do_ajax("slider2", out2);

};
slider3.oninput = function () {
    out3.innerHTML = this.value;
    do_ajax("slider3", out3);
};
slider4.oninput = function () {
    out4.innerHTML = this.value;
    do_ajax("slider4", out4);
};
slider5.oninput = function () {
    out5.innerHTML = this.value;
    do_ajax("slider5", out5);
};
slider6.oninput = function () {
    out6.innerHTML = this.value;
    do_ajax("slider6", out6);
};
slider7.oninput = function () {
    out7.innerHTML = this.value;
    do_ajax("slider7", out7);
};
slider8.oninput = function () {
    out8.innerHTML = this.value;
    do_ajax("slider8", out8);
};
slider9.oninput = function () {
    out9.innerHTML = this.value;
    do_ajax("slider9", out9);
};
slider10.oninput = function () {
    out10.innerHTML = this.value;
    do_ajax("slider10", out10);
}

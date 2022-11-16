
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*
function* indexGenerator() {
    let index = 1;
    while (index < 78) {
        yield index++;
    }
    if (index = 78)
        yield* indexGenerator(); // https://stackoverflow.com/a/72149706/15372196
  };
  
// const number = indexGenerator();
// console.log("gen output:");
// console.log(gen.next().value);
// console.log("gen output:");
// console.log(gen.next().value);
// console.log("gen output:");
// console.log(gen.next().value);
// console.log("gen output:");
// console.log(gen.next().value);


var number = indexGenerator();


setInterval(function animationslider()
{
    
    
    // var testx = number.next().value;
    // console.log("gen output:");
    // console.log(testx);

    
    // var testx = number.next().value;
    // console.log("gen output:");
    // console.log(testx);



    // testx++; 
    // // if (testx>77) testx=1;
    // console.log("gen output test:");
    // console.log(testx);
    // console.log("gen output test:");
    // console.log(testx);

    var file = "<img src=\"../../../static/pawel_pedryc/logos/media/slides_banner/light_mushroom_python_" + number.next().value + ".jpg\" />";
    document.getElementById("animation-slider").innerHTML = file;
    // setTimeout("animationslider()", 5000);


    // number.next().value;
    // console.log("gen output:");
    // console.log(number);

    // number++; 
    // if (number>77) number=1;
    // console.log("gen output:");
    // console.log(number);

    // for (let index = 0; index < number.length; index++) {
    //     var num = number[index];
    //     console.log(num)
    // }
    // var num = 1
    // if looperpic()



 
    
    // var file = "<img src=\"../../../static/pawel_pedryc/logos/media/python_mushroom.jpeg\" />";
    



    $("#animation-slider").fadeIn(1000);
    
    
}, 100);

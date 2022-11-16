
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*
function* indexGenerator() {
    let index = 1;
    while (index < 77) {
        yield index++;
    }
    if (index = 77)
        yield* indexGenerator(); // https://stackoverflow.com/a/72149706/15372196
  };

var number = indexGenerator();


setInterval(function animationslider()
{
    var file = "<img src=\"../../../static/pawel_pedryc/logos/media/slides_banner/light_mushroom_python_" + number.next().value + ".jpg\" />";
    document.getElementById("animation-slider").innerHTML = file;
    
    $("#animation-slider").fadeIn(1000);
    
    
}, 100);




// function* indexGenerator() {
//     let index = 1;
//     while (index < 28) {
//         yield index++;
//     }
//     if (index = 28)
//         yield* indexGenerator();
//   };

// var number = indexGenerator();


// setInterval(function animationslider()
// {
//     var file = "<img src=\"../../../static/pawel_pedryc/logos/media/slides_banner_f/slide_" + number.next().value + ".jpg\" />";
//     document.getElementById("animation-slider").innerHTML = file;
    
//     $("#animation-slider").fadeIn(10);
    
    
// }, 100);

// // The version built below flicker and because of that I decided to make a new approach (above)

// // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/function*
// function* indexGenerator() {
//     let index = 0;
//     while (index < 77) {
//         yield index++;
//     }
//     if (index == 77)
//         yield* indexGenerator(); // https://stackoverflow.com/a/72149706/15372196
//   };

// var number = indexGenerator();
// $("#animation-slider").fadeOut(50);

// setInterval(function animationslider()
// {   
//     var file = "<img src=\"../../../static/pawel_pedryc/logos/media/slides_banner_v1/light_mushroom_python_" + number.next().value + ".jpg\" />";
//     document.getElementById("animation-slider").innerHTML = file;
    
//     $("#animation-slider").fadeIn(50);
    
    
// }, 100);


// // the version suggestet by gilly3 on the stack overflow also flicker  
// // https://stackoverflow.com/a/74467782/15372196

// const animationContainer = document.getElementById("animation-slider");
// for (let i = 0; i < 77; i++) {
//     const img = document.createElement("img");
//     img.src = `../../../static/pawel_pedryc/logos/media/slides_banner/light_mushroom_python_${i}.jpg`;
//     animationContainer.appendChild(img);
// }

// setInterval(() => animationContainer.appendChild(animationContainer.children[0]), 100);



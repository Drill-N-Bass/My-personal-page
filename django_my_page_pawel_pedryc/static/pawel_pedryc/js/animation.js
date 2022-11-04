const frameHeight = 102;
const frames = 15;
const div = document.getElementById("animation");
let frame = 0;
setInterval(function () {
    const frameOffset = (++frame % frames) * -frameHeight;
    div.style.backgroundPosition = "0px " + frameOffset + "px";
}, 100);
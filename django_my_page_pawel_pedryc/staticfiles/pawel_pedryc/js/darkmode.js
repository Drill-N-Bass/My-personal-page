// https://www.youtube.com/watch?v=wodWDIdV9BY

// I will declare darkMode as `let` because I need to update it with each "click" button
let darkMode = localStorage.getItem("darkMode");
const darkModeToggle = document.querySelector(".main-header-dark-btn");

// // test
// console.log(darkMode);

// // test (check in browser shell):
// darkModeToggle.addEventListener("click", () => {
//     console.log("The darkModeToggle test success !!!");
// });


// Check if dark mode is enabled
// if it's enabled, turn it off
// if it's disabled, turn it on

const enableDarkMode = () => {
    // 1. add the class darkmode to the body
    document.body.classList.add('darkmode');
    // 2. update darkMode in the localStorage
    localStorage.setItem('darkMode', 'enabled');
};

const disableDarkMode = () => {
    // 1. add the class darkmode to the body
    document.body.classList.remove('darkmode');
    // 2. update darkMode in the localStorage
    localStorage.setItem('darkMode', 'disabled');
};

// feature that will check last setting on the page
if (darkMode === 'enabled') {
    enableDarkMode();
};

darkModeToggle.addEventListener("click", () => {
    darkMode = localStorage.getItem('darkMode');
    if (darkMode !== 'enabled') {
        enableDarkMode();
        console.log(darkMode);
    } else {
        disableDarkMode();
        console.log(darkMode);
    }
});
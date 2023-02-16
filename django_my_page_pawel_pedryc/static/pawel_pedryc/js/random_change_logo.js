  // Inspired by https://stackoverflow.com/questions/5897573/random-predefined-background-color-and-text-color-on-2-divs
  
  $(document).ready(function(){
    var fonts = [
      "'Black And White Picture', sans-serif",
      "'Swanky and Moo Moo', cursive",
      "'Swanky and Moo Moo', cursive",
      "'Monsieur La Doulaise', cursive",
      "'Roboto Slab', sans-serif"
      ];
    var size = [
      "5rem",
      "4.6rem",
      "4.6rem",
      "5.2rem",
      "3rem"
    ];  
    var rand = Math.floor(Math.random()*fonts.length); 
    $('#main-logo').css("font-family", fonts[rand]);
    $('#main-logo').css("font-size", size[rand]);
  });
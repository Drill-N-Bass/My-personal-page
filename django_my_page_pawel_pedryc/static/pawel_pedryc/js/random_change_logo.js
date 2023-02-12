  // Inspired by https://stackoverflow.com/questions/5897573/random-predefined-background-color-and-text-color-on-2-divs
  
  $(document).ready(function(){
    var fonts = [
      "'Black And White Picture', sans-serif",
      "'Swanky and Moo Moo', cursive",
      "'Swanky and Moo Moo', cursive",
      "'Monsieur La Doulaise', cursive",
      "'Roboto Slab', sans-serif"
      ];  
    var rand = Math.floor(Math.random()*fonts.length); 
    $('#main-logo').css("font-family", fonts[rand]);
  });
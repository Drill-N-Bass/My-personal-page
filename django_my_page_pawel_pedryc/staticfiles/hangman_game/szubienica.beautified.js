var pass = "a";
// "Hell is truth seen too late"

pass = pass.toUpperCase();

var lengthPass = pass.length;

var errorCount = 0;

var pass1 = "";

for (i = 0; i < lengthPass; i++) 
// instead of `.charAt` you can use `split()` to table:
{
    if (pass.charAt(i) == " ") pass1 = pass1 + " "; else pass1 = pass1 + "-";
}

function updatePass() {
    document.getElementById("board").innerHTML = pass1;
}

window.onload = StartGame;

var letters = new Array(36);

letters[0] = "A";

letters[1] = "Ą";

letters[2] = "B";

letters[3] = "C";

letters[4] = "Ć";

letters[5] = "D";

letters[6] = "E";

letters[7] = "Ę";

letters[8] = "F";

letters[9] = "G";

letters[10] = "H";

letters[11] = "I";

letters[12] = "J";

letters[13] = "K";

letters[14] = "L";

letters[15] = "Ł";

letters[16] = "M";

letters[17] = "N";

letters[18] = "Ń";

letters[19] = "O";

letters[20] = "Ó";

letters[21] = "P";

letters[22] = "Q";

letters[23] = "R";

letters[24] = "S";

letters[25] = "Ś";

letters[26] = "T";

letters[27] = "U";

letters[28] = "V";

letters[29] = "W";

letters[30] = "X";

letters[31] = "Y";

letters[32] = "Z";

letters[33] = "Ż";

letters[34] = "Ź";

letters[35] = "-";

function StartGame() {
    var divContent = "";
    for (i = 0; i <= 35; i++) {
        var element = "let" + i;
        divContent = divContent + '<div class="letter" onclick="checkIt(' + i + ')" id="' + element + '">' + letters[i] + "</div>";
        if ((i + 1) % 6 == 0) divContent = divContent + '<div style="clear: both;"></div>';
    }
    document.getElementById("alphabet").innerHTML = divContent;
    updatePass();
}

String.prototype.setCharacter = function(place, character) {
    if (place > this.length - 1) return this.toString(); else return this.substr(0, place) + character + this.substr(place + 1);
};

function checkIt(num) {
    var matched = false;
    for (i = 0; i < lengthPass; i++) {
        if (pass.charAt(i) == letters[num]) {
            //// alert(i); //Test
            pass1 = pass1.setCharacter(i, letters[num]);
            matched = true;
        }
    }
    if (matched == true) {
        var element = "let" + num;
        document.getElementById(element).style.background = "#003300";
        document.getElementById(element).style.background = "#00C000";
        document.getElementById(element).style.background = "3px solid #00C000";
        document.getElementById(element).style.background = "default";
        updatePass();
    } else {
        var element = "let" + num;
        document.getElementById(element).style.background = "#330000";
        document.getElementById(element).style.background = "#C00000";
        document.getElementById(element).style.background = "3px solid #C00000";
        document.getElementById(element).style.background = "default";
        document.getElementById(element).setAttribute("onclick", ";");
        // errorCount for changing picture of gallows:
        errorCount++;
        var picture = "img/s" + errorCount + ".jpg";
        document.getElementById("gallows").innerHTML = '<img src="' + picture + '"alt="" />';
    }
    //when win:
    if (pass == pass1) {
        document.getElementById("alphabet").innerHTML = pass + "<br /><br />" + "is correct password!" + '<br /><br /><span class="reset" onclick="location.reload()">Once again ?</span>';
    }
    //loose game:
    if (errorCount >= 9) {
        document.getElementById("alphabet").innerHTML = pass + "<br /><br />" + "is correct password!" + '<br /><br /><span class="reset" onclick="location.reload()">Once again ?</span>';
    }
}
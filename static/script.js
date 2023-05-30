// morse stuff;
let textinput = document.querySelector(".textin");

textinput.focus();
textinput.select();

const morseOut = document.querySelector("#morseOut");

textinput.addEventListener('input', function() {
  let intext = textinput.value.toLowerCase();
  console.log(intext);
  let mout = ''
  for (let i = 0; i < intext.length; i++) {
    if (alpha.indexOf(intext[i]) != -1) {
      let ind = alpha.indexOf(intext[i]);
      mout += morse[ind] + " ";
    }
  }
  morseOut.innerText = mout;
});
let alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

let morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'];
// morse stuff *********************************

// Sending to arduino
function sendToArduino(event) {
  event.preventDefault();
  let intext = textinput.value.toLowerCase();
  // check if arduino is selected, if not prompt the user to select a device
  // if (!isArduinoSelected) {
  //   handleArduinoSelectiionClick();
  // }
  // send to arduino
  const options = {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({"secret": intext}),
  };
  
  fetch('http://127.0.0.1:5000/send', options)
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(error => console.log(error));

}

// Sending to arduino


// Scramble text

function scrambleText(text) {

 
}

function enigma(r1, r2, r3, r4) {

}

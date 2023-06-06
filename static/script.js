// morse stuff;
let textinput = document.querySelector(".textin");

textinput.focus();
textinput.select();

const morseOut = document.querySelector("#morseOut");

textinput.addEventListener('input', function() {
  let intext = textinput.value;
  console.log(intext);
});
const alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

let morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..'];
// morse stuff *********************************

// Sending to arduino
function sendToArduino(event) {
  event.preventDefault();
  let intext = textinput.value;
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
function scrambleText(text, n=13) {
  // n is the number of rotations you want
  for (let i = n; i < text.length; i++) {
      let rotor1 = rotateAlpha(alpha, i)
      console.log(rotor1);
      // let inptext = textinput.value.toLowerCase();
      let inptext = text.toLowerCase();
      let outtext = "";
      for (let i = 0; i < inptext; i++) {
        if (alpha.indexOf(inptext[i])){
          let index = alpha.indexOf(inptext[i]);
          outtext += rotor1[index];
          console.log(index)
        }
        else {
          outtext += inptext[i];
        }
      }
      console.log(outtext);
      // textinput.value = outtext; 
  }
}

function rotateAlpha(alpharr, r) {
  let rotated = Array(alpharr.length);
  for (let i = 0; i < alpharr.length; i++) {
    rotated[i] = alpha[(i+r) % alpharr.length]
  }
  return rotated;
}

function enigma(r1, r2, r3, r4) {

}

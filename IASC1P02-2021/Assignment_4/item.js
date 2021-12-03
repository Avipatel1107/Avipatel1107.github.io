//https://www.w3schools.com/howto/howto_js_toggle_dark_mode.asp, accessed Dec 1 2021

function myFunction() {
   var element = document.body;
   element.classList.toggle("dark-mode");

}

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}
//author:nemo011,https://www.studytonight.com/post/build-a-simple-digital-clock-with-javascript, Accessed December 1 2021
function clock() {
      let date = new Date();
      let hrs = date.getHours();
      let mins = date.getMinutes();
      let secs = date.getSeconds();
      let period = "AM";
    
      if (hrs == 0) hrs = 12;
      if (hrs > 12) {
        hrs = hrs - 12;
        period = "PM";
      }
    
      hrs = hrs < 10 ? `0${hrs}` : hrs;
      mins = mins < 10 ? `0${mins}` : mins;
      secs = secs < 10 ? `0${secs}` : secs;
    
      let time = `${hrs}:${mins}:${secs} ${period}`;
      setInterval(clock, 1000);
      document.getElementById("clock").innerText = time;
    }
    
    clock();
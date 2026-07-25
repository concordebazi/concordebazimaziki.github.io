/* =====================================================
   CONCORDE BAZIMAZIKI PORTFOLIO
   JavaScript Functions
===================================================== */


/* =====================================================
   MOBILE MENU
===================================================== */


const menuButton = document.querySelector(".menu-btn");

const navLinks = document.querySelector(".nav-links");


if(menuButton){

menuButton.addEventListener("click",()=>{


    navLinks.classList.toggle("active");


});

}






/* =====================================================
   TYPING EFFECT
===================================================== */


const titles = [

"Hydrographic Data Processing Specialist",

"Geomatics Engineer",

"GIS Professional",

"Marine Data Specialist"

];


let titleIndex = 0;

let charIndex = 0;

let typingElement = document.querySelector(".hero h2");



function typeEffect(){


if(!typingElement) return;



if(charIndex < titles[titleIndex].length){


typingElement.textContent += 
titles[titleIndex].charAt(charIndex);


charIndex++;

setTimeout(typeEffect,80);


}

else{


setTimeout(()=>{


typingElement.textContent="";


charIndex=0;


titleIndex++;


if(titleIndex>=titles.length){

titleIndex=0;

}


typeEffect();


},1500);


}



}



typingElement.textContent="";

typeEffect();









/* =====================================================
   SCROLL ANIMATION
===================================================== */


const sections=document.querySelectorAll(".section");



window.addEventListener("scroll",()=>{


sections.forEach(section=>{


let position=section.getBoundingClientRect().top;


let screenHeight=window.innerHeight;



if(position < screenHeight - 100){


section.style.opacity="1";

section.style.transform="translateY(0)";


}



});



});






/* Initial animation setup */


sections.forEach(section=>{


section.style.opacity="0";


section.style.transform="translateY(40px)";


section.style.transition="1s ease";


});









/* =====================================================
   FOOTER YEAR UPDATE
===================================================== */


const footer=document.querySelector("footer p");


if(footer){


let year=new Date().getFullYear();


footer.innerHTML=

`
© ${year} Concorde Bazimaziki

<br>

Geomatics Engineer | Hydrographic Data Processing Specialist

`;

}
/* =====================================================
   INTERACTIVE CAREER MAP
===================================================== */


const mapElement = document.getElementById("map");


if(mapElement){


const map = L.map("map").setView([20,10],2);



L.tileLayer(

"https://tile.openstreetmap.org/{z}/{x}/{y}.png",

{

attribution:
'© OpenStreetMap contributors'

}

).addTo(map);





// Locations

const locations=[


{

name:"University of Rwanda",

coords:[-1.95,30.06],

text:"Bachelor degree in Geography, Environment and Development."

},



{

name:"Lund University - Sweden",

coords:[55.71,13.21],

text:"Master's degree in Geomatics."

},



{

name:"Swedish Maritime Administration",

coords:[58.59,16.18],

text:"Map Engineer - Hydrographic data, nautical charts and marine cartography."

},



{

name:"Ocean Infinity - Gothenburg",

coords:[57.71,11.97],

text:"Hydrographic Data Processor Grade 1 - offshore survey data processing."

}



];





locations.forEach(location=>{


L.marker(location.coords)

.addTo(map)

.bindPopup(

`

<h3>${location.name}</h3>

<p>${location.text}</p>

`

);


});


}


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


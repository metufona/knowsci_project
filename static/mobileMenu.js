// мобильная версия открытие меню
'use strict';
let nav = document.querySelector("nav");
console.log(nav);
var hamburger = document.querySelector(".hamburger");
var count=1;
function open(){
  if (window.innerWidth<835){
    if (count==1) {
      nav.style.left = "0";
      count--;
    } else if(count==0){
      nav.style.left = "-100%";
      count++;
    };
  };
};
hamburger.addEventListener("click", open);

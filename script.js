const backgrounds = [
  "images/bg1.jpg",
  "images/bg2.jpg",
  "images/bg3.jpg",
  "images/bg4.jpg",
  "images/bg5.jpg"
];

const hero = document.getElementById("hero");

if(hero){
  const randomBg = backgrounds[Math.floor(Math.random() * backgrounds.length)];
  hero.style.backgroundImage = `url(${randomBg})`;
}

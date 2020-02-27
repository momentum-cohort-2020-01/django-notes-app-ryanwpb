let lines = document.querySelector("#lines");
menu = document.querySelector(".mobile-menu");
main = document.querySelector("main");
lines.addEventListener("click", function() {
  menu.style.right = "0";
  menu.classList.add("toggled");
});

main.addEventListener("click", function() {
  menu.style.right = "-270px";
  menu.classList.remove("toggled");
});

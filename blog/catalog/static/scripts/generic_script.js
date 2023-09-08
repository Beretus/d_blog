const menuIcon = document.querySelector(".menu-icon");
const menu = document.querySelector(".menu");

menuIcon.addEventListener("click", (e) => {
  menu.classList.toggle("enable");
  menuIcon.classList.toggle("rotate");

  if (menu.classList.contains("enable")) {
    window.addEventListener("click", (e) => {
      if (menu.contains(e.target) || e.target == menuIcon) {
        //pass
      } else {
        menu.classList.remove("enable");
        menuIcon.classList.remove("rotate");
      }
    });
  }
});

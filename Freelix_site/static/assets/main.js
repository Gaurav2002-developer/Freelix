document.addEventListener("DOMContentLoaded", function () {
  const swiper = new Swiper(".mySwiper", {
    loop: true,
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });
});
document.addEventListener("DOMContentLoaded", function () {
  const searchBox = document.querySelector(".search-box");
  const searchInput = document.querySelector(".search-input");
  const searchIcon = document.querySelector(".search-icon");

  searchIcon.addEventListener("click", () => {
    searchBox.classList.toggle("active");
    if (searchBox.classList.contains("active")) {
      searchInput.focus();
      searchBox.style.width = "180px";
      searchInput.style.opacity = "1";
    } else {
      searchBox.style.width = "40px";
      searchInput.style.opacity = "0";
    }
  });
});

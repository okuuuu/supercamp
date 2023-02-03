  const menuToggle = document.querySelector('.navbar-brand');
  const menuItems = document.querySelectorAll('.nav-item');

  menuToggle.addEventListener('click', function () {
    menuItems.forEach(function (item) {
      item.classList.toggle('slide-right');
      item.classList.toggle('show');
    });
  });
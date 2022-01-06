//JavaScript for Posts page
$(function () {
  //Executed when js-menu-icon is clicked
  $(".js-menu-icon").click(function () {
    //$(this) refers to the 'self-element', namely the .js-menu-icon
    //next() refers the pop up menu, namely div.menu (<div class='menu')
    //toggle() switch between show and hide

    $(this).next().toggle();
  });
});

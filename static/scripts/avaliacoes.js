function edituseraval(star) {
    document.getElementById('avaluser').remove();
    document.getElementById("edituser").style.display = "block";
    document.getElementById(star).checked = true;
}

var stars = document.querySelectorAll('.star-icon');
                  
document.addEventListener('click', function(e){
  var classStar = e.target.classList;
  if(!classStar.contains('ativo')){
    stars.forEach(function(star){
      star.classList.remove('ativo');
    });
    classStar.add('ativo');
  }
});

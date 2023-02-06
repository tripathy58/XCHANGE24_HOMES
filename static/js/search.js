/* By Jamal Hassouni*/

document.getElementById("value").addEventListener("keyup", filterSearch);
function filterSearch(){
   var value,name,profile,i;
   value = document.getElementById('value').value.toUpperCase();
profile = document.getElementsByClassName('profile');
  for(i=0;profile.length;i++){
    name = profile[i].getElementsByClassName('name');
    if(name[0].innerHTML.toUpperCase().indexOf(value) > -1){
      profile[i].style.display ="flex";
    }else{
      profile[i].style.display = "none";
    }
  }  
}
// date picker
$('.datepicker').pickadate();

// time picker
$('.timepicker').pickatime();

function pickTime()
{
    var x = document.getElementById("dropDownDate");
    if (x.style.visibility==="hidden") {
      x.style.visibility="visible";
    } 
    else {
        x.style.visibility="hidden";
    }
}
function currentRedirect()
{
  localStorage.setItem("customDate",false);
  window.location.href = "./Stores/stalls.html";
}
function customRedirect()
{
  var Cdate=document.getElementById("exampleDate").value;
  var Ctime=document.getElementById("exampleTime").value;
  var a=Cdate+","+Ctime;
  console.log(a);
  var Ntime=Date.parse(a);
  console.log(Ntime);
  localStorage.setItem("customDate",true);
  localStorage.setItem("customDT",Ntime);
  window.location.assign("./Stores/stalls.html"); 
}


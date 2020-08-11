var customDate=localStorage.getItem("customDate");
var stallname= document.getElementById('stallname').innerHTML;
var i,index;
for(i=0;i<allStalls_dict.length;i++)
{
    if(allStalls_dict[i].Name==stallname)
    {
        index=i;
    }
}
if(customDate=="true")
{
     var custom=parseInt(localStorage.getItem("customDT"));
     var time= new Date(custom);
     console.log(time);
}
else
{
    var time=new Date();
    console.log(time);
}

function checkMenu(time,stallname)
{
    day=time.getDay();
    console.log(day);
    for (var dishname in allStalls_dict[index]["Food available"]) {
        if (!allStalls_dict[index]["Food available"].hasOwnProperty(dishname)) {
            //The current property is not a direct property of p
            continue;
        }
        //Do your logic with the property here
        {
            if(validateDateTime(index,day,dishname,time))
            {
                var newDiv=createMenu();
                newDiv.children[0].src="gallery/"+dishname+".jpg";
                var currentDiv=document.getElementById("start");
                newDiv.children[1].children[0].innerHTML=dishname;
                newDiv.children[1].children[1].innerHTML="Price: "+allStalls_dict[index]["Food available"][dishname][0];
                currentDiv.appendChild(newDiv);       
            }
 
        }
    }
}
function validateDateTime(index,day,dishname,time)
{
    time=time.toTimeString();
    var oT=(allStalls_dict[index]["Food available"][dishname][2][0]+":"+allStalls_dict[index]["Food available"][dishname][2][1]
    +":"+allStalls_dict[index]["Food available"][dishname][2][2]);
    var cT=(allStalls_dict[index]["Food available"][dishname][3][0]+":"+allStalls_dict[index]["Food available"][dishname][3][1]
    +":"+allStalls_dict[index]["Food available"][dishname][3][2]);
    var timeTrue=(oT<time.slice(0,9)&&time.slice(0,9)<cT);
    if(allStalls_dict[index]["Food available"][dishname][1].includes(day)&&timeTrue)
    {
        return true;
    }
    else
    {
        console.log(timeTrue)
        console.log(dishname,typeof(oT),typeof(time.slice(0,9)),typeof(cT),false)
        return false;
    }
}
 function createMenu()
 {
    var dish = document.createElement("div");
    dish.className="dish col-sm-12 d-flex h-100";
    var imgD = document.createElement("img");
    dish.appendChild(imgD);
    var div1=document.createElement("div");
    var nameD=document.createElement("h2");
    var priceD=document.createElement("h3") ;
    div1.className="details align-self-center";
    nameD.className="name";
    priceD.className="price";
    div1.appendChild(nameD);
    div1.appendChild(priceD);
    dish.appendChild(div1);
    return dish;
 }

 function displayInput()
 {
    var qInput= document.getElementById("qInput");
    if(qInput.style.display=="none"){
        qInput.style.display="block";
    }
    else{
        qInput.style.display="none";
    }      
 }

 function calculateQT()
 {
     var number=document.getElementById("ppl").value;
     alert("You'll have to wait about "+number*allStalls_dict[index]["Waiting Time"]+" minutes")
 }

checkMenu(time,stallname);
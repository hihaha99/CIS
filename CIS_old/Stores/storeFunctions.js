var customDate=localStorage.getItem("customDate");
if(customDate=="true")
{
     var custom=parseInt(localStorage.getItem("customDT"));
     console.log(typeof(custom));
     custom= new Date(custom);
     console.log(custom);
     console.log(typeof(custom));
}

var current=new Date();


function getDateTime() {
    if(customDate=="true")
    {
     var diff    = new Date().getTime() - current.getTime();
     var myTime=new Date(custom);
     myTime.setMilliseconds(myTime.getMilliseconds() + diff);      
    }
    else
    {
          var myTime= new Date();
    }
    var year    = myTime.getFullYear();
    var month   = myTime.getMonth()+1; 
    var day     = myTime.getDate();
    var hour    = myTime.getHours();
    var minute  = myTime.getMinutes();
    var second  = myTime.getSeconds(); 
    if(month.toString().length == 1) {
         month = '0'+month;
    }
    if(day.toString().length == 1) {
         day = '0'+day;
    }   
    if(hour.toString().length == 1) {
         hour = '0'+hour;
    }
    if(minute.toString().length == 1) {
         minute = '0'+minute;
    }
    if(second.toString().length == 1) {
         second = '0'+second;
    }   
    var dateTime = year+'/'+month+'/'+day+' '+hour+':'+minute+':'+second;   
     return dateTime;
}

function displayStores(Time)
{
     var i=0;
     var empty=true;
     for(i;i<allStalls_dict.length;i++)
     {
          var day=(new Date(Time)).getDay()
          var dayTrue= (allStalls_dict[i]["Operating Days"]).includes(day);
          var oT=(allStalls_dict[i]["Operating Hours"][0][0]+":"+allStalls_dict[i]["Operating Hours"][0][1]
          +":"+allStalls_dict[i]["Operating Hours"][0][2]);
          var cT=(allStalls_dict[i]["Operating Hours"][1][0]+":"+allStalls_dict[i]["Operating Hours"][1][1]
          +":"+allStalls_dict[i]["Operating Hours"][1][2]);
          console.log(oT,Time.slice(11),cT)
          if(oT<=Time.slice(11)&&Time.slice(11)<=cT&&dayTrue)
          {
               console.log(true);
               document.getElementById(allStalls_dict[i].Name).style.display="block";
               empty=false;
          }
          else
          {
               console.log("10:0:00"<="10:00:10");
          }
     }
     if(empty==true){
          document.getElementById("notifyEmpty").style.display="flex";
     }
}

// real time clock and real time update operating stores.
    setInterval(function(){
    Time = getDateTime();
    console.log(Time);
    document.getElementById("time").innerHTML = "Result by "+ Time;
     displayStores(Time);
    }, 1000);


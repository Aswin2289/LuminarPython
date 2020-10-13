var bday=Number(prompt("enter ur day of brith"))
var bmonth=Number(prompt("enter ur month of brith"))
var byear=Number(prompt("enter ur year of brith"))

var curday=Number(prompt("enter current date"))
var curmonth=Number(prompt("enter current month"))
var curyear=Number(prompt("enter current year"))
var adate=0
var amonth=0
var ayear=0
if(curday<bday)
    {
        curmonth=curmonth-1
        bday=bday+30
    }
else{
        adate=bday-curday
    }

if(curmonth<bmonth)
    {
        curyear=curyear-1
        curmonth=curmonth+12
    }
else{
        amonth=curmonth-bmonth
    }
if(curyear-byear>0)
    {
        ayear=curyear-byear
        alert("age is"+ ayear)
    }
else
    {
        alert("age is"+ ayear)
    }

var num=Number(prompt("Enter Number :"))
function armstrong(num)
{
    var arm=num
    var sub=0
    var sum=0
    while(num!=0)
    {
        sub=num%10
        sum=sum+(sub**3)
        num=parseInt(num/10)
    }

    if(arm==sum)
    {
        alert("Armstrong Number")
    }
    else
    {
        alert("Not Armstrong Number")
    }
}

armstrong(num)
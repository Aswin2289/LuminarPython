var num1=Number(prompt("enter ur number1"))
var num2=Number(prompt("enter ur number2"))
var num3=Number(prompt("enter ur number3"))

if((num1>num2)&(num1>num3))
{
        if(num2>num3)
        {
            alert(num2+":second largest")
        }
        else
        {
            alert(num3+":second largest")
        }
}
else if((num2>num1)&(num2>num3))
{
    if(num1>num3)
    {
        alert(num1+"second largest")
    }
    else
    {
        alert(num3+"second largest")
    }
}
else if((num3>num1)&(num3>num2))
{
    if(num1>num2)
    {
        alert(num1+"second largest")
    }
    else
    {
        alert(num2+"second largest")
    }
}
else
{
    alert(num1+","+num2+","+num3+","+"All numbers are equal")
}
var num1=Number(prompt("enter ur number1"))
var num2=Number(prompt("enter ur number2"))
var num3=Number(prompt("enter ur number3"))

if((num1>num2)&(num1>num3))
{
        if(num2>num3)
        {
            alert(num1+","+num2+","+num3+","+"sorted")
        }
        else
        {
            alert(num1+","+num3+","+num2+","+"sorted")
        }
}

else if((num2>num1)&(num2>num3))
{
    if(num1>num3)
    {
        alert(num2+","+num1+","+num3+","+"sorted")
    }
    else
    {
        alert(num2+","+num3+","+num1+","+"sorted")
    }
}

else if((num3>num1)&(num3>num2))
{
    if(num1>num2)
    {
        alert(num3+","+num1+","+num2+","+"sorted")
    }
    else
    {
        alert(num3+","+num2+","+num1+","+"sorted")
    }
}
else
{
    alert(num1+","+num2+","+num3+","+"All numbers are equal")
}
var num1=Number(prompt("enter ur number1"))
var num2=Number(prompt("enter ur number2"))
var num3=Number(prompt("enter ur number3"))

if((num1>num2)&(num1>num3))
{
    alert("max="+num1)
}
else if((num2>num1)&(num2>num3))
{
    alert("max="+num2)
}
else if((num1==num2)&(num2==num3))
{
    alert(num1+num2+num3+"every number is equal")
}
else
{
    alert("max="+num3)
}
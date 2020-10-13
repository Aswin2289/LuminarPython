var num=Number(prompt("Enter Number :"))
var sub=0
var sum=0
while(num!=0)
{
    sub=num%10
    sum=sum+(sub**3)
    num=parseInt(num/10)
}
alert(sum)
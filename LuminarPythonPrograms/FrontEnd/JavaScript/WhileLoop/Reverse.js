var num=Number(prompt("Enter Number :"))
var sub=0
var rev=0
while(num!=0)
{
    sub=num%10
    rev=rev*10+sub
    num=parseInt(num/10)
}
alert(rev)
var n1=0
var n2=1
var num=Number(prompt("Enter your Limit :"))
var i=0
alert("Fibonacci series up to"+num)
while(i<num)
{
    console.log(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    i=i+1
}
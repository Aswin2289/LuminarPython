var low=Number(prompt("Enter Lower Limit :"))
var upp=Number(prompt("Enter Upper Limit :"))
var even=0
var odd=0


for (let i=low;i<upp+1;i++)
{
    if(i%2==0)
    {
        even=even+i
    }
    else
    {
        odd=odd+i
    }
}
alert(even+":Even")
alert(odd+":Odd")

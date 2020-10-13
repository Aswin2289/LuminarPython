var low=Number(prompt("Enter Lower Limit :"))
var upp=Number(prompt("Enter Upper Limit :"))
var i=0
var flg=0
for(i=low;i<upp+1;i++)
{
    flg=0
    for(let j=2;j<i;j++)
    {
        if(i%j==0)
        {
            flg=1
            break
        }
    }
    if(flg==0)
    {
        console.log(i)
    }
}
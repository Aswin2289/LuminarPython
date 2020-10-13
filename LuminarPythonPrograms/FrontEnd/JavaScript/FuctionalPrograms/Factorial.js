var num=Number(prompt("Enter ur number"))
var f=1
var i=2
function fact(n)
{

    while(i<=n)
    {
        f*=i
        i++
    }
    return(f)
}
var data=fact(num)
console.log("fact="+data)
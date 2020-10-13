var num=Number(prompt("Enter ur number"))

function fact(num)
{
    var fact=1

    for (let i=1;i<num+1;i++)
    {
        fact*=i
    }
    return(fact)

}


var data=fact(num)
alert(data)
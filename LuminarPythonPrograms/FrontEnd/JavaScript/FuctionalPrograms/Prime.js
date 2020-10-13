var num=Number(prompt("Enter Number :"))
var flag=0
function prime(num1)
{


    for(let i=2;i<num1;i++)
    {
        if(num%i==0)
        {
            flag=1
            break
        }
        else
        {
            flag=0
        }
    }
    if(flag==1)
    {
        alert(num1+"Not prime")
    }
    else
    {
        alert(num1+"prime")
    }
}

prime(num)
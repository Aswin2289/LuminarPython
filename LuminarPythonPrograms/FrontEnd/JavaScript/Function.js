function add(num1,num2)
{
    var res=num1+num2;
    console.log(res)
}
function sub(num1,num2)
{
    var res=num1-num2;
    console.log(res)
}
function mul(num1,num2)
{
    var res=num1*num2;
    console.log(res)
}
function div(num1,num2)
{
    var res=num1/num2;
    console.log(res)
}

add(10,20)//function call
sub(20,10)

//function with argument and return value
function cube(num)
{
    var res=num*num*num//num**3
    return res
}
var data=cube(3)
console.log("cube"+data)
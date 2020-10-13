//var arr=[10,20,30,40]
var flg=0
var arr=[]
num=Number(prompt("Enter Limit"))
for(let i=0;i<num;i++)
{
    n=Number(prompt("Enter number"))
    arr.push(n)
}
s=Number(prompt("Enter Number to be searched"))
for(item of arr)
{
    if(item==s)
    {
        flg=1
        break;
        //console.log("item found: "+item)
    }

}
if(flg>0)
{
    alert("item found: "+s)
}
else
{
    alert("item  not found: ")
}

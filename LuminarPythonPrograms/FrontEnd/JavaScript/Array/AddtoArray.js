var arr=[]
var arr1=[]

num=Number(prompt("Enter Limit"))
for(let i=0;i<num;i++)
{
    n=Number(prompt("Enter number"))
    arr.push(n)
}


for (let i=0;i<num;i++)
{

    if (arr[i]>5)
    {
        arr1.push(arr[i]+1)
    }
    else if (arr[i]<5)
    {
        arr1.push(arr[i]-1)
    }
    else
    {
        arr1.push(arr[i])
    }
}
console.log(arr1)
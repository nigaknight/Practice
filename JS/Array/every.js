//every()的判断函数
function isBelowThreshold(currentValue){
    if(currentValue<40){
        return true;
    }
}

var array1=[1,2,4,32,5,21];

//every()是数组的方法，遍历这个数组，判断函数都返回true时返回true
console.log(array1.every(isBelowThreshold));
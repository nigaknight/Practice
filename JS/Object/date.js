//定义日期
var date=new Date();
document.write(date);
//操作日期
date.setFullYear(2018,1,19);
document.write(date);
date.setDate(date.getDate()+5);
//比较日期
var today=new Date();
if(today>date){
    alert("today is after 19th Feburary 2018");
}
else{
    alert("today is before 19th Feburary 2018");
}
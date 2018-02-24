//第一种数组赋值方法
var car=new Array();
car[0]="Saab";
car[1]="Volve";
car[2]="BMW";
//可以控制数组容量
var car=new Array(3);
car[0] = "Saab";
car[1] = "Volve";
car[2] = "BMW";
//第二种数组赋值方法
var car=new Array("Saab","Volve","BMW");
//访问数组
document.write(car[0]);
//修改数组中已有的值
car[0]="Benz";
documetn.write(car[0]);
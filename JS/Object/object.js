//创建js对象的第一种方法
person=new Object();
person.firstname="Bill";
person.lastname="Gates";
person.age=56;
person.eyescolor="blue";
//创建js对象的第二种方法
person={firstname:"Bill",lastname:"Gates",age:56,eyescolor="blue"};
//创建js对象的第三种方法和向js对象中添加方法
function person(firstname,lastname,age,eyescolor){
    this.firstname=firstname;
    this.lastname=lastname;
    this.age=age;
    this.eyescolor=eyescolor;
    this.nameChange=nameChange;
    function nameChange(name){
        lastname=name;
    }
}
var myfather=new person("Bill","Gates",56,"blue");
//js中for...in循环
var person={firstname:"Bill",lastname:"Gates",age:56};
var txt='';
for(x in person){
    txt=txt+person[x];
}

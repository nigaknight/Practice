//在字符串中检索e字符：test()方法，返回false和true
var patt=new RegExp("e");
document.write(patt.test("The best thing in life is free"));
//在字符串中检索e字符：exec()方法，返回字符或null
document.write(patt.exec("The best thing in life is free"));
//exec方法的第二个参数，设置为"g"，可以返回所有检索到的字符
var patt1=new RegExp("e","g");
do{
    result=patt.exec("The best thing in life is free");
    document.write(result);
}
while(result!=false)
//compile方法改变检索的字符
patt.compile("d");
document.write(patt.test("The best thing in life is free"));

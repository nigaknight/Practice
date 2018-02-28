$("p").append("Some appended text.");
//三种方式添加文本
//1、html元素创建
var text1="<p>text</p>";
//2、jquery创建
var text2=$("<p></p>").text("text");
//3、DOM创建
var text3=document.createElement("p");
text3.innerHTML="text";
$("p").append(text1,text2,text3);
//Tips:innerHTML打印的内容不包括标签，而innerText包括标签 
//innerText会把html标签当做普通的文本显示，而innerHTML 则不会。
$("img").before("在前面添加元素");
$("img").after("在后面添加元素");
//Tips:在jQuery中，append/prepend 是在选择元素内部嵌入，而after/before 是在元素外面追加。
//使用text(),html(),val()带参数的方法设置内容
$("#btn1").click(function(){
    $("test1").text("Hello World");
});
$("#btn2").click(function(){
    $("test2").html("<p>www.w3cschool.com</p>");
});
$("#btn3").click(function(){
    $("test3").val("wang jinyan");
});
//text(),html()和val()都有回调函数callback，第一个参数为当前元素的下边，第二个参数为当前被选中的元素
$("#btn4").click(function(){
    $("test4").text(function(i,oldtext){
        return "the old text of the chosen element is "+oldtext+"the next text is the subscript "+i+";"
    });
});
//attr()方法改变属性，可以改变多种属性
$("#btn5").click(function(){
    $("test5").attr({
        "href":"//www.w3cschool.cn/jquery",
        "title":"jquery 教程"
    });
});

$("#btn6").click(function(){
    $("test6").attr(
        "href", function(i,oldAttr){
            return oldAttr+"/jquery"
        }
    );
});




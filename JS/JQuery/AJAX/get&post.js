//从服务器请求数据
//get语法
$.get(url,callback);
//get例子
$("button").click(function(){
    $.get("demo_test.php",function(data,status){
        alert("data:"+data+"\n"+"status:"+status);
    });
});
//post语法
$.post(url,data,callback);
//post例子 其中data参数是将其传给url（这里就是个php文件） 作为这个文件的参数
$("button").click(function(){
    $.post("demo_test.php",{
        name:"wjy",
        campus:"SEU"
    }),
    function(data,status){
        alert("data:"+data+"\nstatus"+status);
    };
});
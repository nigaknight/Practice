//淡入示例
$("button").click(function(){
    $("#p1").fadeIn()
    $("#p2").fadeIn("slow")
    $("#p3").fadeIn(3000)
});
//淡入语法
$(selector).fadeIn(speed,callback);
//淡出语法
$(selector).fadeOut(speed,callback);
//切换语法
$(selector).fadeToggle(speed,callback);
//设置为一定的透明度
$(selector).fadeTo(speed,opacity,callback);
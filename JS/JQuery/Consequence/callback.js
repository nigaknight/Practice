//语法
$(selector).hide(callback);
//例子
$("button").click(function(){
    $("p").hide(function(){
        alert("The paragraph is now hidden!");
    });
})
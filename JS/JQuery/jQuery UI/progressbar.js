//安装小部件(widget)，下面为id为elem的元素添加一个进度条，以默认选项初始化
$("elem").progressbar();
//重写进度条的默认选项
$("elem").progressbar({
    value: 22
});
//在进度条上调用value方法进行动作
$("elem").progressbar("value");
//传递参数40给value方法
$("elem").progressbar("value", 40);
//方法可以链接
$("elem").progressbar("value", 40).addClass("almost-done");
//在小部件安装后通过option方法来改变选项
$("elem").progressbar("option", "value", 30);
//为value选项获取当前值
$("elem").progressbar("option", "value");
//一次更新多个选项
$("elem").progressbar("option", {
    value: 100,
    disabled: true
});
//禁用小部件和激活小部件
$("elem").progressbar("disable");
$("elem").progressbar("enable");
//销毁小部件
$("elem").progressbar("destroy");
//有些小部件生成包装器元素，widget方法返回生成的元素，如果小部件不生成包装器元素，则返回原始元素
$("elem").progressbar("widget");
//向小部件添加事件(bind方法)
$("elem").bind("progresschange", function () {
    alert("The value has changed!");
});
//也可以使用回调添加事件,这里用到了进度条的change方法
$("elem").progressbar({
    change: function () {
        alert("The value has changed!");
    }
});
//创建一个自己的小部件
$.widget("custom.progressbar", {
    _create: function () {
        var progress = this.options.value + "%";
        this.element
            .addClass("progressbar")
            .text(progress);
    }
});
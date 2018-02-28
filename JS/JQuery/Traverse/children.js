//获取直接子元素
$("div").children();
//获取筛选过的直接子元素，下面的表示获取div下的类为1的p元素
$("div").children("p.1");
//获取所有后代
$("div").find("*");
//获取为<span>的后代
$("div").find("span");



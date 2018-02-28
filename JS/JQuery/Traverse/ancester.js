//获取元素的直接祖先
$("span").parent();
//获取元素的所有祖先
$("span").parents();
//获取元素的所有是<li>的祖先（过滤）
$("span").parents("li");
//获取<span>和<div>之间的祖先
$("spam").parentsUntil("div");
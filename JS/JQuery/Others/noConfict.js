//noConflict()方法可以解除对$符号的控制
//$是jQuery的代替符号，解除$符号的控制后依然可以使用全称
$.noConflict();
//noConflict()方法可以返回对jQuery的引用，所以可以用它给jQuery起别名
var jq=$.noConflict();
//接下来就可以使用jq来代替jQuery($)
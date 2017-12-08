$(document).ready(function(){
    $("#btn-1").click(function(){
        $("p").hide();
    });
	$("#btn-2").click(function(){
        $("#test").hide();
    });
    $("#btn-3").click(function(){
        $(".my_class").hide();
    });
    $("#btn-4").click(function(){
        $(".my_class").show();
    });
	
});
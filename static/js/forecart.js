$(function () {
	$("img.cartProductItemIfSelected").click(function () {
	var selectit = $(this).attr("selectit")
	if("selectit"==selectit){
		$(this).attr("src",cartVaule.cartNotSelected)
		$(this).attr("selectit","false")
		$(this).parents("tr.cartProductItemTR").css("background-color","#fff");
	}
	else{
		$(this).attr("src",cartVaule.cartSelected)
		$(this).attr("selectit","selectit")
		$(this).parents("tr.cartProductItemTR").css("background-color","#FFF8E1");
	}
	syncSelect();
    syncCreateOrderButton();
    calcCartSumPriceAndNumber();
})
	//全选
	$("img.selectAllItem").click(function(){
    var selectit = $(this).attr("selectit")
    if("selectit"==selectit){
        $("img.selectAllItem").attr("src",cartVaule.cartNotSelected);
        $("img.selectAllItem").attr("selectit","false")
        $(".cartProductItemIfSelected").each(function(){
            $(this).attr("src",cartVaule.cartNotSelected);
            $(this).attr("selectit","false");
            $(this).parents("tr.cartProductItemTR").css("background-color","#fff");
        });
    }
    else{
        $("img.selectAllItem").attr("src",cartVaule.cartSelected);
        $("img.selectAllItem").attr("selectit","selectit")
        $(".cartProductItemIfSelected").each(function(){
            $(this).attr("src",cartVaule.cartSelected);
            $(this).attr("selectit","selectit");
            $(this).parents("tr.cartProductItemTR").css("background-color","#FFF8E1");
        });
    }
    syncSelect();
    syncCreateOrderButton();
    calcCartSumPriceAndNumber();
});
	$(".numberPlus").click(function(){
    var pid=$(this).attr("pid");
    var stock= $("span.orderItemStock[pid="+pid+"]").text();
    var price= $("span.orderItemPromotePrice[pid="+pid+"]").text();
    var num= $(".orderItemNumberSetting[pid="+pid+"]").val();
    num++;
    if(num>stock)
        num = stock;
    syncPrice(pid,num,price);
});
	$(".numberMinus").click(function(){
    var pid=$(this).attr("pid");
    var stock= $("span.orderItemStock[pid="+pid+"]").text();
    var price= $("span.orderItemPromotePrice[pid="+pid+"]").text();
    var num= $(".orderItemNumberSetting[pid="+pid+"]").val();
    --num;
    if(num<=0)
        num=1;
    syncPrice(pid,num,price);
});
	$(".orderItemNumberSetting").keyup(function(){
		var pid=$(this).attr("pid");
		var stock= $("span.orderItemStock[pid="+pid+"]").text();
		var price= $("span.orderItemPromotePrice[pid="+pid+"]").text();
		var num= $(".orderItemNumberSetting[pid="+pid+"]").val();
		num = parseInt(num);
		if(isNaN(num))
			num= 1;
		if(num<=0)
			num = 1;
		if(num>stock)
			num = stock;
		syncPrice(pid,num,price);
	});

    $("button.createOrderButton").click(function(){
        var params = "";
        $(".cartProductItemIfSelected").each(function(){
        if("selectit"==$(this).attr("selectit")){
            var oiid = $(this).attr("oiid");
            params += "&oiid="+oiid;
        }
    });
    params = params.substring(1);
    location.href=cartVaule.settlement+params;
});

})

/**
 * Created by 24102 on 2017/5/19.
 */
$(function () {
	//显示缩略图
	$("img.smallImage").mouseenter(
		function () {
			var bigImageURL = $(this).attr("bigImageURL");
			$("img.bigImg").attr("src",bigImageURL);
		}
	)
	//图片预加载
	$("img.bigImg").load(
	function(){
		$("img.smallImage").each(function(){
			var bigImageURL = $(this).attr("bigImageURL");
			img = new Image();
			img.src = bigImageURL;
			img.onload = function(){
				console.log(bigImageURL);
				$("div.img4load").append($(img));
			};
		});
	}
);
	//修改购买数量
	var stock = 3;
    $(".productNumberSetting").keyup(function(){
        var num= $(".productNumberSetting").val();
        num = parseInt(num);
        if(isNaN(num))
            num= 1;
        if(num<=0)
            num = 1;
        if(num>stock)
            num = stock;
        $(".productNumberSetting").val(num);
    });

    $(".increaseNumber").click(function(){
        var num= $(".productNumberSetting").val();
        num++;
        if(num>stock)
            num = stock;
        $(".productNumberSetting").val(num);
    });
    $(".decreaseNumber").click(function(){
        var num= $(".productNumberSetting").val();
        --num;
        if(num<=0)
            num=1;
        $(".productNumberSetting").val(num);
    });
	//切换商品详情和累计评价效果
	$("div.productReviewDiv").hide();
    $("a.productDetailTopReviewLink").click(function(){
        $("div.productReviewDiv").show();
        $("div.productDetailDiv").hide();
    });
    $("a.productReviewTopPartSelectedLink").click(function(){
        $("div.productReviewDiv").hide();
        $("div.productDetailDiv").show();
    });
})

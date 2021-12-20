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
	var stock = MyViewVar.stock;
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

    //监听购买按钮
    $(".buyLink").click(function(){
        var page = MyViewVar.foreBoughtPage;
        $.get(
                page,
                function(){
                    if (MyViewVar.is_login) {
                        var num = $(".productNumberSetting").val();
                        location.href = $(".buyLink").attr("href") + "&num=" + num;
                    } else {
                        $("#loginModal").modal('show');
                    }
                }
        );
        return false;
    });

    //加入购物车按钮监听
    $(".addCartButton").removeAttr("disabled");
    $(".addCartLink").click(function(){
        var page = MyViewVar.foreBoughtPage;
        $.get(
                page,
                function(){
                    if(MyViewVar.is_login){
                        var pid = MyViewVar.pid;
                        var num= $(".productNumberSetting").val();
                        var addCartpage = MyViewVar.foreAddCartPage;
                        $.get(
                                addCartpage,
                                {"pid":pid,"num":num},
                                function(ret){
                                    if("success"==ret){
                                        $(".addCartButton").html("已加入购物车");
                                        $(".addCartButton").attr("disabled","disabled");
                                        $(".addCartButton").css("background-color","lightgray")
                                        $(".addCartButton").css("border-color","lightgray")
                                        $(".addCartButton").css("color","black")

                                    }
                                    else{

                                    }
                                }
                        );
                    }
                    else{
                        $("#loginModal").modal('show');
                    }
                }
        );
        return false;
    });
});

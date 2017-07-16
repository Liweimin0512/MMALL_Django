/**
 * Created by 24102 on 2017/5/21.
 */

//以千进制格式化金额，比如金额时123456，就会显示为123，456
function formatMoney(num){
    num = num.toString().replace(/\$|\,/g,'');
    if(isNaN(num))
        num = "0";
    sign = (num == (num = Math.abs(num)));
    num = Math.floor(num*100+0.50000000001);
    cents = num%100;
    num = Math.floor(num/100).toString();
    if(cents<10)
    cents = "0" + cents;
    for (var i = 0; i < Math.floor((num.length-(1+i))/3); i++)
    num = num.substring(0,num.length-(4*i+3))+','+
    num.substring(num.length-(4*i+3));
    return (((sign)?'':'-') + num + '.' + cents);
}

//任意商品被选中时，结算按钮变为天猫红色，并且可点击状态，否则为灰色，且不可点击。
function syncCreateOrderButton(){
    var selectAny = false;
    $(".cartProductItemIfSelected").each(function(){
        if("selectit"==$(this).attr("selectit")){
            selectAny = true;
        }
    });
    if(selectAny){
        $("button.createOrderButton").css("background-color","#C40000");
        $("button.createOrderButton").removeAttr("disabled");
    }
    else{
        $("button.createOrderButton").css("background-color","#AAAAAA");
        $("button.createOrderButton").attr("disabled","disabled");
    }
}

//同步"全选"状态。 选中和未选中是采用了两个不同的图片实现的，遍历所有的商品，看是否全部都选中了，只要有任意一个没有选中，那么就不是全选状态。 然后通过切换图片显示是否全选状态的效果。
function syncSelect(){
    var selectAll = true;
    $(".cartProductItemIfSelected").each(function(){
        if("false"==$(this).attr("selectit")){
            selectAll = false;
        }
    });
    if(selectAll)
        $("img.selectAllItem").attr("src", baseVar.cartSelected);
    else
        $("img.selectAllItem").attr("src", baseVar.cartNotSelected);
}

//显示被选中的商品总数，以及总价格。
//遍历每个商品是否被选中，累加被选中商品的总数和总价格，然后修改在上方的总价格，以及下方的总价格，总数
function calcCartSumPriceAndNumber(){
    var sum = 0;
    var totalNumber = 0;
    $("img.cartProductItemIfSelected[selectit='selectit']").each(function(){
        var oiid = $(this).attr("oiid");
        var price =$(".cartProductItemSmallSumPrice[oiid="+oiid+"]").text();
        price = price.replace(/,/g, "");
        price = price.replace(/￥/g, "");
        sum += new Number(price);
        var num =$(".orderItemNumberSetting[oiid="+oiid+"]").val();
        totalNumber += new Number(num);
    });
    $("span.cartSumPrice").html("￥"+formatMoney(sum));
    $("span.cartTitlePrice").html("￥"+formatMoney(sum));
    $("span.cartSumNumber").html(totalNumber);
}

//根据商品数量，商品价格，同步小计价格，接着调用calcCartSumPriceAndNumber()函数同步商品总数和总价格
function syncPrice(pid,num,price){
    $(".orderItemNumberSetting[pid="+pid+"]").val(num);
    var cartProductItemSmallSumPrice = formatMoney(num*price);
    $(".cartProductItemSmallSumPrice[pid="+pid+"]").html("￥"+cartProductItemSmallSumPrice);
    calcCartSumPriceAndNumber();
}
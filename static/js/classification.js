$(function(){
	$("input.sortBarPrice").keyup(function(){
		var num= $(this).val();
		if(num.length==0){
			$("div.productUnit").show();
			return;
		}

		num = parseInt(num);
		if(isNaN(num))
			num= 1;
		if(num<=0)
			num = 1;
		$(this).val(num);

		var begin = $("input.beginPrice").val();
		var end = $("input.endPrice").val();
		if(!isNaN(begin) && !isNaN(end)){
			console.log(begin);
			console.log(end);
			$("div.productUnit").hide();
			$("div.productUnit").each(function(){
				var price = $(this).attr("price");
				price = new Number(price);

				if(price<=end && price>=begin)
					$(this).show();
			});
		}

	});
});
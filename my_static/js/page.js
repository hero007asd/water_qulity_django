$(document).ready(function(){
	
	var stat;
	
	//初始化自来水公司信息
	com();
	//鼠标点击 事件
	$(".p_corp").click(function(){
		var id=$(this).attr("id");
		$("a").removeClass("p_star");
		 $(this).addClass("p_star");
		if(id=="p_corp"){
			//自来水公司
		      $(this).addClass("p_star");
		      com();
			
			
		}else if(id=="p_star"){
			//行政区域
		      $(this).addClass("p_star");
			
		      area();
		}
	});
	

//行政区信息
$("#region").click(area); 
//自来水公司信息
$("#company").click(com);

//左右箭头滑动切换 
$("#w_con").click(function(){
	
	
	if($("#w_con").hasClass("w_con1")){
		$("#w_con").removeClass("w_con1");
		$("#w_con").addClass("w_con2");
		$(".w_content").stop(true,false).animate({"left":-500},500);
	}else{
		$("#w_con").removeClass("w_con2");
		$("#w_con").addClass("w_con1");
		$(".w_content").stop(true,false).animate({"left":0},500);
	}
});


//地图图标鼠标移出事件
$("#mapicon img").live("mouseout",function(){
	//鼠标移出时删除div
	$(".mapdiv").remove();
});

//地图图标鼠标放上去事件
$("#mapicon img").live("mouseover",function(){
	var id=$(this).attr("id");
	
	var left=$(this).offset().left;
	var top=$(this).offset().top;
	
	$.ajax({
		url:"http://localhost:8000/hardsocket/getOneSpotInfo?spot_id="+id+"",
		type:"GET",
		dataType:"json",
		
		success:function(data){
			var json=eval(data);
			
			
			var mapdiv=" <div class='mapdiv' style='top:"+(top-65)+"px;left:"+left+"px;' id='mapdiv'><table border='1' cellpadding='0' cellspacing='0'>"
			+"<tr class='a'><td>PH</td><td>电导率</td><td>溶解氧</td><td>余氯</td><td>浊度</td><td>水温</td></tr>"
			+"<tr class='b'><td>"+json["spot_ph"]+"</td><td>"+json["spot_conductivity"]+"</td><td>"+json["spot_DO"]+"</td><td>"+json["spot_rc"]+"</td><td>"+json["spot_turbidity"]+"</td><td>"+json["spot_temp"]+"</td></tr>"
			+"</table></div>";
			$("body").append(mapdiv);
			//判断检测值不合格标识出来
			if(json["ph_status"]==0){
				$(".a td:eq(0)").attr("style", "border:1px solid red;color:red");
				$(".b td:eq(0)").attr("style", "border:1px solid red;color:red");
			}else if(json["spot_conductivity"]==0){
				$(".a td:eq(1)").attr("style", "border:1px solid red;color:red");
				$(".b td:eq(1)").attr("style", "border:1px solid red;color:red");
			}else if(json["spot_DO"]==0){
				$(".a td:eq(2)").attr("style", "border:1px solid red;color:red");
				$(".b td:eq(2)").attr("style", "border:1px solid red;color:red");
			}else if(json["spot_rc"]==0){
				$(".a td:eq(3)").attr("style", "border:1px solid red;color:red");
				$(".b td:eq(3)").attr("style", "border:1px solid red;color:red");
			}else if(json["spot_turbidity"]==0){
				$(".a td:eq(4)").attr("style", "border:1px solid red;color:red");
				$(".b td:eq(4)").attr("style", "border:1px solid red;color:red");
			}else if(json["spot_temp"]==0){
				$(".a td:eq(5)").attr("style", "border:1px solid red;color:red");
				$(".b td:eq(5)").attr("style", "border:1px solid red;color:red");
			}
		}
	});
});

//地图图标鼠标点击事件
$("#mapicon img").live("click",function(){
	var id=$(this).attr("id");

	
	
	location.href="../report?id="+id+"";
	
});

//点击公司获取公司分公司的信息

$("#Map area").live("click",function(){
	
	var id=$(this).attr("class");
	if(stat==1){
		//1说明是公司
		$.ajax({
			url:"http://localhost:8000/hardsocket/getOneCorpInfo/?corp_id="+id+"",
			type:"GET",
//	 		 async: false, 
			 contentType:"application/x-www-form-urlencoded;charset=UTF-8", 
//	 		data:{city_id:"310000"},
			dataType:"json",
			
			
			success:function(data){
				var json=eval(data);


				var content="<table width='550' border='0' cellspacing='0' cellpadding='1'><tr><td class='line005'><table width='100%' border='0' cellspacing='0' cellpadding='0'><tr> <td height='50' colspan='6' background='../../site_media/img/005.jpg'><table width='100%' border='0' cellpadding='0' cellspacing='0' class='f20px'> <tr><td width='50' align='center'><img src='../../site_media/img/009.png' alt='' width='11' height='11' /></td> <td>"+json['corp_info'][0]['corp_name']+"</td> <td width='100' align='center'><img src='../../site_media/img/dy.png' width='78' height='27' /></td></tr> </table></td><td background='../../site_media/img/005.jpg' height='50' colspan='6'></td></tr>";
			content+="<tr><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>自来水公司</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>浊度(ntu)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>PH值 </td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>余氯 (mg/L)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>电导率(ms/mv)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>溶解氧(mq/l)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>温度</td></tr>";



				$(".p_right").empty();
				
				for ( var y = 0; y < json['corp_info'].length; y++) {

					if (y%2==0) {
					if((json['corp_info'][y]['spot_ph'])>=5&&(json['corp_info'][y]['spot_ph'])<=9){
					content+="<tr><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corpChild_name']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_ph']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'"+json['corp_info'][y]['spot_conductivity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_DO']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_rc']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_turbidity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_temp']+"</td></tr>";
				}else{
					content+="<tr><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corpChild_name']+"</td><td style='color:red' align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_ph']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_conductivity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_DO']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_rc']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_turbidity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['spot_temp']+"</tr>";
				}

				
			}else
			{
				if((json['corp_info'][y]['spot_ph'])>=5&&(json['corp_info'][y]['spot_ph'])<=9){
					content+="<tr><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corpChild_name']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_ph']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_conductivity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_DO']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_rc']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_turbidity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_temp']+"</td></tr>";
				}else{
					content+="<tr><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corpChild_name']+"</td><td style='color:red' align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['area_ph']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_conductivity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_DO']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_rc']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_turbidity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['spot_temp']+"</td></tr>";
				}

			}




					
				}
				content+="</table>";
				$(".p_right").append(content);
				
				
				
				
				//检测点
				$("#mapicon").empty();
				for (var x = 0;  x< json['spot_info'].length; x++) {
					var st=json['spot_info'][x]['spot_status'];
					if(st==1){
						var img="<img src='../../site_media/img/icongreen.png' id='2"+json['spot_info'][x]['spot_id']+"' style='width:40px;height:45px;'/>";
						$("#mapicon").append(img);
						$("#2"+json['spot_info'][x]['spot_id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
					 	$("#2"+json['spot_info'][x]['spot_id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
					}else if(st==0){
						var img="<img src='../../site_media/img/iconred.png' id='2"+json['spot_info'][x]['spot_id']+"'/>";
						$("#mapicon").append(img);
						$("#2"+json['spot_info'][x]['spot_id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
					 	$("#2"+json['spot_info'][x]['spot_id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
					}
				}
			},
			error:function(XMLHttpRequest, textStatus, errorThrown){
	            alert(XMLHttpRequest.status);
	            alert(XMLHttpRequest.readyState);
	            alert(textStatus);
			}
		
		});
		
		
	}else if(stat==2){
		
	var id=$(this).attr("class");
		//2说明是行政区
			$.ajax({
			url:"http://localhost:8000/hardsocket/getOneAreaInfo/?area_id="+id+"",
			type:"GET",
//	 		 async: false, 
			 contentType:"application/x-www-form-urlencoded;charset=UTF-8", 
//	 		data:{city_id:"310000"},
			dataType:"json",
			
			
			success:function(data){
				var json=eval(data);

				var content="<table width='550' border='0' cellspacing='0' cellpadding='1'><tr><td class='line005'><table width='100%' border='0' cellspacing='0' cellpadding='0'><tr> <td height='50' colspan='6' background='../../site_media/img/005.jpg'><table width='100%' border='0' cellpadding='0' cellspacing='0' class='f20px'> <tr><td width='50' align='center'><img src='../../site_media/img/009.png' alt='' width='11' height='11' /></td> <td>"+json['area_info'][0]['area_anme']+"</td> <td width='100' align='center'><img src='../../site_media/img/dy.png' width='78' height='27' /></td></tr> </table></td><td background='../../site_media/img/005.jpg' height='50' colspan='6'></td></tr>";
			content+="<tr><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>上海行政区检测点</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>浊度(ntu)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>PH值 </td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>余氯 (mg/L)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>电导率(ms/mv)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>溶解氧(mq/l)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>温度</td></tr>";



				$(".p_right").empty();
				
				for ( var y = 0; y < json['area_info'].length; y++) {

					if (y%2==0) {
					
					content+="<tr><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['areaChild_name']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_ph']>=5&&json['area_info'][y]['corp_ph']<=9?'color:red':'color:white'+"</td><td align='center' background='../../site_media/img/007.png' class='line001'"+json['area_info'][y]['area_conductivity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_DO']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_rc']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_turbidity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_temp']+"</td></tr>";
				
				
			}else
			{
				if((json['area_info'][y]['corp_ph'])>=5&&(json['area_info'][y]['corp_ph'])<=9){
					content+="<tr><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['areaChild_name']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_ph']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_conductivity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_DO']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_rc']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_turbidity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_temp']+"</td></tr>";
				}else{
					content+="<tr><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['areaChild_name']+"</td><td style='color:red' align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_ph']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_conductivity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_DO']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_rc']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_turbidity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_temp']+"</td></tr>";
				}

			}

					
				}
				content+="</table>";
				$(".p_right").append(content);
				
				
				
				
				//检测点
				$("#mapicon").empty();
				for ( var x = 0;  x< json['spot_info'].length; x++) {
					var st=json['spot_info'][x]['spot_status'];
					if(st==1){
						var img="<img src='../../site_media/img/icongreen.png' id='"+json['spot_info'][x]['spot_id']+"' style='width:40px;height:45px;'/>";
						$("#mapicon").append(img);
						$("#"+json['spot_info'][x]['spot_id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
					 	$("#"+json['spot_info'][x]['spot_id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
					}else if(st==0){
						var img="<img src='../../site_media/img/iconred.png' id='"+json['spot_info'][x]['spot_id']+"'/>";
						$("#mapicon").append(img);
						$("#"+json['spot_info'][x]['spot_id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
					 	$("#"+json['spot_info'][x]['spot_id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
					}
				}
			},
			error:function(XMLHttpRequest, textStatus, errorThrown){
	            alert(XMLHttpRequest.status);
	            alert(XMLHttpRequest.readyState);
	            alert(textStatus);
			}
		
		
			});
		
		
	}
	
		
	
});


function com(){
	//公司信息(首页)
	stat=1;
	
	$(".p_left").empty();
	$(".p_left").append("<img src='../../site_media/img/004.jpg' width='60%' height='840px;' border='0' usemap='#Map' style='z-index:0;'/><map name='Map' id='Map'>"
			  	+" <area shape='poly' coords='412,107,424,131,432,146,431,159,423,171,428,181,435,189,439,202,445,212,452,220,449,229,445,237,430,238,420,244,424,247,432,247,440,249,453,254,460,263,454,273,441,277,431,283,421,288,407,279,386,267,363,267,337,273,314,267,302,256,290,249,281,236,274,219,267,207,259,198,260,186,299,147,321,131,344,116,361,109,361,111' href='#' title='嘉定区' class='1' />"
			    +"<area shape='poly' coords='363,269,361,277,368,286,373,295,381,305,387,309,398,308,408,316,416,327,422,338,411,342,398,347,388,354,379,362,368,367,354,370,342,368,336,361,325,354,313,357,305,365,299,375,289,385,277,391,263,385,253,380,241,378,235,385,237,394,246,404,249,412,249,420,240,424,226,420,218,418,220,431,226,438,224,450,220,469,215,489,208,502,197,505,183,499,177,497,167,506,162,517,157,528,141,523,131,519,127,514,122,505,127,494,131,479,130,465,124,457,109,454,97,454,84,458,73,460,62,461,50,458,48,450,50,439,54,425,58,414,57,401,51,392,41,388,32,386,28,377,31,367,49,358,65,361,75,364,86,356,94,352,105,355,117,357,131,358,143,359,155,355,165,349,174,354,183,359,192,361,194,348,197,342,210,345,218,346,219,323,216,307,216,290,217,277,215,268,210,263,215,257,230,251,239,247,260,253,277,253,291,252,303,261,317,270,330,276,350,273,361,269' href='#' title='青浦区' class='2'/>"
			    +"<area shape='poly' coords='421,339,436,352,454,379,458,402,437,429,430,461,422,482,454,485,457,513,448,540,451,550,409,545,390,545,380,551,355,548,342,534,315,540,287,546,267,538,232,557,225,538,216,531,197,554,179,560,165,553,154,541,159,526,168,508,177,500,190,503,198,507,209,502,218,481,223,463,226,448,226,439,221,429,220,420,234,424,246,423,250,410,240,395,237,383,245,378,257,383,278,393,299,375,314,359,328,355,338,364,347,371,363,370,379,361,394,349,413,341,420,340' href='#'  title='松江区' class='3'/>"
			    +"<area shape='poly' coords='452,550,479,600,485,616,509,624,526,634,547,652,513,673,493,697,470,726,441,746,420,746,402,751,374,767,358,755,360,730,364,719,346,701,326,688,323,668,307,676,284,685,260,682,243,678,229,655,249,624,230,617,213,608,199,605,166,623,156,638,139,625,125,625,107,630,103,621,108,607,132,589,129,575,119,567,125,547,126,529,127,523,122,509,137,525,153,526,157,539,160,550,172,558,187,560,199,550,209,540,217,533,227,547,233,557,266,540,280,543,287,548,315,541,339,534,355,547,383,550,390,545,426,548' href='#' title='金山区'/>"
			    +"<area shape='poly' coords='548,652,577,642,609,631,637,623,671,615,703,611,718,607,738,603,756,603,771,600,793,603,815,606,832,608,831,525,814,504,785,488,749,470,728,469,702,471,676,464,644,463,631,470,606,468,582,460,564,454,537,462,473,485,455,485,457,514,448,542,458,561,473,590,485,617,505,623,521,632,548,651' href='#' title='奉贤区' />"
			    +"<area shape='poly' coords='834,606,855,605,883,598,902,596,926,592,948,580,959,555,952,528,941,477,928,462,842,351,782,368,764,355,741,360,738,350,732,342,712,359,692,354,690,336,599,329,599,340,610,353,605,362,596,364,615,368,633,378,618,396,631,401,616,419,626,431,622,444,636,456,647,463,672,464,697,470,727,470,749,472,763,477,784,487,807,502,825,513,832,523,834,603,834,603' href='#' title='南汇区' />"
			    +" <area shape='poly' coords='601,365,616,369,629,377,621,394,630,403,617,419,625,433,622,444,643,463,629,470,613,469,567,455,471,487,456,486,423,482,432,458,435,437,439,429,457,408,457,385,403,309,387,309,369,285,365,268,385,268,411,286,431,284,435,297,428,314,439,322,463,319,473,322,524,380,545,372,564,361,592,363,601,366' href='#' title='闵行区' />"
			    +"<area shape='poly' coords='837,350,812,358,785,368,766,354,743,360,733,343,714,359,694,354,691,337,602,330,599,341,610,356,601,365,574,362,553,367,544,353,545,333,555,317,570,308,577,296,572,276,588,268,605,263,622,254,622,237,616,213,581,199,573,187,577,172,600,175,619,185,637,187,658,199,678,211,692,219,709,221,727,230,754,252,788,289,820,324,838,350,838,350' href='#' title='浦东新区'/>"
			    +"<area shape='poly' coords='576,171,570,184,576,195,561,206,559,226,542,219,529,225,505,231,493,250,473,239,447,237,455,222,441,199,435,185,426,169,432,159,434,146,414,107,415,99,435,100,450,102,478,112,512,132,539,146,557,158,567,158,576,172' href='#' title='宝山区' />"
			    +"<area shape='poly' coords='546,320,542,333,543,351,544,364,551,369,534,378,524,379,506,356,488,335,482,325,497,321,507,312,511,306,525,302,538,313,546,321' href='#' title='徐汇区'/><area shape='poly' coords='482,325,469,319,440,323,430,315,432,303,437,292,434,283,440,279,452,290,467,290,487,290,496,291,504,286,511,301,504,312,495,321,483,325' href='#' title='长宁区'/>"
			    +"<area shape='poly' coords='553,320,528,302,538,292,546,289,562,312,548,320' href='#' /><area shape='poly' coords='529,302,521,302,511,307,507,286,510,272,519,268,530,273,535,279,538,292,530,302' href='#' />"
			    +"<area shape='poly' coords='564,310,576,298,574,277,565,273,555,274,536,278,539,291,545,289,561,309' href='#' /><area shape='poly' coords='498,290,453,289,443,278,455,273,461,263,455,251,439,249,423,244,432,237,447,237,474,238,490,249,498,246,513,249,522,260,502,287' href='#' /><area shape='poly' coords='562,272,536,276' href='#' />"
			    +"<area shape='poly' coords='560,274,537,276,517,268,523,259,512,248,500,245,506,233,517,229,525,227,538,241,538,251,549,251,562,266,562,274' href='#' /><area shape='poly' coords='573,275,564,274,563,267,551,251,540,251,541,243,528,226,544,221,556,229,565,236,574,241,583,252,594,267,576,275' href='#' /><area shape='poly' coords='597,266,613,258,623,252,620,229,617,213,579,199,572,199,565,205,560,226,571,242,587,259,596,265' href='#' /><area shape='poly' coords='831,184' href='#' />"
			 	+"<area shape='poly' coords='829,184,821,176,812,170,800,170,780,166,767,163,752,159,730,153,716,147,695,142,685,145,667,139,645,131,624,121,599,114,579,108,567,100,542,90,530,81,529,74,522,72,513,69,508,70,496,70,492,61,475,49,478,38,492,34,509,27,531,26,551,26,572,32,588,46,598,54,618,55,634,71,645,71,662,87,679,91,704,97,736,108,762,115,783,125,809,129,830,136,844,142,852,148,849,165,846,176,832,184' href='#' title='崇明岛'/>"   
			 	+" </map>"
			    +"<div class='mapicon' id='mapicon'> </div>");
	
	
	
	$.ajax({
		url:"http://localhost:8000/hardsocket/getAllCorpAvgInfo/?city_id=310000",
		type:"GET",
// 		 async: false, 
		// contentType:"application/x-www-form-urlencoded;charset=UTF-8", 
// 		data:{city_id:"310000"},
		dataType:"json",
	//	jsonp:"jsonpcallback",
		
		success:function(data){
			var json=eval(data);
			
			$(".p_right").empty();
		
			var content="<table width='550' border='0' cellspacing='0' cellpadding='1'><tr><td class='line005'><table width='100%' border='0' cellspacing='0' cellpadding='0'><tr> <td height='50' colspan='6' background='../../site_media/img/005.jpg'><table width='100%' border='0' cellpadding='0' cellspacing='0' class='f20px'> <tr><td width='50' align='center'><img src='../../site_media/img/009.png' alt='' width='11' height='11' /></td> <td>上海自来水市北有限公司</td> <td width='100' align='center'><img src='../../site_media/img/dy.png' width='78' height='27' /></td></tr> </table></td><td background='../../site_media/img/005.jpg' height='50' colspan='6'></td></tr>";
			content+="<tr><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>上海自来水公司</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>浊度(ntu)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>PH值 </td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>余氯 (mg/L)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>电导率(ms/mv)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>溶解氧(mq/l)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>温度</td></tr>";
			
			
			for ( var y = 0; y < json['corp_info'].length; y++) {
				//style='"+(json['corp_info'][y]['corp_ph']>=5&&json['corp_info'][y]['corp_ph']<=9?'color:red':'color:black')+"'
				
				if (y%2==0) {
					
					content+="<tr><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corp_name']+"</td><td align='center' background='../../site_media/img/007.png' class='line001' style='"+(json['corp_info'][y]['corp_ph']>=5&&json['corp_info'][y]['corp_ph']<=9?'color:white':'color:red')+"'>"+json['corp_info'][y]['corp_ph']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corp_conductivity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corp_DO']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corp_rc']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corp_turbidity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['corp_info'][y]['corp_temp']+"</td></tr>";
			
			}
			else
			{
				
					content+="<tr><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corp_name']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'style='"+(json['corp_info'][y]['corp_ph']>=5&&json['corp_info'][y]['corp_ph']<=9?'color:white':'color:red')+"'>"+json['corp_info'][y]['corp_ph']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corp_conductivity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corp_DO']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corp_rc']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corp_turbidity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['corp_info'][y]['corp_temp']+"</td></tr>";
			}
		}
			content+="</table></td></tr></table>";
			
			$(".p_right").append(content);
			
	
			//检测点
			$("#mapicon").empty();
			for ( var x = 0;  x< json['spot_info'].length; x++) {
				var st=json['spot_info'][x]['spot_status'];
				if(st==1){
					var img="<img src='../../site_media/img/icongreen.png' id='"+json['spot_info'][x]['id']+"'/>";
					$("#mapicon").append(img);
					$("#"+json['spot_info'][x]['id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
				 	$("#"+json['spot_info'][x]['id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
				}else if(st==0){
					var img="<img src='../../site_media/img/iconred.png' id='0"+json['spot_info'][x]['id']+"'/>";
					$("#mapicon").append(img);
					$("#"+json['spot_info'][x]['id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
				 	$("#"+json['spot_info'][x]['id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
				}
			}
		},
		error:function(XMLHttpRequest, textStatus, errorThrown){
            alert(XMLHttpRequest.status);
            alert(XMLHttpRequest.readyState);
            alert(textStatus);
		}
	});
	
};

function area(){
	//行政区信息(首页)
stat=2;
	
$(".p_left").empty();
$(".p_left").append("<img src='../../site_media/img/004.jpg' width='980' height='840' border='0' usemap='#Map' style='z-index:0;'/><map name='Map' id='Map'>"
		  	+" <area shape='poly' coords='412,107,424,131,432,146,431,159,423,171,428,181,435,189,439,202,445,212,452,220,449,229,445,237,430,238,420,244,424,247,432,247,440,249,453,254,460,263,454,273,441,277,431,283,421,288,407,279,386,267,363,267,337,273,314,267,302,256,290,249,281,236,274,219,267,207,259,198,260,186,299,147,321,131,344,116,361,109,361,111' href='#' title='嘉定区' class='1'/>"
		    +"<area shape='poly' coords='363,269,361,277,368,286,373,295,381,305,387,309,398,308,408,316,416,327,422,338,411,342,398,347,388,354,379,362,368,367,354,370,342,368,336,361,325,354,313,357,305,365,299,375,289,385,277,391,263,385,253,380,241,378,235,385,237,394,246,404,249,412,249,420,240,424,226,420,218,418,220,431,226,438,224,450,220,469,215,489,208,502,197,505,183,499,177,497,167,506,162,517,157,528,141,523,131,519,127,514,122,505,127,494,131,479,130,465,124,457,109,454,97,454,84,458,73,460,62,461,50,458,48,450,50,439,54,425,58,414,57,401,51,392,41,388,32,386,28,377,31,367,49,358,65,361,75,364,86,356,94,352,105,355,117,357,131,358,143,359,155,355,165,349,174,354,183,359,192,361,194,348,197,342,210,345,218,346,219,323,216,307,216,290,217,277,215,268,210,263,215,257,230,251,239,247,260,253,277,253,291,252,303,261,317,270,330,276,350,273,361,269' href='#' title='青浦区' class='2'/>"
		    +"<area shape='poly' coords='421,339,436,352,454,379,458,402,437,429,430,461,422,482,454,485,457,513,448,540,451,550,409,545,390,545,380,551,355,548,342,534,315,540,287,546,267,538,232,557,225,538,216,531,197,554,179,560,165,553,154,541,159,526,168,508,177,500,190,503,198,507,209,502,218,481,223,463,226,448,226,439,221,429,220,420,234,424,246,423,250,410,240,395,237,383,245,378,257,383,278,393,299,375,314,359,328,355,338,364,347,371,363,370,379,361,394,349,413,341,420,340' href='#'  title='松江区' />"
		    +"<area shape='poly' coords='452,550,479,600,485,616,509,624,526,634,547,652,513,673,493,697,470,726,441,746,420,746,402,751,374,767,358,755,360,730,364,719,346,701,326,688,323,668,307,676,284,685,260,682,243,678,229,655,249,624,230,617,213,608,199,605,166,623,156,638,139,625,125,625,107,630,103,621,108,607,132,589,129,575,119,567,125,547,126,529,127,523,122,509,137,525,153,526,157,539,160,550,172,558,187,560,199,550,209,540,217,533,227,547,233,557,266,540,280,543,287,548,315,541,339,534,355,547,383,550,390,545,426,548' href='#' title='金山区' class='3'/>"
		    +"<area shape='poly' coords='548,652,577,642,609,631,637,623,671,615,703,611,718,607,738,603,756,603,771,600,793,603,815,606,832,608,831,525,814,504,785,488,749,470,728,469,702,471,676,464,644,463,631,470,606,468,582,460,564,454,537,462,473,485,455,485,457,514,448,542,458,561,473,590,485,617,505,623,521,632,548,651' href='#' title='奉贤区' />"
		    +"<area shape='poly' coords='834,606,855,605,883,598,902,596,926,592,948,580,959,555,952,528,941,477,928,462,842,351,782,368,764,355,741,360,738,350,732,342,712,359,692,354,690,336,599,329,599,340,610,353,605,362,596,364,615,368,633,378,618,396,631,401,616,419,626,431,622,444,636,456,647,463,672,464,697,470,727,470,749,472,763,477,784,487,807,502,825,513,832,523,834,603,834,603' href='#' title='南汇区' />"
		    +" <area shape='poly' coords='601,365,616,369,629,377,621,394,630,403,617,419,625,433,622,444,643,463,629,470,613,469,567,455,471,487,456,486,423,482,432,458,435,437,439,429,457,408,457,385,403,309,387,309,369,285,365,268,385,268,411,286,431,284,435,297,428,314,439,322,463,319,473,322,524,380,545,372,564,361,592,363,601,366' href='#' title='闵行区' />"
		    +"<area shape='poly' coords='837,350,812,358,785,368,766,354,743,360,733,343,714,359,694,354,691,337,602,330,599,341,610,356,601,365,574,362,553,367,544,353,545,333,555,317,570,308,577,296,572,276,588,268,605,263,622,254,622,237,616,213,581,199,573,187,577,172,600,175,619,185,637,187,658,199,678,211,692,219,709,221,727,230,754,252,788,289,820,324,838,350,838,350' href='#' title='浦东新区'/>"
		    +"<area shape='poly' coords='576,171,570,184,576,195,561,206,559,226,542,219,529,225,505,231,493,250,473,239,447,237,455,222,441,199,435,185,426,169,432,159,434,146,414,107,415,99,435,100,450,102,478,112,512,132,539,146,557,158,567,158,576,172' href='#' title='宝山区' />"
		    +"<area shape='poly' coords='546,320,542,333,543,351,544,364,551,369,534,378,524,379,506,356,488,335,482,325,497,321,507,312,511,306,525,302,538,313,546,321' href='#' title='徐汇区'/><area shape='poly' coords='482,325,469,319,440,323,430,315,432,303,437,292,434,283,440,279,452,290,467,290,487,290,496,291,504,286,511,301,504,312,495,321,483,325' href='#' title='长宁区'/>"
		    +"<area shape='poly' coords='553,320,528,302,538,292,546,289,562,312,548,320' href='#' /><area shape='poly' coords='529,302,521,302,511,307,507,286,510,272,519,268,530,273,535,279,538,292,530,302' href='#' />"
		    +"<area shape='poly' coords='564,310,576,298,574,277,565,273,555,274,536,278,539,291,545,289,561,309' href='#' /><area shape='poly' coords='498,290,453,289,443,278,455,273,461,263,455,251,439,249,423,244,432,237,447,237,474,238,490,249,498,246,513,249,522,260,502,287' href='#' /><area shape='poly' coords='562,272,536,276' href='#' />"
		    +"<area shape='poly' coords='560,274,537,276,517,268,523,259,512,248,500,245,506,233,517,229,525,227,538,241,538,251,549,251,562,266,562,274' href='#' /><area shape='poly' coords='573,275,564,274,563,267,551,251,540,251,541,243,528,226,544,221,556,229,565,236,574,241,583,252,594,267,576,275' href='#' /><area shape='poly' coords='597,266,613,258,623,252,620,229,617,213,579,199,572,199,565,205,560,226,571,242,587,259,596,265' href='#' /><area shape='poly' coords='831,184' href='#' />"
		 	+"<area shape='poly' coords='829,184,821,176,812,170,800,170,780,166,767,163,752,159,730,153,716,147,695,142,685,145,667,139,645,131,624,121,599,114,579,108,567,100,542,90,530,81,529,74,522,72,513,69,508,70,496,70,492,61,475,49,478,38,492,34,509,27,531,26,551,26,572,32,588,46,598,54,618,55,634,71,645,71,662,87,679,91,704,97,736,108,762,115,783,125,809,129,830,136,844,142,852,148,849,165,846,176,832,184' href='#' title='崇明岛'/>"   
		 	+" </map>"
		    +"<div class='mapicon' id='mapicon'> </div>");
	//www.wetouching.com
	$.ajax({
		url:"http://localhost:8000/hardsocket/getAreaAvgInfo?city_id=310000",
		type:"GET",
// 		 async: false, 
// 		 contenttype :"application/x-www-form-urlencoded;charset=utf-8", 
// 		data:{city_id:"310000"},
		dataType:"json",
		

		
		success:function(data){
			var json=eval(data);

			$(".p_right").empty();
			
			var content="<table width='550' border='0' cellspacing='0' cellpadding='1'><tr><td class='line005'><table width='100%' border='0' cellspacing='0' cellpadding='0'><tr> <td height='50' colspan='6' background='../../site_media/img/005.jpg'><table width='100%' border='0' cellpadding='0' cellspacing='0' class='f20px'> <tr><td width='50' align='center'><img src='../../site_media/img/009.png' alt='' width='11' height='11' /></td> <td>上海行政区</td> <td width='100' align='center'><img src='../../site_media/img/dy.png' width='78' height='27' /></td></tr> </table></td><td background='../../site_media/img/005.jpg' height='50' colspan='6'></td></tr>";
			content+="<tr><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>上海行政区</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>浊度(ntu)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>PH值 </td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>余氯 (mg/L)</td><td align='center' background='../../site_media/img/006_1.jpg' class='line003'>电导率(ms/mv)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>溶解氧(mq/l)</td><td  align='center' background='../../site_media/img/006_1.jpg' class='line003'>温度</td></tr>";
			
			for ( var y = 0; y < json['area_info'].length; y++) {
				//style='"+(json['corp_info'][y]['corp_ph']>=5&&json['corp_info'][y]['corp_ph']<=9?'color:red':'color:black')+"'
				
				if (y%2==0) {
						
					content+="<tr><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['areaName']+"</td><td align='center' background='../../site_media/img/007.png' class='line001' style='"+(json['area_info'][y]['area_ph']>=5&&json['area_info'][y]['area_ph']<=9?'color:white':'color:red')+"'>"+(json['area_info'][y]['area_ph']==null?'--':json['area_info'][y]['area_ph'])+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_conductivity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_DO']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_rc']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_turbidity']+"</td><td align='center' background='../../site_media/img/007.png' class='line001'>"+json['area_info'][y]['area_temp']+"</td></tr>";

				}else
				{
					
					content+="<tr><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['areaName']+"</td><td align='center' background='../../site_media/img/008.png' class='line001' style='"+(json['area_info'][y]['area_ph']>=5&&json['area_info'][y]['area_ph']<=9?'color:white':'color:red')+"''>"+json['area_info'][y]['area_ph']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_conductivity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_DO']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_rc']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_turbidity']+"</td><td align='center' background='../../site_media/img/008.png' class='line001'>"+json['area_info'][y]['area_temp']+"</td></tr>";
				
				};	

				
			}
			content+="</table></td></tr></table>";
			
			$(".p_right").append(content);
			
//			/*设置表格样式(偶数奇数切换颜色)*/
//			$("#conTab").find("tr").css("background-color", "#f5f7ea");
//			$("#conTab").find("tr:odd").css("background-color", "#eee0a7");
//			
			
			//检测点
			$("#mapicon").empty();
			for ( var x = 0;  x< json['spot_info'].length; x++) {
				var st=json['spot_info'][x]['spot_status'];
				if(st==1){
					var img="<img src='../../site_media/img/icongreen.png' id='"+json['spot_info'][x]['spot_id']+"'/>";
					$("#mapicon").append(img);
					
					$("#"+json['spot_info'][x]['spot_id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
				 	$("#"+json['spot_info'][x]['spot_id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
				}else if(st==0){
					var img="<img src='../../site_media/img/iconred.png' id='"+json['spot_info'][x]['spot_id']+"'/>";
					$("#mapicon").append(img);
					$("#"+json['spot_info'][x]['spot_id']).css("top",""+json['spot_info'][x]['y_pos']+"px"); 
				 	$("#"+json['spot_info'][x]['spot_id']).css("left",""+json['spot_info'][x]['x_pos']+"px");
				}
			}
		},
		error:function(XMLHttpRequest, textStatus, errorThrown){
            alert(XMLHttpRequest.status);
            alert(XMLHttpRequest.readyState);
            alert(textStatus);
		}
	});
}


});
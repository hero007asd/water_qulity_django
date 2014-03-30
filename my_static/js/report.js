//返回按钮状态
var st;
//趋势图放大或缩小状态
var star;
//趋势图状态(是总公司还是分公司的趋势图)
var tu;



//趋势图值
var res1= new Array();
var res2= new Array();
var res3= new Array();
var res4= new Array();
var res5= new Array();
var res6= new Array();
var  color =new Array('#AF0202','#99CDFB','#3366FB','#0000FA','#F8CC00',
			'#F89900','#F76600', '#EC7A00', '#FCD200', '#81C714',
			'#FA5E1F', '#FDCB3F', '#71D743', '#D23333', '#BAE73F',
			'#AB7B55', '#B381C9','#A5DBFC', '#CDE8FA', '#D9F0FA', 
			'#0099F9', '#1BA4F9', '#41B2FA', '#63C1FA', '#83CDFA',
			'#0673B8', '#0091F1', '#F85900', '#1CC2E6', '#C32121');

jQuery(document).ready(function(){

	var url=window.location.href;
	if(url.indexOf("id")>=0)
	{
		//有id代表是某个检测点的信息,显示检测点信息
		st=5;
		var wen=url.split("?");
		var arrm=wen[1];
		var de=arrm.split("=");
		var ids=de[1];

		
		$.ajax({
		url:"http://localhost:8000/hardsocket/getSpotDetailInfo?spot_id="+ids+"",
		type:"GET",
		dataType:"json",
		
		success:function(data){
			var json=eval(data);
			$(".r_top").append("<input type='button' class='backs' value='返回'/>");
			$(".r_con").append("<div class='r_con1'></div><div class='r_con2'></div>");
			$(".r_con1").append("<table border='1' cellpadding='0' cellspacing='0' id='r_re'></table>");
			var con="<tr><th colspan='25'>"+json['corp_name']+json['area_name']+json['spot_name']+"</th></tr><tr><td>参数</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td></tr>";
			
			var con1;
			var con2;
			var con3;
			var con4;
			var con5;
			var con6;
			
			
			for ( var y = 0; y < json['spt_detail'].length; y++) {
				
				con1+="<td style='"+(json['spt_detail'][y]['ph_status']==1?'color:red':'color:white')+"' class='line001'>"+json['spt_detail'][y]['spot_ph']+"</td>";
				con2+="<td style='"+(json['spt_detail'][y]['conductivity_status']==1?'color:red':'color:white')+"' class='line001'>"+json['spt_detail'][y]['spot_conductivity']+"</td>";
				con3+="<td style='"+(json['spt_detail'][y]['do_status']==1?'color:red':'color:white')+"' class='line001'>"+json['spt_detail'][y]['spot_DO']+"</td>";
				con4+="<td style='"+(json['spt_detail'][y]['rc_status']==1?'color:red':'color:white')+"' class='line001'>"+json['spt_detail'][y]['spot_rc']+"</td>";
				con5+="<td style='"+(json['spt_detail'][y]['turbidity_status']==1?'color:red':'color:white')+"' class='line001'>"+json['spt_detail'][y]['spot_turbidity']+"</td>";
				con6+="<td style='"+(json['spt_detail'][y]['temp_status']==1?'color:red':'color:white')+"' class='line001'>"+json['spt_detail'][y]['spot_temp']+"</td>";
				
			}
			
			con+="<tr><td width='100'>PH</td>"+con1+"</tr>";
			con+="<tr><td width='100'>电导率</td>"+con2+"</tr>";
			con+="<tr><td width='100'>溶解氧</td>"+con3+"</tr>";
			con+="<tr><td width='100'>余氯</td>"+con4+"</tr>";
			con+="<tr><td width='100'>浊度</td>"+con5+"</tr>";
			con+="<tr><td width='100'>温度</td>"+con6+"</tr>";
			$("#r_re").append(con);
			
			$(".r_con2").append("<input type='button' value='PH值本日趋势' id='r1'/><input type='button' value='电导率值本日趋势' id='r1'/><input type='button' value='溶解氧值本日趋势' id='r1'/><input type='button' value='余氯值本日趋势' id='r1'/><input type='button' value='浊度值本日趋势' id='r1'/><input type='button' value='温度值本日趋势' id='r1'/>");
			
			
			/*设置表格样式(偶数奇数切换颜色)*/
			$("#r_re").find("tr").css("background-image", "url(../../site_media/img/007.png)");
			$("#r_re").find("tr:odd").css("background-image", "url(../../site_media/img/008.png)");
		}
	});
	}
	
	if(url.indexOf("stat")>=0){
		//stat=1代表报表，stat=2代表趋势图
		var wen=url.split("?");
		var arrm=wen[1];
		var de=arrm.split("=");
		var ids=de[1];
		if(ids==1){
			allrep();
		}else if(ids==2){
			corpTu(1);
		}
	}

	
	
	/*返回按钮*/
$(".backs").live('click',function(){
	if(st==1||st==3||st==5){
		//1是总公司，返回总页,3是趋势图，返回 总页，5是某个检测点信息，返回 总页
		location.href="../aa";
	}else if(st==2){
		//是子公司 返回总公司
		allrep();
	}
//	else if(st==4){
//		//进入某个趋势图之一   返回总览图
//		trend(0);
//	}
});
	
//点击下拉框
$(".r_con div").live('click',function(){
	st=4;
	star=1;
	var id=$(this).attr("id");
	$(".r_top").empty();
	$(".r_top").append("<input type='button' class='backs' value='返回'/><span class='maspan'>选择参数：</span>"
						+"<select class='mapsele' id='mapsele' onchange='selectid()'><option value='divmap1'>PH值</option><option value='divmap2'>电导率</option><option value='divmap3'>溶解氧</option><option value='divmap4'>余氯</option><option value='divmap5'>浊度</option><option value='divmap6'>温度</option></select>");
	
	//方法
	selectid(id);
});	
});

//下拉框触发事件方法
function selectid(id){
	if(id==""||id==null){
		id=$(".mapsele").val();
	}
	if(id=="divmap1"){
		$(".r_con").empty();
		$(".r_con").append("<div class='r_divcon' id='divmap1' style='width:100%;height: 800px;margin:auto;'></div>");
		divmap1();
		$(".mapsele").val('divmap1');   
	}else if(id=="divmap2"){
		$(".r_con").empty();
		$(".r_con").append("<div class='r_divcon' id='divmap2' style='width:100%;height: 800px;margin:auto;'></div>");
		divmap2();
		$(".mapsele").val('divmap2'); 
	}else if(id=="divmap3"){
		$(".r_con").empty();
		$(".r_con").append("<div class='r_divcon' id='divmap3' style='width:100%;height: 800px;margin:auto;'></div>");
		divmap3();
		$(".mapsele").val('divmap3'); 
	}else if(id=="divmap4"){
		$(".r_con").empty();
		$(".r_con").append("<div class='r_divcon' id='divmap4' style='width:100%;height: 800px;margin:auto;'></div>");
		divmap4();
		$(".mapsele").val('divmap4'); 
	}else if(id=="divmap5"){
		$(".r_con").empty();
		$(".r_con").append("<div class='r_divcon' id='divmap5' style='width:100%;height: 800px;margin:auto;'></div>");
		divmap5();
		$(".mapsele").val('divmap5'); 
	}else if(id=="divmap6"){
		$(".r_con").empty();
		$(".r_con").append("<div class='r_divcon' id='divmap6' style='width:100%;height: 800px;margin:auto;'></div>");
		divmap6();
		$(".mapsele").val('divmap6'); 
	}
}




/*页面初始化(显示所有某个城市所有公司的信息)*/
function allrep(){
	st=1;
	tu=1;
	$(".r_top").empty();
	$(".r_con").empty();
	
	$(".r_top").append("<input type='button' name='back'  class='backs' value='返回'/><input type='button' name='report' id='repotr' value='趋势图' onclick='corpTu(1)'/>");
	$(".r_con").append("<table border='1' cellpadding='0' cellspacing='0' id='r_re'></table>");
// 	$("#r_re").empty();
	
	//ajax请求
	
	
	
	$.ajax({
		url:"http://localhost:8000/hardsocket/getAllCorpReports/?city_id=310000",
		type:"GET",
		dataType:"json",
		
		success:function(data){
			var json=eval(data);
			var con="<tr><th></th><th colspan='6' class='ri'>当日总体水质</th><th colspan='6'  class='ri'>本周总体水质</th><th colspan='6'  class='ri'>本月总体水质</th></tr><tr><td></td><td  class='ri'>PH</td><td>电导</td><td>溶氧</td><td>余氯</td><td>浊度</td><td>温度</td><td  class='ri'>PH</td><td>电导</td><td>溶氧</td><td>余氯</td><td>浊度</td><td>温度</td><td  class='ri'>PH</td><td>电导</td><td>溶氧</td><td>余氯</td><td>浊度</td><td>温度</td></tr>";
			
			for ( var y = 0; y < json['todayInfo'].length; y++) {
				
				con+="<tr><td onclick='getreps("+json['todayInfo'][y]['corp_id']+")'>"+json['todayInfo'][y]['corp_name']+"</td><td  class='ri'>"+json['todayInfo'][y]['day_ph']+"</td><td>"+json['todayInfo'][y]['day_conductivity']+"</td><td>"+json['todayInfo'][y]['day_DO']+"</td><td>"+json['todayInfo'][y]['day_rc']+"</td><td>"+json['todayInfo'][y]['day_turbidity']+"</td><td>"+json['todayInfo'][y]['day_temp']+"</td><td  class='ri'>"+json['weekInfo'][y]['week_ph']+"</td><td>"+json['weekInfo'][y]['week_conductivity']+"</td><td>"+json['weekInfo'][y]['week_DO']+"</td><td>"+json['weekInfo'][y]['week_rc']+"</td><td>"+json['weekInfo'][y]['week_turbidity']+"</td><td>"+json['weekInfo'][y]['week_temp']+"</td><td  class='ri'>"+json['MonthInfo'][y]['month_ph']+"</td><td>"+json['MonthInfo'][y]['month_conductivity']+"</td><td>"+json['MonthInfo'][y]['month_DO']+"</td><td>"+json['MonthInfo'][y]['month_rc']+"</td><td>"+json['MonthInfo'][y]['month_turbidity']+"</td><td>"+json['MonthInfo'][y]['month_temp']+"</td></tr>";
			}

			$("#r_re").append(con);
			
			/*设置表格样式(偶数奇数切换颜色)*/
			$("#r_re").find("tr").css("background-image", "url(../../site_media/img/007.png)");
			$("#r_re").find("tr:odd").css("background-image", "url(../../site_media/img/008.png)");
		}
	});

};



/*单击某个公司显示子公司的信息*/
function getreps(id){
	st=2;
	tu=2;
	$(".r_top").empty();
	$(".r_con").empty();
	$(".r_top").append("<input type='button' name='back'  class='backs' value='返回'/><input type='button' name='report' id='repotr' value='趋势图' onclick='chirdCorpTu("+id+",1)'/>");
	$(".r_con").append("<table border='1' cellpadding='0' cellspacing='0' id='r_re'></table>");
	//ajax请求
	
	$.ajax({
		url:"http://localhost:8000/hardsocket/getSubCorpReports/?corp_id="+id,
		type:"GET",
		dataType:"json",
		
		success:function(data){
			var json=eval(data);
			var con="<tr style='background-color:#f5faad'><th></th><th colspan='6' class='ri'>当日总体水质</th><th colspan='6'  class='ri'>本周总体水质</th><th colspan='6'  class='ri'>本月总体水质</th></tr><tr><td></td><td  class='ri'>PH</td><td>电导</td><td>溶氧</td><td>余氯</td><td>浊度</td><td>温度</td><td  class='ri'>PH</td><td>电导</td><td>溶氧</td><td>余氯</td><td>浊度</td><td>温度</td><td  class='ri'>PH</td><td>电导</td><td>溶氧</td><td>余氯</td><td>浊度</td><td>温度</td></tr>";
			
			for ( var y = 0; y < json['todayInfo'].length; y++) {
				
				con+="<tr><td id='"+json['todayInfo'][y]['corp_id']+"'>"+json['todayInfo'][y]['corp_name']+"</td><td  class='ri'>"+json['todayInfo'][y]['day_ph']+"</td><td>"+json['todayInfo'][y]['day_conductivity']+"</td><td>"+json['todayInfo'][y]['day_DO']+"</td><td>"+json['todayInfo'][y]['day_rc']+"</td><td>"+json['todayInfo'][y]['day_turbidity']+"</td><td>"+json['todayInfo'][y]['day_temp']+"</td><td  class='ri'>"+json['weekInfo'][y]['week_ph']+"</td><td>"+json['weekInfo'][y]['week_conductivity']+"</td><td>"+json['weekInfo'][y]['week_DO']+"</td><td>"+json['weekInfo'][y]['week_rc']+"</td><td>"+json['weekInfo'][y]['week_turbidity']+"</td><td>"+json['weekInfo'][y]['week_temp']+"</td><td  class='ri'>"+json['MonthInfo'][y]['month_ph']+"</td><td>"+json['MonthInfo'][y]['month_conductivity']+"</td><td>"+json['MonthInfo'][y]['month_DO']+"</td><td>"+json['MonthInfo'][y]['month_rc']+"</td><td>"+json['MonthInfo'][y]['month_turbidity']+"</td><td>"+json['MonthInfo'][y]['corp_temp']+"</td></tr>";
			}
			$("#r_re").append(con);
			
			/*设置表格样式(偶数奇数切换颜色)*/
			$("#r_re").find("tr").css("background-image", "url(../../site_media/img/007.png)");
			$("#r_re").find("tr:odd").css("background-image", "url(../../site_media/img/008.png)");
		}
	});
	

};



function corpTu(type){
	
	//res1="";
	res2="";
	res3="";
	res4="";
	res5="";
	res6="";

	//获取总公司日，周，月
	$.ajax({
		url:"http://localhost:8000/hardsocket/getCorpTrend/?city_id=310000&reports_type="+type,
		type:"GET",
		dataType:"json",
	
		success:function(data){
		//var	result=eval(data);
		//alert("data[0]['time']:"+data[0]['time']);
			
		
		

			for(var i= 0; i < data.length; i++) {
				
//				var thre=result[x][2];
					//res1[0]=
					
						res1[i]= new Array();
						res1[i][0]= data[i]['time']==null?0:data[i]['time'];
			 			res1[i][1]= parseInt(data[i]['corp_ph']);
					
 					
		 			//res1[1]=color[i];
					

				
					//res1+=result[x][0];
					//res2+=result[x][1];
					//res3+=result[x][2];
					//res4+=result[x][3];
					//res5+=result[x][4];
					//res6+=result[x][5];
				
			}
			
		}
	});
	
	
	star=0;
	st=3;
	
	$(".r_con").empty();
	$(".r_top").empty();
	
	$(".r_top").append("<input type='button' name='back' class='backs' value='返回' onclick=''/><input type='button' name='day' id='day' value='本日 ' onclick='chirdCorpTu(1)'/>"
			+"<input type='button' name='week' id='week' value='本周' onclick='chirdCorpTu(2)'/><input type='button' name='month' id='month' value='本月' onclick='chirdCorpTu(3)'/><input type='button' name='reportBiao' id='reportBiao' value='报表' onclick='allrep()'/>");
	
	$(".r_con").append("<div class='r_divcon' id='divmap1' style='width:30%;height: 320px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap2' style='width:30%;height: 320px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap3' style='width:30%;height: 320px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap4' style='width:30%;height: 320px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap5' style='width:30%;height: 320px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap6' style='width:30%;height: 320px;margin-left:20px;float: left;'></div>");
	
	
	//PH值
	alert(res1);
	divmap1(res1);
	//电导率
	divmap2(res2);
	//溶解氧
	divmap3(res3);
	//余氯
	divmap4(res4);
	//浊度
	divmap5(res5);
	//温度
	divmap6(res6);
	
}

function chirdCorpTu(cordId,type){
	//获取分公司日，周，月
	res1="";
	res2="";
	res3="";
	res4="";
	res5="";
	res6="";
	
	$.ajax({
		url:"http://localhost:8000/hardsocket/getSubCorpTrend/?corp_id="+id+"&reports_type="+type,
		type:"GET",
		dataType:"json",
		
		success:function(data){
			result=eval(data);
			
			
			for ( var x = 0; x < result.length; x++) {
				
//				var thre=result[x][2];
				var threle=result[x][2].length;
				for ( var y = 0; y < threle.length; y++) {
					res1+=threle[y][0];
					res2+=threle[y][1];
					res3+=threle[y][2];
					res4+=threle[y][3];
					res5+=threle[y][4];
					res6+=threle[y][5];
				}
			}
		
		}
	});
	
	
	
	star=0;
	st=3;
	
	$(".r_con").empty();
	$(".r_top").empty();
	
	$(".r_top").append("<input type='button' name='back' class='backs' value='返回' onclick=''/><input type='button' name='day' id='day' value='本日 ' onclick='chirdCorpTu("+cordId+",1)'/>"
			+"<input type='button' name='week' id='week' value='本周' onclick='chirdCorpTu("+cordId+",2)'/><input type='button' name='month' id='month' value='本月' onclick='chirdCorpTu("+cordId+",3)'/><input type='button' name='reportBiao' id='reportBiao' value='报表' onclick='allrep()'/>");
	
	$(".r_con").append("<div class='r_divcon' id='divmap1' style='width:400px;height: 400px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap2' style='width:400px;height: 400px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap3' style='width:400px;height: 400px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap4' style='width:400px;height: 400px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap5' style='width:400px;height: 400px;margin-left:20px;float: left;'></div>"
	+"<div class='r_divcon' id='divmap6' style='width:400px;height: 400px;margin-left:20px;float: left;'></div>");
	
	//PH值
	divmap1(res1);
	//电导率
	divmap2();
	//溶解氧
	divmap3(res2);
	//余氯
	divmap4(res3);
	//浊度
	divmap5(res4);
	//温度
	divmap6(res5);
	
	
}


function divmap1(data){
	
	//PH值
	/*创建趋势图*/
	var myChart = new JSChart('divmap1', 'line');
	myChart.setTitle('PH值');
	
	//alert("data:"+data);
//	myChart.setDataArray([[1, 2],[2, 5],[3, 10],[4, 1],[5, 6],[6, 9],[7, 7],[8, 3],[9, 13],[10, 12],[11, 12],[12, 12],[13, 12]], 'blue');
	//myChart.setDataArray([[6, 9],[7,10]], 'blue');
	//myChart.setDataArray([[1, 2],[2, 5],[3, 7],[4, 10],[5, 11],[6, 2],[7, 3],[8, 13],[9, //10],[10, 9],[11, 12],[12, 12],[13, 12]], 'green');
	//myChart.setDataArray([[1, 1],[2, 2],[3, 10],[4, 8],[5, 2],[6, 6],[7, 0],[8, 5],[9, //9],[10, 2],[11, 12],[12, 12],[13, 12]], 'gray');
	myChart.setDataArray(data);
	myChart.setAxisPaddingBottom(40);
	myChart.setTextPaddingBottom(10);
	myChart.setAxisValuesNumberY(14);
	myChart.setIntervalStartY(0);
	myChart.setIntervalEndY(14);
	
	myChart.setLabelX([0,'0']);
	myChart.setLabelX([1,'1']);
	myChart.setLabelX([2,'2']);
	myChart.setLabelX([3,'3']);
	myChart.setLabelX([4,'4']);
	myChart.setLabelX([5,'5']);
	myChart.setLabelX([6,'6']);
	myChart.setLabelX([7,'7']);
	myChart.setLabelX([8,'8']);
	myChart.setLabelX([9,'9']);
	myChart.setLabelX([10,'10']);
	myChart.setLabelX([11,'11']);
	myChart.setLabelX([12,'12']);
	myChart.setLabelX([13,'13']);
	myChart.setLabelX([14,'14']);
	myChart.setLabelX([15,'15']);
	myChart.setLabelX([16,'16']);
	myChart.setLabelX([17,'17']);
	myChart.setLabelX([18,'18']);
	myChart.setLabelX([19,'19']);
	myChart.setLabelX([20,'20']);
	myChart.setLabelX([21,'21']);
	myChart.setLabelX([22,'22']);
	myChart.setLabelX([23,'23']);
//	
	
	myChart.setAxisValuesNumberX(24);
	myChart.setShowXValues(false);
	myChart.setTitleColor('#454545');
	myChart.setAxisValuesColor('#454545');
	myChart.setLineColor('#A4D314', 'green');
	myChart.setLineColor('#BBBBBB', 'gray');
	myChart.setTooltip([0]);
	myChart.setTooltip([1]);
	myChart.setTooltip([2]);
	myChart.setTooltip([3]);
	myChart.setTooltip([4]);
	myChart.setTooltip([5]);
	myChart.setTooltip([6]);
	myChart.setTooltip([7]);
	myChart.setTooltip([8]);
	myChart.setTooltip([9]);
	myChart.setTooltip([10]);
	myChart.setTooltip([11]);
	myChart.setTooltip([12]);
	myChart.setTooltip([13]);
	myChart.setTooltip([14]);
	myChart.setTooltip([15]);
	myChart.setTooltip([16]);
	myChart.setTooltip([17]);
	myChart.setTooltip([18]);
	myChart.setTooltip([19]);
	myChart.setTooltip([20]);
	myChart.setTooltip([21]);
	myChart.setTooltip([22]);
	myChart.setTooltip([23]);
	myChart.setFlagColor('#9D16FC');
	myChart.setFlagRadius(4);
	myChart.setBackgroundImage('../../site_media/img/chart_bg.jpg');
	if(star==0){
		myChart.setSize(400, 300);
//		myChart.setLegendShow(true);
//		myChart.setLegendPosition(400, 80);
//		myChart.setAxisPaddingRight(110);
//		myChart.setLegendForLine('blue', '市北公司');
//		myChart.setLegendForLine('green', '市南公司');
//		myChart.setLegendForLine('gray', '市东公司');
	}else if(star==1){
		myChart.setSize(1300, 700);
//		myChart.setLegendShow(true);
//		myChart.setLegendPosition(1200, 300);
//		myChart.setAxisPaddingRight(150);
//		myChart.setLegendForLine('blue', '市北公司');
//		myChart.setLegendForLine('green', '市南公司');
//		myChart.setLegendForLine('gray', '市东公司');
	}
	
	
	myChart.draw();
	
	
	
};


function divmap2(data){
	
	//电导率
	
	/*创建趋势图*/
	var myChart = new JSChart('divmap2', 'line');
	myChart.setTitle('电导率');
	myChart.setDataArray([[1, 800],[2, 400],[3, 600],[4, 650],[5, 500],[6, 500],[7, 600],[8, 800],[9, 1500],[10, 1000]], 'blue');
	myChart.setDataArray([[1, 1000],[2, 550],[3, 800],[4, 1150],[5, 800],[6, 700],[7, 300],[8, 1300],[9, 1600],[10, 1700]], 'green');
	myChart.setDataArray([[1, 1500],[2, 250],[3, 1000],[4, 800],[5, 200],[6, 650],[7, 1100],[8, 1550],[9, 1900],[10, 2000]], 'gray');
	myChart.setAxisPaddingBottom(40);
	myChart.setTextPaddingBottom(10);
	myChart.setAxisValuesNumberY(200);
	myChart.setIntervalStartY(1.0);
	myChart.setIntervalEndY(2000);
	myChart.setLabelX([0,'0']);
	myChart.setLabelX([1,'1']);
	myChart.setLabelX([2,'2']);
	myChart.setLabelX([3,'3']);
	myChart.setLabelX([4,'4']);
	myChart.setLabelX([5,'5']);
	myChart.setLabelX([6,'6']);
	myChart.setLabelX([7,'7']);
	myChart.setLabelX([8,'8']);
	myChart.setLabelX([9,'9']);
	myChart.setLabelX([10,'10']);
	myChart.setLabelX([11,'11']);
	myChart.setLabelX([12,'12']);
	myChart.setLabelX([13,'13']);
	myChart.setLabelX([14,'14']);
	myChart.setLabelX([15,'15']);
	myChart.setLabelX([16,'16']);
	myChart.setLabelX([17,'17']);
	myChart.setLabelX([18,'18']);
	myChart.setLabelX([19,'19']);
	myChart.setLabelX([20,'20']);
	myChart.setLabelX([21,'21']);
	myChart.setLabelX([22,'22']);
	myChart.setLabelX([23,'23']);
//	
	
	myChart.setAxisValuesNumberX(24);
	myChart.setShowXValues(false);
	myChart.setTitleColor('#454545');
	myChart.setAxisValuesColor('#454545');
	myChart.setLineColor('#A4D314', 'green');
	myChart.setLineColor('#BBBBBB', 'gray');
	myChart.setTooltip([0]);
	myChart.setTooltip([1]);
	myChart.setTooltip([2]);
	myChart.setTooltip([3]);
	myChart.setTooltip([4]);
	myChart.setTooltip([5]);
	myChart.setTooltip([6]);
	myChart.setTooltip([7]);
	myChart.setTooltip([8]);
	myChart.setTooltip([9]);
	myChart.setTooltip([10]);
	myChart.setTooltip([11]);
	myChart.setTooltip([12]);
	myChart.setTooltip([13]);
	myChart.setTooltip([14]);
	myChart.setTooltip([15]);
	myChart.setTooltip([16]);
	myChart.setTooltip([17]);
	myChart.setTooltip([18]);
	myChart.setTooltip([19]);
	myChart.setTooltip([20]);
	myChart.setTooltip([21]);
	myChart.setTooltip([22]);
	myChart.setTooltip([23]);
	myChart.setFlagColor('#9D16FC');
	myChart.setFlagRadius(4);
	myChart.setBackgroundImage('../../site_media/img/chart_bg.jpg');
	if(star==0){
		myChart.setSize(400, 300);
		
	}else if(star==1){
		myChart.setSize(1300, 700);
		
	}
	
	
	myChart.draw();
	
	
	
};


function divmap3(data){
	
	//溶解氧
	
	/*创建趋势图*/
	var myChart = new JSChart('divmap3', 'line');
	myChart.setTitle('溶解氧');
	myChart.setDataArray([[1, 80],[2, 40],[3, 60],[4, 65],[5, 50],[6, 50],[7, 60],[8, 80],[9, 50],[10, 100]], 'blue');
	myChart.setDataArray([[1, 100],[2, 55],[3, 80],[4, 15],[5, 80],[6, 70],[7, 30],[8, 30],[9, 60],[10, 90]], 'green');
	myChart.setDataArray([[1, 100],[2, 25],[3, 100],[4, 80],[5, 20],[6, 65],[7, 0],[8, 55],[9, 100],[10, 100]], 'gray');
	myChart.setAxisPaddingBottom(40);
	myChart.setTextPaddingBottom(10);
	myChart.setAxisValuesNumberY(10);
	myChart.setIntervalStartY(0);
	myChart.setIntervalEndY(100);
	myChart.setLabelX([0,'0']);
	myChart.setLabelX([1,'1']);
	myChart.setLabelX([2,'2']);
	myChart.setLabelX([3,'3']);
	myChart.setLabelX([4,'4']);
	myChart.setLabelX([5,'5']);
	myChart.setLabelX([6,'6']);
	myChart.setLabelX([7,'7']);
	myChart.setLabelX([8,'8']);
	myChart.setLabelX([9,'9']);
	myChart.setLabelX([10,'10']);
	myChart.setLabelX([11,'11']);
	myChart.setLabelX([12,'12']);
	myChart.setLabelX([13,'13']);
	myChart.setLabelX([14,'14']);
	myChart.setLabelX([15,'15']);
	myChart.setLabelX([16,'16']);
	myChart.setLabelX([17,'17']);
	myChart.setLabelX([18,'18']);
	myChart.setLabelX([19,'19']);
	myChart.setLabelX([20,'20']);
	myChart.setLabelX([21,'21']);
	myChart.setLabelX([22,'22']);
	myChart.setLabelX([23,'23']);
//	
	
	myChart.setAxisValuesNumberX(24);
	myChart.setShowXValues(false);
	myChart.setTitleColor('#454545');
	myChart.setAxisValuesColor('#454545');
	myChart.setLineColor('#A4D314', 'green');
	myChart.setLineColor('#BBBBBB', 'gray');
	myChart.setTooltip([0]);
	myChart.setTooltip([1]);
	myChart.setTooltip([2]);
	myChart.setTooltip([3]);
	myChart.setTooltip([4]);
	myChart.setTooltip([5]);
	myChart.setTooltip([6]);
	myChart.setTooltip([7]);
	myChart.setTooltip([8]);
	myChart.setTooltip([9]);
	myChart.setTooltip([10]);
	myChart.setTooltip([11]);
	myChart.setTooltip([12]);
	myChart.setTooltip([13]);
	myChart.setTooltip([14]);
	myChart.setTooltip([15]);
	myChart.setTooltip([16]);
	myChart.setTooltip([17]);
	myChart.setTooltip([18]);
	myChart.setTooltip([19]);
	myChart.setTooltip([20]);
	myChart.setTooltip([21]);
	myChart.setTooltip([22]);
	myChart.setTooltip([23]);
	myChart.setFlagColor('#9D16FC');
	myChart.setFlagRadius(4);
	myChart.setBackgroundImage('../../site_media/img/chart_bg.jpg');
	if(star==0){
		myChart.setSize(400, 300);
		
	}else if(star==1){
		myChart.setSize(1300, 700);
		
	}
	
	
	myChart.draw();
	
	
};


function divmap4(data){
	
	//余氯
	
	/*创建趋势图*/
	var myChart = new JSChart('divmap4', 'line');
	myChart.setTitle('余氯');
	myChart.setDataArray([[1, 80],[2, 40],[3, 60],[4, 65],[5, 50],[6, 50],[7, 60],[8, 80],[9, 150],[10, 100]], 'blue');
	myChart.setDataArray([[1, 100],[2, 55],[3, 80],[4, 115],[5, 80],[6, 70],[7, 30],[8, 130],[9, 160],[10, 170]], 'green');
	myChart.setDataArray([[1, 150],[2, 25],[3, 100],[4, 80],[5, 20],[6, 65],[7, 0],[8, 155],[9, 190],[10, 200]], 'gray');
	myChart.setAxisPaddingBottom(40);
	myChart.setTextPaddingBottom(10);
	myChart.setAxisValuesNumberY(20);
	myChart.setIntervalStartY(0);
	myChart.setIntervalEndY(200);
	myChart.setLabelX([0,'0']);
	myChart.setLabelX([1,'1']);
	myChart.setLabelX([2,'2']);
	myChart.setLabelX([3,'3']);
	myChart.setLabelX([4,'4']);
	myChart.setLabelX([5,'5']);
	myChart.setLabelX([6,'6']);
	myChart.setLabelX([7,'7']);
	myChart.setLabelX([8,'8']);
	myChart.setLabelX([9,'9']);
	myChart.setLabelX([10,'10']);
	myChart.setLabelX([11,'11']);
	myChart.setLabelX([12,'12']);
	myChart.setLabelX([13,'13']);
	myChart.setLabelX([14,'14']);
	myChart.setLabelX([15,'15']);
	myChart.setLabelX([16,'16']);
	myChart.setLabelX([17,'17']);
	myChart.setLabelX([18,'18']);
	myChart.setLabelX([19,'19']);
	myChart.setLabelX([20,'20']);
	myChart.setLabelX([21,'21']);
	myChart.setLabelX([22,'22']);
	myChart.setLabelX([23,'23']);
//	
	
	myChart.setAxisValuesNumberX(24);
	myChart.setShowXValues(false);
	myChart.setTitleColor('#454545');
	myChart.setAxisValuesColor('#454545');
	myChart.setLineColor('#A4D314', 'green');
	myChart.setLineColor('#BBBBBB', 'gray');
	myChart.setTooltip([0]);
	myChart.setTooltip([1]);
	myChart.setTooltip([2]);
	myChart.setTooltip([3]);
	myChart.setTooltip([4]);
	myChart.setTooltip([5]);
	myChart.setTooltip([6]);
	myChart.setTooltip([7]);
	myChart.setTooltip([8]);
	myChart.setTooltip([9]);
	myChart.setTooltip([10]);
	myChart.setTooltip([11]);
	myChart.setTooltip([12]);
	myChart.setTooltip([13]);
	myChart.setTooltip([14]);
	myChart.setTooltip([15]);
	myChart.setTooltip([16]);
	myChart.setTooltip([17]);
	myChart.setTooltip([18]);
	myChart.setTooltip([19]);
	myChart.setTooltip([20]);
	myChart.setTooltip([21]);
	myChart.setTooltip([22]);
	myChart.setTooltip([23]);
	myChart.setFlagColor('#9D16FC');
	myChart.setFlagRadius(4);
	myChart.setBackgroundImage('../../site_media/img/chart_bg.jpg');
	if(star==0){
		myChart.setSize(400, 300);
		
	}else if(star==1){
		myChart.setSize(1300, 700);
		
	}
	
	
	myChart.draw();
};

function divmap5(data){
	
	//浊度
	

	/*创建趋势图*/
	var myChart = new JSChart('divmap5', 'line');
	myChart.setTitle('浊度');
	myChart.setDataArray([[1, 8],[2, 4],[3, 6],[4, 6],[5, 5],[6, 5],[7, 6],[8, 8],[9, 15],[10, 10]], 'blue');
	myChart.setDataArray([[1, 10],[2, 5],[3, 8],[4, 15],[5, 8],[6, 7],[7, 3],[8, 13],[9, 16],[10, 17]], 'green');
	myChart.setDataArray([[1, 15],[2, 5],[3, 10],[4, 8],[5, 2],[6, 6],[7, 0],[8, 15],[9, 19],[10, 20]], 'gray');
	myChart.setAxisPaddingBottom(40);
	myChart.setTextPaddingBottom(10);
	myChart.setAxisValuesNumberY(20);
	myChart.setIntervalStartY(0);
	myChart.setIntervalEndY(20);
	myChart.setLabelX([0,'0']);
	myChart.setLabelX([1,'1']);
	myChart.setLabelX([2,'2']);
	myChart.setLabelX([3,'3']);
	myChart.setLabelX([4,'4']);
	myChart.setLabelX([5,'5']);
	myChart.setLabelX([6,'6']);
	myChart.setLabelX([7,'7']);
	myChart.setLabelX([8,'8']);
	myChart.setLabelX([9,'9']);
	myChart.setLabelX([10,'10']);
	myChart.setLabelX([11,'11']);
	myChart.setLabelX([12,'12']);
	myChart.setLabelX([13,'13']);
	myChart.setLabelX([14,'14']);
	myChart.setLabelX([15,'15']);
	myChart.setLabelX([16,'16']);
	myChart.setLabelX([17,'17']);
	myChart.setLabelX([18,'18']);
	myChart.setLabelX([19,'19']);
	myChart.setLabelX([20,'20']);
	myChart.setLabelX([21,'21']);
	myChart.setLabelX([22,'22']);
	myChart.setLabelX([23,'23']);
//	
	
	myChart.setAxisValuesNumberX(24);
	myChart.setShowXValues(false);
	myChart.setTitleColor('#454545');
	myChart.setAxisValuesColor('#454545');
	myChart.setLineColor('#A4D314', 'green');
	myChart.setLineColor('#BBBBBB', 'gray');
	myChart.setTooltip([0]);
	myChart.setTooltip([1]);
	myChart.setTooltip([2]);
	myChart.setTooltip([3]);
	myChart.setTooltip([4]);
	myChart.setTooltip([5]);
	myChart.setTooltip([6]);
	myChart.setTooltip([7]);
	myChart.setTooltip([8]);
	myChart.setTooltip([9]);
	myChart.setTooltip([10]);
	myChart.setTooltip([11]);
	myChart.setTooltip([12]);
	myChart.setTooltip([13]);
	myChart.setTooltip([14]);
	myChart.setTooltip([15]);
	myChart.setTooltip([16]);
	myChart.setTooltip([17]);
	myChart.setTooltip([18]);
	myChart.setTooltip([19]);
	myChart.setTooltip([20]);
	myChart.setTooltip([21]);
	myChart.setTooltip([22]);
	myChart.setTooltip([23]);
	myChart.setFlagColor('#9D16FC');
	myChart.setFlagRadius(4);
	myChart.setBackgroundImage('../../site_media/img/chart_bg.jpg');
	if(star==0){
		myChart.setSize(400, 300);
		
	}else if(star==1){
		myChart.setSize(1300, 700);
		
	}
	
	
	myChart.draw();
	
	
};
function divmap6(){
	
	//温度

	/*创建趋势图*/
	var myChart = new JSChart('divmap6', 'line');
	myChart.setTitle('温度');
	myChart.setDataArray([[1, 25],[2, 40],[3, 10],[4, 15],[5, 50],[6, 50],[7, 20],[8, 48],[9, 15],[10, 10]], 'blue');
	myChart.setDataArray([[1, 10],[2, 50],[3, 40],[4, 25],[5, 30],[6, 10],[7, 30],[8, 13],[9, 16],[10, 17]], 'green');
	myChart.setDataArray([[1, 15],[2, 25],[3, 50],[4, 48],[5, 20],[6, 25],[7, 30],[8, 15],[9, 19],[10, 20]], 'gray');
	myChart.setAxisPaddingBottom(40);
	myChart.setTextPaddingBottom(10);
	myChart.setAxisValuesNumberY(10);
	myChart.setIntervalStartY(0);
	myChart.setIntervalEndY(50);
	myChart.setLabelX([0,'0']);
	myChart.setLabelX([1,'1']);
	myChart.setLabelX([2,'2']);
	myChart.setLabelX([3,'3']);
	myChart.setLabelX([4,'4']);
	myChart.setLabelX([5,'5']);
	myChart.setLabelX([6,'6']);
	myChart.setLabelX([7,'7']);
	myChart.setLabelX([8,'8']);
	myChart.setLabelX([9,'9']);
	myChart.setLabelX([10,'10']);
	myChart.setLabelX([11,'11']);
	myChart.setLabelX([12,'12']);
	myChart.setLabelX([13,'13']);
	myChart.setLabelX([14,'14']);
	myChart.setLabelX([15,'15']);
	myChart.setLabelX([16,'16']);
	myChart.setLabelX([17,'17']);
	myChart.setLabelX([18,'18']);
	myChart.setLabelX([19,'19']);
	myChart.setLabelX([20,'20']);
	myChart.setLabelX([21,'21']);
	myChart.setLabelX([22,'22']);
	myChart.setLabelX([23,'23']);
//	
	
	myChart.setAxisValuesNumberX(24);
	myChart.setShowXValues(false);
	myChart.setTitleColor('#454545');
	myChart.setAxisValuesColor('#454545');
	myChart.setLineColor('#A4D314', 'green');
	myChart.setLineColor('#BBBBBB', 'gray');
	myChart.setTooltip([0]);
	myChart.setTooltip([1]);
	myChart.setTooltip([2]);
	myChart.setTooltip([3]);
	myChart.setTooltip([4]);
	myChart.setTooltip([5]);
	myChart.setTooltip([6]);
	myChart.setTooltip([7]);
	myChart.setTooltip([8]);
	myChart.setTooltip([9]);
	myChart.setTooltip([10]);
	myChart.setTooltip([11]);
	myChart.setTooltip([12]);
	myChart.setTooltip([13]);
	myChart.setTooltip([14]);
	myChart.setTooltip([15]);
	myChart.setTooltip([16]);
	myChart.setTooltip([17]);
	myChart.setTooltip([18]);
	myChart.setTooltip([19]);
	myChart.setTooltip([20]);
	myChart.setTooltip([21]);
	myChart.setTooltip([22]);
	myChart.setTooltip([23]);
	myChart.setFlagColor('#9D16FC');
	myChart.setFlagRadius(4);
	myChart.setBackgroundImage('../../site_media/img/chart_bg.jpg');
	if(star==0){
		myChart.setSize(400, 300);
		
	}else if(star==1){
		myChart.setSize(1300, 700);
		
	}
	
	myChart.draw();
};



// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('main'));
var data = ""
$(document).ready(function(){
    $.getJSON("/jsondata",function(rs){
        data = rs.name;
    });
});

// 指定图表的配置项和数据
option = {
    tooltip : {
        formatter: "{a} <br/>{b} : {c}%"
    },
    toolbox: {
        feature: {
            restore: {},
            saveAsImage: {}
        }
    },
    series: [
        {
            name: '业务指标',
            type: 'gauge',
            detail: {formatter:'{value}%'},
//            data: [{value: 50, name: '完成率'}]
            data: [{value: 50, name: data}]
        }
    ]
};

setInterval(function () {
    option.series[0].data[0].value = (Math.random() * 100).toFixed(2) - 0;
    myChart.setOption(option, true);
},2000);

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);

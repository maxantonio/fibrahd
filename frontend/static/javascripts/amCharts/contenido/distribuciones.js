$(function () {
    if ($("#chartdiv")) {
        var chart = AmCharts.makeChart("chartdiv", {
            "type": "serial",
            "theme": "light",
            // "marginRight": 80,
            // "autoMarginOffset": 20,
            "dataProvider": distribuciones,
            "valueAxes": [{
                "axisAlpha": 0,
                "position": "left",
                "tickLength": 0
            }],
            "graphs": [{
                "balloonText": "[[category]]<br><b><span style='font-size:14px;'>[[value]]</span></b>",
                "bullet": "round",

                // "dashLength": 3,
                "colorField": "color",
                "valueField": "value"
            }],
            "categoryField": "perido",
            "categoryAxis": {
                // "parseDates": true,
                "axisAlpha": 0,
                "gridAlpha": 0.1,
                "minorGridAlpha": 0.1,
                "minorGridEnabled": true
            },
            "export": {
                "enabled": true
            }
        });
    }
});
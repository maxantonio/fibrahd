var distribuciones_index = [
    {
        "year": "2001",
        "value": 33.1,
        value2: 30.1
    }, {
        "year": "2004",
        "value": 71.7,
        value2: 36.9

    }, {
        "year": "2005",
        "value": 177.7,
        value2: 39.0

    }, {
        "year": "2006",
        "value": 151.9,
        value2: 41.1

    }, {
        "year": "2007",
        "value": 190.3,
        value2: 40.7

    }, {
        "year": "2010",
        "value": 223.4,
        value2: 40.3

    }, {
        "year": "2014",
        "value": 285.9,
        value2: 37.8

    }, {
        "year": "2015",
        "value": 303.3,
        value2: 37.7
    }
];


if (locale == "es") {
    var title = 'Distribuciones y Desempeño del CBFI';
    var distriucionnes = "ACUM EBITDA (M USD)";
    var crecimiento="Crecimiento";
} else {
    var title = 'Solid track record';
    var distriucionnes = "Acum EBITDA (M USD)";
    var crecimiento="% of acum total revenue";
}


$(document).ready(function () {
    if ($("#chartdiv")) {
        var chart = AmCharts.makeChart("chartdiv", {
            "legend": {
                "useGraphSettings": true,
                align: "center"
            },
            "titles": [
                {
                    "size": 15,
                    "text": title
                }
            ],
            "colors": ["#2D2D56", "#218FB5", "#218FB5", "#073855", "#a8dded", "#396077", "#91919"],
            "type": "serial",
            "theme": "light",
            "marginRight": 80,
            "autoMarginOffset": 20,
            "dataProvider": distribuciones_index,
            "valueAxes": [{
                "id": "v1",
                // "axisAlpha": 0,
                // "position": "left",
                "tickLength": 0,
                // minimum:0.10

            },
                {
                     "id": "v2",
                //    "axisColor": "#FCD202",
                //     // "tickLength": 0,
                //     // "axisAlpha": 0,
                     "position": "right",
                     unit: "%",
                     labelFrequency: 1
                }
            ],
            "graphs": [{
                "valueAxis": "v1",
                "balloonText": "<b><span style='font-size:14px;'>[[value]]</span></b>",
                // "bullet": "round",
                "colorField": "color",
                "title": distriucionnes,
                "valueField": "value",
                type: "column",
                "fillAlphas": 1,
            },
                 {
                     "valueAxis": "v2",
                     "balloonText": "<b><span style='font-size:14px;'>[[value]]%</span></b>",
                     "bullet": "round",
                     "colorField": "color",
                     "valueField": "value2",
                     title: crecimiento,
                 }
            ],
            "categoryField": "year",
            "categoryAxis": {
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

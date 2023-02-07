AmCharts.theme = AmCharts.themes.light;
var chart = new AmCharts.AmSerialChart();
var chart1 = new AmCharts.AmSerialChart();

if (locale == "es") {
    var giroLabel = ['Alimentos y bebidas', 'Ropa y calzado', 'Entretenimiento', 'Departamental', 'Especializados', 'Accesorios', 'Telefonía', 'Autoservicio', 'Deportes', 'Bancos','Mueblería','Otros'];
    var otrosLabel = ['Alimentos y bebidas', 'Ropa y calzado', 'Entretenimiento', 'Departamental', 'Especializados', 'Accesorios', 'Telefonía', 'Autoservicio', 'Deportes', 'Bancos','Mueblería','Otros'];

} else {
    var giroLabel = ['Consumer Durables & Apparel', 'Capital Goods', 'Automobiles & Components', 'Materials', 'Software & Services', 'Other Sectors*', 'Commercial and Professional Services', 'Telecommunication Services', 'Banks', 'Retailing'];
    var otrosLabel = ['Transportation', 'Personal Products', 'Real Estate', 'Utilities', 'Insurance', 'Consumer Services', 'Diversified Financials', 'Food Retail', 'T. Hardware & Equipment', 'Food, Beverage & Tobacco', 'Entertainment', 'Health Care Equipment and Services'];

}


var chartData1 = [
    {
        giro: giroLabel[0],
        valor:17
    }, {
        giro: giroLabel[1],
        valor: 16
    }, {
        giro: giroLabel[2],
        valor: 14
    }, {
        giro: giroLabel[3],
        valor: 12
    }, {
        giro: giroLabel[4],
        valor: 9
    }, {
        giro: giroLabel[5],
        valor: 6
    }, {
        giro: giroLabel[6],
        valor: 4
    }, {
        giro: giroLabel[7],
        valor: 4
    }, {
        giro: giroLabel[8],
        valor: 3
    }, {
        giro: giroLabel[9],
        valor: 3
    }, {
        giro: giroLabel[10],
        valor: 2
    }, {
        giro: giroLabel[11],
        valor: 12
    }
];


chart1.dataProvider = chartData1;
chart1.categoryField = "giro";
chart1.theme = "light";
chart1.startDuration = 2;
chart1.rotate = true;
chart1.labelRadius = -25;
chart1.labelText = "[[percents]]%";
chart1.colors = ["#194F90", "#052a40", "#25abd1", "#073855", "#a8dded", "#396077", "#91919"];

var categoryAxis = chart.categoryAxis;
categoryAxis.gridPosition = "start";

var valueAxis = new AmCharts.ValueAxis();
valueAxis.axisAlpha = 0;
valueAxis.gridAlpha = 0.1;
chart1.addValueAxis(valueAxis);
valueAxis.integersOnly = true;

var graph1 = new AmCharts.AmGraph(AmCharts.themes.light);
graph1.type = "column";
graph1.title = "Ano";
graph1.colors = ["#194F90"];
graph1.valueField = "valor";
graph1.fillAlphas = 1,
    graph1.balloonText = "[[value]]%";
graph1.labelText = "[[value]]%";
// chart1.addTitle("Desglose de principales arrendatarios por giro económico (% rentas)", 25, "#4a5158", 1, true);
chart1.addGraph(graph1);
chart1.creditsPosition = "top-right";
chart1.write("chart");


// el nuevo
var chartDataNew = [
    {
        giro: otrosLabel[0],
        valor: 10
    }, {
        giro: otrosLabel[1],
        valor: 13
    }, {
        giro: otrosLabel[2],
        valor: 22
    }, {
        giro: otrosLabel[3],
        valor: 20
    }, {
        giro: otrosLabel[4],
        valor: 6
    }, {
        giro: otrosLabel[5],
        valor: 2
    }, {
        giro: otrosLabel[6],
        valor: 2
    }, {
        giro: otrosLabel[7],
        valor: 12
    }, {
        giro: otrosLabel[8],
        valor: 2
    }, {
        giro: otrosLabel[9],
        valor: 2
    }, {
        giro: otrosLabel[10],
        valor: 3
    }, {
        giro: otrosLabel[11],
        valor: 8
    }
];
var chartnew = new AmCharts.AmSerialChart();

chartnew.dataProvider = chartDataNew;
chartnew.categoryField = "giro";
chartnew.theme = "light";
chartnew.startDuration = 2;
chartnew.rotate = true;
chartnew.labelRadius = -25;
chartnew.labelText = "[[percents]]%";
chartnew.colors = ["#194F90"];


var categoryAxis = chart.categoryAxis;
categoryAxis.gridPosition = "start";

var valueAxis = new AmCharts.ValueAxis();
valueAxis.axisAlpha = 0;
valueAxis.gridAlpha = 0.1;
chart1.addValueAxis(valueAxis);
valueAxis.integersOnly = true;

var graphnew = new AmCharts.AmGraph(AmCharts.themes.light);
graphnew.type = "column";
graphnew.title = "Ano";
graphnew.colors = ["#194F90", "#052a40", "#25abd1", "#073855", "#a8dded", "#396077", "#91919"];
graphnew.valueField = "valor";
graphnew.fillAlphas = 1,
    graphnew.balloonText = "[[value]]%";
graphnew.labelText = "[[value]]%";
chartnew.addGraph(graphnew);
chartnew.creditsPosition = "top-right";
chartnew.write("chartotros");


// chart 2
var chartPie1 = new AmCharts.AmPieChart();
chartPie1.dataProvider = [{
    "activo":"Top 10 arrendatarios",
    "valor": 47

}, {
    "activo": "Resto",
    "valor": 53

}, ];

chartPie1.titleField = "activo";
chartPie1.accessibleTitle = "Prueba";
//chartPie1.innerRadius = "50%";
chartPie1.valueField = "valor";
chartPie1.outlineColor = "#f9f9f9";
chartPie1.outlineAlpha = 0.8;
chartPie1.outlineThickness = 2;
chartPie1.labelRadius = -25;
chartPie1.labelText = "[[value]]%";
chartPie1.color = "#f9f9f9";

chartPie1.colors = ["#5e9cd3", "#eb7d3c", "#7B868C"];


var legend1 = new AmCharts.AmLegend();
legend1.align = "center";
legend1.markerType = "circle";
legend1.labelText = "[[title]]";
legend1.valueText = " ";

chartPie1.balloonText = "[[title]] <br> <b>[[value]]%</b>";
chartPie1.addLegend(legend1);
chartPie1.write("chart2");

// chart 3
var chartPie3 = new AmCharts.AmPieChart();
chartPie3.dataProvider = [{
   "activo":"Top 10 arrendatarios",
    "valor": 28
}, {
    "activo": "Resto",
    "valor": 72
}];

chartPie3.titleField = "activo";
chartPie3.accessibleTitle = "Prueba";
//chartPie3.innerRadius = "50%";
chartPie3.valueField = "valor";
chartPie3.outlineColor = "#f9f9f9";
chartPie3.outlineAlpha = 0.8;
chartPie3.outlineThickness = 2;
chartPie3.labelRadius = -25;
chartPie3.labelText = "[[value]]%";
chartPie3.color = "#f9f9f9";

chartPie3.colors = ["#5e9cd3", "#eb7d3c", "#7B868C"];


var legend3 = new AmCharts.AmLegend();
legend3.align = "center";
legend3.markerType = "circle";
legend3.labelText = "[[title]]";
legend3.valueText = " ";

chartPie3.balloonText = "[[title]] <br> <b>[[value]]%</b>";
chartPie3.addLegend(legend3);
chartPie3.write("chart7");
//chart 6

if (locale == "es") {
    var ingresostotales = "Ingresos totales";
    var ion = "ION";
    var uafirda = "UAFIRDA";
    var ffo = "FFO";

} else {
    var ingresostotales = "Total revenues";
    var ion = "NOI";
    var uafirda = "EBITDA";
    var ffo = "FFO";
}

//chart 8
if (locale == "es") {

    var ion = "ION";
    var uafirda = "UAFIDA";
    var ffo = "FFO";

} else {

    var ion = "NOI";
    var uafirda = "EBITDA";
    var ffo = "FFO";
}

chart.addTitle(last, 20, "#4a5158", 1, true);


var configNumeros = {
    g1: {
        "balloonText": "[[title]] <br> <b>[[value]]%</b>",
        "legend": {
            "align": "center",
            "markerType": "circle",
            labelText: "[[title]]",
            valueText: " "
        },
        "dataProvider": [
            {
                "activo": hover2[0],
                "valor": 46.9

            }, {
                "activo": hover2[1],
                "valor": 50.5

            }, {
                "activo": hover2[2],
                "valor": 2.6

            }
        ],
        "labelText": "[[value]]% ",
        "colors": ["#194F90", "#052a40", "#25abd1"],
        "labelRadius": -25,
        "outlineAlpha": 0.8,
        "outlineThickness": 2,
        "theme": "light",
        "titleField": "activo",
        title: "[[title]]",
        "type": "pie",
        "valueField": "valor"
    },
    g2: {
        "balloonText": "[[title]] <br> <b>[[value]]%</b>",
        "legend": {
            "align": "center",
            "markerType": "circle",
            labelText: "[[title]]",
            valueText: " "
        },
        "dataProvider": [
            {
                "activo": "USD",
                "valor": 74.4,
            }, {
                "activo": "MXN",
                "valor": 25.6
            }
        ],
        "labelText": "[[value]]% ",
        "colors": ["#194F90", "#052a40", "#25abd1"],
        "labelRadius": -25,
        "outlineAlpha": 0.8,
        "outlineThickness": 2,
        "theme": "light",
        "titleField": "activo",
        title: "[[title]]",
        "type": "pie",
        "valueField": "valor"
    },
    g3: {
        "balloonText": "[[title]] <br> <b>[[value]]%</b>",
        "legend": {
            "align": "center",
            "markerType": "circle",
            labelText: "[[title]]",
            valueText: " "
        },
        "dataProvider": [
            {
                ven: "0-1",
                valor: 17.4
            }, {
                ven: "1-3",
                valor: 20.0
            }, {
                ven: "3-5",
                valor: 9.0
            }, {
                ven: "5-7",
                valor: 18.2
            }, {
                ven: "7-10",
                valor: 34.3
            }, {
                ven: "+10",
                valor: 1.1
            }
        ],
        "labelText": "[[value]]% ",
        "colors": ["#194F90", "#052a40", "#25abd1", "#073855", "#a8dded", "#396077", "#91919"],
        "labelRadius": -25,
        "outlineAlpha": 0.8,
        "outlineThickness": 2,
        "theme": "light",
        "titleField": "ven",
        "type": "pie",
        "valueField": "valor"
    }
};

$('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {
    var index = e.target.getAttribute("data-index");
    var div_id = e.target.getAttribute("data-chart");
    AmCharts.makeChart(div_id, configNumeros[index]);
});
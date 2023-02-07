var loaded = 0;
var ipc = [];
var precios = [];
var frmex = [];
var intradia = {};
ticker_symbol = "FMTY14";
$.ajax({
    url: 'https://hkpy.irstrat.com/intradia/148',
    // url: location.protocol + '//' + location.host + "/51.json",
    async: false,
    dataType: 'jsonp',
    // dataType: 'json',
    jsonpCallback: 'intradia',
    contentType: "application/json",
    success: function (json) {
        Datatabla(json.intradia)
    }
});
$.ajax({
    url: 'https://hkpy.irstrat.com/intradia/history/148?start=2014-12-10',
    async: false,
    dataType: 'jsonp',
    contentType: "application/json",
    jsonpCallback: 'jsonCallback1',
    success: function (json) {
        precios = json.precios;
        // ipc = json.ipc;
        // intradia = json.intradia;

        loaded += 1;
        if (loaded == 3) {
            // Datatabla(intradia);
            fillData(precios, ipc, frmex, ticker_symbol);
        }
    }

});
$.ajax({
    //CARGANDO LOS DATOS DE FRMEX
    url: 'https://hkpy.irstrat.com/intradia/history/12?start=2014-12-10',
    async: false,
    dataType: 'jsonp',
    jsonpCallback: 'jsonCallback2',
    // jsonpCallback: 'jsonCallback',
    contentType: "application/json",
    success: function (json) {
        frmex = json.precios;
        loaded += 1;
        if (loaded == 3) {
            // Datatabla(intradia);
            fillData(precios, ipc, frmex, ticker_symbol);
        }
        //            console.dir(json.sites);
    }

});
$.ajax({
    //CARGANDO LOS DATOS DE FRMEX
    url: 'https://hkpy.irstrat.com/intradia/history/11?start=2014-12-10',
    async: false,
    dataType: 'jsonp',
    jsonpCallback: 'jsonCallback',
    contentType: "application/json",
    success: function (json) {
        ipc = json.precios;
        loaded += 1;
        if (loaded == 3) {
            // Datatabla(intradia);
            fillData(precios, ipc, frmex, ticker_symbol);
        }
        //            console.dir(json.sites);
    }

});

function Datatabla(intradia) {
    $('#table-date').html(intradia["date"]);
    $('#table-price').html(intradia["price"]);
    $('#table-change').html(intradia["change"]);
    $('#table-range').html(intradia["min"] + " - " + intradia["max"]);
    $('#table-volume').html(intradia["volume"]);
    $('#price-ticker').html("$" + intradia["price"]);
    $('#change-ticker').html(intradia["change"]);
}

//filling empty values from non operation
function fillData(precios, ipc, frmex, ticker_symbol) {
    var lvva = 0;
    var lvvo = 0;
    precios_fill = $.map(precios, function (n, i) {
        if (n.value !== null) {
            lvva = n.value;
            lvvo = n.volume
        }
        if (n.volume === null) {
            lvvo = 0
        }
        return [{"date": n.date, "value": lvva, "volume": lvvo}];
    }).reverse();

    ipc_fill = $.map(ipc, function (n, i) {
        if (n.value !== null) {
            lvva = n.value;
            lvvo = n.volume
        }
        if (n.volume === null) {
            lvvo = 0
        }
        return [{"date": n.date, "value": lvva, "volume": lvvo}];
    }).reverse();
    frmex_fill = $.map(frmex, function (n, i) {
        if (n.close !== null) {
            lvva = n.close;
            lvvo = n.volume
        }
        if (n.volume === null) {
            lvvo = 0
        }
        return [{"date": n.date, "value": lvva, "volume": lvvo}];
    }).reverse();
    ajustado_fill = $.map(precios, function (n, i) {
        // console.log(n);
        if (n.adjusted !== null) {
            lvva = n.adjusted;
            lvvo = n.volume
        }
        if (n.volume === null) {
            lvvo = 0
        }
        return [{"date": n.date, "value": lvva, "volume": lvvo}];
    }).reverse();
    AmCharts.theme = AmCharts.themes.light;

///tercera
    AmCharts.ready(function () {
        createStockChart();
    });
}


function createStockChart() {
    var chart = new AmCharts.AmStockChart();
    chart.dataDateFormat = "YYYY-MM-DD";
    // chart.marginRight = 150;
    // chart.marginLeft = 150;
    // chart.autoMarginOffset = 150;
    chart.pathToImages = location.protocol + '//' + location.host + "/static/js/amCharts/images/";


    // DATASETS //////////////////////////////////////////
    // create data sets first
    var dataSet1 = new AmCharts.DataSet();
    dataSet1.title = ticker_symbol;
    dataSet1.fieldMappings = [{
        fromField: "value",
        toField: "value"
    }, {
        fromField: "volume",
        toField: "volume"
    }];
    dataSet1.dataProvider = precios_fill;
    dataSet1.categoryField = "date";

    var dataSet2 = new AmCharts.DataSet();
    dataSet2.title = "IPC";
    dataSet2.fieldMappings = [{
        fromField: "value",
        toField: "value"
    }, {
        fromField: "volume",
        toField: "volume"
    }];
    dataSet2.dataProvider = ipc_fill;
    dataSet2.categoryField = "date";

    var dataSet3 = new AmCharts.DataSet();
    dataSet3.title = "FIBRAS RT";
    dataSet3.fieldMappings = [{
        fromField: "value",
        toField: "value"
    }, {
        fromField: "volume",
        toField: "volume"
    }];
    dataSet3.dataProvider = frmex_fill;
    dataSet3.categoryField = "date";

    var dataSet4 = new AmCharts.DataSet();
    dataSet4.title = ticker_symbol + " ajustado*";
    if (locale == "en") {
        dataSet4.title = ticker_symbol + " Adjusted*";
    }
    dataSet4.fieldMappings = [{
        fromField: "value",
        toField: "value"
    }, {
        fromField: "volume",
        toField: "volume"
    }];
    dataSet4.dataProvider = ajustado_fill;
    dataSet4.categoryField = "date";
    // set data sets to the chart
    chart.dataSets = [dataSet4, dataSet1, dataSet3, dataSet2];

    // PANELS ///////////////////////////////////////////
    // first stock panel
    var stockPanel1 = new AmCharts.StockPanel();
    stockPanel1.showCategoryAxis = false;
    if (locale == "es")
        stockPanel1.title = "Precio al último cierre registrado";
    else
        stockPanel1.title = "Historical prices at last close";
    stockPanel1.percentHeight = 70;

    // graph of first stock panel
    var graph1 = new AmCharts.StockGraph();
    graph1.valueField = "value";
    graph1.comparable = true;
    graph1.compareField = "value";
    graph1.bullet = "round";
    graph1.hideBulletsCount = 32;
    graph1.bulletBorderColor = "#f9f9f9";
    graph1.bulletBorderAlpha = 1;
    graph1.balloonText = "[[title]]: <b>[[value]]</b>";
    graph1.compareGraphBalloonText = "[[title]]:<b>[[value]]</b>";
    graph1.compareGraphBullet = "round";
    graph1.compareGraphBulletBorderColor = "#f9f9f9";
    graph1.compareGraphBulletBorderAlpha = 1;
    stockPanel1.addStockGraph(graph1);

    // create stock legend
    var stockLegend1 = new AmCharts.StockLegend();
    stockLegend1.periodValueTextComparing = "[[percents.value.close]]%";
    stockLegend1.periodValueTextRegular = "[[value.close]]";
    stockPanel1.stockLegend = stockLegend1;


    // second stock panel
    var stockPanel2 = new AmCharts.StockPanel();
    if (locale == "es")
        stockPanel2.title = "Volumen";
    else
        stockPanel2.title = "Volume";

    stockPanel2.percentHeight = 30;
    var graph2 = new AmCharts.StockGraph();
    graph2.valueField = "volume";
    graph2.type = "column";
    graph2.showBalloon = true;
    graph2.fillAlphas = 1;
    graph2.periodValue = "Sum";
    stockPanel2.addStockGraph(graph2);

    var stockLegend2 = new AmCharts.StockLegend();
    stockLegend2.periodValueTextRegular = "[[value.close]]";
    stockPanel2.stockLegend = stockLegend2;

    // set panels to the chart
    chart.panels = [stockPanel1, stockPanel2];


    // OTHER SETTINGS ////////////////////////////////////
    var sbsettings = new AmCharts.ChartScrollbarSettings();
    sbsettings.graph = graph1;
    chart.chartScrollbarSettings = sbsettings;

    // CURSOR
    var cursorSettings = new AmCharts.ChartCursorSettings();
    cursorSettings.valueBalloonsEnabled = true;
    chart.chartCursorSettings = cursorSettings;


    // PERIOD SELECTOR ///////////////////////////////////
    var periodSelector = new AmCharts.PeriodSelector();
    periodSelector.position = "left";
    if (locale == "en") {
        periodSelector.fromText = "From:";
        periodSelector.toText = "To:";
        periodSelector.periodsText = "Range:";
    }
    if (locale == "es") {
        periodSelector.periods = [{
            period: "MM",
            count: 1,
            label: "1 mes"
        },
            {
                period: "YYYY",
                count: 1,
                label: "1 año"
            },
            {
                period: "YYYY",
                count: 5,
                selected: true,
                label: "5 años"
            }];
    } else {
        periodSelector.periods = [{
            period: "MM",
            count: 1,
            label: "1 month"
        }, {
            period: "YYYY",
            count: 1,
            label: "1 Year"
        }, {
            period: "YYYY",
            count: 5,
            selected: true,
            label: "5 years"
        }];
    }
    chart.periodSelector = periodSelector;


    // DATA SET SELECTOR
    var dataSetSelector = new AmCharts.DataSetSelector();
    dataSetSelector.position = "left";
    if (locale == "en") {
        dataSetSelector.selectText = "Select:";
        dataSetSelector.compareText = "Compare:"
    }

    chart.dataSetSelector = dataSetSelector;

    var categoryAxesSettings = new AmCharts.CategoryAxesSettings();
    categoryAxesSettings.maxSeries = 0;
    chart.categoryAxesSettings = categoryAxesSettings;

    if (locale == 'es') {
        chart.addListener('rendered', function (event) {
            $(".amChartsPeriodSelector .amChartsInputField").datepicker({
                dateFormat: (locale === 'es') ? "dd-mm-yy" : "mm/dd/yy",
                closeText: "Cerrar",
                prevText: "&#x3C;Ant",
                nextText: "Sig&#x3E;",
                currentText: "Hoy",
                monthNames: ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                    "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
                monthNamesShort: ["ene", "feb", "mar", "abr", "may", "jun",
                    "jul", "ago", "sep", "oct", "nov", "dic"],
                dayNames: ["domingo", "lunes", "martes", "miércoles", "jueves", "viernes", "sábado"],
                dayNamesShort: ["dom", "lun", "mar", "mié", "jue", "vie", "sáb"],
                dayNamesMin: ["D", "L", "M", "X", "J", "V", "S"],
                weekHeader: "Sm",
                firstDay: 1,
                isRTL: false,
                showMonthAfterYear: false,
                yearSuffix: ""
            });
        });
    } else {
        chart.addListener('rendered', function (event) {
            $(".amChartsPeriodSelector .amChartsInputField").datepicker({
                dateFormat: (locale === 'es') ? "dd-mm-yy" : "mm/dd/yy",
            });
        });
    }

    if ($(window).width() < 768) {
        periodSelector.position = "top";
        dataSetSelector.position = "top";
        chart.periodSelector = periodSelector;
        chart.dataSetSelector = dataSetSelector;
        chart.write('chartdiv3');
    } else {
        chart.write('chartdiv3');
    }
}

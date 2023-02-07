//= require amCharts/amcharts
//= require amCharts/serial
//= require amCharts/amstock
//= require amCharts/themes/iredge


var chart = AmCharts.makeChart("renta1", {
    "type": "serial",
    "theme": "light",
    "categoryField": "year",
    "rotate": false,
    "startDuration": 1,
    "titles": [
        {
            "text": "Vencimiento de la deuda",
            "size": 15
        },
        {
            "text": "(Millones de pesos)",
            "size": 12
        }
    ],
    "colors": ["#499cd3", "#f8bd2a", "#ec3e32", "#e6e43d", "#3669af", "#761317"],
    "categoryAxis": {
        "gridPosition": "start",
        "position": "left",
        "gridAlpha": 0
    },
    "trendLines": [],
    "graphs": [
        {
            "balloonText": "$[[value]]",
            "fillAlphas": 1,
            "labelText": "$[[value]]",
            "id": "AmGraph-1",
            "lineAlpha": 0.2,
            // "title": ventas,
            "type": "column",
            "valueField": "ventas"
        },
    ],
    "guides": [],
    "valueAxes": [
        {
            "labelsEnabled": false,
            "unit": "$",
            "unitPosition": "left",
            // "autoGridCount": false,
            // "gridCount": 12,
            "position": "left",
            "axisAlpha": 0,
            "gridAlpha": 0
        }
    ],
    // "legend": {
    //     "align": "center",
    //     "position": "bottom",
    //     "right": -4,
    //
    //     "color": "gray",
    //     "textClickEnabled": true
    // },
    "balloon": {},
    "dataProvider": [
        {
            "year": 2018,
            "ventas": 100,
        },
        {
            "year": 2019,
            "ventas": 372,
        },
        {
            "year": 2020,
            "ventas": 2513,
        },
        {
            "year": 2021,
            "ventas": 972,
        }
    ],
    "export": {
        "enabled": true
    }

});

var chart = AmCharts.makeChart("renta2", {
    "type": "serial",
    "theme": "light",
    "categoryField": "year",
    "rotate": false,
    "startDuration": 1,
    "titles": [
        {
            "text": "Razón de Apalancamiento",
            "size": 15
        },
        // {
        //     "text": "Millones de pesos mexicanos",
        //     "size": 12
        // }
    ],
    "colors": ["#f8bd2a", "#499cd3", "#ec3e32", "#e6e43d", "#3669af", "#761317"],
    "categoryAxis": {
        "gridPosition": "start",
        "position": "left",
        "gridAlpha": 0
    },
    "trendLines": [],
    "graphs": [
        {
            "balloonText": "[[value]]x",
            "fillAlphas": 1,
            "labelText": "[[value]]x",
            "id": "AmGraph-1",
            "lineAlpha": 0.2,
            // "title": ventas,
            "type": "column",
            "valueField": "ventas"
        },
    ],
    "guides": [],
    "valueAxes": [
        {
            "labelsEnabled": false,
            "unit": "$",
            "unitPosition": "left",
            // "autoGridCount": false,
            // "gridCount": 12,
            "position": "left",
            "axisAlpha": 0,
            "gridAlpha": 0
        }
    ],
    // "legend": {
    //     "align": "center",
    //     "position": "bottom",
    //     "right": -4,
    //
    //     "color": "gray",
    //     "textClickEnabled": true
    // },
    "balloon": {},
    "dataProvider": [
      {
          "year": "3T17",
          "ventas": 1.2,
      },
        {
            "year": "3T18",
            "ventas": 3.2,
        },

    ],
    "export": {
        "enabled": true
    }

});

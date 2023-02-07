var map = AmCharts.makeChart("amchart", {
    "type": "map",
    "theme": "light",
    "color": "#FFCCc0",
    "fontFamily": "Helvetica",

    "balloon": {
        horizontalPadding: 0,
        verticalPadding: 0,
        maxWidth: 250,
        borderAlpha: 0,
        borderThickness: 0,
        pointerWidth: 0,
        fontFamily: "Helvetica",
        fontSize: "14",
        background:"red",
    },

    // allLabels: [
    //     {
    //         "color":"black",
    //         "text": "Cancún",
    //         "bold": true,
    //         "x": "92%",
    //         "y": "65%"
    //     }
    // ],
    "dataProvider": {
        "map": "mexicoLow",
        "getAreasFromMap": true,
        "areas": [
            {//ok
                "id": "MX-BCN",
                "description": "",
                color: "#0E0F34",
                customData: `<b>Baja California:</b><br/><ul><li>Parque Industrial</li><li>Hotel Dreams</li></ul>`,

            },
            {//ok
                "id": "MX-JAL",
                "description": "",
                color: "#0E0F34",
                customData: `<b>Puerto Vallarta:</b><br/><ul><li>Marina Vallarta</li></ul>`,
            },
            {//ok
                "id": "MX-DIF",
                "description": "",
                color: "#0E0F34",
                customData: `<b>${cdmx}:</b><br/><ul><li>Wyndham Condesa</li></ul>`,

            },
            {//ok
                "id": "MX-ROO",
                "description": "",
                color: "#0E0F34",
                customData: `<b>${cancun}:</b><br/><ul><li>Grand Island Cancún I</li><li>Grand Island Cancún II</li></ul>`,

            }

        ],
        "images": [
            {
                labelPosition: "center",
                label: cancun,
                "theme": "dark",
                "width": 75,
                "height": 20,
                latitude: 20.679931,
                longitude: -86.177644,
                labelColor: "#111135",
                labelFontSize: 11,
                imageURL: "/static/images/ubicacion.svg",
                labelShiftX: 35,
                labelShiftY: 8

            },


            {
                "theme": "dark",
                "width": 105,
                "height": 20,
                latitude: 31.942389157900553,
                longitude: -115.2065185546875,
                labelPosition: "center",
                label: "Baja California",
                labelColor: "#111135",
                labelFontSize: 11,
                imageURL: "/static/images/ubicacion.svg",
                labelShiftX: 61,
                labelShiftY: 8
                //svgPath:"M9,0C4.029,0,0,4.029,0,9s4.029,9,9,9s9-4.029,9-9S13.971,0,9,0z M9,15.93 c-3.83,0-6.93-3.1-6.93-6.93S5.17,2.07,9,2.07s6.93,3.1,6.93,6.93S12.83,15.93,9,15.93 M12.5,9c0,1.933-1.567,3.5-3.5,3.5S5.5,10.933,5.5,9S7.067,5.5,9,5.5 S12.5,7.067,12.5,9z"

            },

            {
                "theme": "dark",
                "width": 105,
                "height": 20,
                color: "red",
                latitude: 20.799891182088334,
                longitude: -104.07338867187499,
                labelPosition: "center",
                label: "Puerto Vallarta",
                labelColor: "#111135",
                labelFontSize: 11,
                imageURL: "/static/images/ubicacion.svg",
                labelShiftX: 61,
                labelShiftY: 8

            },
            {

                latitude: 19.448697990350824,
                longitude: -98.01069824218749,
                label: cdmx,
                labelPosition: "center",
                "theme": "dark",
                "width": 75,
                "height": 20,
                labelColor: "#111135",
                labelFontSize: 11,
                imageURL: "/static/images/ubicacion.svg",
                labelShiftX: 35,
                labelShiftY: 8

                //SALTILLO BOLA NARANJA
            },

        ]

    },
    "areasSettings": {
        // "autoZoom": true,
        "balloonText": "[[customData]]",
        "selectable": false,
        "color": "#DDDDDD",
        "rollOverOutlineColor":undefined


    }
});
// ["#1c809d","#8eb4e3","#25abd1","#073855","#a8dded","#396077","#91919"]

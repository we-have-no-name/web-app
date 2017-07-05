/**
 * Created by ahmed on 1/7/2017.
 */
$(function () {

    Highcharts.chart('pichart', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: "Data for Date: " + new Date().toJSON().slice(0, 10).replace(/-/g, '/')
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.percentage:.1f} %',
                    style: {
                        color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
                    }
                }
            }
        },
        series: [{
            name: 'Feeling',
            colorByPoint: true,
            data: [{
                name: 'Happy',
                y: 20,
                sliced: true,
                selected: true
            }, {
                name: 'Love',
                y: 10
            }, {
                name: 'Sad',
                y: 10
            }, {
                name: 'Hopeful',
                y: 10
            }, {
                name: 'Angry',
                y: 10
            }, {
                name: 'Hate',
                y: 10
            }, {
                name: 'Natural',
                y: 20
            }, {
                name: 'Hopeless',
                y: 10
            }
            ]
        }]
    });
});

/*
 1 = happy
 2 = love
 3 = hopeful
 4= nutral
 5 = angry
 6 = hopeless
 7 = hate
 8 = sad
 */
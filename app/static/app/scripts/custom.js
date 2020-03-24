$(function(){
    function pageheight(){
        $(".page-height").css("min-height", $(window).height() - $(".navbar").innerHeight() - $(".footer").innerHeight());
    }
    pageheight();
    $(window).resize(function(){
    pageheight();
    });

    if($('[data-toggle="tooltip"]').length > 0){
        $('[data-toggle="tooltip"]').tooltip({
            container: 'body',
            trigger: 'hover click',
            html: true,
            placement: "auto"
        })
    }

    if($('.timepicker').length > 0){
        $('.timepicker').mdtimepicker();
    }
})
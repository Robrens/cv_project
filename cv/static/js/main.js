jQuery(document).ready(function () {

    var novice = $('.novice').attr('data-percent');
    var adenced = $('.advanced-beginer').attr('data-percent');
    var competent = $('.competent').attr('data-percent');
    var professionnel = $('.professionnel').attr('data-percent');
    var expert = $('.expert').attr('data-percent');
    novice = $('.novice').attr('data-percent', '20%');
    adenced = $('.advanced-beginer').attr('data-percent', '40%');
    competent = $('.competent').attr('data-percent', '60%');
    professionnel = $('.professionnel').attr('data-percent', '80%')
    expert = $('.expert').attr('data-percent', '100%');



    jQuery('.skillbar').each(function () {
        jQuery(this).find('.skillbar-bar').animate({
            width: jQuery(this).attr('data-percent')
        }, 4000);
    });
});



var scene = document.getElementById('scene');
var parallaxInstance = new Parallax(scene);
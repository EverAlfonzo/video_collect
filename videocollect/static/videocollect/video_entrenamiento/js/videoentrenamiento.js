$(document).ready(function () {
    var video_div = $('#div_id_video');

    video_div.hide();
    document.querySelector("#id_signo").onchange=function() {
        $.ajax({
                url: '/url_from_signo/',
                data: {
                    'id_signo': $('#id_signo').val(),
                },
                dataType: 'json',
                type: 'get',
                success: function (data) {
                    if(data){
                        if(data['url']){
                            set_video_url(video_div, data['url'], $('#id_signo'));
                        }
                    }
                }
            }
        )};
});

function set_video_url(video_div, video_url, signo) {
    if(signo.val()!==''){
        video_div.html('' +
            '<iframe width="640" height="360" frameborder="0" src="'+video_url.replace("nz/","nz/embed")+'" allowfullscreen"></iframe>');
        video_div.show();
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

jQuery(function($){
    $(document).ready(function(){
        $('#id_tuition_class').change(function(){
            console.log($(this).val());
            $.ajax({
                url:'/api/profile/get-subjects/',
                type: 'POST',
                headers: {
                    content_type: 'application/json',
                    'X-CSRFToken': csrftoken
                },
                data: {'tuition_class': $(this).val()},
                success: function(res) {
                    console.log(res);
                    cols = document.getElementById("id_subject");
                    cols.options.length = 0;
                    for(var k in res){
                        cols.options.add(new Option(k, res[k]));
                    }
                },
                error: function(err){
                    console.error(JSON.stringify(err));
                }
            });
        });
    });
});
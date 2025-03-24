
        function getTimezoneName()
        {
            timezone = jstz.determine();
            var a = timezone.name();
            //console.log(a);
            if (a != 'Asia/Kolkata')
            {
                $('#india_paypal').hide();
                $('#rest_world_paypal').show();
            }
            else
            {
                $('#india_paypal').show();
                $('#rest_world_paypal').hide();
            }
        }
        
        $(function(){
            getTimezoneName();
        });
    
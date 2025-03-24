
            StackExchange.ready(function () {
                var $div = $('#h-related-tags').parent();
                $div.find('.js-show-more').on("click", function () {
                    $div.find('.js-hidden').show();
                    $(this).remove();
                    return false;
                });
            });
        
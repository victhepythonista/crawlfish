
            $(function () {
                function getPosts() {
                    $.get("/users/profile/posts/4934004", {
                        postType: $(".js-post-filters > .js-post-filter-btn.is-selected[data-type]").data("type"),
                        sort: $(".js-post-sorts > .js-post-sort-btn.is-selected").data("sort")
                    }).done(function (html) {
                        $("#js-top-posts").replaceWith(html);
                    });

                }

                $(".js-post-sorts .js-post-sort-btn:not(.js-selected)").on("click", function () {
                    $(".js-post-sorts .js-post-sort-btn").removeClass("is-selected");
                    $(this).addClass("is-selected");
                    getPosts();
                });
                $(".js-post-filters .js-post-filter-btn:not(.js-selected)").on("click", function () {
                    $(".js-post-filters .js-post-filter-btn").removeClass("is-selected");
                    $(this).addClass("is-selected");
                    getPosts();
                });
            })
        
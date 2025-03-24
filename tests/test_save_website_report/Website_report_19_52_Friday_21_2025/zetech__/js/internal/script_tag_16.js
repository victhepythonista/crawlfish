
//<![CDATA[
jQuery(document).ready(function($){
	;(function(element){
		$element = $(element);
		$('li:first-child',$element).addClass("fm-first");
		$('li:last-child',$element).addClass("fm-last");
		$('.fm-container',$element).each(function(){
			$('ul > li',$(this)).eq(0).addClass("fm-first");
			$('ul > li:last-child',$(this)).addClass("fm-last");
		});
		if($('li.fm-active ',$element).length > 0){
			$('li.fm-active ',$element).parents($('li',$element)).addClass('fm-active');
		}
		
				var _time = 0;
		$element.find("li").mouseenter(function(){
			var ul = $(this).children(".fm-container");
			if(ul.length > 0) {
				if(_time > 0)  clearTimeout(_time);
				$(this).addClass("fm-opened");
								_time = setTimeout(function(){
					ul.show(300);
				}, 100);
								$(this).children(".fm-item").children(".fm-button").children("img").attr("src", "https://www.zetech.ac.ke/modules/mod_sj_flat_menu/assets/images/icon_normal.png");
			}
		}).mouseleave(function(){
			var $this = $(this);
			if($this.children(".fm-container").length > 0) {
			if(_time > 0)  clearTimeout(_time);
						time = setTimeout(function(){
					$this.children(".fm-container").hide(300);
				}, 100);
			//$(this).children(".fm-container").hide(300);
						$this.removeClass("fm-opened");
			$this.children(".fm-item").children(".fm-button").children("img").attr("src", "https://www.zetech.ac.ke/modules/mod_sj_flat_menu/assets/images/icon_active.png");
			//$(this).find(".fm-container").css("display","none");
			$this.find(".fm-opened").removeClass("fm-opened");
			//return false;
			}
		});
		
	
	})('#sj_flat_menu_15534362701742576239');
});
//]]>

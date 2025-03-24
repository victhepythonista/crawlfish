BTCJ = jQuery.noConflict();
jQuery(document).ready(function () {
	if (typeof(btcModuleIds) != 'undefined') {
		for (var i = 0; i < btcModuleIds.length; i++) {
			jQuery('#btcontentslider' + btcModuleIds[i]).css("direction", "ltr");
			jQuery('#btcontentslider' + btcModuleIds[i]).fadeIn("fast");
			
			if(btcModuleOpts[i].width=='auto'){
				jQuery('#btcontentslider' + btcModuleIds[i] + ' .slide').width(jQuery('#btcontentslider' + btcModuleIds[i] + ' .slide').width());
			}
			
			BTCJ('#btcontentslider' + btcModuleIds[i]).slides(btcModuleOpts[i]);
			if (jQuery("html").css("direction") == "rtl") {
				jQuery('#btcontentslider' + btcModuleIds[i] + ' .slides_control').css("direction", "rtl");
			}
		}
	}
	jQuery('img.hovereffect').hover(function () {
		jQuery(this).stop(true).animate({
			opacity : 0.5
		}, 300)
	}, function () {
		jQuery(this).animate({
			opacity : 1
		}, 300)
	})
})


jQuery(window).on('load',  function() {
				new JCaption('img.caption');
			});
		jQuery(document).ready(function(){
			new Slideshowck('#camera_wrap_183', {
				height: '37%',
				minHeight: '150',
				pauseOnClick: false,
				hover: 1,
				fx: 'random',
				loader: 'pie',
				pagination: 0,
				thumbnails: 0,
				thumbheight: 75,
				thumbwidth: 100,
				time: 7000,
				transPeriod: 1500,
				alignment: 'center',
				autoAdvance: 1,
				mobileAutoAdvance: 1,
				portrait: 0,
				barDirection: 'leftToRight',
				imagePath: '/media/com_slideshowck/images/',
				lightbox: 'mediaboxck',
				fullpage: 0,
				mobileimageresolution: '0',
				navigationHover: true,
				mobileNavHover: true,
				navigation: true,
				playPause: true,
				barPosition: 'bottom',
				responsiveCaption: 0,
				keyboardNavigation: 0,
				titleInThumbs: 0,
				container: ''
		});
}); 

	
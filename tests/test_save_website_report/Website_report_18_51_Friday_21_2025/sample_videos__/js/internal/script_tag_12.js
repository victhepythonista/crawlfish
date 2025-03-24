
   $(function(){
      $('body').on('click','ul a',function(){
         $('ul a').removeClass('active');
         $(this).addClass('active');
      });
      
      (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');
      ga('create', 'UA-103823277-1', 'auto');
      ga('send', 'pageview');
      
      //(function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
      //(i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
      //m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
      //})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
      //ga('create', 'UA-53116293-1', 'auto');
      //ga('send', 'pageview');
   });
   
   $('.download_video').click(function(){
	var this1 = $(this);
        var id = $(this).attr('data');
        var same_configuration_id = $(this).attr('same_configuration_id');
        var user_id = $(this).attr('user_id');
        
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id , same_configuration_id:same_configuration_id, user_id:user_id},
	    beforeSend : function(){
		//$('body').addClass('class_to_blur');
		//$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
                     //$('body').removeClass('class_to_blur');
                     //$('#ajax_loader').css('display','none');
                     $('#download_video_count').text(parseInt($('#download_video_count').text())+1);
                     
                     data = $.parseJSON(data);
                     console.log(data);
                     
                     if (data.question != undefined)
                     {
                        $('#model-opener').trigger('click');
                        $('#model-img-div').html('<img src="images/kb/'+data.image+'" style="max-width:100%;" >');
                        $('#model-question').text(data.question);
                        $('#model-answer').html(data.answer_short);
                        
                        if (data.link != undefined)
                        {
                           $('#model-link').html('<a href="'+data.link+'" target="_blank" >Know More</a>');
                        }
                     }
                          $.jGrowl.defaults.closer = false;
			  $.jGrowl.defaults.pool = 5;
                          
                          $('#one').jGrowl('Please like us on facebook, thanks in advance!!', {
                                  life: 10000,
                          });
                  },
	    error: function(){
		//$('body').removeClass('class_to_blur');
		//$('#ajax_loader').css('display','none');
	    }
	
	});
	
    });
    
    $('.download_audio').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'audio' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	
	});
	
    });
    
    
    $('.download_xls').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'xls_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	
	});
	
    });
    
    $('.download_image').click(function(){
      //alert(id);
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'image' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
                    $('#download_video_count').text(parseInt($('#download_video_count').text())+1);
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    $('.download_sql').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'sql_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    $('.download_ppt').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'ppt_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    $('.download_csv').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'csv_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	
	});
	
    });
    
    $('.download_pdf').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'pdf_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
	
    });
    
    $('.download_doc').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'doc_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    $('.download_zip').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'zip_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
                    $('#download_video_count').text(parseInt($('#download_video_count').text())+1);
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    
    $('.download_psd').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'psd_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
                    $('#download_video_count').text(parseInt($('#download_video_count').text())+1);
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    $('.download_dxf').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'dxf_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
                    $('#download_video_count').text(parseInt($('#download_video_count').text())+1);
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    $('.download_text').click(function(){
	var id = $(this).attr('data');
	$.ajax({
	    type: "POST",
	    url: "query/download.php",
	    data: { id: id,type:'text_file' },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
                    $('#download_video_count').text(parseInt($('#download_video_count').text())+1);
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	});
    });
    
    
    $('#select_format').change(function(){
	self = $('#select_resolution');
	$.ajax({
	    type: "POST",
	    url: "query/format.php",
	    data: { video_format: $(this).val() },
	    beforeSend : function(){
		$('body').addClass('class_to_blur');
		$('#ajax_loader').css('display','block');
	    },
	    success : function(data){
		    
		    data = $.parseJSON(data);
		    self.empty();
		    $option = $("<option></option>")
			.attr("value", "")
			.text("Select Resolution");
			self.append($option);
		    
		    for (var i = 0;i<data.length; i++) {
			$option = $("<option></option>")
			.attr("value", data[i])
			.text(data[i]);
			self.append($option);
		    }
		    
		    $('body').removeClass('class_to_blur');
		    $('#ajax_loader').css('display','none');
		},
	    error: function(){
		$('body').removeClass('class_to_blur');
		$('#ajax_loader').css('display','none');
	    }
	
	});
	
    });
    
    $('.send-quick-feedback').click(function(){
         var email = $('#quick_feedback_email').val();
         var message = $('#quick_feedback_message').val();
         if ($('#quick_feedback_message').val() == '')
         {
            $('#quick_feedback_message').attr('placeholder','This field is required.');
            $('#quick_feedback_message').focus();
            return false;
         }
         //alert('asd');
         
         $.ajax({
	    type: "POST",
	    url: "query/quickfeedback.php",
	    data: { message: message, email:email },
	    success : function(data){
                     if (data == 'done')
                     {
                        $('.quick-feedback-success').show('slow');
                        $('.quick-feedback-div').hide();
                     }
                     else
                     {
                        $('quick-feedback-error').show('slow');
                        $('.quick-feedback-div').hide();
                     }
                  },
	    error: function(){
		//$('body').removeClass('class_to_blur');
		//$('#ajax_loader').css('display','none');
	    }
         });
      });

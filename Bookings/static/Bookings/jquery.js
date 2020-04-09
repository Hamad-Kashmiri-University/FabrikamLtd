jQuery(function(){
   jQuery('.targetDiv').hide();
   jQuery('.showSingle').click(function(){
         jQuery('.intialDiv').hide();
         jQuery('.targetDiv').hide();
         jQuery('#content'+$(this).attr('target')).fadeIn();
   });
});
// hiding and revealing content on click, all hidden on load


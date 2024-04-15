//$(document).ready(function(){		
	//$('#addResult').click(function(){
	//	$('#resultModal').modal({
	//		backdrop: 'static',
	//		keyboard: false
	//	});		
	//	$("#resultModal").on("shown.bs.modal", function () {
		//	$('#resultForm')[0].reset();				
	//		$('.modal-title').html("<i class='fa fa-plus'></i> Add Result");					
		//	$('#action').val('addResult');
		//	$('#save').val('Save');
	//	});
	//});
//});

$(document).ready(function(){
	$('#addResult').click(function(){
		$('#resultModal').modal('show');
		$('#resultForm')[0].reset();		
		$('.modal-title').html("<i class='fa fa-plus'></i> Add Result");
		$('#action').val('addResult');
		$('#save').val('Save');
	});	
	
});
$(document).ready(function(){
	$('#addStudent').click(function(){
		$('#studentModal').modal('show');
		$('#studentForm')[0].reset();		
		$('.modal-title').html("<i class='fa fa-plus'></i> Add Student");
		$('#action').val('addStudent');
		$('#save').val('Save');
	});	
	
});
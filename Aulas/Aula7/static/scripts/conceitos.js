
function delete_conceito(designation){
    $.ajax( "/conceitos/" + designation, {                                  //$ jQuery; ajax framework
        type:"DELETE",
        success: function(data){
            console.log(data)
            window.location.href= data["redirect_url"]

        },
        error: function(error){
            console.log(error)

        }
    })
}

$(document).ready( function () {
    $('#myTable').DataTable();
} );
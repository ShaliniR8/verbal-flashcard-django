document.addEventListener('DOMContentLoaded', function() {
     updateTags();
     
     document.querySelector('.taggable').addEventListener('mouseup', function() {
          setTimeout(function() {
              const selectedText = window.getSelection().toString();
              if (selectedText.length > 0) {
                   Swal.fire({
                        position: "bottom",
                        title: "Add Tag",
                        showConfirmButton: true,
                        customClass: {
                             popup: 'my-swal'
                         }
                    }).then((result) => {
                         if (result.isConfirmed){
                              var csrftoken = $("[name=csrfmiddlewaretoken]").val();
                              var id = $('input[name="id"]').val()
                              $.ajax({
                                   url: createTagUrl,
                                   method: 'POST',
                                   data: { 
                                        id: id,
                                        tag: selectedText,
                                   },
                                   headers: {
                                        'X-CSRFToken': csrftoken
                                    },
                                   success: function(response){
                                        console.log(response)
                                        updateTag(selectedText)
                                   },
                                   error: function(response){
                                        console.log(response)
                                   }
                              })
                              
                         }
                    });
                    const swalContainer = Swal.getContainer();
                    swalContainer.classList.remove('swal2-backdrop-show')
                  console.log(`User has highlighted: ${selectedText}`);
              }
          }, 10);
      });
      
     $('#toggleTags').on('click', function() {
          var list = document.getElementById('tagsContainer');
          if ($('#tagsContainer').css('display', 'none') ){
               $('#tagsContainer').css('display', '')
          } else {
               $('#tagsContainer').css('display', 'none')
          }
      });
});

function updateTags(){
     tags = $('#all-tags').text().replace(/'/g, '"')
     console.log(tags)
     tags = JSON.parse(tags)
     tags.forEach((tag) => updateTag(tag))
}

function updateTag(tag){
     document.querySelectorAll('.taggable').forEach(function(el){
          text = $(el).html()
          text = text.replace(tag, `<i class='tag'>${tag}</i>`)
          $(el).html(text)
     })
}
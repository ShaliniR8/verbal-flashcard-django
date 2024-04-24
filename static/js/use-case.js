document.addEventListener('DOMContentLoaded', function() {
     // let target;
     // let formGroup;
     // $('.edit').on('click', function(){
     //      target = $(this).closest('.editable').prop('id')
     //      formGroup = $(`.form-group[name="${target}"]`)
     //      formGroupInputElement = document.getElementById(formGroup.find('label').prop('for'))
     //      formGroup.css('display', '')
     // })

     // $('.topic-edit-submit').on('click', function(e){
     //      e.preventDefault()
     //      var id = $('input[name="id"]').val()
     //      var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
     //      $.ajax({
     //           url: editTopicUrl,
     //           type: 'POST',
     //           data:  $('#topic-form').serialize(),
     //           headers: {
     //                'X-CSRFToken': csrfToken
     //           },
     //           complete: function(response){
     //                $(`#${target} span`).text($(formGroupInputElement).val())
                    
     //                $('#editTopic').modal('toggle')
     //                response = response.responseJSON
     //                if (response)
     //                {
     //                     var messageHtml = `
     //                     <div class="alert alert-${response['tag']} mt-5">
     //                          ${response['message']}
     //                          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
     //                          <span aria-hidden="true">&times;</span>
     //                          </button>
     //                     </div>  `;
                         
     //                     $('#message-container').append(messageHtml);
     //                }
                    
     //           }
     //      })
     // })

     $('.delete-use-case').on('click', function(){
          var id = $('input[name="id"]').val()
          var use_case = $(this).closest('.use_case')
          var use_case_id = use_case.attr('id')
          var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
          $.ajax({
               url: deleteUseCaseUrl,
               type: 'POST',
               data:  {
                    id: id,
                    use_case_id: use_case_id
               },
               headers: {
                    'X-CSRFToken': csrfToken
               },
               success: function(response){
                    use_case.remove()
               }
          })
     })
})
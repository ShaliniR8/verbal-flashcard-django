document.addEventListener('DOMContentLoaded', function() {
     // let target;
     // let formGroup;
     $('.edit-use-case').on('click', function(){
          target = $(this).closest('.use_case').find('.editable')
          form_text = target.html().replaceAll('<br>', '\n')
          $('#editUseCase #id_description').val(form_text)
          $('#use-case-form input[name="id"]').val($(this).closest('.use_case').attr('id').replace('use_case_', ''))
     
     })

     $('.use-case-edit-submit').on('click', function(e){
          e.preventDefault()
          var csrfToken = $('[name="csrfmiddlewaretoken"]').val();
          $.ajax({
               url: editUseCaseUrl,
               type: 'POST',
               data:  $('#use-case-form').serialize(),
               headers: {
                    'X-CSRFToken': csrfToken
               },
               complete: function(response){
                    setTimeout(function() {
                         location.reload();
                     }, 1000);
               }
          })
          location.reload()

     })

     $('.delete-use-case').on('click', function(){
          var id = $('input[name="id"]').val()
          var use_case = $(this).closest('.use_case')
          var use_case_id = use_case.attr('id').replace('use_case_', '')
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
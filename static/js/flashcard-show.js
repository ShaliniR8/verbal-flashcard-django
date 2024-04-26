document.addEventListener('DOMContentLoaded', function() {
     updateTags();
     var selectedText;

     $('.taggable').on('mouseup', function() {
          setTimeout(function() {
              selectedText = window.getSelection().toString().trim();
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
              }
          }, 10);
     });

     $('.taggable').on('click', '.tag', function(){
          tag = $(this).text()
          btn_group = $('.tag-button-grp')
          pos = $(this).offset()
          btn_group.css('display', '')
          new_pos = {'top': pos['top'] - 50, 'left': pos['left']}
          btn_group.css(new_pos)
          $('body').on('click', function(e){
              if (!$(e.target).closest('.tag').length){
                    btn_group.css('display', 'none')
              }
          })
          $('.remove-tag').on('click', function(){
               var csrftoken = $("[name=csrfmiddlewaretoken]").val();
               var id = $('input[name="id"]').val();
               console.log(tag)
               $.ajax({
                    url: removeTagUrl,
                    method: 'POST',
                    data: { 
                         id: id,
                         tag: tag,
                    },
                    headers: {
                         'X-CSRFToken': csrftoken
                         },
                    success: function(response){
                         removeTag(tag)
                    },
                    error: function(response){
                         console.log(response)
                    }
               })
               
          })

          $('.tag-to-topic').attr('href', `../create-topic/${tag}`)
     })
});

function updateTags(){
     tags = $('#all-tags').text().replace(/'/g, '"')
     tags = JSON.parse(tags)
     tags.forEach((tag) => updateTag(tag))
}

function updateTag(tag){
     document.querySelectorAll('.taggable').forEach(function(el){
          text = $(el).html()
          text = text.replaceAll(tag, `<span style=""><i class='tag'>${tag}</i></span>`)
          $(el).html(text)
     })
}

function removeTag(tag){
     document.querySelectorAll('.taggable').forEach(function(el){
          text = $(el).html()
          Array.from($(el).find('.tag')).forEach(function(i_tag){
               span_tag =  $(i_tag).closest('span')
               if ( ($(i_tag).text().trim() == tag.trim()) && span_tag){
                    span_html = span_tag.html()
                    text = text.replaceAll(span_html, tag)
                    $(el).html(text)
               }
          })
     })
}
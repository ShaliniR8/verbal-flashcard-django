document.addEventListener('DOMContentLoaded', function() {
     document.querySelectorAll('input[type="text"], textarea').forEach((el) => el.classList.add('form-control'))
     document.querySelectorAll('input[type="text"], textarea').forEach(function(el){
          pTag = $(el).closest('p')
          pTagHTML = pTag.html()
          children = pTag.children()
          newParent = $('<div class="form-group"></div>')
          pTag.wrapAll(newParent).parent().replaceWith(newParent.html(pTagHTML))
     })
     document.querySelectorAll('input[type="text"], textarea').forEach(function(el){
          labelElement = $(`label[for="${el.id}"]`)
          labelText = labelElement.text()
          labelElement.html(`<b> ${labelText} </b>`)
          if (el.required == true){
               labelElement.html(`<b style="color:red"> ${labelText} *</b>`)
          }
     })

});
document.addEventListener('DOMContentLoaded', function() {
     $('#add_comp_row').on('click', function(){
          tr = document.createElement('tr')
          $('table').append(tr)
          i = $(tr).index()
          td1 = `<td><textarea name="comparison_rows-${i}-row1" id="id_comparison_rows-${i}-row1" class="form-control"></textarea></td>`
          td2 = `<td><textarea name="comparison_rows-${i}-row2" id="id_comparison_rows-${i}-row2" class="form-control"></textarea></td>`
          td3 = `<td><input type="checkbox" name="comparison_rows-${i}-DELETE" id="id_comparison_rows-${i}-DELETE" class="form-control"></td>`
          $('table tr:last').append(td1)
          $('table tr:last').append(td2)
          $('table tr:last').append(td3)

          p = document.createElement('p')
          inp1 = `<input type="hidden" name="comparison_rows-${i}-id" id="id_comparison_rows-${i}-id">`
          inp2 = `<input type="hidden" name="comparison_rows-${i}-comparison" id="id_comparison_rows-${i}-comparison">`
          $('form').append(p)
          $(p).append(inp1)
          $(p).append(inp2)

     })

     $('.comp.table').each(function() {
            url = $(this).data('url')
            $(this).DataTable({
                "processing": true,
                "serverSide": true,
                "ajax": {
                    "url":url,
                    "type": "GET"
                },
                "columns": [
                    { "data": "row1" },
                    { "data": "row2" },
                ]
            });
      })
     
    $('.dt-length').each(function(){
        link = $(this).closest('.table-responsive').find('#cmp-url').val()
        html = `<button type="button" class="btn btn-warning bi-trash3-fill delete-comparison" title="Delete this Comparison Table"></button>`
        html += `<a href='${link}' class="btn btn-success bi-pencil-fill edit-comparison ml-1" title="Edit this Comparison Table"></a>`
        
        $(this).closest('.col-md-auto').html(html)
    })

    $('.dt-paging').each(function(){
        $(this).closest('.row').hide()
    })

    $('.delete-comparison').on('click', function(){
        id = $(this).closest('.table-responsive').find('#cmp-id').val()
        var csrftoken = $(".all_comparisons input[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: '/delete-comp/',
            type: 'POST',
            data: {
                id: id
            },
            headers: {
                'X-CSRFToken': csrftoken
            },
        })
        $(this).closest('.table-responsive').remove()
    })

    $('.temp_comp_row').each(function(){
        textareas = $(this).find('textarea')
        ck = $(this).find('input[type="checkbox"]')[0]
        ck.classList.add('form-control')
        row1 = textareas[0]
        row1.removeAttribute('rows')
        row1.removeAttribute('cols')
        row1.classList.add('form-control')
        row2 = textareas[1]
        row2.classList.add('form-control')
        row2.removeAttribute('rows')
        row2.removeAttribute('cols')

        $(this).find('label').each(function(){ $(this).remove()})

        tr = document.createElement('tr')
        td1 = document.createElement('td')
        td2 = document.createElement('td')
        td3 = document.createElement('td')
        td1.append(row1)
        td2.append(row2)
        td3.append(ck)
        tr.append(td1)
        tr.append(td2)
        tr.append(td3)
        $('tbody').append(tr)

        $(this).find('input[type="hidden"]').each(function(){
            $('form').append(this)
        })
    })
})
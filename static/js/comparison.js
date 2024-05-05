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
        $(this).hide()
    })

    $('.dt-paging').each(function(){
        $(this).closest('.row').hide()
    })
})
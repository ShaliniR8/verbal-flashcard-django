document.addEventListener('DOMContentLoaded', function() {
     // $('textarea')[0].addEventListener('mouseup', function() {
     //      setTimeout(function() {
     //          const selectedText = window.getSelection().toString();
     //          if (selectedText.length > 0) {
     //               Swal.fire({
     //                    position: "bottom",
     //                    title: "Add Tag",
     //                    showConfirmButton: true,
     //                    customClass: {
     //                         popup: 'my-swal'
     //                     }
     //                });
     //                const swalContainer = Swal.getContainer();
     //                swalContainer.classList.remove('swal2-backdrop-show')
     //              console.log(`User has highlighted: ${selectedText}`);
     //          }
     //      }, 10);
     //  });

     // $('textarea')[0].addEventListener('keyup', function() {
     // setTimeout(function() {
     //      const selectedText = window.getSelection().toString();
     //      if (selectedText.length > 0) {
     //           Swal.fire({
     //                position: "bottom",
     //                title: "Add Tag",
     //                showConfirmButton: true,
     //                customClass: {
     //                     popup: 'my-swal'
     //                   }
     //                }).then((result) => {
     //                     if (result.isConfirmed){
     //                          $.ajax({
     //                               type: 'POST',
     //                          })
     //                     }
     //                });
     //                const swalContainer = Swal.getContainer();
     //                swalContainer.classList.remove('swal2-backdrop-show')
     //                console.log(`User has highlighted: ${selectedText}`);
     //      }
     // }, 10);
     // });

     $('.flip-card').on('click', function(){
          if ($(this).hasClass('clicked')){
               $(this).removeClass('clicked')
          }else{
               $(this).addClass('clicked')
          }
     }) 
      
});
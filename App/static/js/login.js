 
$(function(){

     //使用Ajax进行登录
     $('#kaka').blur(function () {
        // console.log(1)

         var data = $('#kaka').val()
         rest = {'phone':data}
         $.get('/check/',rest,function (response) {
             console.log(response)
             // console.log(2)
             if (response == '0') {
                 $('#abc').html('')
                 console.log(1)
             }else{
                 $('#abc').html('电话不正确')
             }

         })


     })






})

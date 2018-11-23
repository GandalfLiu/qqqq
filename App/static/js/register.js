

$(function(){
	console.log(1)
	//使用Ajax进行注册
    console.log('哈哈')

    // 验证电话格式
    $('#phone').blur(function () {
        $phone = $('#phone').val()
        // var result = reg1.test($phone)
        if ( $phone.length < 6 | $phone.length > 16) {
            $('#haha').html('')
        }
        else{
            $('#haha').html('帐号格式不正确')
        }
    })

    // 验证密码格式
    $('#password').blur(function () {
        console.log(2)
        var password1 = $('#password').val()
        if (password1.length < 6) {
            $('#hehe').html('密码格式不正确')

        }else{
            $('#hehe').html('')
        }


    })

    // 验证两次密码是否一致
    $('#password2').blur(function () {
        var password1 = $('#password').val()
        var password2 = $('#password2').val()
        if (password1 == password2) {
            $('#oo').html('')
        }else{
            $('#oo').html('两次密码不一致')
        }
    })


    // ajax验证帐号是否电话是否存在

    // $('#phone').blur(function (event) {
    //     var phone = $('#phone').val()
    //     data = {'phone':phone}
    //     $.getJSON('/checkuser/',data,function (response) {
    //         // console.log(response)
    //         if (response == '0') {
    //             $('#qqq').html('电话已经存在')
    //             console.log(1)
    //
    //         }else {
    //             $('#qqq').html('')
    //             console.log(2)
    //         }
    //     })
    //
    // })

    $('#mail').blur(function () {
        var mail = $('#mail').val()
        var pattern = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/;
        var result = pattern.test(mail)
        console.log(33)
        if (result){

        }else{
            $('#aa').html('邮箱不正确')
        }



    })




	
})

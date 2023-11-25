$(document).ready(function () {
 $('.razorpaybutton').click(function (e) { 
   e.preventDefault();
  var fname = $("[name='fname']").val();
  var lname = $("[name='lname']").val();
  var mobile = $("[name='mobile']").val();
  var email = $("[name='email']").val();
  var address = $("[name='address']").val();
  var country = $("[name='country']").val();
  var state = $("[name='state']").val();
  var city = $("[name='city']").val();
  var pincode = $("[name='pincode']").val();
  var token = $("[name='csrfmiddlewaretoken']").val();

  if (fname == "" || lname == "" || mobile == "" || email == "" || address == "" || country == "" || state == "" || city == "" || pincode == ""){
   // alert("all Fields are mandatary")
   swal("Alert!", "all Fields are mandatary!", "warning");
   return false
  }
  else{
       $.ajax({
        method:"GET",
        url: "/procced-to-pay",
        success: function (response) {
         // console.log(response)
         var options = {
          "key": "rzp_test_ivK4czMb2V1yYm", // Enter the Key ID generated from the Dashboard
           "amount": response.total_price * 100, //Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
          "currency": "INR",
          "name": "RJStore", //your business name
          "description": "Thanks for buying a item ..and Visit again",
           "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyBfsjeHSWzhsA3S7y96H00p5bJrFBj7Ysm5w5NL4zOA&s",
          // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
          "handler": function (responseb) {
           alert(responseb.razorpay_payment_id);
           data = {
            'fname':fname,
            'lname':lname,
            'mobile':mobile,
            'email':email,
            'address':address,
            'country':country,
            'state':state,
            'city':city,
            'pincode':pincode,
            'payment_mode':'paid with rajorpay',
            'payment_id':responseb.razorpay_payment_id,
            csrfmiddlewaretoken:token
            
           }
           $.ajax({
            method :"POST",
            url: "/placeorder",
            data: data,
            success: function (responsec) {
             console.log(responsec.status)
             swal("Congratulations!", responsec.status, "success").then((value) => {
              window.location.href = "/my-orders"
             })
             
            }
           });

          },
          "prefill": {
           "name": fname,  //your customer's name
           "email": email,  //"gaurav.kumar@example.com",
           "contact":mobile //"9000090000"
          },
          "notes": {
           "address": "Razorpay Corporate Office"
          },
          "theme": {
           "color": "#3399cc"
          }
         };
         var rzp1 = new Razorpay(options);
         rzp1.open();

         
        }
       });


  }

   

  });
});
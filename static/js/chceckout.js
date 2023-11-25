
$(document).ready(function () {
 $('.razorpaybutton').click(function (e) { 
   e.preventDefault();

   var fname = $('[name = fname]').val();
   var lname = $('[name = lname]').val();
   var email = $('[name = email]').val();
   var mobile = $('[name = mobile]').val();
   var address = $('[name = address]').val();
   var country = $('[name = country]').val();
   var state = $('[name = state]').val();
   var city = $('[name = city]').val();
   var pincode = $('[name = pincode]').val();
   var token = $("[name='csrfmiddlewaretoken']").val();

  if (fname == "" || lname == "" || email == "" || Phone == "" || address == "" || country == "" || city == "" || pincode== "" || state ==""){
   // alert("all Fields are mandarary")
   swal("Alert!", "All fields Mandatary!","warning");
   return false
  }
  else{
   $.ajax({
    method : "GET",
    url: "/procced-to-pay",
    success: function (response) {
     var options = {
       "key": "rzp_test_ivK4czMb2V1yYm", // Enter the Key ID generated from the Dashboard
       "amount": 1 * 100, //response.total_price Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
      "currency": "INR",
      "name": "RJ Store", //your business name
      "description": "Thank you for visiting and Buying..",
      "image": "https://example.com/your_logo",
      // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
      "handler": function (responseb) {
       alert(responseb.razorpay_payment_id);
      //  alert(response.razorpay_order_id);
      //  alert(response.razorpay_signature)
      data = {  
        'fname':fname,
        'lname':lname,
        'mobile': mobile,
        'email': email,
        'address': address,
        'country': country,
        'city': city,
        'state': state,
        'pincode': pincode,
        'payment_mode':"paid by Razorpay",
        'payment_id': responseb.razorpay_payment_id,
        // csrfmiddlewaretoken : token,
        csrfmiddlewaretoken: token
        
      }


      $.ajax({
        method: 'POST' ,
        url: "/placeorder",
        success: function (responsec) {
          console.log(responsec.status)
          swal("Congratulations!", responsec.status, "success").then((value) => {
            window.location.href = "/my-orders"
          })
          // swal(responsec.status);
          
        }
      });
      },
      "prefill": {
       "name": fname + " " +lname , //your customer's name
       "email": email,
       "contact": mobile
      },
      // "notes": {
      //  "address": "Razorpay Corporate Office"
      // },
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




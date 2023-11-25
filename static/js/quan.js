var i = 1;
// function Increment() {
//   if (i < 10) {
//     i++;
//     document.getElementById('quantity_value').value = i;
//   }
// }

// var i = 1;
// function Decrement() {
//   if (i > 1) {
//     i--;
//     document.getElementById('quantity_value').value = i;
//   }
// }

$(document).ready(function () {
  // increment Btn
  $('.increment-btn').click(function (e) { 
    e.preventDefault();

    var inc_value = $(this).closest('.product_data').find('.qty-input').val();
    var value = parseInt(inc_value,10);
    value = isNaN(value) ? 0 : value;
    if(value < 10)

    {
      value++;
      $(this).closest('.product_data').find('.qty-input').val(value);
    }
    
  });
  

  $('.decrement-btn').click(function (e) {
    e.preventDefault();

    var dec_value = $(this).closest('.product_data').find('.qty-input').val();
    var value = parseInt(dec_value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > 1) {
      value--;
      $(this).closest('.product_data').find('.qty-input').val(value);
    }

  }); 
  // add Cart button
  $('.addtocartbtn').click(function (e) { 
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var product_qty = $(this).closest('.product_data').find('.qty-input').val();
    var token = $('input[name = csrfmiddlewaretoken]').val();
    $.ajax({
      method: "POST",
      url: "/add-to-cart",
      data: {
        'product_id':product_id,
        'product_qty': product_qty,
        csrfmiddlewaretoken : token
        
      },
      success: function (response) {
        alertify.success(response.status);

        
      }
    });
    
  });
// add Wishlistbtn
  $('.addwishbtn').click(function (e) {
    e.preventDefault();

    var product_id = $(this).closest('.product_data').find('.prod_id').val();
    var token = $('input[name = csrfmiddlewaretoken]').val();
    $.ajax({
      method: "POST",
      url: "/add-to-wish",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        alertify.success(response.status);
      }
    });
  });


// change quantity
  $('.changequantity').click(function (e) {
    e.preventDefault();

    var product_id =parseInt($(this).closest('.product_data').find('.prod_id').val());
    console.log(typeof(product_id))
    console.log(product_id)
    var product_qty = $(this).closest('.product_data').find('.qty-input').val();
    var token = $('input[name = csrfmiddlewaretoken]').val();
    $.ajax({
      method: "POST",
      url: "/update-to-cart",
      data: {
        'product_id': product_id,
        'product_qty': product_qty,
        csrfmiddlewaretoken: token
      },
      success: function (response) {
        console.log(response)
        alertify.success(response.status);
      }
    });
  });


//  cart delete btn
  $('.delete-to-cart').click(function (e) {
    e.preventDefault();

    var product_id = parseInt($(this).closest('.product_data').find('.prod_id').val());
    var token = $('input[name = csrfmiddlewaretoken]').val();
    $.ajax({
      method: "POST",
      url: "/delete-to-cart",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token

      },
      success: function (response) {
        console.log(response)
        alertify.success(response.status);

        $('.cartdata').load(location.href + " .cartdata");


      }
    });

  });
  $(document).on('click','.delete-wish-button' ,function (e) {
    
    e.preventDefault();

    var product_id = parseInt($(this).closest('.product_data').find('.prod_id').val());
    var token = $('input[name = csrfmiddlewaretoken]').val();
    $.ajax({
      method: "POST",
      url: "/delete-to-wishlist",
      data: {
        'product_id': product_id,
        csrfmiddlewaretoken: token

      },
      success: function (response) {
        console.log(response)
        alertify.success(response.status);

        $('.cartdata').load(location.href + " .cartdata");


      }
    });

  });


});


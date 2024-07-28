 // accordoin Functionality
 function appendTdOne(event, index) {
  target = event.currentTarget;
  classList = target.classList;
// change shape of icon
  if (classList.toString().endsWith("fa-plus")) {
    classList.remove('fa-plus');
    classList.add('fa-minus');
  }
  else {
    classList.remove('fa-minus');
    classList.add('fa-plus');
    console.log("asdasd");
  }
  // get order details table

  var orders = document.getElementById("orders_details-" + index);

  orders.style.display = orders.style.display === 'none' ? 'block' : 'none';
}


  
  function toggleAllOne(action){
    orders_details = document.querySelectorAll('.orders_details');
    // closing 
    console.log(action)
    if (action === 0){
      console.log('asd')
      icons = document.querySelectorAll('.fa-minus');
      orders_details.forEach((order)=>{
        order.style.display = 'none'
      });
      icons.forEach((icon)=>{
        if (icon.classList.contains('fa-minus')){
              icon.classList.remove('fa-minus')
              icon.classList.add('fa-plus')
        }
      });


    // Openning
    }else if(action === 1){
      icons = document.querySelectorAll('.fa-plus');
      orders_details.forEach((order)=>{
        order.style.display = 'block'
      });
      icons.forEach((icon)=>{
          icon.classList.remove('fa-plus')
          icon.classList.add('fa-minus')});
    }

  }
/* With Jquery
    function toggleAll(index)
    {
        if(index == 1) //Expanding
        {                  
            $('table[id*="OrderDetails-"]').show();
            $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-plus")
            $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-minus")                  
        }
        else if(index == 2) //Collapsing
        {
            $('table[id*="OrderDetails-"]').hide();
            $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-minus")
            $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-plus") 
        }
    }
*/

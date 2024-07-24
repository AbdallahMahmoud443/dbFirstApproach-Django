function appendTd(event, index, Level) {
    target = event.currentTarget;
    classList = target.classList;
    if (classList.toString().endsWith("fa-plus")) {
        classList.remove('fa-plus');
        classList.add('fa-minus');
    }
    else {
        classList.remove('fa-minus');
        classList.add('fa-plus');
    }
    if (Level == 1) {
        const orders = document.getElementById("orders-" + index);
        orders.style.display = orders.style.display === 'none' ? 'block' : 'none';
    }
    if (Level == 2) {
        const orders = document.getElementById("orders_details-" + index);
        orders.style.display = orders.style.display === 'none' ? 'block' : 'none';
    }

}

// focus on id of table and id of i in html page to understand
function toggleAll(index) {
    if (index == 1) {
        $('table[id*="orders-"]').show();
        $('table[id*="orders_details-"]').show();

        $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-plus")
        $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-minus")

        $('i[id*="EmployeeId"]').removeClass("my-icon fa fa-solid fa-plus")
        $('i[id*="EmployeeId"]').addClass("my-icon fa fa-solid fa-minus")
    }
    else if (index == 2) {

        $('table[id*="orders-"]').hide();
        $('table[id*="orders_details-"]').hide();

        $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-minus")
        $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-plus")

        $('i[id*="EmployeeId"]').removeClass("my-icon fa fa-solid fa-minus")
        $('i[id*="EmployeeId"]').addClass("my-icon fa fa-solid fa-plus")

    }
    else if (index == 3) {
        $('table[id*="orders-"]').show();
        //$('table[id*="orders_details-"]').hide();
        /*
        $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-minus")
        $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-plus")
        */
        $('i[id*="EmployeeId"]').removeClass("my-icon fa fa-solid fa-plus")
        $('i[id*="EmployeeId"]').addClass("my-icon fa fa-solid fa-minus")

    }
    else if (index == 4) {
        $('table[id*="orders-"]').hide();
        $('table[id*="orders_details-"]').hide();
        
        $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-minus")
        $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-plus")
        
        $('i[id*="EmployeeId"]').removeClass("my-icon fa fa-solid fa-minus")
        $('i[id*="EmployeeId"]').addClass("my-icon fa fa-solid fa-plus")
    }
    else if (index == 5) {
        $('table[id*="orders-"]').show();
        $('table[id*="orders_details-"]').show();
        
        $('i[id*="EmployeeId"]').removeClass("my-icon fa fa-solid fa-plus")
        $('i[id*="EmployeeId"]').addClass("my-icon fa fa-solid fa-minus")
        $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-plus")
        $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-minus")

    }
    else if (index == 6) {
        //$('table[id*="Orders_"]').hide();
        $('table[id*="orders_details-"]').hide();
        $('i[id*="OrderId"]').removeClass("my-icon fa fa-solid fa-minus")
        $('i[id*="OrderId"]').addClass("my-icon fa fa-solid fa-plus")
    }


}
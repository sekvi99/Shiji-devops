function handleAccordion(id) {
    let x = document.getElementById(id);

    if (x.className.indexOf("show") == -1) {
        x.className += " show";
        x.previousElementSibling.className = 
        x.previousElementSibling.className.replace("accord_closed", "accord_open");
        
    } else { 
        x.className = x.className.replace(" show", "");
        x.previousElementSibling.className = 
        x.previousElementSibling.className.replace("accord_open", "accord_closed");
        y.previousElementSibling.className.replace("icon_open", "icon_closed")
    }
    }
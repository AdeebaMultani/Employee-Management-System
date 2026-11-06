//let button = document.getElementById("testButton");
//let message = document.getElementById("message");
//button.addEventListener("click", function () 
//{
//    message.textContent = "JavaScript is working successfully!";
//});

document.addEventListener("DOMContentLoaded", function () {

    // Get all sidebar menu items
    let menuItems = document.querySelectorAll(".menu-item");

    // Get the current URL path
    let currentPath = window.location.pathname;

    menuItems.forEach(function (item) 
    {
        let page = item.dataset.page;

        // Remove active class first
        item.classList.remove("active");

        // Dashboard
        if 
        (
            page === "dashboard" &&
            (currentPath === "/" || currentPath === "")
        ) 
        {
            item.classList.add("active");
        }
        
        // Employees
        else if 
        (
            page === "employees" &&
            currentPath.startsWith("/employees/")
        ) 
        {
            item.classList.add("active");
        }
    });
});
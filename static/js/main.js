document.addEventListener("DOMContentLoaded", function () {


// SIDEBAR ACTIVE MENU

let menuItems = document.querySelectorAll(".menu-item");
let currentPath = window.location.pathname;

menuItems.forEach(function (item) {

    let page = item.dataset.page;

    // Remove active class from every menu item
    item.classList.remove("active");

    // Dashboard
    if (page === "dashboard" && currentPath === "/") {
        item.classList.add("active");
    }

    // Add Employee - check this BEFORE Employees
    else if (page === "add-employee" && currentPath.startsWith("/employees/add/")) {
        item.classList.add("active");
    }

    // Employees
    else if (page === "employees" && currentPath.startsWith("/employees/") && !currentPath.startsWith("/employees/add/")) {
        item.classList.add("active");
    }

    // Departments
    else if (page === "departments" && currentPath.startsWith("/departments/")) {
        item.classList.add("active");
    }

    // Attendance
    else if (page === "attendance" && currentPath.startsWith("/attendance/")) {
        item.classList.add("active");
    }

});



    // EMPLOYEE SEARCH

    let searchInput = document.getElementById("employeeSearch");

    if (searchInput) {

        searchInput.addEventListener("input", function () {

            let searchValue = searchInput.value.toLowerCase();

            let rows = document.querySelectorAll(
                "#employeesTable tbody tr"
            );

            rows.forEach(function (row) {

                let rowText = row.textContent.toLowerCase();

                if (rowText.includes(searchValue)) {
                    row.style.display = "";
                }

                else {
                    row.style.display = "none";
                }

            });

        });

    }

});
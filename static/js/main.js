document.addEventListener("DOMContentLoaded", function () {

    // SIDEBAR ACTIVE MENU

    let menuItems = document.querySelectorAll(".menu-item");

    let currentPath = window.location.pathname;

    menuItems.forEach(function (item) {

        let page = item.dataset.page;

        item.classList.remove("active");

        if (
            page === "dashboard" &&
            (currentPath === "/" || currentPath === "")
        ) {
            item.classList.add("active");
        }

        else if (
            page === "employees" &&
            currentPath.startsWith("/employees/")
        ) {
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
document.addEventListener("DOMContentLoaded", () => {
    // Month Selection - render selected month
    let month = window.location.href.split('months=')[1];
    let options = document.querySelectorAll("option");
    for (let opt of options) {
        if (opt.value == month) {
            opt.selected = true;
        }
        if (opt.value === 'Select Month') {
            opt.selected = true;
        }
    }

    // Display Today Is date
    const n = new Date();
    const y = n.getFullYear();
    const m = n.toLocaleString('default', { month: 'long' });
    const d = n.getDate();
    document.getElementById("date").innerHTML = d + " " + m + " " + y;

    // Task Details Modal
    $('#exampleModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var title = button.data('title');
        var description = button.data('description');
        var taskId = button.data('id');
        var userRank = button.data('userRank');
        var assigned = button.data('assigned');
        var assignedRank = button.data('assignedRank');
        var username = button.data('username');
        var startDate = button.data('startDate');
        var endDate = button.data('endDate');
        var duration = button.data('duration');
        var createdOn = button.data('createdOn');
        var updatedOn = button.data('updatedOn');
        let dayDisplay = duration === 1 ? "day" : "days";
        var modal = $(this);

        modal.find('.description-buttons').addClass('d-flex').removeClass('d-none');
        if (userRank === 3 || userRank === 2 && assigned != username || assignedRank === 0 && userRank !== 0) {
            modal.find('.description-buttons').removeClass('d-flex').addClass('d-none');
        }
        modal.find('.modal-title').text(title);
        modal.find('.modal-body').text(description);
        modal.find('#edit-task-anchor').attr('href', `/tasks/edit/${taskId}`);
        modal.find('#delete-task-anchor').attr('href', `/tasks/delete/${taskId}`);
        modal.find('#start-date-modal').text(startDate);
        modal.find('#end-date-modal').text(endDate);
        modal.find('#duration-modal').text(duration + " " + dayDisplay);
        modal.find('#created-on-modal').text(createdOn);
        modal.find('#updated-on-modal').text(updatedOn);
    });

    // Task Status Modal
    $('#completeModal').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget);
        var title = button.data('title');
        var taskId = button.data('id');
        var userRank = button.data('userRank');
        var taskStatus = button.data('taskStatus');
        var changeStatus = taskStatus === 0 || taskStatus === 2 ? "Completed" : "Scheduled";
        var modal = $(this);

        modal.find('.modal-title').text(title);
        modal.find('.modal-body').text(`Do you want to mark this task as ${changeStatus} ?`);
        modal.find('#yes-anchor').attr('href', `/tasks/complete/${taskId}`);
        modal.find('#no-anchor').attr('href', `/tasks/`);
    });

    // Trigger browser's cofirmation box
    $(document).on('click', '.confirm-delete', function () {
        return confirm('Are you sure you want to delete this?');
    });


    // Month Selection - submitting the form
    const monthForm = document.getElementById("my_form");
    const months = document.getElementById('months');
    months.addEventListener('change', () => monthForm.submit());
    function convertDate(d) {
        const months = { "January": 01, "February": 02, "March": 03, "April": 04, "May": 05, "June": 06, "July": 07, "August": 08, "September": 09, "October": 10, "November": 11, "December": 12 };
        var p = d.split(" ");
        return +(p[2] + "0" + months[p[1]] + p[0]);
    }

    // Table Sorting Functionality
    [...document.querySelectorAll('th')].forEach((item, i) => {
        item.addEventListener('click', () => sortTable(i));
    });

    function sortTable(n) {
        var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
        const headings = document.getElementsByTagName('th');
        let arrowUp = `<i class="fas fa-caret-up"></i>`;
        let arrowDown = `<i class="fas fa-caret-down"></i>`;
        table = document.getElementById("home-table");
        switching = true;

        dir = "asc";

        while (switching) {
            switching = false;
            rows = table.rows;

            for (i = 1; i < (rows.length - 1); i++) {
                shouldSwitch = false;
                x = rows[i].getElementsByTagName("TD")[n];
                y = rows[i + 1].getElementsByTagName("TD")[n];

                if (n === 5) {
                    x = convertDate(x.textContent.trim());
                    y = convertDate(y.textContent.trim());
                }
                else if (n === 0) {
                    x = parseInt(x.innerHTML);
                    y = parseInt(y.innerHTML);
                }
                else {
                    x = x.querySelector('i') && x.querySelector('i').classList.contains('fa-check-circle') ? "completed" : x = x.textContent.trim().toLowerCase();
                    y = y.querySelector('i') && y.querySelector('i').classList.contains('fa-check-circle') ? "completed" : y = y.textContent.trim().toLowerCase();
                }

                if (dir == "asc") {
                    if (x > y) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (dir == "desc") {
                    if (x < y) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }
            if (shouldSwitch) {
                rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
                switching = true;
                switchcount++;
            } else {
                if (switchcount == 0 && dir == "asc") {
                    dir = "desc";
                    switching = true;
                }
            }
        }
        for (let heading of headings) {
            heading.innerHTML = heading.textContent;
        }
        if (dir === "asc") {
            headings[n].innerHTML = headings[n].textContent + `  ` + arrowUp;
        }
        if (dir === "desc") {
            headings[n].innerHTML = headings[n].textContent + `  ` + arrowDown;
        }
    }

});
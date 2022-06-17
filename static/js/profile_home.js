document.addEventListener("DOMContentLoaded", () => {
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
});

$(document).on('click', '.approve-btn', function (event) {
    var form = $('#approve-form');
    var taskId = $(this).data('id');
});

$('#exampleModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var title = button.data('title');
    var description = button.data('description');
    var taskId = button.data('id');
    var userRank = button.data('userRank');
    var assigned = button.data('assigned');
    var username = button.data('username');
    var modal = $(this);
    modal.find('.description-buttons').addClass('d-flex').removeClass('d-none');
    modal.find('.modal-title').text(title);
    modal.find('.modal-body').text(description);
    modal.find('#edit-task-anchor').attr('href', `/tasks/edit/${taskId}`);
    modal.find('#delete-task-anchor').attr('href', `/tasks/delete/${taskId}`);
    if (userRank === 2 && !(assigned == username)) {
        modal.find('.description-buttons').removeClass('d-flex').addClass('d-none');
    }
})

$('#completeModal').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var title = button.data('title');
    var taskId = button.data('id');
    var userRank = button.data('userRank');
    var assigned = button.data('assigned');
    var username = button.data('username');
    var taskStatus = button.data('taskStatus');
    var changeStatus = taskStatus === 0 ? "Completed" : "In Progress";
    var modal = $(this);
    // modal.find('.description-buttons').addClass('d-flex').removeClass('d-none');
    modal.find('.modal-title').text(title);
    modal.find('.modal-body').text(`Do you want to mark this task as ${changeStatus} ?`);
    modal.find('#yes-anchor').attr('href', `/tasks/complete/${taskId}`);
    modal.find('#no-anchor').attr('href', `/tasks/`);
    console.log(userRank);
    // if (userRank === 2 && assigned !== username) {
    //     modal.find('.description-buttons').removeClass('d-flex').addClass('d-none');
    // }
})

$(document).on('click', '.confirm-delete', function () {
    return confirm('Are you sure you want to delete this?');
})

n = new Date();
y = n.getFullYear();
let m = n.toLocaleString('default', { month: 'long' });
d = n.getDate();
document.getElementById("date").innerHTML = d + " " + m + " " + y;

function submit_form(id) {
    console.log(typeof(id));
    var form = document.getElementById(id);
    console.log(form);
    form.submit();
}

function sortTable(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    const headings = document.getElementsByTagName('th');
    let arrowUp = `<i class="fas fa-caret-up"></i>`;
    let arrowDown = `<i class="fas fa-caret-down"></i>`;
    table = document.getElementById("home-table");
    switching = true;
    // Set the sorting direction to ascending:
    dir = "asc";
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        /* Loop through all table rows (except the
        first, which contains table headers): */
        for (i = 1; i < (rows.length - 1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;
            /* Get the two elements you want to compare,
            one from current row and one from the next: */
            x = rows[i].getElementsByTagName("TD")[n];
            y = rows[i + 1].getElementsByTagName("TD")[n];
            /* Check if the two rows should switch place,
            based on the direction, asc or desc: */
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark that a switch has been done: */
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            // Each time a switch is done, increase this count by 1:
            switchcount++;
        } else {
            /* If no switching has been done AND the direction is "asc",
            set the direction to "desc" and run the while loop again. */
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    };
    for (let heading of headings) {
        heading.innerHTML = heading.textContent;
    }
    if (dir === "asc") {
        console.log('dir asc');
        headings[n].innerHTML = headings[n].textContent + `  ` + arrowUp;
    }
    if (dir === "desc") {
        console.log('dir asc');
        headings[n].innerHTML = headings[n].textContent + `  ` + arrowDown;
    }
}
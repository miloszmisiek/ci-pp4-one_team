const thNodes = document.querySelectorAll('th');
var count = 0

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
    if (status === 1) {
        modal.find('.description-buttons').removeClass('d-flex').addClass('d-none');
    }
})

$(document).on('click', '.confirm-delete', function () {
    return confirm('Are you sure you want to delete this?');
})

n = new Date();
y = n.getFullYear();
let m = n.toLocaleString('default', { month: 'long' });
d = n.getDate();
document.getElementById("date").innerHTML = d + " " + m + " " + y;

const getCellValue = (tr, idx) => tr.children[idx].innerText || tr.children[idx].textContent;
const comparer = (idx, asc) => (a, b) => ((v1, v2) =>
    v1 !== '' && v2 !== '' && !isNaN(v1) && !isNaN(v2) ? v1 - v2 : v1.toString().localeCompare(v2)
)(getCellValue(asc ? a : b, idx), getCellValue(asc ? b : a, idx));

thNodes.forEach(th => th.addEventListener('click', ((e) => {
    const table = th.closest('table');
    const tbody = table.querySelector('tbody');
    let arrowUp = `<i class="fas fa-caret-up"></i>`;
    let arrowDown = `<i class="fas fa-caret-down"></i>`;
    let detailsHeading = document.getElementById('details');
    let endDate = document.getElementById('end-date');

    thNodes.forEach(node => node.querySelector('i') ? node.querySelector('i').classList.add('d-none') : null);
    if (e.target === endDate) {
        if (count === 0 && e.target.querySelector('i')) {
            th.innerHTML = th.textContent +  arrowDown;
            count++;
        }
        else if (count % 2 == 0) {
            th.innerHTML = th.textContent + arrowDown;
            count++;
        } else {
            th.innerHTML = th.textContent + arrowUp;
            count++;
        }
    } else {
        th.innerHTML = count % 2 == 0 ? th.textContent + arrowUp : th.textContent + arrowDown;
        count++;
    }
    e.target.querySelector('i') ? e.target.querySelector('i').classList.remove('d-none') : null;
    Array.from(tbody.querySelectorAll('tr'))
        .sort(comparer(Array.from(th.parentNode.children).indexOf(th), this.asc = !this.asc))
        .forEach(tr => tbody.appendChild(tr));
    detailsHeading.querySelector('i') ? detailsHeading.querySelector('i').classList.add('d-none') : null;
})));

function submit_form() {
    var form = document.getElementById("my_form");
    form.submit();
}
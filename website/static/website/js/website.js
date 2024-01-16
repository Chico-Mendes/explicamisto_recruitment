let testemunhosTimeoutId;
let col1_height = 0;
let col2_height = 0;
let listTestemunhos = JSON.parse(document.getElementById('listTestemunhos').textContent);

$(document).ready(function () {
    fillTestemunhos();

    // JavaScript for disabling form submissions if there are invalid fields
    (() => {
        'use strict'

        const t_form = document.getElementById("t-form");
        t_form.addEventListener('submit', event => {
            if (!t_form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
                t_form.classList.add('was-validated');
            } else {
                // Prevent the default form submission
                event.preventDefault();
                postTestemunho();
                t_form.reset();
            }
        }, false)
    })()

    $('#t-year').mask('00/00');
    testemunhosTimeoutId = setTimeout(() => {
        getTestemunhos();
    }, 30000);
});

function fillTestemunhos() {
    console.log("fillTestemunhos");

    const col1 = document.getElementById('testemunhos-col1');
    const col2 = document.getElementById('testemunhos-col2');
    col1.innerHTML = "";
    col2.innerHTML = "";
    col1_height = 0;
    col2_height = 0;

    listTestemunhos.forEach(testemunho => {
        putTestemunho(testemunho);
    });
}

function putTestemunho(testemunho) {
    const col1 = document.getElementById('testemunhos-col1');
    const col2 = document.getElementById('testemunhos-col2');

    // Create a new entry
    const newEntry = document.createElement('div');
    newEntry.className = 'mt-3';

    const par = document.createElement('p');
    par.classList.add('border', 'rounded', 'border-dark', 'p-4');
    par.innerHTML = `"${testemunho.text.replace(/\n/g, '<br>')}"`;
    newEntry.appendChild(par);

    const user = document.createElement('div');
    user.className = 'd-flex';
    user.innerHTML = `<img class="rounded-circle flex-shrink-0 me-3 fit-cover border rounded border-dark" width="50" height="50" alt="User avatar" src="${img_src}" />
        <div>
        <p class="fw-bold text-primary mb-0">
        <strong>${testemunho.username}</strong>
        </p>
        <p class="mb-0">${testemunho.occupation} ${testemunho.year}</p>
        </div>`
    newEntry.appendChild(user);

    // Append the new entry to the smaller column
    if (col1_height <= col2_height) {
        col1.appendChild(newEntry);
        col1_height += newEntry.offsetHeight;
    } else {
        col2.appendChild(newEntry);
        col2_height += newEntry.offsetHeight;
    }
}

function getTestemunhos() {
    $.ajax({
        url: "/api/testemunhos/",
        type: 'GET',
    })
        .done(function (data) {
            if (!arraysAreEqual(data, listTestemunhos)) {
                listTestemunhos = data
                fillTestemunhos()
            }
        })
        .fail(function (error) {
            console.error(error.statusText, ":", error.responseText);
        })
        .always(function () {
            testemunhosTimeoutId = setTimeout(() => {
                getTestemunhos();
            }, 30000);
        });
}

function postTestemunho() {
    // Create a dictionary to store form data
    let postData = {};

    // Retrieve values from the form and store in the dictionary
    postData.user = {
        name: $("#t-username").val()
    };
    postData.occupation = $("#t-occupation").val();
    postData.year = $("#t-year").val();
    postData.text = $("#t-testemunho").val();


    console.log("POST", postData);
    $.ajax({
        url: "/api/testemunhos/",
        type: "POST",
        data: JSON.stringify(postData), // Convert data to JSON string
        contentType: "application/json", // Set content type to JSON
    })
        .done(function (data) {
            listTestemunhos.push(data);
            putTestemunho(data);
        })
        .fail(function (error) {
            console.error(error.statusText, ":", error.responseText);
        })
        .always(function () {
            clearTimeout(testemunhosTimeoutId);
            testemunhosTimeoutId = setTimeout(() => {
                getTestemunhos();
            }, 30000);
        });
}

// Function to compare two arrays of objects
function arraysAreEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }

    for (let i = 0; i < arr1.length; i++) {
        // Compare each object's properties
        for (let key in arr1[i]) {
            if (arr1[i][key] !== arr2[i][key]) {
                return false;
            }
        }
    }

    return true;
}
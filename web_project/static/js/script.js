function showPage(pageId) {
    const pages = document.querySelectorAll('.page');
    pages.forEach(page => {
        page.style.display = 'none';
    });
    document.getElementById(pageId).style.display = 'block';
}

document.querySelectorAll('.arrow').forEach(arrow => {
    arrow.addEventListener('click', () => {
        alert('矢印がクリックされました');
    });
});

function getVariable() {
    axios.get('/get_variable')
        .then(function (response) {
            document.getElementById('variableValue').textContent = response.data.variable;
        })
        .catch(function (error) {
            console.log(error);
        });
    }

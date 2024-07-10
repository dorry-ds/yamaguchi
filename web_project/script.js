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

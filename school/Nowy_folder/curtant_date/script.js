function curant_date() {
    function update() {
        const now = new Date();
        let dd = now.getDate();
        let mm = now.getMonth() + 1;
        let yyyy = now.getFullYear();

        let hh = now.getHours();
        let min = now.getMinutes();
        let ss = now.getSeconds();

        dd = ('0' + dd).slice(-2);
        mm = ('0' + mm).slice(-2);
        hh = ('0' + hh).slice(-2);
        min = ('0' + min).slice(-2);
        ss = ('0' + ss).slice(-2);

        const dateStr = dd + '/' + mm + '/' + yyyy;
        const timeStr = hh + ':' + min + ':' + ss;

        const dateEl = document.getElementById('date_pl');
        if (dateEl) dateEl.textContent = dateStr;

        const timeEl = document.getElementById('time_pl');
        if (timeEl) timeEl.textContent = timeStr;
    }

    update();
    return setInterval(update, 1000);
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', curant_date);
} else {
    curant_date();
}
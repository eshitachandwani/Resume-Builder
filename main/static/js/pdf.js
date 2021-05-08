window.onload = function() {
    document.getElementById("download")
        .addEventListener("click", () => {
            const template = this.document.getElementById("w");
            console.log(template);
            console.log(window);
            var opt = {
                filename: 'Resume.pdf',
                image: { type: 'jpeg', quality: 3 },
                html2canvas: { scale: 3 },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().from(template).set(opt).save();
        })
}

//! Html to pdf converter
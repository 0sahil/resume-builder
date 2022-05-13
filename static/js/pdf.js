window.onload = function () {
    document.getElementById("download")
        .addEventListener("click", () => {
            const invoice = this.document.getElementById("formContainer");
            console.log(invoice);
            console.log(window);
            var opt = {
                margin: 2,
                filename: 'myfile.pdf',
                image: { type: 'jpeg', quality: 1 },
                html2canvas: { scale: 0.5 },
                jsPDF: { unit: 'in', format: 'letter', orientation: 'portrait' }
            };
            html2pdf().from(invoice).set(opt).save();
        })
}
window.addEventListener('load',function () {
    var receipts = document.getElementsByTagName("tr");
    var numReceipts = receipts.length - 1;

//Changes color of checkbox in /receipts depending approved or not
    for (let i = 1; i <= numReceipts; i++) {
        const currentId = "RECEIPTID" + i;
        const currentCheckbox = document.getElementById(currentId);
        if(currentCheckbox.checked){
            console.log(currentId);
            document.getElementsByClassName("receipt-label")[i - 1].style.backgroundColor = "green";
        }
    }
});



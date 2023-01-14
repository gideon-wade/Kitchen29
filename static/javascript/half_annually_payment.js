
//Changes color of balance in /half_annually_payment depending on negative or not
for (let i = 1; i <= 17; i++) {
    if(i < 10) {
        i = "0" + i
    }
    const currentId = "23" + i + "balance";
    const currentBalance = document.getElementById(currentId).textContent;
    if(currentBalance > 0){
        document.getElementById(currentId).style.color="green"
    } else if(currentBalance < 0){
        document.getElementById(currentId).style.color="red"
    }
}
var residents = document.getElementsByTagName("tr");
var numResidents = residents.length - 1;

//Changes color of checkbox in /receipts depending approved or not
for (let i = 1; i < numResidents; i++) {
    const currentId = "23" + i + "balance";
    const currentBalance = document.getElementById(currentId).textContent;
    if(currentBalance > 0){
        document.getElementById(currentId).style.color="green"
    } else if(currentBalance < 0){
        document.getElementById(currentId).style.color="red"
    }
}


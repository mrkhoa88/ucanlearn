var person = {
    ho:         "Tran",
    ten:        "Khoa",
    chaomung:   function(){
        console.log("Welcome " + this.ho + " " + this.ten)
    }
}

person.chaomung();

console.log(person["ten"]);
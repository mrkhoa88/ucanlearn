function tinhtong(a,b){
    return a+b;
}

var x = tinhtong(5,4);
console.log("Tong bang: ",x);

function hello(){
    console.log("Welcome to khoatran.com")
}

function goiham(fn){
    fn();
}

goiham(hello);

var tong = function(){
    console.log("Lap trinh NodeJS")
}

tong();
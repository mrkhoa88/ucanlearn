var http = require("http");
var fs = require("fs");
http.createServer(function(req, res){ //request al khach hang goi len, res la ket qua tra ve
    res.writeHead(200,{"Content-Type":"application/json"});
    var obj = {
        ho: "Tran",
        ten: "Khoa",
        namsinh: "1988"

    };
    res.end(JSON.stringify(obj));
}).listen(7777);
var http = require("http");
var fs = require("fs");
http.createServer(function(req, res){ //request al khach hang goi len, res la ket qua tra ve
    res.writeHead(200,{"Content-Type":"text/html"});
    fs.createReadStream(__dirname + "/8-index.html").pipe(res);
}).listen(8888);
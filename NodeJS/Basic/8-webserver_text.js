var http = require("http");
http.createServer(function(req, res){
    res.writeHead(200,{"Content-Type":"text/plain"});
    res.end("KhoaTran.com")
}).listen(8888);
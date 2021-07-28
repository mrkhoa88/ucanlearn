function KhoaHoc(ten,hocphi){
    this.Ten = ten;
    this.HocPhi = hocphi;
}
//khoa hoc se co hanh dong mo ta nhu sau:
KhoaHoc.prototype.mota = function(){
    console.log("Hello " + this.Ten + " " + this.HocPhi);
}

var nodejs = new KhoaHoc("NodeJS", 100);

nodejs.mota()
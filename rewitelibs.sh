#!/usr/bin/bash
oldprefix="/usr/darwinx/usr"
newprefix="/Library/Frameworks/GSharpKit"
test=`otool -L $1 | grep $oldprefix | cut -d ' ' -f 1`
newid=""
for file in $test
do
	newpath=$(echo $file | sed "s!$oldprefix!$newprefix!")
	if [ "$newid" = "" ]; then
		newid=$newpath
	fi
	install_name_tool -change $file $newpath -id $newid $1
done


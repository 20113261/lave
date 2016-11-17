#/bin/sh

for file in `ls $1`
do
    sed -i -e 's/'$2'/'$3'/g' $1$file
done

# Setting the folder path
cd $(dirname $([ -L $0 ] && readlink -f $0 || echo $0))


# Deleting all generated files
cd gen
find . -name "*.py" -type f -delete
cd trash
find . -name "*.py" -type f -delete

cd .. 
cd ..
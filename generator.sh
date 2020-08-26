# Setting the folder path
cd $(dirname $([ -L $0 ] && readlink -f $0 || echo $0))


# Deleting old generated files
cd gen
find . -name "*.py" -type f -delete
find . -name "generated.sh" -type f -delete
cd trash
find . -name "*.py" -type f -delete

cd .. 
cd ..


# Executing app
/usr/bin/python3  code_generator.py
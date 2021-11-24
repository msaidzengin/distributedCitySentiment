BASEDIR=$(dirname "$0")
echo "$BASEDIR"
python "$BASEDIR"/main.py >> "$BASEDIR"/log_`date +\%Y\-\%m\-\%d\-\%H:\%M:\%S`.txt 2>&1 &
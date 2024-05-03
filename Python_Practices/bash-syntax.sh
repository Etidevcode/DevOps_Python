
# shellcheck disable=SC2034
x=0

echo "Learning Indentation"
echo

if [ $x -eq 0 ]
then
  echo "In the If Block."
  echo "Value of is 0"
else
  echo "In the else block."
  echo "Value of x is non zero"
fi

echo
echo "This statement is out of if/else block."

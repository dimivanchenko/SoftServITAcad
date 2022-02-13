#!/bin/sh


echo "---===task 1===---"
echo "Введіть форму прізвища Іванченко"
read sname
if echo $sname | grep -qE '^Іванченк(о|а|у)$'; then
echo "$sname - це форма прізвища Іванченко"
else
echo "$sname - це не форма призвища Іванченко"
fi
echo "Press any key"
read a

echo "---===task 2===---"
echo "Введіть форму ім'я Дмитро"
read name
if echo $name | grep -qE '^Ді{0,1}м(((у|а|к){0,1}(ся|а)$)|(итр(о|ик)$))'; then
echo "Це форма імені Дмитро"
else
echo "Це не форма імені Дмитро"
fi
echo "Press any key"
read a

echo "---===task 3===---"
cod ()
{
case $1 in
  031|0312|03122) echo "$1 - Закарпаття";;
  032|0322|03222) echo "$1 - Львів";;
  033|0332|03322) echo "$1 - Волинь";;
  034|0342|03422) echo "$1 - Івано-Фр";;
  035|0352|03522) echo "$1 - Тернопіль";;
  036|0362|03622) echo "$1 - Рівне";;
  037|0372|03722) echo "$1 - Чернівці";;
  038|0382|03822) echo "$1 - Хмельницький";;
			   *) echo "$1 - Не західна зона"
esac
}

echo "Введіть телефонний код: ";
read tcod;
cod $tcod;

if echo $tcod | grep -qE '^03[1-8]2{0,2}$'; then
echo "Номер західної зони"
else
echo "Номер не західної зони "
fi
echo "Press any key"
read a

echo "---===task 4===---"
while IFS= read -r line
do
  grep -E "bash$" | grep -Eo "^\w+"

done < /etc/passwd
echo "Press any key"
read a

echo "---===task 5===---"
while IFS= read -r line
do
  grep -E "^daemon"

done < /etc/group
echo "Press any key"
read a

echo "---===task 6===---"
while IFS= read -r line
do
  grep -vE "^daemon"

done < /etc/group
echo "Press any key"
read a

echo "---===task 7===---"
sudo -s find /etc -name *README* | grep -E "README$" > ~/SoftServ/Scripts/temp7.txt;

count=0;

while IFS= read -r line
do
  count=$(($count+1))
done < ~/SoftServ/Scripts/temp7.txt

echo "Сount of file - $count";

rm ~/SoftServ/Scripts/temp7.txt
echo "Press any key"
read a

echo "---===task 8===---"
cd ~ && find -maxdepth 1 -cmin -600 -type f
echo "---====Bye===----"









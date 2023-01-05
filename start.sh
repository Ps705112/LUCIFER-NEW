if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/Pankajpandiyar/LUCIFER-NEW.git /Lucifer-NEW
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Lucifer-NEW
fi
cd /LUCIFER-NEW
pip3 install -U -r requirements.txt
echo "Starting Lucifer...."
python3 bot.py

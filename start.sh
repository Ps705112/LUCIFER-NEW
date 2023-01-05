if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://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@github.com/Pankajpandiyar/LUCIFER-NEW.git /LUCIFER-NEW
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /LUCIFER-NEW
fi
cd /LUCIFER-NEW
pip3 install -U -r requirements.txt
echo "Starting Lucifer...."
python3 bot.py

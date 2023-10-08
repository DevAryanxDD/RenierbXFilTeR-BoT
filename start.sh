if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/DevAryanxDD/RenierbXFilTeR-BoT.git /RenierbXFilTeR-BoT 
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /RenierbXFilTeR-BoT
fi
cd /RenierbXFilTeR-BoT
pip3 install -U -r requirements.txt
echo "Starting RenierbX...."
python -m RenierbX

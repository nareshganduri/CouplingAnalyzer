virtualenv venv
venv\Scripts\pip install -r requirements.txt
mkdir instance
python -c "import os; print 'SECRET_KEY = %%s' %% repr(os.urandom(24));" > instance/config.py
@echo All set up! Run venv\Scripts\python run.py to run the local server
@echo Visit localhost:3000 in your browser to try it out

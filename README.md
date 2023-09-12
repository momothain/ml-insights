# ml-insights
new ml-service: Creates and updates a database in a Python Flask application with Pandas to store ML tagging data for media from native-pipeline

## Instructions
### create venv using requirements.txt
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
flask run #run
python app.app #alt run
pytest #test
```

## Postgres
https://instalily.slack.com/docs/T03AKM3LMGX/F05N944CQBF?focus_section_id=temp:C:MNbb4cc8ac61f02438a8e4744315
```
brew install postgresql@13
```

## File Structure
https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

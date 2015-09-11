This code allows you to query a GitHub repo and export into a csv file suitable for import into Jira

# Setup #

* `virtualenv venv` # initialize a virtual environment
* `. ./activate.sh` # to activate the virtual environment
* `pip install -r requirements.txt` # install the dependencies
* rename `.env_sample` to `.env`, update the credentials and remove the comments
* Change the value of `repository` in `test.py` to match the repository you wish to query
* `python test.py`

The result will be a csv.txt file that you can use to import Jira.

## Notes:
I added "'s around the title to account for commas that would have broken the csv file. You'll want to remove the quotes before uploading to Jira

The process for importing the CSV file into JIRA is [here](https://confluence.atlassian.com/jira/importing-data-from-csv-185729516.html)
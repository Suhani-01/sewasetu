# 1. Imports tools – Imports tools to create fake database objects, mock SMS requests, and handle file paths.
# 2. Finds the script – Sets the project root path and locates the original deemed_approval.py file.
# 3. Loads the original script – Loads the script so the test can access and execute its main() function.
# 4. Creates a fake database – Uses MagicMock() to simulate the database connection and cursor without modifying real records.
# 5. Runs the job safely – Mocks the database connection and SMS requests, then runs job.main().
# 6. Checks the SQL query – Verifies that the original script updates the applications table, targets PENDING applications, and checks whether their submission date is earlier than the SLA cutoff.


from unittest.mock import MagicMock, patch

# MagicMock - To create a fake database connection and cursor.
# patch - To prevent real database connections and SMS requests.


import importlib.util # To load script for testing.
from pathlib import Path # To locate script 

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "app" / "scripts" / "deemed_approval.py"


# to load deemed_approval script to use its functions
def load_job():
    spec = importlib.util.spec_from_file_location(
        "deemed_approval", SCRIPT
    )

    # job will let us access things defined in the script
    job = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(job)
    return job


def test_approval_query_targets_overdue_pending_applications():
    job = load_job()

    #fake connection with the db
    fake_conn = MagicMock()
    # fake cursor to process sql query
    fake_cursor = fake_conn.cursor.return_value

    # Prevent any real SMS request
    with patch.object(job.requests, "post"):
        # Prevent any real database connection
        with patch.object(
            job.psycopg2, "connect", return_value=fake_conn
        ):
            job.main()

    query = fake_cursor.execute.call_args[0][0]

    assert "UPDATE applications" in query
    assert "status = 'PENDING'" in query
    assert "submitted_at < %s" in query
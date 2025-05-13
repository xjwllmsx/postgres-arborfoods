# Arbor Foods Trading Co.: SQL Data Analysis Project

This project simulates data analysis for **Arbor Foods Trading Co.**, a fictional wholesale food distributor. The goal is to showcase SQL-based analytical workflows using **PostgreSQL**, including:

-   Common Table Expressions (CTEs)
-   Window Functions (`RANK`, `LAG`, `AVG OVER`)
-   Sales and customer analysis
-   Employee performance metrics

The project includes a full PostgreSQL setup, a Jupyter notebook with analysis, and a lightweight SQLite-powered Binder demo for live viewing.

## Tech Stack

<div>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" title="PostgreSQL" width="40" height="40" />&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" title="Docker" width="40" height="40" />&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" title="Python" width="40" height="40" />&nbsp;
  <img src="https://cdn.simpleicons.org/jupyter/F37626" title="Jupyter" width="40" height="40" />&nbsp;
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" title="SQLite" width="40" height="40" />&nbsp;
</div>

## Contents

-   [Project Structure](#project-structure)
-   [Scripts](#scripts)
-   [Live Demo (via Binder)](#live-demo-via-binder)
-   [Running the Full PostgreSQL Version](#running-the-full-postgresql-version)
    -   [Environment Variables to Set](#environment-variables-to-set)
    -   [Steps to Run](#steps-to-run)
        -   [1. Clone the repository](#1-clone-the-repository)
        -   [2. Edit Docker credentials (if needed)](#2-edit-docker-credentials-if-needed)
        -   [3. Start the PostgreSQL container](#3-start-the-postgresql-container)
        -   [4. Restore the database](#4-restore-the-database)
        -   [5. Open the Jupyter Notebook](#5-open-the-jupyter-notebook)
-   [License](#license)
-   [Acknowledgments](#acknowledgments)

## Project Structure

```
postgres-arborfoods/
├── binder/ # Binder demo environment (SQLite-based)
│ ├── binder-demo.ipynb # SQLite version of the notebook
│ ├── arborfoods.db # Auto-generated SQLite database
│ ├── data/ # CSVs generated from PostgreSQL
│ │ ├── suppliers.csv
│ │ ├── customers.csv
│ │ └── ...
│ ├── postBuild # Script to build arborfoods.db from CSVs
│ ├── requirements.txt # Python dependencies for Binder
│ ├── runtime.txt # Python version for Binder
│ └── setup_sqlite.py # Loads CSVs into SQLite (arborfoods.db)
│
├── data/ # PostgreSQL database dumps
│ ├── arborfoods_dump.sql # Optional: SQL dump (for psql restore)
│ └── arborfoods_dump.tar # SQL binary dump (for pg_restore)
│
├── docker/ # Docker Compose setup for PostgreSQL
│ └── docker-compose.yml
│
├── notebook/
│ └── postgresql-arborfoods.ipynb # Full PostgreSQL notebook
│
├── scripts/ # Utility scripts
│ └── export_postgres_tables.py # Exports all PostgreSQL tables to CSV
│
├── LICENSE # MIT license for code/scripts
├── pyproject.toml # Project dependencies (managed with uv)
├── uv.lock # Locked dependency versions
├── README.md # Project overview and instructions
└── .gitignore # Standard ignore file
```

## Scripts

This project includes two utility scripts that support reproducibility and Binder compatibility:

### `scripts/export_postgres_tables.py`

Exports all tables from the PostgreSQL `arborfoods_db` database into individual CSV files using `pandas` and `SQLAlchemy`.

-   Output location: `binder/data/`
-   Run from the project root:

```bash
python scripts/export_postgres_tables.py
```

### binder/setup_sqlite.py

Loads the exported CSV files into a local SQLite database (arborfoods.db) for use in the Binder demo notebook.

Run automatically on Binder via postBuild

Can be run manually during testing:

```bash
python binder/setup_sqlite.py
```

## Live Demo (via Binder)

You can explore a demo version of this project using SQLite, directly in your browser — no setup required.

[![Launch in Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/xjwllmsx/postgres-arborfoods/HEAD?filepath=binder/binder-demo.ipynb)

## Running the Full PostgreSQL Version

This project includes a docker-compose.yml file to spin up a PostgreSQL database in a containerized environment.

**Note**: The Docker Compose file is configured to:

-   Create a container named `postgresql_arborfoods`
-   Create a database (e.g., `arborfoods_db`)
-   Set your desired `POSTGRES_USER` and `POSTGRES_PASSWORD`
-   Expose PostgreSQL on port `5432`
-   Persist data in a named Docker volume

### Environment Variables to Set

Update these placeholders in the docker-compose.yml before launching:
| Placeholder | Description |
| ---------------- | ----------------------------------------- |
| `userName` | The PostgreSQL username you want to use |
| `userPassword` | The corresponding password for the user |
| `arborfoods_db` | The name of the database to create |
| `volumeLocation` | Name of the Docker volume to persist data |

### Steps to Run

#### 1. Clone the repository

```bash
git clone https://github.com/xjwllmsx/postgres-arborfoods.git
cd postgres-arborfoods
```

#### 2. Edit Docker credentials (if needed)

Open docker/docker-compose.yml and set:

```yaml
POSTGRES_USER: your_username
POSTGRES_PASSWORD: your_password
POSTGRES_DB: your_database_name
```

Example:

```yaml
POSTGRES_USER: joseph
POSTGRES_PASSWORD: secretpassword
POSTGRES_DB: arborfoods_db
```

#### 3. Start the PostgreSQL container

```bash
cd docker
docker-compose up -d
```

This will spin up the container and create the database.

#### 4. Restore the database

Return to the project root and run:

```bash
# Copy the .tar file into the container
docker cp ./data/arborfoods_dump.tar postgresql_arborfoods:/arborfoods.tar

# Execute the SQL script inside the container
docker exec -it postgresql_arborfoods psql -U your_username -d your_database_name -f /arborfoods.tar
```

Replace:

-   `your_username` → same as `POSTGRES_USER`
-   `your_database_name` → same as `POSTGRES_DB`

#### 5. Open the Jupyter Notebook

Navigate to:

```bash
notebooks/postgresql-arborfoods.ipynb
```

Inside the notebook, connect to your Postgres DB using:

```python
%sql postgresql://your_username:your_password@localhost:5432/your_database_name
```

## License

This project is dual-licensed:

-   **Code, SQL scripts, and setup files** are licensed under the [MIT License](LICENSE).
-   **Notebook markdown, analysis commentary, and educational content** are licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

The dataset used in this project is based on the [Northwind PostgreSQL dataset](https://github.com/pthom/northwind_psql/tree/master), adapted for demonstration purposes.

## Acknowledgments

-   [Northwind Traders dataset](https://github.com/pthom/northwind_psql/tree/master)
-   [Binder Project](https://mybinder.org/)

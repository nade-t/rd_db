import sqlalchemy as db
user = "root"
password = "admin"
host = "localhost"
db_name = "rd_scoring"
engine = db.create_engine("mysql+pymysql://{}:{}@{}/{}".format(user, password, host, db_name), echo=False)
metadata = db.MetaData()

def setup_tables():
    """
    Initialises all of the database tables - only required to run at first initialisation of the program.
    No input required. Checks that the tables do not exist before creating them: if a table already exists, a
    new table is not created and a message is printed to the screen.
    """
    # Create the skater table
        
    inspector = db.inspect(engine)
    if not inspector.has_table("skater"):
        skater = db.Table("skater", metadata,
                       db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                       db.Column("skater_number", db.VARCHAR(4), nullable=False),
                       db.Column("skater_name", db.String(50), nullable=False)) 
        metadata.create_all(engine)
        print("Skater table created successfully")
    else:
        print("Skater table already exists in the database")

    # Create the adv_skater table
    adv_skater = db.Table("adv_skater", metadata,
                         db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                         db.Column("skater_reference", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                         db.Column("eligible_for_selection", db.Boolean, nullable=False),
                         db.Column("primary_position", db.String(10), nullable=False))     
    inspector = db.inspect(engine)
    if not inspector.has_table("adv_skater"):
        metadata.create_all(engine)
        print("Advanced Skater table created successfully")
    else:
        print("Advanced Skater table already exists in the database")

  

    # Create the game table
    game = db.Table("game", metadata,
                    db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                    db.Column("date", db.DATE, nullable=False),
                    db.Column("opposition", db.VARCHAR(50), nullable=False),
                    db.Column("home_game", db.Boolean, nullable=False),
                    db.Column("game_type", db.VARCHAR(10), nullable=False),
                    db.Column("sanctioned", db.Boolean, nullable=False))    
    inspector = db.inspect(engine)
    if not inspector.has_table("game"):
        metadata.create_all(engine)
        print("Game table created successfully")
    else:
        print("Game table already exists in the database")

  # Create the roster table
    roster = db.Table("roster", metadata,
                      db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                      db.Column("game_id", db.Integer, db.ForeignKey("game.id"), nullable=False),
                      db.Column("player1", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                      db.Column("player2", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                      db.Column("player3", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                      db.Column("player4", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                      db.Column("player5", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                      db.Column("player6", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player7", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player8", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player9", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player10", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player11", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player12", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player13", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player14", db.Integer, db.ForeignKey("skater.id"), nullable=True),
                      db.Column("player15", db.Integer, db.ForeignKey("skater.id"), nullable=True))    
    inspector = db.inspect(engine)
    if not inspector.has_table("roster"):
        metadata.create_all(engine)
        print("Roster table created successfully")
    else:
        print("Roster table already exists in the database")

    # Create the game score table
    gamescore = db.Table("gamescore", metadata,
                          db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                          db.Column("game_id", db.Integer, db.ForeignKey("game.id"), nullable=False),
                          db.Column("team_score", db.Integer, nullable=False),
                          db.Column("opposition_score", db.Integer, nullable=False),
                          db.Column("notes", db.Text, nullable=True))    
    inspector = db.inspect(engine)
    if not inspector.has_table("gamescore"):
        metadata.create_all(engine)
        print("Gamescore table created successfully")
    else:
        print("Gamescore table already exists in the database")

    # Create the skill score table
    skill_score = db.Table("skill_score", metadata,
                           db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                           db.Column("game_id", db.Integer, db.ForeignKey("game.id"), nullable=False),
                           db.Column("skater_id", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                           db.Column("blocker_speed", db.Float, nullable=False),
                           db.Column("blocker_pos_blocking", db.Float, nullable=False),
                           db.Column("blocker_comms", db.Float, nullable=False),
                           db.Column("blocker_agility", db.Float, nullable=False),
                           db.Column("blocker_stability", db.Float, nullable=False),
                           db.Column("jammer_speed", db.Float, nullable=False),
                           db.Column("jammer_comms", db.Float, nullable=False),
                           db.Column("jammer_agility", db.Float, nullable=False),
                           db.Column("jammer_attacking", db.Float, nullable=False),
                           db.Column("jammer_stability", db.Float, nullable=False),
                           db.Column("strategy_blocking", db.Float, nullable=False),
                           db.Column("strategy_jamming", db.Float, nullable=False),
                           db.Column("strategy_general", db.Float, nullable=False),
                           db.Column("coachability", db.Integer, nullable=False),
                           db.Column("game_day_behaviour", db.Integer, nullable=False),
                           db.Column("attendance", db.Integer, nullable=False))    
    inspector = db.inspect(engine)
    if not inspector.has_table("skill_score"):
        metadata.create_all(engine)
        print("Skill score table created successfully")
    else:
        print("Skill score table already exists in the database")

    # Create the GTSC score table
    gtsc_score = db.Table("gtsc_score", metadata,
                          db.Column("id", db.Integer, primary_key=True, autoincrement=True, nullable=False),
                          db.Column("skill_score_id", db.Integer, db.ForeignKey("skill_score.id"), nullable=False),
                          db.Column("skater_id", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                          db.Column("blocker_avg", db.Float, nullable=False),
                          db.Column("jammer_avg", db.Float, nullable=False),
                          db.Column("blocker_strats", db.Float, nullable=False),
                          db.Column("jammer_strats", db.Float, nullable=False),
                          db.Column("position_taken_forward", db.VARCHAR(50), nullable=False),
                          db.Column("general_strats", db.Float, nullable=False),
                          db.Column("coachability", db.Integer, nullable=False),
                          db.Column("game_day_behaviour", db.Integer, nullable=False),
                          db.Column("attendance", db.Integer, nullable=False),
                          db.Column("eligible_to_play", db.Boolean, nullable=False),
                          db.Column("total_score", db.Float, nullable=False))    
    inspector = db.inspect(engine)
    if not inspector.has_table("gtsc_score"):
        metadata.create_all(engine)
        print("Skill score table created successfully")
    else:
        print("Skill score table already exists in the database")

    # Create the scores comments table
    gtsc_comments = db.Table("gtsc_comments", metadata,
                             db.Column("id", primary_key=True, autoincrement=True, nullable=False),
                             db.Column("skill_score_link", db.Integer, db.ForeignKey("skill_score.id"), nullable=False),
                             db.Column("skater_link", db.Integer, db.ForeignKey("skater.id"), nullable=False),
                             db.Column("blocker_comments", db.Text, nullable=True),
                             db.Column("jammer_comments", db.Text, nullable=True),
                             db.Column("coachability_comments", db.Text, nullable=True),
                             db.Column("game_day_behaviour_comments", db.Text, nullable=True))

def add_sample_data():
    """
    Populates the database with sample data so the system can be trialled
    """
    pass
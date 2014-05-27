DROP TABLE unit;
CREATE TABLE unit ( 
  name text , 
  level int, 
  cost int, 
  dps int, 
  hp_max int , 
  PRIMARY KEY (name)
);

INSERT INTO unit (name, level , cost , dps , hp_max  ) 
VALUES ( 'barbarian_1', 1, 25, 8, 45 );
INSERT INTO unit (name, level , cost , dps , hp_max  ) 
VALUES( 'barbarian_2', 2, 40, 11, 54 );
INSERT INTO unit (name, level , cost , dps , hp_max  ) 
VALUES( 'barbarian_3', 3, 60, 14, 65 );
INSERT INTO unit (name, level , cost , dps , hp_max  ) 
VALUES( 'barbarian_4', 4, 80, 18, 78 );
INSERT INTO unit (name, level , cost , dps , hp_max  ) 
VALUES( 'barbarian_5', 5, 100, 23, 95 );
INSERT INTO unit (name, level , cost , dps , hp_max  ) 
VALUES( 'barbarian_5', 5, 150, 26, 110 );
